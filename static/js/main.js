/**
 * Portfolio interactions: theme toggle, scroll-reveal, thoughts disclosure,
 * mobile nav. Each behavior is a single-responsibility init function, guarded so
 * a page lacking the relevant elements is a no-op. No globals leak.
 *
 * Note: the *initial* theme and the `js` class are set by an inline script in the
 * document head (before paint). This file only wires up user interaction.
 */
(function () {
  "use strict";

  /**
   * Wire the light/dark theme toggle button: flip `data-theme`, persist the
   * choice to localStorage, and keep `aria-pressed` in sync.
   */
  function initTheme() {
    var toggle = document.getElementById("theme-toggle");
    if (!toggle) return;

    var root = document.documentElement;

    function sync() {
      toggle.setAttribute("aria-pressed", String(root.dataset.theme === "dark"));
    }

    sync();
    toggle.addEventListener("click", function () {
      var next = root.dataset.theme === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try {
        localStorage.setItem("theme", next);
      } catch (e) {
        /* storage unavailable (private mode) — theme still applies for the session */
      }
      sync();
    });
  }

  /**
   * Reveal `[data-reveal]` elements as they scroll into view via a single
   * IntersectionObserver. If reduced motion is requested or IntersectionObserver
   * is unavailable, reveal everything immediately (content is never gated behind
   * animation).
   */
  function initScrollReveal() {
    var elements = document.querySelectorAll("[data-reveal]");
    if (!elements.length) return;

    var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced || !("IntersectionObserver" in window)) {
      elements.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }

    var observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.05 });

    elements.forEach(function (el) { observer.observe(el); });
  }

  /**
   * Enhance the reading "thoughts" disclosures. They are native
   * `<details>/<summary>` (keyboard-operable without JS); here we mirror the open
   * state onto `aria-expanded` for assistive tech.
   */
  function initThoughtsDisclosure() {
    var items = document.querySelectorAll("details.thoughts");
    if (!items.length) return;

    items.forEach(function (details) {
      var summary = details.querySelector("summary");
      if (!summary) return;
      summary.setAttribute("aria-expanded", String(details.open));
      details.addEventListener("toggle", function () {
        summary.setAttribute("aria-expanded", String(details.open));
      });
    });
  }

  /**
   * Wire the mobile hamburger menu: toggle the stacked nav, keep `aria-expanded`
   * current, and close on link click or Escape.
   */
  function initMobileNav() {
    var toggle = document.getElementById("nav-toggle");
    var menu = document.getElementById("nav-menu");
    if (!toggle || !menu) return;

    function setOpen(open) {
      menu.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    }

    toggle.addEventListener("click", function () {
      setOpen(!menu.classList.contains("is-open"));
    });

    menu.addEventListener("click", function (event) {
      if (event.target.closest("a")) setOpen(false);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && menu.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  /** Run all initializers once the DOM is ready. */
  function init() {
    initTheme();
    initScrollReveal();
    initThoughtsDisclosure();
    initMobileNav();
  }

  if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
