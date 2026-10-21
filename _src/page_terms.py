# -*- coding: utf-8 -*-
"""Terms of service page body."""
from build import TERMS_UPDATED, esc

SECTIONS = [
    ("What SourceTrac is",
     ["SourceTrac is a survey app for Shopify, published by SourceTrac Survey. It adds a short "
      "survey to your Thank-you page, and optionally to the Order status page, and shows you which "
      "channels bring in revenue.",
      "You may use SourceTrac if you are a Shopify merchant who installs it, and if you are allowed "
      "to agree to these terms for your store."]),
    ("Plans and billing",
     ["SourceTrac has a Free plan and the paid Growth and Scale plans. The features of each plan "
      "and the prices are set out on the Pricing page.",
      "Paid plans are billed through Shopify. Charges appear on your Shopify invoice alongside your "
      "other app subscriptions. SourceTrac never stores your card details. Shopify handles the "
      "payment and tells us when a subscription starts, changes or ends.",
      "Yearly billing costs 10% less than paying monthly and is charged once a year. An upgrade, or "
      "a switch to yearly, replaces your current charge once you approve it in Shopify. A downgrade, "
      "or a switch from yearly to monthly, starts when your current billing period ends.",
      "Prices are in USD."]),
    ("Changing or cancelling your plan",
     ["You can change or cancel any time on the Plans page.",
      "If you cancel, your answers stay saved and Shopify credits the unused part of your billing "
      "period. On the Free plan only your top live survey keeps showing to buyers, Shopify tags, "
      "metafields and Flow stop, and answers past 50 in a month are kept but marked over the limit.",
      "If you reach the Free plan's monthly answer limit, answers keep being collected, stored and "
      "counted in your dashboard totals. Nothing is hidden. Upgrading only removes the monthly limit."]),
    ("Your responsibilities",
     ["You are responsible for your store and for the questions your survey asks. Ask questions "
      "that do not invite personal details such as names or emails.",
      "You are responsible for mentioning the survey in your own store's privacy policy. Because you "
      "decide what your survey asks, you are the controller of your buyers' data and SourceTrac "
      "processes it for you.",
      "You must only use SourceTrac in the way Shopify and the law allow."]),
    ("Data and privacy",
     ["Our privacy policy at /privacy forms part of these terms. It explains what SourceTrac "
      "stores, how long it is kept, and how to have it removed.",
      "When you uninstall SourceTrac we delete your access tokens immediately. Shopify sends a "
      "redaction request 48 hours after uninstall, and we delete your shop's stored data when it "
      "arrives."]),
    ("Availability",
     ["SourceTrac is provided as is. We work to keep it running, but we do not guarantee "
      "uninterrupted or error-free availability. Shopify, and the way checkout works on Shopify, "
      "can change. Some features need permissions your store must approve, and some need Shopify's "
      "new customer accounts.",
      "We may change or stop parts of the service. If we make a material change to these terms, we "
      "will update this page and its date."]),
    ("Limitation of liability",
     ["To the extent the law allows, SourceTrac Survey is not liable for indirect or consequential "
      "loss, or for lost profits, lost sales or lost data, arising from your use of SourceTrac.",
      "SourceTrac does not promise any particular business result from the answers your buyers give."]),
    ("Changes to these terms",
     ["We may update these terms from time to time. The date at the top of this page shows when "
      "they last changed. If you keep using SourceTrac after a change, you accept the updated terms."]),
    ("Contact",
     ["Questions about these terms? Email sourcetracsupport@gmail.com."]),
]


def build_terms():
    parts = []
    for title, paragraphs in SECTIONS:
        body = "\n      ".join("<p>%s</p>" % esc(p) for p in paragraphs)
        parts.append("<h2>%s</h2>\n      %s" % (esc(title), body))
    return """
<section class="section hero">
  <div class="wrap wrap--narrow">
    <div class="section-head">
      <span class="eyebrow">Terms</span>
      <h1>Terms of service</h1>
      <p class="lede">Published by SourceTrac Survey. Last updated: %s</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow prose">
    %s
  </div>
</section>
""" % (esc(TERMS_UPDATED), "\n\n    ".join(parts))
