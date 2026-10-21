# -*- coding: utf-8 -*-
"""Help and FAQ page body."""
from build import ICON, app_store_button, esc
from faq_data import FAQ

def build_help():
    items = []
    for question, answer in FAQ:
        items.append(
            '<details>\n'
            '        <summary>%s<span aria-hidden="true">%s</span></summary>\n'
            '        <div class="faq-body"><p>%s</p></div>\n'
            '      </details>' % (esc(question), ICON["check"], esc(answer))
        )

    return """
<section class="section hero">
  <div class="wrap wrap--narrow">
    <div class="section-head">
      <span class="eyebrow">Help</span>
      <h1>Help</h1>
      <p class="lede">Answers to the questions we are asked most.</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow">
    <div class="faq">
      %s
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap wrap--narrow">
    <div class="band band--mint">
      <h2>Still stuck?</h2>
      <p>Tell us what is happening and we will take a look.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="/support">Contact support</a>
      </div>
    </div>
  </div>
</section>
""" % "\n      ".join(items)
