<!--
Plain-text backup of my GSoC 2026 final work product for konflux-ci (Red Hat).
The formatted version lives at https://jamesolaitan.com/writing/reproducible-builds-konflux-gsoc.
This file exists so the report has a permanent copy even if the site above changes.
-->

# Reproducible Builds: Pipeline Wiring, Verification Tooling, and Benchmark Suite

*GSoC 2026, konflux-ci (Red Hat)*

## What I set out to do

Konflux is a build system. You give it your source code, and it turns that into a container image you can run. My project was about a specific property those images didn't have: if you build the exact same source code twice, you should get the exact same image back, byte for byte. Right now, in most build systems including Konflux's default setup, you don't. Build the same code twice and you get two images that behave the same but aren't actually identical underneath.

Why does this matter? If a build is reproducible, anyone can take your source code, build it themselves, and check whether the image they get matches the one you shipped. If it matches, they know the image really came from that source and nothing was added or swapped in along the way. If builds aren't reproducible, that check is impossible, because you'd expect the two images to differ even when nothing suspicious happened.

My job was to make Konflux builds reproducible on an opt-in basis, wire that into the pipelines people actually use, and build a way to check reproducibility automatically instead of just claiming it works.

## The design

Before writing code, I wrote up a proposal (Konflux calls these ADRs, architecture decision records) so the maintainers could weigh in on the approach first. This became [ADR-0069](https://github.com/konflux-ci/architecture/pull/360), merged June 24 and my first-ever contribution to the project.

Here's the core idea a reproducibility check relies on: every container image has a digest, a number computed from every byte in it. Change one byte anywhere inside the image, even a timestamp buried in a file nobody looks at, and the digest changes completely. That's what makes reproducibility checkable at all: build the same source twice, compare the two digests, and if they match, the images are identical down to the byte.

The problem is that build tools normally stamp the current time into an image while building it, and record some history about the build itself. Build the same source at two different times and you get two different digests, even though nothing about the code changed. The ADR proposes three settings to fix that, all off by default:

- **source-date-epoch**: a fixed timestamp to use instead of "whatever time it is right now."
- **rewrite-timestamp**: makes sure files inside the image's layers also get stamped with that fixed time, not just the image's own metadata. Timestamps hiding inside individual files are exactly the kind of thing that quietly breaks reproducibility if you only fix the outer metadata.
- **omit-history**: drops the build-history record from the image, which can also carry the real build time.

Before writing any of this up, I tested whether it would actually work. I built three kinds of images twice each on a test cluster: a plain Alpine image that just copies files in, a Go program built with a couple of extra flags, and a Fedora image that installs a package with `dnf`. The first two came out byte-identical both times once those three settings were on. The Fedora one didn't. It turned out `dnf` writes a log file with a timestamp inside it as part of installing the package, and that log ends up baked into the image regardless of the three settings. I wrote that down as a known limitation instead of hiding it, along with the workaround: delete that log file in the same build step that created it.

## Getting it into real pipelines

The three settings already existed at the level of Konflux's build task, from work that landed before I started. What was missing was the pipeline layer: the actual pipeline definitions that Konflux users build their images with never asked for those settings, so nobody could turn them on even though the underlying support already existed.

[#3670](https://github.com/konflux-ci/build-definitions/pull/3670), merged July 15, added the three parameters to the docker-build family of pipelines and passed them through to the build task. All three still default to off, so nothing changes for anyone who doesn't ask for it. I checked this actually worked by building the same commit twice through the real pipeline on a local cluster, for two different kinds of images, and getting matching digests both times.

That covered pipelines going forward, but a lot of users don't pull a fresh pipeline from Konflux directly. They have a copy that was generated into their own repo earlier, and that copy doesn't automatically pick up changes made upstream. [#24](https://github.com/konflux-ci/container-build-catalog/pull/24), merged July 21, adds a migration so those existing copies get the same three parameters too, still off by default.

## Refining the CLI

`konflux-build-cli` is the small command-line tool that Konflux's build task actually runs to do the real work with buildah, the underlying build engine. The `rewrite-timestamp` setting needs a number to clamp file times to, and the obvious number to use is the timestamp of the git commit being built. My first instinct was to have `rewrite-timestamp` automatically pull that timestamp in behind the scenes whenever it was turned on.

Discussion on #3670 talked me out of that. One setting silently reaching over and filling in a different setting can surprise someone reading the pipeline later, and it also means you can't ask for "use the commit's timestamp" without also asking for the file-rewriting behavior, even if that's not what you wanted. So the design changed to something a user has to type on purpose: a special value, `:from-commit-timestamp:`, that you can write into the `source-date-epoch` field to mean "use the commit's timestamp." Nothing happens automatically. [#225](https://github.com/konflux-ci/konflux-build-cli/pull/225) is the code that recognizes that value and substitutes the real timestamp before buildah ever sees it, following three rules: an actual number you type always wins, the special value gets replaced by the real commit timestamp (with a clear error if that timestamp is missing or broken), and leaving the field empty still does nothing, same as before.

You might be wondering why the build step can't just read the commit timestamp off the checkout directly. On a pull-request build, the code you're looking at is a merge commit created fresh at build time, so its own timestamp is always "just now," not the timestamp of the actual commit being tested. An earlier step in the pipeline, the one that clones the code, captures the real commit's timestamp before doing that merge, and #225 is what carries that captured value through to the build step. As of writing this, reviewers have approved #225 and it's marked ready to merge, just not merged yet.

## A finding along the way

While testing all of this, I ran into a separate bug. When Konflux builds an image for more than one CPU architecture, like amd64 and arm64, it assembles them into one "index" that lists all of them together. Buildah loops over those architectures using a Go map internally, and Go maps don't guarantee you get items back out in the same order you put them in. That means the same build could produce that list of architectures in a different order on different runs, changing the digest even though none of the actual images changed.

I wrote a fix for `konflux-build-cli` that explicitly sorts the images by architecture before adding them to the index, so the order would always come out the same. I opened [#226](https://github.com/konflux-ci/konflux-build-cli/pull/226) with it.

A maintainer reviewing the PR asked a direct question: doesn't Konflux's pipeline already add these images one at a time, in a fixed order, through separate commands, rather than looping over a map all at once? I went and checked. He was right. The specific way this pipeline calls buildah never touches the code path where that map-ordering problem happens. It goes through a different path that adds each image individually, in the order it's given. I'd reproduced the bug, but it lived in a part of buildah that this pipeline simply doesn't use.

So I closed my own PR. The right response to finding a bug isn't always to ship the fix, sometimes it's to check whether the system you're working on actually exercises the code path where that bug lives, and this one didn't.

## Verification tooling and the benchmark suite

Everything above makes a build reproducible if you ask for it, but none of it checks that a given image actually is reproducible. That's what [#3803](https://github.com/konflux-ci/build-definitions/pull/3803), opened August 23, is for.

It's a separate, on-demand pipeline. You give it an image and the source it claims to be built from, and it rebuilds that source from scratch into a separate scratch location, so it doesn't overwrite the real image's own signature and attestation tags in the process. Then it compares the digest of the image it just built to the digest of the image you handed it. A match means the image really was built from that source. A mismatch means something's off. It has to be a pipeline rather than a task, because a task in Konflux isn't allowed to call another task to trigger the rebuild, only a pipeline can do that.

I wrote the limitations into the PR directly rather than leaving them implicit. It only handles single-architecture images for now. Multi-architecture support is later work. A matching digest also only proves that the same build platform, given the same source, produces the same bytes, it can't catch the case where the build platform itself is compromised in a way that's consistent with itself every time it runs. A stronger check, rebuilding independently on a different platform and comparing signed build records, is named as the direction to grow into later.

This PR is also where the benchmark suite lives. It ships with its own automated test suite that runs in CI on every change: one case where the digests should match, one where they shouldn't, and one with a broken or malformed image reference, each checked automatically. That's the repeatable, automated proof that the verification logic does what it claims, rather than a one-off check I ran by hand once. As of writing, the PR is still undergoing review.

## Where things stand, and what's left

- **#225** (CLI sentinel): approved by reviewers, waiting to be merged.
- **#3803** (verification pipeline): open, still under review.

A few pieces are still on the list. Extending verification to multi-architecture images is one. The stronger independent-platform rebuild check described above is another, still just an idea in the ADR. And there's one open question I wrote down but haven't answered yet, whether the SBOM (the automatically generated list of everything inside an image) itself comes out byte-identical across two runs. If it doesn't, the way those SBOMs get tagged and stored will need to change too.

One more piece I looked into but haven't shipped is wiring in a tool called diffoci, so a failed verification shows exactly which layers differ instead of just "the digest didn't match." That one turned out to be bigger than a single PR. diffoci doesn't publish a container image, only signed binary releases, and build-definitions isn't where new CLI tools get added, that lives in a separate repo called task-runner, alongside the other tools like syft and cosign that Konflux's tasks already use. Adding a new one there means opening an issue first and getting maintainer sign-off before any code, per that repo's own contributor guidance. That conversation may not be settled before the GSoC program ends, but it's not something I'm dropping. I plan to open that issue and keep contributing to konflux-ci after the program is over.

## The work, linked directly

- [ADR-0069: Reproducible Container Builds in Konflux](https://github.com/konflux-ci/architecture/pull/360) · merged
- [Add opt-in reproducibility params to docker-build](https://github.com/konflux-ci/build-definitions/pull/3670) · merged
- [init: add migration for reproducibility params](https://github.com/konflux-ci/container-build-catalog/pull/24) · merged
- [Accept `:from-commit-timestamp:` for source-date-epoch](https://github.com/konflux-ci/konflux-build-cli/pull/225) · approved, awaiting merge
- [Sort image index entries by platform](https://github.com/konflux-ci/konflux-build-cli/pull/226) · closed by me, finding described above
- [Add verify-reproducibility pipeline and task](https://github.com/konflux-ci/build-definitions/pull/3803) · open, in review
