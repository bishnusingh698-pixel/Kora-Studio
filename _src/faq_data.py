# -*- coding: utf-8 -*-
"""Help page FAQ. Answers are used exactly as supplied by the app."""

FAQ = [
    (
        "How do I create my survey?",
        "Go to Surveys and choose New survey. Pick a template or start from scratch, edit the questions and press Go live. To show it to buyers, in Shopify admin go to Settings › Checkout, click Customize, choose Thank you from the page menu at the top, add the “SourceTrac survey” block and press Save. You only add the block once.",
    ),
    (
        "Why is the question not showing on my thank-you page?",
        "Four things are worth checking. First, the survey must be live in SourceTrac. Second, the “SourceTrac survey” block must be on the Thank you page in Shopify's checkout editor (Settings › Checkout › Customize, then Thank you in the page menu), and the editor saved. Third, each order is asked only once: an order that already answered never shows the survey again, so test with a new order. Fourth, Shopify does not offer the Thank you page block on the Starter plan.",
    ),
    (
        "I answered once and now the survey doesn't show. Why?",
        "Each order is asked only once. After an answer, SourceTrac never shows that order the survey again, even if the page is reloaded, so buyers are never asked twice. To test again, place a new order.",
    ),
    (
        "Can the survey also show on the Order status page?",
        "Yes, as an optional extra. The Order status page is where buyers land when they open “View your order” from their order emails. Tick it under “Where it shows” in the survey, then in the checkout editor choose Order status from the page menu, add the “SourceTrac survey” block and press Save. It's in the menu only if your store uses Shopify's new customer accounts (Settings › Customer accounts). Each order is still asked only once.",
    ),
    (
        "Why is one of my answers missing revenue?",
        "The buyer answered a moment before Shopify sent us the order, so we had their answer but not the order value yet. Revenue usually appears within a minute. If it is still missing after a day, the answer is shown as waiting rather than counted as zero, so your totals stay honest.",
    ),
    (
        "What happens to refunded orders?",
        "Refunded value is subtracted from the order total before it is attributed, so a refunded order contributes little or nothing. Cancelled and test orders are excluded from revenue entirely. Test orders are also excluded from your response rate.",
    ),
    (
        "I reached my free limit. Did I lose my answers?",
        "No. Answers keep being collected, stored and counted in your dashboard totals. Nothing is hidden. Upgrading only removes the monthly limit.",
    ),
    (
        "Does SourceTrac ask for anything about my customers?",
        "SourceTrac stores the answers, the order number and total, and a few details: the buyer's checkout language and country, the products and whether it was their first order. It never collects names, emails, phone numbers or addresses. Text buyers type is stored as written, so ask questions that don't invite personal details.",
    ),
    (
        "Can I change the question after going live?",
        "Yes. Open the survey from Surveys, change it and save. A live survey updates from the next order. Answers already collected stay as they were.",
    ),
    (
        "Can I run more than one survey?",
        "Yes. Free has 1 live survey, Growth 10 and Scale no limit. Create them from Surveys. A thank-you page shows one survey at a time, chosen by priority.",
    ),
    (
        "What kinds of question can I ask?",
        "Multiple choice, a single choice, a rating, a scale from 0 to 10, yes/no, and free text. You can show a question only when an earlier answer matches, and show questions one at a time on a phone.",
    ),
    (
        "Why is Shopify sync not running?",
        "Sync tags orders and customers and only runs when Shopify has granted the matching permission. Reopen the app and approve the permissions, or leave them off. Your survey collects and reports either way.",
    ),
    (
        "How do I cancel?",
        "Cancel from the Plans page. Your survey keeps working on the Free plan with 50 responses a month, and nothing is deleted.",
    ),
    (
        "Which Shopify plans does it work on?",
        "Every plan except Shopify Starter, where Shopify does not offer checkout blocks. The Order status page block needs Shopify's new customer accounts.",
    ),
    (
        "Can I change the survey's colours?",
        "The survey uses your store's own checkout styling automatically, so it always matches your checkout. You control the wording: the title, intro, questions, answers and buttons.",
    ),
]
