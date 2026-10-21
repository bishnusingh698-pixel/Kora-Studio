# -*- coding: utf-8 -*-
"""Features page body."""
from build import app_store_button, esc
from templates_data import TEMPLATE_GROUPS

def bullets(items, two_col=False):
    out = []
    for item in items:
        if isinstance(item, tuple):
            title, body = item
            out.append("<li><strong>%s</strong> %s</li>" % (esc(title), body))
        else:
            out.append("<li>%s</li>" % item)
    cls = "feature-list feature-list--2" if two_col else "feature-list"
    return '<ul class="%s">\n      %s\n    </ul>' % (cls, "\n      ".join(out))


def section(anchor, title, intro, body, alt=False):
    return """
<section class="section%s" id="%s">
  <div class="wrap">
    <div class="section-head">
      <h2>%s</h2>
      <p>%s</p>
    </div>
    %s
  </div>
</section>""" % (" section--alt" if alt else "", anchor, esc(title), intro, body)


def q(text):
    return "“%s”" % esc(text)


def build_features():
    # 1. The survey on your checkout pages
    checkout = bullets([
        ("Thank-you page, always on.", q("Right after checkout, when buyers are most likely to answer.")),
        ("Order status page, optional.",
         q("Also asks buyers who come back to check on their order. Needs Shopify's new customer accounts and the SourceTrac block on the Order status page.")
         + " The Order status page is where buyers land when they open “View your order” from their order emails."),
        ("Asked once per order.",
         q("Each order is asked once. If a buyer answers on one page, the survey is hidden on the other.")
         + " Buyers are never asked twice, even if they reload the page."),
        ("Never gets in the way.",
         "The survey appears after the order is placed and never blocks the page."),
        ("Looks like your store.",
         "The survey uses your store's own checkout styling automatically. You choose the title, the intro text and the button text."),
        ("Several surveys, one at a time.",
         "When more than one survey matches an order, the highest one in your list is shown. A survey ID setting on the block lets a block show one particular survey."),
        ("Shown one question at a time on a phone",
         ", if you choose."),
    ])

    # 2. Question types
    types = bullets([
        "Pick one (single choice)",
        "Pick several (multiple choice)",
        "Dropdown list",
        "Yes or no",
        "Rating 1 to 5",
        "Satisfaction (5-point)",
        "Recommend score (0 to 10, NPS)",
        "Written answer",
    ], two_col=True)
    extra = bullets([
        ("Follow-up questions:", "show a question only when an earlier answer matches."),
        (q("Other (please specify)") + ":",
         "buyers can type their own answer when none of the options fit."),
        (q("None of these") + ":",
         "an answer that can't be combined with others (full templates, Growth)."),
        "Answer options can be shown in random order.",
    ])
    question_types = (
        '<h3>Eight kinds of question, as named in the app</h3>%s'
        '<h3 style="margin-top:2rem">Extra options</h3>%s'
        '<p class="spec" style="margin-top:1.25rem">The editor\'s advice: %s</p>'
        % (types, extra, q("Keep it short. One to three questions get the most answers."))
    )

    # 3. Templates
    groups = []
    for group in TEMPLATE_GROUPS:
        groups.append(
            "<li><strong>%s</strong>: %s</li>" % (esc(group["title"]), q(group["desc"]))
        )
    templates = (
        '<p>%s</p>%s'
        '<p>Templates can be searched by word (for example NPS, gift, delivery, discount), and you '
        'can also start from scratch. <a href="/templates">See the full list of 50 templates</a>.</p>'
        % (q("Pick what you want to learn. Every template is ready to use, and you can change any question before it goes live."),
           bullets(groups, two_col=False))
    )

    # 4. Who sees it
    who = bullets([
        "<strong>Everyone, first-time buyers only, or returning buyers only</strong> (every plan).",
        'On Growth and Scale: %s' % q("Show a survey by order value, country, share of buyers or dates, and stop after a set number of answers."),
        "Dates follow your store's own calendar days.",
    ])

    # 5. Languages
    languages = bullets([
        "The app's admin is available in 10 languages: English, Deutsch (German), Français (French), Español (Spanish), Português (Brazilian Portuguese), 中文 (Simplified Chinese), 日本語 (Japanese), Italiano (Italian), Nederlands (Dutch) and Svenska (Swedish).",
        "%s Templates come translated into all 10 languages, and you can add your own translation for any text."
        % q("Buyers see the survey in their checkout language."),
    ])

    # 6. Results and reports
    honest = bullets([
        "Revenue is matched to real orders and kept separate for each currency. It is never added up across currencies.",
        "Refunded value is taken off, and cancelled and test orders are left out.",
        "An answer that arrives before Shopify sends the order is shown as waiting (“Pending”), never as $0.00.",
        "POS orders are left out of the answer rate, because they never see a Thank-you page.",
    ])
    results = bullets([
        ("Dashboard:", q("Your store at a glance: revenue by channel, customer scores and every survey.")
         + " Shows revenue, orders and average order value by channel, top channels, new vs returning buyers, every live survey's key result and a trend of answers over time, for the last 7, 30 or 90 days."),
        ("Channel report:", q("Which channels bring you buyers, and how much each one is worth.")
         + " A full table of channels with answers, revenue and average order value, plus “In buyers' own words”: what buyers wrote when none of your channels fit."),
        ("Results:", q("How buyers answered across your surveys.")
         + " For each survey: answers, answer rate, revenue and average order value, first-order vs returning buyers, and for each answer its share, revenue and average order value. An “All surveys” table compares every survey. Date range: 7, 30 or 90 days, or all time."),
        ("Customer scores:", "NPS is %s CSAT is the %s With no answers, no score is shown rather than a zero."
         % (q("Percent of promoters minus percent of detractors, from −100 to +100."),
            q("Share of answers that were 4 or 5 out of 5."))),
        ("How sure the results are:", "each result is labelled “Too early” (fewer than 30 answers), “Early signal”, “Getting clear” or “Reliable” (%s)."
         % q("More answers are unlikely to change the picture much")),
        ("Responses:", q("Every answer your buyers gave.")),
    ])
    results += '<h3 style="margin-top:2rem">Honest revenue</h3>' + honest

    # 7. Export
    export = bullets([
        ("All surveys:", q("One row per answer, with its survey and question.")
         + " Columns: survey, order, submitted_at, timezone, where, question, answer, order_total, currency, revenue_status, order_link."),
        ("One survey:", q("One row per buyer, with one column per question.")),
        ("Channel report only:", q("One row per order, with the channel the buyer chose.")
         + " Columns: order, submitted_at, timezone, channel, other_answer, order_total, currency, revenue_status, order_link."),
    ]) + '<p class="spec" style="margin-top:1.25rem">Times are in your store\'s time zone, and the file opens cleanly in Excel, including non-English text.</p>'

    # 8. Shopify actions
    tags = bullets([
        ("Order tags and customer tags:", "up to four each. <code>{channel}</code> becomes the buyer's answer, for example <code>source:{channel}</code>. A tag without a colon is written as <code>sourcetrac:tag</code>."),
        ("Metafields:", "write the answer to the order as the metafield <code>sourcetrac.channel</code>, or save a buyer's profile or reorder window to the customer."),
        ("Shopify Flow:", "start a workflow with the trigger “SourceTrac survey answered”. It gives you the order, Channel (a key such as <code>instagram</code>) and Channel label (what the buyer chose)."),
        ("Ready-made actions", "that come with templates. Order tags: <code>found:</code>, <code>heard:</code>, <code>trigger:</code>, <code>offer:</code>, <code>social:</code>, <code>delivery-check:</code>, <code>delivery-time:</code>, <code>fit:unsure</code>, <code>needs-by-date</code>, <code>first-order:low-rating</code> and <code>bulk-interest</code>. Customer tags: <code>nps:</code>, <code>gifter</code>, <code>gift-occasion:</code>, <code>reorder:</code>, <code>profile:</code>, <code>subscribe-interest:</code>, <code>referral:</code>, <code>buy-again:</code>, <code>eco:</code> and <code>moment:</code>. Customer metafields: <code>sourcetrac.profile</code> and <code>sourcetrac.reorder_window_days</code>."),
        "Tags are built from fixed answer keys, so a tag is the same in every language.",
        "Actions only run when your store has approved the permissions they need. Your survey collects and reports either way.",
    ])
    actions = (
        '<p>%s</p>%s'
        % (q("Tag orders and customers from their answers, save answers to metafields and start Shopify Flow."), tags)
    )

    # 9. Automation
    automation = bullets([
        ("Pause when results are reliable:", q("Pauses this survey once its first choice or score question has a clear answer: at least 100 answers with the top answer known to within 10%, or 150 answers for a rating or NPS question.")),
        ("Share space with other surveys:", q("Surveys with this on take turns on the Thank-you page: each order sees one of them, picked evenly.")),
    ])

    # 10. Inside your Shopify admin
    admin = bullets([
        "A <strong>SourceTrac attribution</strong> card on each order page shows “How they heard about us”.",
        "A card on each customer page shows the answer from their recent orders (about the last 60 days).",
    ])

    # 11. Help when a survey doesn't show
    help_section = bullets([
        ("Checkout check", "lists, for each page, whether a survey is live, whether the SourceTrac block has loaded, and what to do next."),
        ("Recent checkouts:", q("Each time the SourceTrac block loads on a buyer's Thank-you or Order status page, it's listed here with the survey it showed, or why it showed nothing. The last 20 are kept for 30 days.")),
        "The editor warns “Buyers can't see this survey yet” until the block has loaded, and opens the checkout editor for you.",
        "Unsaved survey changes can't be lost by accident.",
    ])

    return (
        """
<section class="section hero">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Features</span>
      <h1>Everything SourceTrac does</h1>
      <p class="lede">A short survey after checkout, and honest revenue per channel. Everything below is included from the Free plan unless a plan is named.</p>
      <div class="btn-row">
        %(app)s
        <a class="btn btn--ghost" href="/templates">See the 50 templates</a>
      </div>
    </div>
  </div>
</section>
""" % {"app": app_store_button()}
        + section("survey", "The survey on your checkout pages",
                  "Where the survey appears, and how it behaves.", checkout)
        + section("questions", "Question types",
                  "Ask the way that suits your store.", question_types, alt=True)
        + section("templates", "50 ready-made templates",
                  "Grouped by what you want to learn.", templates)
        + section("who", "Who sees it",
                  "Choose who is asked, and narrow it further on paid plans.", who, alt=True)
        + section("languages", "Languages",
                  "The admin and the survey follow your buyers' language.", languages)
        + section("results", "Results and reports",
                  "Everything you need to see which channels earn revenue.", results, alt=True)
        + section("export", "Export", q("Download every answer as a spreadsheet.")
                  + " Choose what to download:", export)
        + section("actions", "Shopify actions (Scale plan)",
                  "Copy answers into your own Shopify store.", actions, alt=True)
        + section("automation", "Automation (Scale plan)",
                  "Let a survey pause itself, or share the Thank-you page with others.", automation)
        + section("admin", "Inside your Shopify admin",
                  "Answers where you already work.", admin, alt=True)
        + section("troubleshooting", "Help when a survey doesn't show",
                  "If a survey is not appearing, these tools show why.", help_section)
        + """
<section class="section section--tight">
  <div class="wrap">
    <div class="band band--mint">
      <h2>Ready to ask your buyers?</h2>
      <div class="btn-row">
        %s
      </div>
    </div>
  </div>
</section>
""" % app_store_button()
    )
