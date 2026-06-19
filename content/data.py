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
        "name": "AccessGraph",
        "blurb": "Finds multi-hop AWS IAM privilege-escalation paths that per-policy analyzers miss, by modeling IAM as a directed graph and running BFS over offline snapshots.",
        "year": "2026", "type": "personal", "domain": "cloud security", "lang": "Go",
        "repo": "https://github.com/JamesOlaitan/accessgraph",
        "image": "img/projects/accessgraph.svg",
    },
    {
        "name": "Distributed Systems Profiler",
        "blurb": "Sustains 1,000 RPS at sub-300ms p95 across a 3-service testbed, using a custom C++ rolling-percentile engine over streaming Prometheus samples.",
        "year": "2025", "type": "personal", "domain": "distributed systems", "lang": "C++ / Python",
        "repo": "https://github.com/JamesOlaitan/Distributed-Systems-Profiler",
        "image": "img/projects/profiler.svg",
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
        "artifact": {"title": "ADR: Reproducible Builds (PR #360)", "host": "github.com",
                     "url": "https://github.com/konflux-ci/architecture/pull/360"},
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
