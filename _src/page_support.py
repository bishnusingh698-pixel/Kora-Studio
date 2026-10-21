# -*- coding: utf-8 -*-
"""Support page body."""
from build import EMAIL, attr, esc

SUBJECT = "Support request: SourceTrac"
BODY = "Shop:\nPlan:\nPage:\n\n\nDescribe your question or problem here:"

CHECKLIST = [
    "The survey is live in SourceTrac.",
    "The “SourceTrac survey” block is on the Thank you page in Shopify's checkout editor "
    "(Settings › Checkout › Customize, then Thank you in the page menu), and the editor is saved.",
    "You are testing with a new order, because each order is asked only once.",
    "Your store is not on the Shopify Starter plan.",
    "For the Order status page: your store uses Shopify's new customer accounts, and the block is "
    "added on that page too.",
]


def build_support():
    from urllib.parse import quote
    mailto = "mailto:%s?subject=%s&body=%s" % (
        EMAIL, quote(SUBJECT), quote(BODY))
    items = "\n      ".join("<li>%s</li>" % esc(c) for c in CHECKLIST)

    return """
<section class="section hero">
  <div class="wrap wrap--narrow">
    <div class="section-head">
      <span class="eyebrow">Support</span>
      <h1>Support</h1>
      <p class="lede">Questions or problems? Email us and we'll help.</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow">
    <div class="copybox">
      <div class="copybox__head">
        <h2 style="font-size:1.0625rem;margin:0">Email us</h2>
      </div>
      <p class="email-display" id="support-email">%s</p>
      <div class="copy-field">
        <button class="btn btn--ghost btn--sm" type="button" data-copy="#support-email" data-copy-status="#copy-status">Copy</button>
        <a class="btn btn--primary btn--sm" href="%s" target="_blank" rel="noopener noreferrer" data-gmail data-mailto="%s">Write in Gmail</a>
        <a class="btn btn--ghost btn--sm" href="%s">Use my email app</a>
      </div>
      <p class="copy-status" id="copy-status" role="status" data-label="Email address copied"></p>
      <div class="prefill">
        <p class="tpl__q-label">These details are filled in for you</p>
        <pre>Subject: %s

%s</pre>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow">
    <h2>Before you write</h2>
    <p>The fastest fix for a missing survey is usually the checkout editor check.</p>
    <ul class="feature-list">
      %s
    </ul>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow">
    <div class="note-box">
      <p><strong>Tip.</strong> In the app, Surveys › Checkout check and Recent checkouts show why a survey did or didn't show on a recent order.</p>
    </div>
    <p class="spec" style="margin-top:1.25rem">More answers are on the <a href="/help">Help and FAQ page</a>.</p>
  </div>
</section>
""" % (esc(EMAIL), attr(mailto), attr(mailto), attr(mailto), esc(SUBJECT), esc(BODY), items)
