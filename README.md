# Kora Studio website

Static marketing site for Kora Studio, an independent studio that makes apps for
Shopify merchants. The first app is SourceTrac.

## Structure

- `index.html` — home (studio overview, our apps grid, how we build, contact)
- `sourcetrac/index.html` — SourceTrac app page (how it works, features, pricing, FAQ)
- `privacy/index.html` — privacy policy (also reachable at `/sourcetrac/privacy`)
- `terms/index.html` — terms of service
- `support/index.html` — support page
- `assets/styles.css`, `assets/site.js` — shared styles and the theme/menu script
- `assets/sourcetrac-icon.png` — SourceTrac app icon

No build step. Netlify can publish the repository root as plain files
(`netlify.toml` sets `publish = "."`).

## Placeholders to fill in before launch

Search the site for these and replace them:

| Placeholder | Where |
| --- | --- |
| `[APP STORE LISTING URL]` | home, SourceTrac page |
| `[LEGAL BUSINESS NAME]` | privacy policy, terms |
| `[CONTACT ADDRESS]` | privacy policy |
| `[ADD OR CONFIRM SUB-PROCESSORS AND REGIONS]` | privacy policy |
| `[COUNTRY / GOVERNING LAW]` | terms |
| `[DATE]` | privacy policy, terms |
| `[YEAR]` | footer on every page |

`[YEAR]` can be replaced with a literal year or wired up to a build step if one is
added later.

## Notes

- The SourceTrac icon in `assets/sourcetrac-icon.png` is a temporary placeholder.
  Replace it with the final square PNG at the same path and keep the `alt` text
  accurate.
- The site has no analytics, no cookies and no tracking scripts.
- A Monthly / Yearly toggle on the pricing table is done with CSS only
  (`:has()` plus radio inputs), so it works without extra JavaScript.
