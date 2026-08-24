"""Site content for the James Olaitan portfolio.

This module is the single source of truth for everything shown on the site. It holds
**pure data only** — no logic, no imports, no formatting. All reads go through the
accessor functions in ``content/__init__.py``; routes and templates never import these
globals directly.

To edit the site's copy, edit this file. To change *how* content is served, edit the
accessors instead.
"""

PROFILE = {
    "name": "James Olaitan",
    "role": "Infrastructure & systems engineer",
    # Hero clause after "I'm James Olaitan, and " — single editable string:
    "hero_clause": "I build the layer underneath.",
    "supporting": "I work across Linux internals, distributed systems, and reliability.",
    "location": "San Francisco Bay Area",
    "availability": "Open to engineering roles",
    "email": "olaitan@uni.minerva.edu",
    "github": "https://github.com/JamesOlaitan",
    "linkedin": "https://www.linkedin.com/in/james-olaitan/",
    # Served from static/files/ via url_for('static', filename=PROFILE['resume']).
    "resume": "files/James_Olaitan_Resume.pdf",
}

PROJECTS = [
    {
        "name": "IAM Privilege Escalation Detector",
        "blurb": "Finds multi-hop AWS IAM privilege-escalation paths that per-policy analyzers miss, by modeling IAM as a directed graph (9 edge types) and running BFS over offline snapshots — no AWS calls.",
        "year": "2026", "type": "personal", "domain": "cloud security", "lang": "Go",
        "repo": "https://github.com/JamesOlaitan/iam-privilege-escalation-detector",
        "image": "img/projects/accessgraph.svg",
    },
    {
        "name": "Systemd Prometheus Exporter",
        "blurb": "A Rust daemon that polls systemd services over systemctl and exposes real-time service health as Prometheus metrics over HTTP, so Grafana can alert the moment a unit fails.",
        "year": "2026", "type": "personal", "domain": "observability", "lang": "Rust",
        "repo": "https://github.com/JamesOlaitan/systemd-prometheus-exporter",
        "image": "img/projects/systemd-exporter.svg",
    },
    {
        "name": "Market Anomaly Detection",
        "blurb": "Detects correlation breakdowns in S&P 500 sector data at 75% precision and 0.9998 ROC-AUC with an 18K-parameter LSTM trained on 14 years of history.",
        "year": "2025", "type": "personal", "domain": "machine learning", "lang": "Python",
        "repo": "https://github.com/JamesOlaitan/Anomalous-Market-Behavior-Recognition-with-Machine-Learning",
        "image": "img/projects/market-anomaly.svg",
    },
]

EXPERIENCE = [
    {
        "company": "Red Hat",
        "logo": "img/logos/red-hat.svg",
        "role": "Open Source Contributor, Konflux (Google Summer of Code)",
        "dates": "May 2026 – Aug 2026", "in_progress": True,
        "impact": "Authored a reproducible-build architecture (ADR-0069, under Red Hat review) to keep tampered builds from shipping, wiring opt-in buildah flags through a verification pipeline.",
        "tags": ["Tekton", "Go", "buildah", "Bash"],
        "artifact": {"title": "GSoC Final Report: Reproducible Builds in Konflux", "host": "jamesolaitan.com",
                     "url": "https://jamesolaitan.com/writing/reproducible-builds-konflux-gsoc"},
    },
    {
        "company": "Meta",
        "logo": "img/logos/meta.svg",
        "role": "Production Engineering Fellow, SRE (Meta × MLH)",
        "dates": "Jun 2026 – Sep 2026", "in_progress": True,
        "impact": "A 12-week Linux Foundation SRE curriculum under Meta Production Engineers: containerizing and deploying a Flask service through a GitHub Actions CI/CD pipeline, instrumented with Prometheus and Grafana.",
        "tags": ["Linux", "Docker", "Flask", "Prometheus", "Grafana", "CI/CD"],
        "artifact": None,
    },
    {
        "company": "UL Solutions",
        "logo": "img/logos/ul-solutions.svg",
        "role": "Engineering Intern",
        "dates": "Apr 2024 – Aug 2024 · May 2025 – Jul 2025", "in_progress": False,
        "impact": "Debugged firmware-flashing pipelines across 30+ IoT variants in FCC/ETSI-certified product lines, tracing calibration drift in Linux RF/EMC test environments to raise throughput 20%.",
        "tags": ["Linux", "Bash", "RF/EMC Testing"],
        "artifact": None,
    },
]

