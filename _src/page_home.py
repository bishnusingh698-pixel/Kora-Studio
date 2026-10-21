# -*- coding: utf-8 -*-
"""Home page body."""
from build import ICON, app_store_button, esc

SURVEY_OPTIONS = [
    ("Instagram", True),
    ("Google search", False),
    ("A friend or family member", False),
    ("Podcast", False),
]

INTRO_PARAGRAPH = (
    "SourceTrac adds a short survey to your Thank-you page, and optionally to the Order status "
    "page. Each answer is tied to its order, so you see orders, revenue and average order value "
    "per channel, kept separate for each currency. Start from a ready-made template or write your "
    "own questions with follow-ups. Export answers to CSV. On Scale, answers can tag orders and "
    "customers, set a customer metafield, or start a Shopify Flow workflow."
)

STEPS = [
    ("Create your survey.",
     "Pick a template, adjust the questions in your own words and press Go live."),
    ("Add the block to your Thank-you page.",
     "In Shopify's checkout editor, choose Thank you from the page menu at the top, add the "
     "“SourceTrac survey” block and press Save. You only do this once."),
    ("Answer it with a test order.",
     "Place a test order and answer the survey on the Thank-you page. Each order is asked only "
     "once, so use a new order for every test. Your answer appears here within a minute."),
    ("Read your results.",
     "Results groups answers by question and shows the revenue behind each channel."),
]

HIGHLIGHTS = [
    ("survey", "A survey on your Thank-you page",
     "With an optional Order status page block, right after checkout."),
    ("revenue", "Revenue per channel",
     "Revenue, orders and average order value per channel, by currency."),
    ("templates", "50 ready-made templates",
     "Every template comes with follow-up questions you can change."),
    ("score", "NPS and CSAT scores",
     "See how happy buyers are and who would recommend you."),
    ("export", "CSV export of every answer",
     "Download every answer as a spreadsheet, with times in your store's time zone."),
    ("actions", "Tags, metafields and Flow (Scale)",
     "Order and customer tags, metafields and a Shopify Flow trigger."),
]


def survey_illustration():
    rows = []
    for label, picked in SURVEY_OPTIONS:
        cls = ' class="is-picked"' if picked else ""
        rows.append(
            '<li%s><span class="dot" aria-hidden="true"></span><span>%s</span></li>'
            % (cls, esc(label))
        )
    rows.append(
        '<li><span class="dot" aria-hidden="true"></span><span>Other (please specify)</span></li>'
    )
    return """<div class="survey-illo">
      <div class="survey-card" role="img" aria-label="Illustration of a SourceTrac survey card shown on a Thank-you page, asking: Where did you first hear about us?">
        <span class="survey-card__label">Thank-you page survey</span>
        <p class="survey-card__q">Where did you first hear about us?</p>
        <ul class="survey-opts">
          %s
        </ul>
        <span class="survey-submit">Submit</span>
      </div>
      <p class="survey-caption">A drawn example. Your survey uses your store's own checkout styling.</p>
    </div>""" % ("\n          ".join(rows))


def plan_cards_short():
    """Three plan cards in short form, matching the pricing page."""
    cards = [
        ("Free", "$0", "Free forever, no card needed",
         "For trying SourceTrac, or stores with a few orders a month.",
         ["Collect up to 50 answers a month", "1 live survey at a time",
          "Every template in its short version"], False, ""),
        ("Growth", "$4.99", "a month",
         "For most stores: ask every buyer, with no monthly limit.",
         ["Unlimited answers, no monthly limit", "Up to 10 live surveys at a time",
          "The full version of every template"], True, "Recommended"),
        ("Scale", "$9.99", "a month",
         "For stores that want answers to tag orders and customers automatically.",
         ["All your surveys live at once (up to 50)",
          "Tag orders and customers from their answers",
          "Stop a survey on its own once the answer is clear"], False, ""),
    ]
    out = []
    for name, price, suffix, blurb, points, featured, tag in cards:
        items = "".join("<li>%s</li>" % esc(p) for p in points)
        tag_html = '<span class="plan__tag">%s</span>' % esc(tag) if tag else ""
        out.append("""<div class="plan%s">
        %s
        <h3 class="plan__name">%s</h3>
        <p class="plan__price plan__price--free">%s <small>%s</small></p>
        <p class="plan__for">%s</p>
        <ul>%s</ul>
      </div>""" % (" plan--featured" if featured else "", tag_html, esc(name), esc(price), esc(suffix), esc(blurb), items))
    return '<div class="plans">\n      %s\n    </div>' % ("\n      ".join(out))


def build_home():
    steps = []
    for title, body in STEPS:
        steps.append("<li><h3>%s</h3><p>%s</p></li>" % (esc(title), esc(body)))

    highlights = []
    for svg_key, title, body in HIGHLIGHTS:
        highlights.append(
            '<a class="card card--link" href="/features">'
            '<span class="card-icon">%s</span><h3>%s</h3><p>%s</p>'
            '<span class="card-more">Learn more</span></a>'
            % (ICON[svg_key], esc(title), esc(body))
        )

    return """
<section class="section hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Find out which channels actually bring in your sales.</h1>
      <p class="lede">Ask buyers how they found you, right after checkout, and see which channels bring in revenue.</p>
      <div class="btn-row">
        %(app)s
        <a class="btn btn--ghost" href="/pricing">See pricing</a>
      </div>
      <p class="hero-note"><strong>Free forever, no card needed.</strong> Paid plans from $4.99 a month.</p>
    </div>
    %(illo)s
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <h2>What SourceTrac does</h2>
    </div>
    <p>%(intro)s</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Get started</span>
      <h2>How it works</h2>
      <p>Four steps, and you only set up the checkout block once.</p>
    </div>
    <ol class="steps">
      %(steps)s
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What you get</h2>
      <p>Everything below is included from the Free plan unless a plan is named.</p>
    </div>
    <div class="grid grid--3">
      %(highlights)s
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="band">
      <h2>SourceTrac collects only what it needs to show which channels bring you sales.</h2>
      <p>It never stores buyer names, emails, phone numbers, addresses or payment details.</p>
      <p><a href="/privacy">See what SourceTrac stores</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Plans</h2>
      <p>Every plan includes the full channel report. Paid plans remove the monthly answer limit.</p>
    </div>
    %(plans)s
    <p style="margin-top:1.5rem"><a href="/pricing">See full pricing and what each plan includes</a></p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="note-box">
      <h3>Requirements</h3>
      <p>Works on every Shopify plan except Shopify Starter, where Shopify does not offer checkout blocks. The Order status page block needs Shopify's new customer accounts.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="band band--mint">
      <h2>Ask your next buyer how they found you.</h2>
      <div class="btn-row">
        %(app)s
      </div>
    </div>
  </div>
</section>
""" % {
        "app": app_store_button(),
        "illo": survey_illustration(),
        "intro": esc(INTRO_PARAGRAPH),
        "steps": "\n      ".join(steps),
        "highlights": "\n      ".join(highlights),
        "plans": plan_cards_short(),
    }
