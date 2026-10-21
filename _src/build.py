# -*- coding: utf-8 -*-
"""Static site generator for the SourceTrac website.

Run:  python3 _src/build.py
Output: plain HTML files in the repository root, ready to upload to Netlify.
No cookies, no analytics, no external requests.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from faq_data import FAQ
from privacy_data import MERCHANT_DETAIL, MERCHANT_QUOTE, POLICY_BLOCKS, POLICY_INTRO, POLICY_UPDATED
from templates_data import TEMPLATE_GROUPS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Site-wide values. Replace APP_STORE_URL with the real listing link.
# ---------------------------------------------------------------------------
APP_STORE_URL = "[APP STORE LISTING URL]"
SITE_NAME = "SourceTrac"
PUBLISHER = "SourceTrac Survey"
EMAIL = "sourcetracsupport@gmail.com"
YEAR = "2026"
TERMS_UPDATED = "15 October 2026"

NAV = [
    ("/features", "Features"),
    ("/templates", "Templates"),
    ("/pricing", "Pricing"),
    ("/help", "Help"),
    ("/support", "Support"),
]


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def attr(text):
    return esc(text).replace('"', "&quot;")


# ---------------------------------------------------------------------------
# Small inline icons. Drawn for this site; no app screenshots are used.
# ---------------------------------------------------------------------------
ICON = {
    "survey": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8 8h8M8 12h5"/><path d="M8 16.5l1.6 1.6L13 14.7"/></svg>',
    "revenue": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19h16"/><rect x="6" y="11" width="3.2" height="6" rx="1"/><rect x="11" y="7" width="3.2" height="10" rx="1"/><rect x="16" y="13" width="3.2" height="4" rx="1"/></svg>',
    "templates": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="2"/><rect x="13.5" y="3.5" width="7" height="7" rx="2"/><rect x="3.5" y="13.5" width="7" height="7" rx="2"/><rect x="13.5" y="13.5" width="7" height="7" rx="2"/></svg>',
    "score": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14.5A8.5 8.5 0 0 1 20 14.5"/><path d="M12 14.5l4.2-4.2"/><circle cx="12" cy="14.5" r="1.6"/></svg>',
    "export": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.5v11"/><path d="M8 10.5l4 4 4-4"/><path d="M4.5 19.5h15"/></svg>',
    "actions": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 3.5 5 13h5l-1 7.5L18 11h-5z"/></svg>',
    "check": '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
}


def icon_card(svg_key, title, body, href=None):
    inner = (
        '<span class="card-icon">%s</span>'
        '<h3>%s</h3><p>%s</p>' % (ICON[svg_key], esc(title), body)
    )
    if href:
        return '<a class="card card--link" href="%s">%s<span class="card-more">Learn more</span></a>' % (
            attr(href), inner)
    return '<div class="card">%s</div>' % inner


def app_store_button(label="Get it on the Shopify App Store", extra=""):
    return '<a class="btn btn--primary %s" href="%s">%s</a>' % (extra, attr(APP_STORE_URL), esc(label))


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------
def header(active):
    items = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        items.append('<li><a href="%s"%s>%s</a></li>' % (attr(href), current, esc(label)))
    return """<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">
      <img src="/assets/logo-64.png" width="32" height="32" alt="" decoding="async">
      <span>SourceTrac</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      Menu
    </button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>
        %s
      </ul>
      <div class="nav-cta">
        <a class="btn btn--primary btn--sm" href="%s">Get it on the Shopify App Store</a>
      </div>
    </nav>
  </div>
</header>""" % ("\n        ".join(items), attr(APP_STORE_URL))


def footer():
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="footer-brand" href="/">
          <img src="/assets/logo-64.png" width="28" height="28" alt="" loading="lazy" decoding="async">
          <span>SourceTrac</span>
        </a>
        <p class="footer-note">A survey app for Shopify that shows which channels bring in revenue.</p>
      </div>
      <div>
        <h2>Pages</h2>
        <ul>
          <li><a href="/privacy">Privacy</a></li>
          <li><a href="/terms">Terms</a></li>
          <li><a href="/support">Support</a></li>
          <li><a href="/help">Help</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:%s">%s</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; %s %s</p>
      <p>SourceTrac works with Shopify.</p>
    </div>
  </div>
</footer>""" % (attr(EMAIL), esc(EMAIL), YEAR, esc(PUBLISHER))