ABOUT_PARAGRAPHS = [
    "Two years ago I was on the phone with my mum, spiraling. I couldn't decide which branch of CS to commit to. The field felt too broad, and I kept getting tossed around like the wind: ML one week, data science the next, backend after that, then nothing but LeetCode, then wherever I happened to get hired. I never really held my own in anything.",
    "Then, one night shift at my internship, head wonky from fighting sleep, a client came by to drop off devices for certification. He asked what I studied. CS, I said. A few questions later we were standing at the PXA analyzer, and he told me the people who can program these things are extremely valuable: custom operating systems, recurring servicing revenue. I didn't know what bare metal was yet, and I won't pretend that was the moment it all clicked; if it were, I'd have walked away with a clear direction, and I didn't. But it stuck. Building the underlying infrastructure, writing the algorithm that powers the thing. I wanted that.",
    "Now I work across infrastructure and reliability. At Red Hat's Konflux I built a reproducible-build pipeline so tampered builds can't ship — the same class of supply-chain attack behind SolarWinds. I did an SRE rotation under Meta engineers, learning to read a live system with nothing but `grep`, `ps`, and `journald`. And I've built projects like a C++ percentile engine that holds a thousand requests a second under 300ms. I care about the boring, load-bearing layer because when it's done well nobody notices, and when it isn't, everyone does.",
    "Lately I've been pulled further down: toward embedded and RTOS, and, further out, quantum. I don't fully know where that leads yet. But I've never been able to stop asking what the layer beneath the one I just learned actually does. I'd rather build the floor everything stands on than the thing standing on it.",
]
ABOUT_FOOTER = "Currently studying CS at Minerva University, which has taken me through Taipei and Seoul. Open to engineering roles."

READING = [
    {"category": "Systems", "items": [
        {"title": "Operating Systems: Three Easy Pieces", "author": "Remzi & Andrea Arpaci-Dusseau",
         "blurb": "Understanding systems starts with the most battle-tested one of all: the operating system.",
         "source": "https://pages.cs.wisc.edu/~remzi/OSTEP/", "thoughts": None},
        {"title": "kernel-internals.org", "author": None,
         "blurb": "A most-recurring visit for anything Linux internals.",
         "source": "https://kernel-internals.org/", "thoughts": None},
        {"title": "LearnLinuxTV", "author": "YouTube",
         "blurb": "My go-to channel for hands-on Linux.",
         "source": "https://www.youtube.com/@LearnLinuxTV", "thoughts": None},
    ]},
    {"category": "Ideas & growth", "items": [
        {"title": "Peak: Secrets from the New Science of Expertise", "author": "Anders Ericsson & Robert Pool",
         "blurb": None, "source": None, "thoughts": None},
        {"title": "The Richest Man in Babylon", "author": "George S. Clason",
         "blurb": "The most direct, no-fluff framework for financial discipline. Worth reading once in your life.",
         "source": None, "thoughts": None},
    ]},
    {"category": "Fiction", "items": [
        {"title": "The Fault in Our Stars", "author": "John Green",
         "blurb": "One of the most touching novels I've read.",
         "source": None,
         "thoughts": "Eyes closed, intubated, dark cancer water dripping from Hazel's chest. \"A desert blessing, an ocean curse,\" as Augustus put it. Love, anguish, pain. It shows how a moment that seems trivial can turn positive or negative depending on the circumstance, especially when it might mean losing someone you love."},
        {"title": "All the Light We Cannot See", "author": "Anthony Doerr",
         "blurb": None, "source": None, "thoughts": None},
        {"title": "Mistborn trilogy", "author": "Brandon Sanderson",
         "blurb": "Barely touched fiction once college apps started, until this. A real page-turner, with allomancy and a universe all its own.",
         "source": None, "thoughts": None},
        {"title": "Percy Jackson & the Olympians", "author": "Rick Riordan",
         "blurb": "My favorite series growing up; always has a place in my heart.",
         "source": None, "thoughts": None},
        {"title": "The Heroes of Olympus", "author": "Rick Riordan",
         "blurb": "Riordan's best series yet, but read Percy Jackson first as the build-up.",
         "source": None,
         "thoughts": "The stretch from the back half of The Mark of Athena into The House of Hades is the best part. How do you survive and escape Tartarus? The more I sit with it, the more love is the core of that survival, not just power and shrewdness."},
    ]},
]

