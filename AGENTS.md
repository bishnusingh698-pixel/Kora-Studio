# SourceTrac website

Static marketing site for SourceTrac, a survey app for Shopify merchants.
Published by **SourceTrac Survey**. Sole contact: sourcetracsupport@gmail.com.

## Build

```
python3 _src/build.py     # regenerate all HTML + icons
```

Published output is the repository root: `index.html`, `<page>/index.html`,
`404.html`, `sitemap.xml`, `robots.txt`, `_headers`, `assets/`.
`_src/` is generator source and is not part of the deployed site.

Pillow is needed only to resize the source icon.

## Where content lives

- `_src/templates_data.py` — 50 templates: name, description, plan label, questions
- `_src/faq_data.py` — Help page Q&A (15 items)
- `_src/privacy_data.py` — privacy policy and merchant detail text
- `_src/page_*.py` — per-page body markup
- `_src/build.py` — page shell, nav, footer, `APP_STORE_URL`, meta tags
- `_src/source/sourcetrac-icon.png` — the uploaded app icon (source for all sizes)

## Rules that must not be broken

- Copy text verbatim. Much of it is quoted from the app; do not reword it.
- Never invent statistics, reviews, testimonials, awards, competitor names,
  customer logos or press mentions. No "most popular", "best", "#1" claims.
  The only allowed plan label is "Recommended" on Growth.
- Do not put "Shopify" in the app or business name. Saying it works with
  Shopify is fine. Do not use the Shopify logo.
- No screenshots of the app. Illustrations only.
- No analytics, cookies, tracking, sign-in or external requests. Everything is
  self-hosted (Inter fonts are in `assets/fonts`).
- Each page needs its own title and meta description; one `h1` per page and no
  skipped heading levels.

## Verification

There is no test suite in the repo. Checks used when building this:

- all internal links resolve; every `img` has `alt`; one `h1` per page
- no skipped heading levels; no horizontal scroll at 320 px and 390 px
- colour contrast at or above WCAG AA in both light and dark mode
- pricing toggle, template search, FAQ details and copy buttons work

If you change content, re-run the build and re-check those points.
