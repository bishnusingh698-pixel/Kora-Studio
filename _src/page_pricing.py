# -*- coding: utf-8 -*-
"""Pricing page body."""
from build import app_store_button, esc

PLANS = [
    {
        "name": "Free",
        "monthly": "$0",
        "yearly": "$0",
        "suffix": "a month",
        "suffix_yearly": "a month",
        "featured": False,
        "tag": "",
        "note": "Free forever, no card needed",
        "for": "For trying SourceTrac, or stores with a few orders a month.",
        "points": [
            "Collect up to 50 answers a month",
            "1 live survey at a time",
            "Follow-up questions, and surveys for first-time or returning buyers",
            "See which channels bring in sales, with revenue and average order value for each",
            "Compare the last 7, 30 or 90 days",
            "Download every answer as a spreadsheet (CSV)",
            "Every template in its short version, and the full “How did you hear about us?” survey",
        ],
    },
    {
        "name": "Growth",
        "monthly": "$4.99",
        "yearly": "$4.49",
        "suffix": "a month",
        "suffix_yearly": "a month, billed yearly",
        "strike": "$4.99",
        "total": "$53.89 billed once a year",
        "save": "You save $5.99 a year (10%)",
        "featured": True,
        "tag": "Recommended",
        "note": "For most stores: ask every buyer, with no monthly limit.",
        "for": "For most stores: ask every buyer, with no monthly limit.",
        "points": [
            "Unlimited answers, no monthly limit",
            "Everything in Free, plus:",
            "Up to 10 live surveys at a time",
            "The full version of every template, including “None of these” answers and results by product",
            "Show a survey by order value, country, share of buyers or dates, and stop after a set number of answers",
        ],
    },
    {
        "name": "Scale",
        "monthly": "$9.99",
        "yearly": "$8.99",
        "suffix": "a month",
        "suffix_yearly": "a month, billed yearly",
        "strike": "$9.99",
        "total": "$107.89 billed once a year",
        "save": "You save $11.99 a year (10%)",
        "featured": False,
        "tag": "",
        "note": "For stores that want answers to tag orders and customers automatically.",
        "for": "For stores that want answers to tag orders and customers automatically.",
        "points": [
            "Unlimited answers, no monthly limit",
            "Everything in Growth, plus:",
            "All your surveys live at once (up to 50)",
            "Tag orders and customers from their answers, save answers to metafields and start Shopify Flow",
            "Stop a survey on its own once the answer is clear, and rotate several surveys",
        ],
    },
]

REASSURANCE = [
    "Change or cancel any time on the Plans page",
    "Billed on your Shopify invoice",
    "Your answers stay if you downgrade",
]


def plan_card(plan):
    points = "".join("<li>%s</li>" % esc(p) for p in plan["points"])
    tag = '<span class="plan__tag">%s</span>' % esc(plan["tag"]) if plan["tag"] else ""
    if plan["monthly"] == "$0":
        price_block = (
            '<p class="plan__price plan__price--free" data-amount data-no-billing data-monthly="$0" data-yearly="$0">$0 <small>a month</small></p>'
        )
        extra = '<p class="plan__billing">%s</p>' % esc(plan["note"])
    else:
        price_block = (
            '<p class="plan__price" data-amount data-monthly="%s" data-yearly="%s">%s <small>a month</small></p>'
            % (esc(plan["monthly"]), esc(plan["yearly"]), esc(plan["monthly"]))
        )
        extra = (
            '<p class="plan__strike-wrap" data-strike hidden><span class="plan__strike">%s</span> a month</p>'
            '<p class="plan__billing" data-billing hidden>%s</p>'
            '<p class="plan__save" data-save hidden>%s</p>'
            % (esc(plan["strike"]), esc(plan["total"]), esc(plan["save"]))
        )
    return """<div class="plan%s">
        %s
        <h2 class="plan__name">%s</h2>
        %s
        %s
        <p class="plan__for">%s</p>
        <ul>%s</ul>
        %s
      </div>""" % (
        " plan--featured" if plan["featured"] else "",
        tag,
        esc(plan["name"]),
        price_block,
        extra,
        esc(plan["for"]),
        points,
        app_store_button("Get it on the Shopify App Store", "btn--sm"),
    )


def build_pricing():
    cards = "\n      ".join(plan_card(p) for p in PLANS)
    reassure = "".join("<li>%s</li>" % esc(r) for r in REASSURANCE)

    return """
<section class="section hero">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h1>Plans</h1>
      <p class="lede">Every plan includes the full channel report. Paid plans remove the monthly answer limit.</p>
    </div>
    <div class="toggle-wrap">
      <div class="toggle" data-price-toggle role="group" aria-label="Billing period">
        <button type="button" data-period="monthly" aria-pressed="true">Monthly</button>
        <button type="button" data-period="yearly" aria-pressed="false">Yearly</button>
      </div>
      <p class="save-note">Save 10%% with yearly</p>
    </div>
    <div class="plans">
      %s
    </div>
    <ul class="reassure">
      %s
    </ul>
    <p class="spec" style="margin-top:1.5rem">Prices are in USD.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap wrap--narrow prose">
    <h2>How billing works</h2>
    <p>Charges appear on your Shopify invoice alongside your other app subscriptions. SourceTrac never stores your card details — Shopify handles the payment and tells us when a subscription starts, changes or ends.</p>

    <h2>Yearly billing</h2>
    <p>Yearly billing costs 10%% less than paying monthly and is charged once a year. An upgrade, or a switch to yearly, replaces your current charge once you approve it in Shopify. A downgrade, or a switch from yearly to monthly, starts when your current billing period ends.</p>

    <h2>If you reach the Free limit</h2>
    <p>Answers keep being collected, stored and counted in your dashboard totals. Nothing is hidden. Upgrading only removes the monthly limit.</p>

    <h2>If you cancel</h2>
    <p>Your answers stay saved. Shopify credits the unused part of your billing period. On Free only your top live survey keeps showing to buyers, Shopify tags, metafields and Flow stop, and answers past 50 this month are kept but marked over the limit.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="band band--mint">
      <h2>Start free, upgrade when you need more.</h2>
      <div class="btn-row">
        %s
        <a class="btn btn--ghost" href="/help">Read the FAQ</a>
      </div>
    </div>
  </div>
</section>
""" % (cards, reassure, app_store_button())