# Prose blocks support `` `code` `` spans and `[text](url)` links via the
# `richtext` template filter. Bold terms and links live in structured `definitions` /
# `status` / `links` blocks instead of inline markdown, so the filter only has to
# handle two token types.
WRITING = {
    "title": "Reproducible Builds: Pipeline Wiring, Verification Tooling, and Benchmark Suite",
    "kicker": "GSoC 2026 · konflux-ci (Red Hat)",
    "description": "My GSoC 2026 final work product for konflux-ci (Red Hat): making container builds reproducible, wiring that into real pipelines, and building the tooling to verify it.",
    "sections": [
        {"heading": "What I set out to do", "blocks": [
            {"type": "p", "text": "Konflux is a build system. You give it your source code, and it turns that into a container image you can run. My project was about a specific property those images didn't have: if you build the exact same source code twice, you should get the exact same image back, byte for byte. Right now, in most build systems including Konflux's default setup, you don't. Build the same code twice and you get two images that behave the same but aren't actually identical underneath."},
            {"type": "p", "text": "Why does this matter? If a build is reproducible, anyone can take your source code, build it themselves, and check whether the image they get matches the one you shipped. If it matches, they know the image really came from that source and nothing was added or swapped in along the way. If builds aren't reproducible, that check is impossible, because you'd expect the two images to differ even when nothing suspicious happened."},
            {"type": "p", "text": "My job was to make Konflux builds reproducible on an opt-in basis, wire that into the pipelines people actually use, and build a way to check reproducibility automatically instead of just claiming it works."},
        ]},
        {"heading": "The design", "blocks": [
            {"type": "p", "text": "Before writing code, I wrote up a proposal (Konflux calls these ADRs, architecture decision records) so the maintainers could weigh in on the approach first. This became [ADR-0069](https://github.com/konflux-ci/architecture/pull/360), merged June 24 and my first-ever contribution to the project."},
            {"type": "p", "text": "Here's the core idea a reproducibility check relies on: every container image has a digest, a number computed from every byte in it. Change one byte anywhere inside the image, even a timestamp buried in a file nobody looks at, and the digest changes completely. That's what makes reproducibility checkable at all: build the same source twice, compare the two digests, and if they match, the images are identical down to the byte."},
            {"type": "p", "text": "The problem is that build tools normally stamp the current time into an image while building it, and record some history about the build itself. Build the same source at two different times and you get two different digests, even though nothing about the code changed. The ADR proposes three settings to fix that, all off by default:"},
            {"type": "definitions", "items": [
                {"term": "source-date-epoch", "detail": 'a fixed timestamp to use instead of "whatever time it is right now."'},
                {"term": "rewrite-timestamp", "detail": "makes sure files inside the image's layers also get stamped with that fixed time, not just the image's own metadata. Timestamps hiding inside individual files are exactly the kind of thing that quietly breaks reproducibility if you only fix the outer metadata."},
                {"term": "omit-history", "detail": "drops the build-history record from the image, which can also carry the real build time."},
            ]},
            {"type": "p", "text": "Before writing any of this up, I tested whether it would actually work. I built three kinds of images twice each on a test cluster: a plain Alpine image that just copies files in, a Go program built with a couple of extra flags, and a Fedora image that installs a package with `dnf`. The first two came out byte-identical both times once those three settings were on. The Fedora one didn't. It turned out `dnf` writes a log file with a timestamp inside it as part of installing the package, and that log ends up baked into the image regardless of the three settings. I wrote that down as a known limitation instead of hiding it, along with the workaround: delete that log file in the same build step that created it."},
        ]},
        {"heading": "Getting it into real pipelines", "blocks": [
            {"type": "p", "text": "The three settings already existed at the level of Konflux's build task, from work that landed before I started. What was missing was the pipeline layer: the actual pipeline definitions that Konflux users build their images with never asked for those settings, so nobody could turn them on even though the underlying support already existed."},
            {"type": "p", "text": "[#3670](https://github.com/konflux-ci/build-definitions/pull/3670), merged July 15, added the three parameters to the docker-build family of pipelines and passed them through to the build task. All three still default to off, so nothing changes for anyone who doesn't ask for it. I checked this actually worked by building the same commit twice through the real pipeline on a local cluster, for two different kinds of images, and getting matching digests both times."},
            {"type": "p", "text": "That covered pipelines going forward, but a lot of users don't pull a fresh pipeline from Konflux directly. They have a copy that was generated into their own repo earlier, and that copy doesn't automatically pick up changes made upstream. [#24](https://github.com/konflux-ci/container-build-catalog/pull/24), merged July 21, adds a migration so those existing copies get the same three parameters too, still off by default."},
        ]},
        {"heading": "Refining the CLI", "blocks": [
            {"type": "p", "text": "`konflux-build-cli` is the small command-line tool that Konflux's build task actually runs to do the real work with buildah, the underlying build engine. The `rewrite-timestamp` setting needs a number to clamp file times to, and the obvious number to use is the timestamp of the git commit being built. My first instinct was to have `rewrite-timestamp` automatically pull that timestamp in behind the scenes whenever it was turned on."},
            {"type": "p", "text": 'Discussion on #3670 talked me out of that. One setting silently reaching over and filling in a different setting can surprise someone reading the pipeline later, and it also means you can\'t ask for "use the commit\'s timestamp" without also asking for the file-rewriting behavior, even if that\'s not what you wanted. So the design changed to something a user has to type on purpose: a special value, `:from-commit-timestamp:`, that you can write into the `source-date-epoch` field to mean "use the commit\'s timestamp." Nothing happens automatically. [#225](https://github.com/konflux-ci/konflux-build-cli/pull/225) is the code that recognizes that value and substitutes the real timestamp before buildah ever sees it, following three rules: an actual number you type always wins, the special value gets replaced by the real commit timestamp (with a clear error if that timestamp is missing or broken), and leaving the field empty still does nothing, same as before.'},
            {"type": "p", "text": 'You might be wondering why the build step can\'t just read the commit timestamp off the checkout directly. On a pull-request build, the code you\'re looking at is a merge commit created fresh at build time, so its own timestamp is always "just now," not the timestamp of the actual commit being tested. An earlier step in the pipeline, the one that clones the code, captures the real commit\'s timestamp before doing that merge, and #225 is what carries that captured value through to the build step. As of writing this, reviewers have approved #225 and it\'s marked ready to merge, just not merged yet.'},
        ]},
        {"heading": "A finding along the way", "blocks": [
            {"type": "p", "text": 'While testing all of this, I ran into a separate bug. When Konflux builds an image for more than one CPU architecture, like amd64 and arm64, it assembles them into one "index" that lists all of them together. Buildah loops over those architectures using a Go map internally, and Go maps don\'t guarantee you get items back out in the same order you put them in. That means the same build could produce that list of architectures in a different order on different runs, changing the digest even though none of the actual images changed.'},
            {"type": "p", "text": "I wrote a fix for `konflux-build-cli` that explicitly sorts the images by architecture before adding them to the index, so the order would always come out the same. I opened [#226](https://github.com/konflux-ci/konflux-build-cli/pull/226) with it."},
            {"type": "p", "text": "A maintainer reviewing the PR asked a direct question: doesn't Konflux's pipeline already add these images one at a time, in a fixed order, through separate commands, rather than looping over a map all at once? I went and checked. He was right. The specific way this pipeline calls buildah never touches the code path where that map-ordering problem happens. It goes through a different path that adds each image individually, in the order it's given. I'd reproduced the bug, but it lived in a part of buildah that this pipeline simply doesn't use."},
            {"type": "p", "text": "So I closed my own PR. The right response to finding a bug isn't always to ship the fix, sometimes it's to check whether the system you're working on actually exercises the code path where that bug lives, and this one didn't."},
        ]},
        {"heading": "Verification tooling and the benchmark suite", "blocks": [
            {"type": "p", "text": "Everything above makes a build reproducible if you ask for it, but none of it checks that a given image actually is reproducible. That's what [#3803](https://github.com/konflux-ci/build-definitions/pull/3803), opened August 23, is for."},
            {"type": "p", "text": "It's a separate, on-demand pipeline. You give it an image and the source it claims to be built from, and it rebuilds that source from scratch into a separate scratch location, so it doesn't overwrite the real image's own signature and attestation tags in the process. Then it compares the digest of the image it just built to the digest of the image you handed it. A match means the image really was built from that source. A mismatch means something's off. It has to be a pipeline rather than a task, because a task in Konflux isn't allowed to call another task to trigger the rebuild, only a pipeline can do that."},
            {"type": "p", "text": "I wrote the limitations into the PR directly rather than leaving them implicit. It only handles single-architecture images for now. Multi-architecture support is later work. A matching digest also only proves that the same build platform, given the same source, produces the same bytes, it can't catch the case where the build platform itself is compromised in a way that's consistent with itself every time it runs. A stronger check, rebuilding independently on a different platform and comparing signed build records, is named as the direction to grow into later."},
            {"type": "p", "text": 'This PR is also where the benchmark suite lives. It ships with its own automated test suite that runs in CI on every change: one case where the digests should match, one where they shouldn\'t, and one with a broken or malformed image reference, each checked automatically. That\'s the repeatable, automated proof that the verification logic does what it claims, rather than a one-off check I ran by hand once. As of writing, the PR is still undergoing review.'},
        ]},
        {"heading": "Where things stand, and what's left", "blocks": [
            {"type": "status", "items": [
                {"label": "#225 (CLI sentinel)", "detail": "approved by reviewers, waiting to be merged."},
                {"label": "#3803 (verification pipeline)", "detail": "open, still under review."},
            ]},
            {"type": "p", "text": "A few pieces are still on the list. Extending verification to multi-architecture images is one. The stronger independent-platform rebuild check described above is another, still just an idea in the ADR. And there's one open question I wrote down but haven't answered yet, whether the SBOM (the automatically generated list of everything inside an image) itself comes out byte-identical across two runs. If it doesn't, the way those SBOMs get tagged and stored will need to change too."},
            {"type": "p", "text": 'One more piece I looked into but haven\'t shipped is wiring in a tool called diffoci, so a failed verification shows exactly which layers differ instead of just "the digest didn\'t match." That one turned out to be bigger than a single PR. diffoci doesn\'t publish a container image, only signed binary releases, and build-definitions isn\'t where new CLI tools get added, that lives in a separate repo called task-runner, alongside the other tools like syft and cosign that Konflux\'s tasks already use. Adding a new one there means opening an issue first and getting maintainer sign-off before any code, per that repo\'s own contributor guidance. That conversation may not be settled before the GSoC program ends, but it\'s not something I\'m dropping. I plan to open that issue and keep contributing to konflux-ci after the program is over.'},
        ]},
        {"heading": "The work, linked directly", "blocks": [
            {"type": "links", "items": [
                {"title": "ADR-0069: Reproducible Container Builds in Konflux", "url": "https://github.com/konflux-ci/architecture/pull/360", "status": "merged"},
                {"title": "Add opt-in reproducibility params to docker-build", "url": "https://github.com/konflux-ci/build-definitions/pull/3670", "status": "merged"},
                {"title": "init: add migration for reproducibility params", "url": "https://github.com/konflux-ci/container-build-catalog/pull/24", "status": "merged"},
                {"title": "Accept `:from-commit-timestamp:` for source-date-epoch", "url": "https://github.com/konflux-ci/konflux-build-cli/pull/225", "status": "approved, awaiting merge"},
                {"title": "Sort image index entries by platform", "url": "https://github.com/konflux-ci/konflux-build-cli/pull/226", "status": "closed by me, finding described above"},
                {"title": "Add verify-reproducibility pipeline and task", "url": "https://github.com/konflux-ci/build-definitions/pull/3803", "status": "open, in review"},
            ]},
        ]},
    ],
}
