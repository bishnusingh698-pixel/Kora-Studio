# -*- coding: utf-8 -*-
"""Templates page body."""
from build import app_store_button, esc
from templates_data import TEMPLATE_GROUPS

INTRO = "Pick what you want to learn. Every template is ready to use, and you can change any question before it goes live."

NOTE = ("Free includes the short version of every template and the full “How did you hear about us?” "
        "survey. Growth unlocks the full version of every template, including “None of these” answers "
        "and results by product.")


def template_card(group_title, tpl):
    questions = "\n            ".join("<li>%s</li>" % esc(x) for x in tpl["questions"])
    search_blob = " ".join([group_title, tpl["name"], tpl["desc"], tpl["plan"]] + tpl["questions"]).lower()
    plan = tpl["plan"]
    plan_pill = "pill pill--mint" if "Growth" in plan else "pill"
    return """<article class="tpl" data-tpl data-search="%s">
          <h3>%s</h3>
          <p class="tpl__desc">%s</p>
          <div class="tpl__meta"><span class="%s">%s</span></div>
          <p class="tpl__q-label">Questions</p>
          <ol>
            %s
          </ol>
        </article>""" % (esc(search_blob), esc(tpl["name"]), esc(tpl["desc"]), plan_pill, esc(plan), questions)


def build_templates():
    groups_html = []
    for group in TEMPLATE_GROUPS:
        cards = "\n        ".join(template_card(group["title"], t) for t in group["templates"])
        groups_html.append("""<section class="tpl-group" data-tpl-group id="%s">
      <div class="tpl-group__head">
        <h2>%s</h2>
        <span class="tpl-group__count" data-group-count>%d templates</span>
        <p class="tpl-group__desc">%s</p>
      </div>
      <div class="tpl-grid">
        %s
      </div>
    </section>""" % (group["id"], esc(group["title"]), len(group["templates"]), esc(group["desc"]), cards))

    return """
<section class="section hero">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Templates</span>
      <h1>50 ready-made templates</h1>
      <p class="lede">%s</p>
      <div class="note-box" style="margin-top:1.25rem">
        <p>%s</p>
      </div>
    </div>
  </div>
</section>

<div class="filter-bar">
  <div class="wrap filter-inner">
    <form role="search" action="/templates" method="get">
      <label class="filter-label" for="tpl-search">Search templates</label>
      <input type="search" id="tpl-search" name="q" placeholder="Try NPS, gift, delivery or discount" autocomplete="off">
    </form>
    <p class="filter-count" role="status" aria-live="polite">Showing <strong id="tpl-count">50 templates</strong></p>
  </div>
</div>

<section class="section section--tight">
  <div class="wrap">
    %s
    <p class="tpl-empty" id="tpl-empty">No templates match that search. Try another word, or start from scratch in the app.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="band band--mint">
      <h2>Start from a template, or write your own.</h2>
      <p>Every template is ready to use, and you can change any question before it goes live.</p>
      <div class="btn-row">
        %s
        <a class="btn btn--ghost" href="/pricing">See plans</a>
      </div>
    </div>
  </div>
</section>
""" % (esc(INTRO), esc(NOTE), "\n    ".join(groups_html), app_store_button())
