#!/usr/bin/env python3
"""
Scaffolds the interior pages so every one carries identical chrome.

The header, drawer, spine and footer are lifted straight out of index.html,
so the homepage stays the single source of truth for site chrome. Run from
the repo root after editing index.html's header or footer:

    python3 tools/build_pages.py

Page bodies live in pages/*.py — edit those, not the generated HTML.
"""
import os, re, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

src = open('index.html', encoding='utf-8').read()

def between(start, end, s=src):
    i = s.index(start); j = s.index(end, i)
    return s[i:j]

FONTS  = between('<link rel="preconnect"', '<link rel="stylesheet" href="assets/css/site.css">')
CHROME = between('<a class="skip"', '<main id="main">')
FOOTER = between('<footer class="site-footer">', '<script src="assets/js/site.js" defer></script>')

# interior pages sit at / or /blog/, so assets are referenced from the root
CHROME = CHROME.replace('"assets/', '"/assets/').replace('href="/"', 'href="/"')
FOOTER = FOOTER.replace('"assets/', '"/assets/')
FONTS  = FONTS.replace('"assets/', '"/assets/')

NAV = {
    '#procedure': '/patient-information',
    '#doctors':   '/about-us',
    '#fees':      '/vasectomy-fees',
    '#location':  '/location',
    '#reviews':   '/#reviews',
    '#faq':       '/patient-information#faq',
    '/blog/':     '/blog',
    '/contact/':  '/contact-us',
    '/privacy-policy/': '/privacy-policy',
}
def relink(html):
    for a, b in NAV.items():
        html = html.replace('href="%s"' % a, 'href="%s"' % b)
    return html

CHROME_P, FOOTER_P = relink(CHROME), relink(FOOTER)

SHELL = '''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/brand/favicon_hobartvasectomy_com_au_64x64.png">
{fonts}<link rel="stylesheet" href="/assets/css/site.css">
<link rel="stylesheet" href="/assets/css/pages.css">
</head>
<body>
{chrome}<main id="main">
{body}
</main>

{footer}<button class="totop" id="toTop" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
    <path d="M12 19V5M5 12l7-7 7 7"/>
  </svg>
</button>

<script src="/assets/js/site.js" defer></script>
<script src="/assets/js/pages.js" defer></script>
</body>
</html>
'''

BOOK = ('https://bookings.gettimely.com/vasectomyaustralia/bb/book'
        '?location=311811&amp;product=3705203%3ASV&amp;staff=288783')

def crumb(here):
    return ('<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a>'
            '<span aria-hidden="true">&rsaquo;</span>%s</nav>' % here)

def phero(img, alt, kicker, h1, lede, acts=True, spine=''):
    a = ''
    if acts:
        a = ('<div class="phero__act">'
             '<a class="btn btn--gold" href="%s" rel="noopener"><span class="btn__dot"></span>Book online</a>'
             '<a class="btn btn--ghost" href="tel:1800764763">Call 1800 SNIPME</a>'
             '</div>' % BOOK)
    return '''<section class="phero" data-spine="{spine}">
  <div class="phero__media"><img src="{img}" alt="{alt}" width="2400" height="1018" fetchpriority="high"></div>
  <div class="phero__scrim"></div>
  <div class="wrap phero__in">
    {crumb}
    <p class="kicker kicker--dk">{kicker}</p>
    <h1>{h1}</h1>
    <p class="phero__lede">{lede}</p>
    {acts}
  </div>
</section>'''.format(img=img, alt=alt, kicker=kicker, h1=h1, lede=lede,
                     acts=a, crumb=crumb(kicker), spine=spine or kicker)

def cta(h2, p):
    return '''<section class="pagecta">
  <div class="wrap pagecta__in">
    <div>
      <h2 data-rev>{h2}</h2>
      <p data-rev data-rev-d="1">{p}</p>
    </div>
    <div class="pagecta__act" data-rev data-rev-d="2">
      <a class="btn btn--ink" href="{book}" rel="noopener"><span class="btn__dot"></span>Book online</a>
      <a class="btn btn--ink" href="tel:1800764763">Call 1800 SNIPME</a>
    </div>
  </div>
</section>'''.format(h2=h2, p=p, book=BOOK)

TICK = ('<span class="check__i" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M20 6 9 17l-5-5"/></svg></span>')

# the FAQ is authored once, on the homepage, and reused verbatim
FAQ = between('<!-- faq ==', '<!-- location ==').replace('id="faq"', 'id="faq"')

def write(path, title, desc, body):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    body = body.replace('__FAQ__', relink(FAQ))
    html = SHELL.format(title=title, desc=desc, fonts=FONTS,
                        chrome=CHROME_P, footer=FOOTER_P, body=body)
    open(path, 'w', encoding='utf-8').write(html)
    print('  wrote %-58s %6d bytes' % (path, len(html.encode())))

# ---------------------------------------------------------------- pages ---
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import page_content
page_content.build(write, phero, cta, crumb, TICK, BOOK)
print('done')
