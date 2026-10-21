# -*- coding: utf-8 -*-
"""SourceTrac template library. Text is used exactly as supplied."""

GROUP_FIND = {
    "id": "find-you",
    "title": "Where buyers find you",
    "desc": "The ads, creators, searches, people and places that send you buyers.",
    "templates": [
        {
            "name": "How did you hear about us?",
            "desc": "Ask buyers where they first heard of you and see which channels bring in your sales.",
            "plan": "3 questions; Free, full version",
            "questions": [
                "Where did you first hear about us?",
                "When was that?",
                "Which creator or account was it?",
            ],
        },
        {
            "name": "How many times did you see us?",
            "desc": "Ask how many times buyers saw your brand before they ordered, and where.",
            "plan": "2 questions; Short version on Free, full version on Growth",
            "questions": [
                "Before today, how many times had you seen or heard about us?",
                "Where did you see us? Choose up to 3.",
            ],
        },
        {
            "name": "Which ad do you remember?",
            "desc": "Ask which of your ads or messages buyers remember seeing.",
            "plan": "1 question; Short version on Free, full version on Growth",
            "questions": [
                "Which of these have you seen from us recently?",
            ],
        },
        {
            "name": "What did you use before us?",
            "desc": "Ask what buyers used before you and why they switched.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Before this, what did you use instead?",
                "Which brand was it?",
                "What made you switch to us?",
            ],
        },
        {
            "name": "What brought you here today?",
            "desc": "The last thing that sent buyers to your store today, next to where they first heard of you.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "What brought you to our store today?",
                "Where was the ad?",
            ],
        },
        {
            "name": "Did you compare us?",
            "desc": "Which other brands buyers looked at, and what made them choose you.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Did you look at other brands before choosing us?",
                "Which brands did you look at?",
                "What made you choose us?",
            ],
        },
        {
            "name": "Where do you see us most?",
            "desc": "The places buyers keep running into you, beyond where they first found you.",
            "plan": "1 question; Free, full version",
            "questions": [
                "Where do you see us most often? Choose up to 3.",
            ],
        },
        {
            "name": "Did the discount matter?",
            "desc": "Whether your offers win sales you would not get otherwise, or give away margin.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "Did a discount or offer help you decide today?",
                "Where did you find the offer?",
            ],
        },
        {
            "name": "Podcast and creator tracker",
            "desc": "Names the exact podcasts and creators that send you buyers, and whether their discount code was used.",
            "plan": "4 questions; Short version on Free, full version on Growth",
            "questions": [
                "Where did you first hear about us?",
                "Which podcast was it?",
                "Which creator or influencer was it?",
                "Did you use their discount code?",
            ],
        },
        {
            "name": "Social media deep dive",
            "desc": "Which app buyers were on, and whether an ad, a creator's video or your own post made them click.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Did you find us on social media?",
                "Which app were you using?",
                "What did you see?",
            ],
        },
        {
            "name": "What did you search for?",
            "desc": "The words buyers typed, and where: Google, an AI assistant, a marketplace or a video app.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How did you look for what you bought today?",
                "What did you type into the search box?",
                "Did you click an ad or a regular result?",
            ],
        },
        {
            "name": "Word of mouth and offline",
            "desc": "The friends, events, shops, print and TV that send you buyers, which online tracking never sees.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Where did you first come across us?",
                "Who told you about us?",
                "Which one was it?",
            ],
        },
        {
            "name": "Email and text impact",
            "desc": "Whether your emails and texts led to this order, and how often subscribers want to hear from you.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Do you get our emails or text messages?",
                "Did one of our messages lead to this order?",
                "How often would you like to hear from us?",
            ],
        },
    ],
}