def page(path, title, description, body, active="", head_extra="", canonical=None):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(path)s">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#3B2F8F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="%(site)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="/assets/icon-512.png">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="/assets/styles.css">
%(head_extra)s</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
<script src="/assets/site.js" defer></script>
</body>
</html>
""" % {
        "title": esc(title),
        "desc": attr(description),
        "path": attr(canonical if canonical is not None else path),
        "site": attr(SITE_NAME),
        "head_extra": head_extra,
        "header": header(active),
        "body": body,
        "footer": footer(),
    }
    return html


def write(rel_path, content):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    return full


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
PAGES = [
    ("/", "index.html", "SourceTrac — find out which channels bring in your sales",
     "Ask buyers how they found you, right after checkout, and see which channels bring in revenue. "
     "A survey app for Shopify. Free forever, no card needed.",
     "home", ""),
    ("/features", "features/index.html", "Features — SourceTrac",
     "Everything SourceTrac does: the survey on your checkout pages, eight question types, 50 "
     "templates, results per channel, CSV export and Shopify actions.",
     "features", ""),
    ("/templates", "templates/index.html", "50 survey templates — SourceTrac",
     "All 50 ready-made survey templates for Shopify, grouped by goal: where buyers find you, why "
     "they buy, delivery, loyalty and who your buyers are.",
     "templates", ""),
    ("/pricing", "pricing/index.html", "Pricing — SourceTrac",
     "Free forever, Growth at $4.99 a month and Scale at $9.99 a month. Every plan includes the full "
     "channel report. Billed through your Shopify invoice.",
     "pricing", ""),
    ("/help", "help/index.html", "Help and FAQ — SourceTrac",
     "Answers to the questions we are asked most about SourceTrac: creating a survey, the checkout "
     "block, missing revenue, refunds, the Free limit and cancelling.",
     "help", ""),
    ("/privacy", "privacy/index.html", "Privacy policy — SourceTrac",
     "What SourceTrac stores, what it never stores, how long it is kept, and how to have it removed.",
     "privacy", ""),
    ("/terms", "terms/index.html", "Terms of service — SourceTrac",
     "The terms of service for SourceTrac, published by SourceTrac Survey.",
     "terms", ""),
    ("/support", "support/index.html", "Support — SourceTrac",
     "Email SourceTrac support, and check the five things that explain a missing survey before you "
     "write.",
     "support", ""),
]


def build_all():
    import page_features
    import page_help
    import page_home
    import page_pricing
    import page_privacy
    import page_support
    import page_templates
    import page_terms

    builders = {
        "home": page_home.build_home,
        "features": page_features.build_features,
        "templates": page_templates.build_templates,
        "pricing": page_pricing.build_pricing,
        "help": page_help.build_help,
        "privacy": page_privacy.build_privacy,
        "terms": page_terms.build_terms,
        "support": page_support.build_support,
    }

    written = []
    for path, rel, title, desc, key, head_extra in PAGES:
        body = builders[key]()
        active = path if path != "/" else ""
        written.append(write(rel, page(path, title, desc, body, active, head_extra)))

    written.append(write("404.html", page(
        "/404.html", "Page not found — SourceTrac",
        "That page could not be found. Links to the main SourceTrac pages are below.",
        """<section class="section hero">
  <div class="wrap wrap--narrow">
    <div class="section-head">
      <h1>Page not found</h1>
      <p class="lede">That page could not be found. Try one of these instead.</p>
      <ul class="feature-list">
        <li><a href="/">Home</a></li>
        <li><a href="/features">Features</a></li>
        <li><a href="/templates">Templates</a></li>
        <li><a href="/pricing">Pricing</a></li>
        <li><a href="/help">Help and FAQ</a></li>
        <li><a href="/support">Support</a></li>
      </ul>
    </div>
  </div>
</section>""", "")))

    written.append(write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: /sitemap.xml\n"))
    urls = "".join("  <url><loc>%s</loc></url>\n" % (path if path != "/" else "/") for path, _, _, _, _, _ in PAGES)
    written.append(write("sitemap.xml",
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls))
    written.append(write("_headers", """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: geolocation=(), microphone=(), camera=(), interest-cohort=()

/assets/*
  Cache-Control: public, max-age=31536000, immutable
"""))
    return written


def make_icons():
    """Write favicon and app icon sizes from the uploaded square PNG."""
    try:
        from PIL import Image
    except ImportError:
        print("Pillow not installed: skipping icon sizes (the source PNG is still used).")
        return
    src = os.path.join(ROOT, "_src", "source", "sourcetrac-icon.png")
    if not os.path.exists(src):
        print("Source icon not found: %s" % src)
        return
    im = Image.open(src).convert("RGBA")
    targets = {
        "logo-64.png": 64,
        "favicon-32.png": 32,
        "favicon-48.png": 48,
        "icon-192.png": 192,
        "icon-512.png": 512,
        "apple-touch-icon.png": 180,
    }
    for name, size in targets.items():
        out = os.path.join(ROOT, "assets", name)
        im.resize((size, size), Image.LANCZOS).save(out, optimize=True)
        print("wrote %s (%dx%d)" % (name, size, size))


if __name__ == "__main__":
    make_icons()
    files = build_all()
    print("\nWrote %d files:" % len(files))
    for f in files:
        print("  %s" % os.path.relpath(f, ROOT))
