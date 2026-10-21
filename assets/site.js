/* SourceTrac Survey — small progressive-enhancement scripts.
   No cookies, no storage, no analytics, no network requests. */
(function () {
  "use strict";

  /* Mobile navigation toggle */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
  }

  /* Pricing: monthly / yearly toggle */
  var priceToggle = document.querySelector("[data-price-toggle]");
  if (priceToggle) {
    var amounts = document.querySelectorAll("[data-monthly]");
    var billings = document.querySelectorAll("[data-billing]");
    var strikes = document.querySelectorAll("[data-strike]");
    var saves = document.querySelectorAll("[data-save]");
    var buttons = priceToggle.querySelectorAll("button[data-period]");

    var show = function (period) {
      var yearly = period === "yearly";
      amounts.forEach(function (el) {
        var value = yearly ? el.getAttribute("data-yearly") : el.getAttribute("data-monthly");
        var small = el.querySelector("small");
        el.firstChild.nodeValue = value;
        if (small) {
          var billedYearly = yearly && !el.hasAttribute("data-no-billing");
          small.textContent = billedYearly ? " a month, billed yearly" : " a month";
        }
      });
      billings.forEach(function (el) { el.hidden = !yearly; });
      strikes.forEach(function (el) { el.hidden = !yearly; });
      saves.forEach(function (el) { el.hidden = !yearly; });
      buttons.forEach(function (b) {
        b.setAttribute("aria-pressed", String(b.getAttribute("data-period") === period));
      });
    };

    priceToggle.addEventListener("click", function (event) {
      var btn = event.target.closest("button[data-period]");
      if (!btn) return;
      show(btn.getAttribute("data-period"));
    });
    show("monthly");
  }

  /* Templates: client-side search */
  var search = document.getElementById("tpl-search");
  if (search) {
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-tpl]"));
    var groups = Array.prototype.slice.call(document.querySelectorAll("[data-tpl-group]"));
    var empty = document.getElementById("tpl-empty");
    var count = document.getElementById("tpl-count");

    var filter = function () {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      cards.forEach(function (card) {
        var match = q === "" || (card.getAttribute("data-search") || "").indexOf(q) !== -1;
        card.hidden = !match;
        if (match) shown++;
      });
      groups.forEach(function (group) {
        var visible = group.querySelectorAll("[data-tpl]:not([hidden])").length;
        group.hidden = visible === 0;
        var badge = group.querySelector("[data-group-count]");
        if (badge) badge.textContent = visible + (visible === 1 ? " template" : " templates");
      });
      if (empty) empty.classList.toggle("is-shown", shown === 0);
      if (count) count.textContent = shown + (shown === 1 ? " template" : " templates");
    };

    search.addEventListener("input", filter);
    var form = search.closest("form");
    if (form) form.addEventListener("submit", function (e) { e.preventDefault(); });
    filter();
  }

  /* Copy buttons */
  var copy = function (text, statusEl) {
    var done = function () {
      if (!statusEl) return;
      var original = statusEl.getAttribute("data-label") || "Copied";
      statusEl.textContent = original;
      window.setTimeout(function () { statusEl.textContent = ""; }, 4000);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
    } else {
      fallback(text, done);
    }
  };

  var fallback = function (text, done) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); done(); } catch (e) { /* leave selection for manual copy */ }
    document.body.removeChild(ta);
  };

  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var target = document.querySelector(btn.getAttribute("data-copy"));
      if (!target) return;
      var text = target.getAttribute("data-copy-text") || target.textContent;
      copy(text.trim(), document.querySelector(btn.getAttribute("data-copy-status") || ""));
    });
  });

  /* Gmail compose link, built from the mailto link so the two never drift */
  document.querySelectorAll("[data-gmail]").forEach(function (link) {
    var mailto = link.getAttribute("data-mailto") || "";
    var withoutScheme = mailto.replace(/^mailto:/, "");
    var parts = withoutScheme.split("?");
    var to = parts[0];
    var params = new URLSearchParams(parts[1] || "");
    var gmail = new URLSearchParams();
    gmail.set("view", "cm");
    gmail.set("fs", "1");
    gmail.set("to", to);
    if (params.get("subject")) gmail.set("su", params.get("subject"));
    if (params.get("body")) gmail.set("body", params.get("body"));
    link.setAttribute("href", "https://mail.google.com/mail/?" + gmail.toString());
  });
})();