GROUP_WHY = {
    "id": "why-buy",
    "title": "Why they buy",
    "desc": "What convinced buyers, what nearly stopped them, and what they wanted to know.",
    "templates": [
        {
            "name": "What made you trust us?",
            "desc": "Ask first-time buyers what made them feel safe ordering from you.",
            "plan": "1 question; Free, full version",
            "questions": ["What made you trust us enough to order? Choose up to 2."],
        },
        {
            "name": "What helped you decide?",
            "desc": "Ask which part of your product page helped buyers decide, and what was missing.",
            "plan": "2 questions; Growth plan, includes results by product",
            "questions": [
                "Which part of the product page helped you decide most?",
                "Was anything missing that would have helped?",
            ],
        },
        {
            "name": "What made you buy today?",
            "desc": "Ask for the main reason buyers ordered, so you know what to say in your ads and product pages.",
            "plan": "2 questions; Short version on Free, full version on Growth",
            "questions": [
                "What was the main reason you bought today?",
                "Anything else that helped you decide?",
            ],
        },
        {
            "name": "What almost stopped you?",
            "desc": "Ask what nearly stopped buyers from ordering, so you can fix it for the next ones.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "Did anything nearly stop you from ordering today?",
                "What would have made it easier?",
            ],
        },
        {
            "name": "Was anything hard to use?",
            "desc": "Ask buyers whether anything on your website was hard to use, and read what to fix.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "Was anything on our website hard to use today?",
                "What was hard to use?",
            ],
        },
        {
            "name": "How do our prices feel?",
            "desc": "Ask buyers whether your prices feel fair.",
            "plan": "2 questions; Growth plan, includes results by product",
            "questions": [
                "How did the price feel for what you bought?",
                "What would make it feel worth it?",
            ],
        },
        {
            "name": "How did you find the product?",
            "desc": "How buyers reached what they bought: search, menus, recommendations or a link.",
            "plan": "2 questions; Short version on Free, full version on Growth",
            "questions": [
                "How did you find the product you bought today?",
                "How easy was it to find?",
            ],
        },
        {
            "name": "Reviews that convinced you",
            "desc": "Where new buyers read reviews before trusting you, and which part of a review won them over.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Did you read reviews of us before buying?",
                "Where did you read them?",
                "What mattered most in the reviews?",
            ],
        },
        {
            "name": "Payment options check",
            "desc": "Whether buyers could pay the way they wanted, which method they missed, and how much paying later matters.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Could you pay the way you wanted to?",
                "Which way did you want to pay?",
                "Did paying in instalments matter for this order?",
            ],
        },
        {
            "name": "Questions before buying",
            "desc": "The questions new buyers had before ordering, in their own words, and where they found the answer.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Did you have a question before you bought?",
                "What did you want to know?",
                "Where did you find the answer?",
            ],
        },
    ],
}

GROUP_DELIVERY = {
    "id": "delivery",
    "title": "Delivery and shipping",
    "desc": "What buyers expect from delivery, and how shipping cost changes what they order.",
    "templates": [
        {
            "name": "Will you be home for delivery?",
            "desc": "Ask whether buyers will be available to receive the order, before you ship.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Will someone be available to receive this order?",
                "When is the best time to deliver?",
                "Would you like to pay online next time?",
            ],
        },
        {
            "name": "Are you sure about the size?",
            "desc": "Ask buyers how sure they are about size or fit, so you can help before shipping.",
            "plan": "2 questions; Growth plan, includes results by product",
            "questions": [
                "How sure are you about the size or fit you chose?",
                "What are you unsure about?",
            ],
        },
        {
            "name": "How fast do you need it?",
            "desc": "Ask how fast buyers expect their order and whether they need it by a date.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "When are you expecting your order to arrive?",
                "Do you need it by a specific date?",
            ],
        },
        {
            "name": "What matters in packaging?",
            "desc": "Ask what buyers want from your packaging, from less plastic to gift-ready.",
            "plan": "1 question; Short version on Free, full version on Growth",
            "questions": ["What matters most to you in packaging? Choose up to 2."],
        },
        {
            "name": "Shipping cost check",
            "desc": "Whether free shipping made buyers order or add items, and what shipping they'd accept.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How did the shipping cost affect your order?",
                "What would have felt fair?",
                "What matters most to you about delivery?",
            ],
        },
        {
            "name": "International order check",
            "desc": "Whether buyers abroad understood duties and taxes before paying, and how sure they are about delivery.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Before paying, did you know about import duties or taxes?",
                "How sure are you about when your order will arrive?",
                "What would have made the costs clearer?",
            ],
        },
    ],
}

