/* Kora Studio — theme toggle and mobile menu. No tracking, no cookies. */
(function () {
  "use strict";

  var root = document.documentElement;

  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  function applyTheme(theme, remember) {
    root.setAttribute("data-theme", theme);
    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      btn.setAttribute("aria-label", theme === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
    if (remember) {
      try {
        localStorage.setItem("kora-theme", theme);
      } catch (e) {
        /* storage blocked: theme still applies for this page */
      }
    }
  }

  applyTheme(currentTheme(), false);

  // Pricing toggle fallback for browsers without CSS :has().
  var yearly = document.getElementById("bill-yearly");
  if (yearly) {
    var pricing = yearly.closest(".pricing");
    var supportsHas = window.CSS && CSS.supports && CSS.supports("selector(:has(*))");
    if (pricing && !supportsHas) {
      var syncPricing = function () {
        pricing.classList.toggle("is-yearly", yearly.checked);
      };
      syncPricing();
      document.addEventListener("change", function (event) {
        if (event.target === yearly) syncPricing();
      });
    }
  }

  document.addEventListener("click", function (event) {
    var toggle = event.target.closest(".theme-toggle");
    if (toggle) {
      applyTheme(currentTheme() === "dark" ? "light" : "dark", true);
      return;
    }

    var menuBtn = event.target.closest(".menu-toggle");
    if (menuBtn) {
      var nav = document.getElementById(menuBtn.getAttribute("aria-controls"));
      if (!nav) return;
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", open ? "false" : "true");
      menuBtn.setAttribute("aria-expanded", open ? "false" : "true");
      return;
    }

    var navLink = event.target.closest("#site-nav a");
    if (navLink) {
      var siteNav = document.getElementById("site-nav");
      var btn = document.querySelector(".menu-toggle");
      if (siteNav && siteNav.getAttribute("data-open") === "true") {
        siteNav.setAttribute("data-open", "false");
        if (btn) btn.setAttribute("aria-expanded", "false");
      }
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    var siteNav = document.getElementById("site-nav");
    var btn = document.querySelector(".menu-toggle");
    if (siteNav && siteNav.getAttribute("data-open") === "true") {
      siteNav.setAttribute("data-open", "false");
      if (btn) {
        btn.setAttribute("aria-expanded", "false");
        btn.focus();
      }
    }
  });
})();
