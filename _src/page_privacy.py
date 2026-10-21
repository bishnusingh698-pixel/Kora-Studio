# -*- coding: utf-8 -*-
"""Privacy policy page body."""
from build import esc
from privacy_data import (MERCHANT_DETAIL, MERCHANT_QUOTE, POLICY_BLOCKS,
                          POLICY_INTRO, POLICY_UPDATED)

def render_policy():
    out = []
    for kind, value in POLICY_BLOCKS:
        if kind == "h2":
            out.append("<h2>%s</h2>" % esc(value))
        elif kind == "p":
            out.append("<p>%s</p>" % esc(value))
        elif kind == "ul":
            items = "".join("<li>%s</li>" % esc(v) for v in value)
            out.append("<ul>%s</ul>" % items)
    return "\n    ".join(out)


def render_merchant():
    parts = []
    for lead, body in MERCHANT_DETAIL:
        parts.append("<p><strong>%s</strong> %s</p>" % (esc(lead), esc(body)))
    parts.append('<blockquote><p>“%s”</p></blockquote>' % esc(MERCHANT_QUOTE))
    return "\n      ".join(parts)


def plain_merchant_text():
    """Plain text for the copy button, matching the box exactly."""
    lines = []
    for lead, body in MERCHANT_DETAIL:
        lines.append("%s %s" % (lead, body))
        lines.append("")
    lines.append("“%s”" % MERCHANT_QUOTE)
    return "\n".join(lines)


def build_privacy():
    return """
<section class="section hero">
  <div class="wrap wrap--narrow">
    <div class="section-head">
      <span class="eyebrow">Privacy</span>
      <h1>SourceTrac privacy policy</h1>
      <p class="lede">Last updated: %s</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow prose">
    <p>%s</p>
    %s
  </div>
</section>

<section class="section section--alt">
  <div class="wrap wrap--narrow">
    <h2>More detail for merchants</h2>
    <p>This is the same text as the “Privacy and data” page inside the app.</p>
    <div class="copybox">
      <div class="copybox__head">
        <h3>Privacy and data</h3>
        <button class="btn btn--ghost btn--sm" type="button" data-copy="#merchant-text" data-copy-status="#merchant-status">Copy</button>
      </div>
      <div class="copybox__body" id="merchant-text">
      %s
      </div>
      <p class="copy-status" id="merchant-status" role="status" data-label="Copied to clipboard"></p>
      <p class="visually-hidden" id="merchant-plain">%s</p>
    </div>
    <p class="spec" style="margin-top:1.5rem">See also the <a href="/terms">terms of service</a>.</p>
  </div>
</section>
""" % (esc(POLICY_UPDATED), esc(POLICY_INTRO), render_policy(), render_merchant(), esc(plain_merchant_text()))