GROUP_LOYALTY = {
    "id": "loyalty",
    "title": "Loyalty and satisfaction",
    "desc": "How happy buyers are, whether they'll come back, and who would recommend you.",
    "templates": [
        {
            "name": "How was your first order?",
            "desc": "Ask first-time buyers how ordering went and whether they'd order again.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How easy was it to order from us for the first time?",
                "What got in the way?",
                "Would you order from us again?",
            ],
        },
        {
            "name": "Would you recommend us? (NPS)",
            "desc": "The 0 to 10 recommend score, with a follow-up asking why.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How likely are you to recommend us to a friend?",
                "What do you love most about us?",
                "What should we fix first?",
            ],
        },
        {
            "name": "How satisfied are you? (CSAT)",
            "desc": "The 1 to 5 satisfaction question, with a follow-up for buyers who were not happy.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "How satisfied are you with your order today?",
                "What could we have done better?",
            ],
        },
        {
            "name": "Would you miss us? (product-market fit)",
            "desc": "Ask returning buyers how they'd feel if they could no longer buy from you, and why they buy.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "How would you feel if you could no longer buy from us?",
                "What's the main reason you buy from us?",
            ],
        },
        {
            "name": "Why did you come back?",
            "desc": "Ask returning buyers what brought them back.",
            "plan": "1 question; Free, full version",
            "questions": ["What brought you back today? Choose up to 2."],
        },
        {
            "name": "Would you subscribe?",
            "desc": "How many buyers want automatic deliveries, and how often.",
            "plan": "1 question; Free, full version",
            "questions": ["Would you like this delivered automatically?"],
        },
        {
            "name": "Referral readiness",
            "desc": "Who would recommend you, the reward that would make them share, and what holds everyone else back.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How likely are you to recommend us to a friend?",
                "What would make you share us with friends?",
                "What would make you more likely to recommend us?",
            ],
        },
        {
            "name": "What you'll buy next",
            "desc": "When buyers plan to order again, what they'd like next, and what would bring them back sooner.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Do you think you'll order from us again?",
                "What would you like to buy from us next?",
                "What would bring you back sooner?",
            ],
        },
    ],
}

GROUP_BUYERS = {
    "id": "who-buyers",
    "title": "Who your buyers are",
    "desc": "Who buys from you, what they use it for, and what matters to them.",
    "templates": [
        {
            "name": "Is this a gift?",
            "desc": "Ask which orders are gifts, and for which occasion.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "Who is this order for?",
                "What's the occasion?",
                "When is the occasion?",
            ],
        },
        {
            "name": "When will you run out?",
            "desc": "Ask when buyers expect to run out, so reminders arrive at the right time.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "How long do you think this will last you?",
                "Would a reminder when it's time to reorder be helpful?",
            ],
        },
        {
            "name": "What are your preferences?",
            "desc": "Ask about each buyer's preferences, like skin type or style, to personalise what you send.",
            "plan": "2 questions; Short version on Free, full version on Growth",
            "questions": ["What would you like to hear about? Choose up to 3."],
        },
        {
            "name": "What's your age range?",
            "desc": "Ask buyers their age range, to see which age groups buy from you.",
            "plan": "1 question; Free, full version",
            "questions": ["What's your age range?"],
        },
        {
            "name": "Are you buying for a business?",
            "desc": "Ask whether the order is for a business, to spot buyers who may want bulk pricing.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "Who are you buying for?",
                "Would you like us to share bulk pricing with you?",
            ],
        },
        {
            "name": "What couldn't you find?",
            "desc": "Ask what buyers looked for in your store but couldn't find.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "Did you look for anything you couldn't find?",
                "What were you looking for?",
            ],
        },
        {
            "name": "How should we stay in touch?",
            "desc": "The channels buyers want to hear from you on, so your messages get read.",
            "plan": "1 question; Short version on Free, full version on Growth",
            "questions": ["How would you like to hear from us? Choose up to 3."],
        },
        {
            "name": "Where else do you shop?",
            "desc": "Whether your buyers also shop on Amazon, in physical stores or with other brands.",
            "plan": "1 question; Short version on Free, full version on Growth",
            "questions": ["Where else do you buy products like this? Choose up to 3."],
        },
        {
            "name": "Anything else to tell us?",
            "desc": "One open question, for what your other questions never ask.",
            "plan": "1 question; Free, full version",
            "questions": ["Is there anything else you'd like to tell us?"],
        },
        {
            "name": "Sustainability check",
            "desc": "How much sustainability mattered in choosing you, and which green practices buyers value most.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How much did sustainability matter when choosing us?",
                "Which of these matter most to you?",
                "Would you choose a slower delivery if it were greener?",
            ],
        },
        {
            "name": "How you'll use it",
            "desc": "What buyers use your products for, who uses them, and how often.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "What will you use it for?",
                "Who will mostly use it?",
                "How often will it be used?",
            ],
        },
        {
            "name": "Household snapshot",
            "desc": "Three optional questions about buyers' homes: how many live there, whether there are children, and where.",
            "plan": "3 questions; Short version on Free, full version on Growth",
            "questions": [
                "How many people live in your home?",
                "Are there children at home?",
                "Where do you live?",
            ],
        },
        {
            "name": "Life moments",
            "desc": "The life moment behind an order, like moving, a new baby or a new hobby, and when it happens.",
            "plan": "2 questions; Free, full version",
            "questions": [
                "Is this order for something happening in your life?",
                "When is it happening?",
            ],
        },
    ],
}

TEMPLATE_GROUPS = [GROUP_FIND, GROUP_WHY, GROUP_DELIVERY, GROUP_LOYALTY, GROUP_BUYERS]
