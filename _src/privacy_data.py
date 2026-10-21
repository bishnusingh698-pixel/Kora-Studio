# -*- coding: utf-8 -*-
"""Privacy policy text, used word for word as supplied by the app."""

POLICY_UPDATED = "15 October 2026"

POLICY_INTRO = (
    "SourceTrac is a survey app for Shopify. It asks your buyers a short survey after checkout "
    "and shows you which channels bring in revenue. This page explains what we store and how to "
    "have it removed."
)

# Each block: ("h2", text) | ("p", text) | ("ul", [items])
POLICY_BLOCKS = [
    ("h2", "What we store"),
    ("p", "We keep the smallest set of data needed to attribute an order to a channel:"),
    ("ul", [
        "the Shopify order ID and order number",
        "the answers the buyer gave, including any text they typed",
        "the time of the answer and the page it was given on",
        "the order total, currency, sales channel (such as online store or POS) and status (paid, refunded, cancelled or test), read from the order",
        "the buyer's checkout country and language",
        "the products in the order, and whether it was the buyer's first order",
    ]),
    ("h2", "What we do not store"),
    ("p", "We do not store names, email addresses, phone numbers, postal addresses, or payment "
          "details. We never see card numbers. We do not use the data for advertising, profiling, "
          "or resale, and we do not sell it."),
    ("h2", "Why we store it"),
    ("p", "To show you, the merchant, which marketing channels earn revenue. No other merchant can "
          "see it. It leaves SourceTrac only when you download a CSV export, or when you turn on "
          "Shopify actions, which copy answers into your own store as order tags, customer tags, "
          "customer metafields or a Shopify Flow trigger."),
    ("h2", "How long we keep it"),
    ("p", "Survey answers and cached orders are deleted after 24 months, and webhook delivery "
          "records (which hold no order or buyer details) after 30 days, as is the “Recent "
          "checkouts” list merchants see (which survey each order was shown, with its country). "
          "These periods are fixed and the same for every store."),
    ("h2", "Deletion"),
    ("p", "When you uninstall SourceTrac we delete your access tokens immediately. Shopify sends a "
          "redaction request 48 hours after uninstall, and we delete your shop's stored data when "
          "it arrives."),
    ("p", "A buyer can ask for their data to be removed through you, the merchant. We act on that "
          "request through Shopify's mandatory compliance webhooks. When Shopify sends a redaction "
          "request naming a buyer's orders, we delete the matching survey answers and cached order "
          "rows, and only those."),
    ("h2", "Who processes the data"),
    ("ul", [
        "Neon — database hosting",
        "Render — application hosting",
        "Shopify — the platform the data comes from",
    ]),
    ("h2", "Your rights"),
    ("p", "Depending on where you live, you may have the right to access, correct, export, or "
          "delete your personal data, or to object to its processing. Because SourceTrac does not "
          "collect identifying buyer data, most requests are handled by the merchant who installed "
          "the app. To make a request about data held by SourceTrac, contact us at the address below."),
    ("h2", "Contact"),
    ("p", "For privacy questions, email sourcetracsupport@gmail.com."),
]

# In-app "Privacy and data" page, word for word.
MERCHANT_DETAIL = [
    ("About your store.", "SourceTrac also keeps your shop domain and the Shopify session the app needs to run."),
    ("Typed answers.", "Typed answers are stored exactly as the buyer wrote them. Ask questions that don't invite personal details such as names or emails."),
    ("Who can see it and where it is kept.", "You and the staff you allow to use the app. The app runs on Render and the database is hosted by Neon. Data is sent over encrypted connections, and the Shopify access token is encrypted when stored."),
    ("Buyers' rights.", "Buyers ask you, not SourceTrac, and Shopify forwards their requests to us. When a buyer asks for their data, we look up their answers and list the request on the Settings page. When a buyer asks to be erased, we delete their answers automatically."),
    ("Shopify actions.", "Shopify actions copy answers into your Shopify store as order tags, customer tags or customer metafields. They then follow Shopify's rules for your store data, not SourceTrac's deletion schedule."),
    ("CSV exports.", "The file contains order numbers, answers and order totals, and any text buyers typed. Keep it as safely as your other store records."),
    ("For your privacy policy.", "You decide what your survey asks, so for your buyers' data you are the controller and SourceTrac processes it for you. Mention the survey in your store's privacy policy. You can adapt this text:"),
]

MERCHANT_QUOTE = (
    "After checkout we may ask you a short optional survey, such as how you heard about us. Your "
    "answers are stored with your order number by our survey provider, SourceTrac, for up to 24 "
    "months, and are used only to understand which channels bring us customers. They are never "
    "sold or used for advertising."
)
