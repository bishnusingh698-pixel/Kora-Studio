# SourceTrac website source

The site is plain static HTML in the repository root. It is ready to upload to Netlify as is.

`_src/` holds the generator used to produce the HTML. It is not needed on the web server.

## Editing content

- `_src/templates_data.py` — the 50 template names, descriptions, plans and questions
- `_src/faq_data.py` — the Help page questions and answers
- `_src/privacy_data.py` — the privacy policy and the merchant detail text
- `_src/page_*.py` — the body of each page
- `_src/build.py` — site-wide values (app store link, email, year) and the page shell

## Rebuilding

```
python3 _src/build.py
```

This regenerates every HTML file, `404.html`, `sitemap.xml`, `robots.txt` and the
icon sizes in `assets/` from the uploaded `assets/sourcetrac-icon.png`.
It needs Pillow (`pip install Pillow`) only for the icon sizes.

## Before publishing

Set `APP_STORE_URL` in `_src/build.py` to the real App Store listing URL, then rebuild.
