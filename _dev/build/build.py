import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from parts import SITE
from pages_home import home
from pages_other import ecole, formation, ESTH, ADU, DERMO, inscription, contact, merci, notfound

OUT = os.path.join(os.path.dirname(__file__), "..", "..")
pages = {
  "index.html": home(),
  "ecole-esthe-pro/index.html": ecole(),
  "formation-estheticienne/index.html": formation(ESTH),
  "formation-esthetique-pour-adultes/index.html": formation(ADU),
  "formation-dermocosmetique-appliquee-a-la-parapharmacie/index.html": formation(DERMO),
  "inscription/index.html": inscription(),
  "contact/index.html": contact(),
  "merci/index.html": merci(),
  "404.html": notfound(),
}
for p, html in pages.items():
    f = os.path.join(OUT, p); os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(html)

urls = ["/", "/ecole-esthe-pro", "/formation-estheticienne", "/formation-esthetique-pour-adultes",
        "/formation-dermocosmetique-appliquee-a-la-parapharmacie", "/inscription", "/contact"]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nDisallow: /merci\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(OUT, "vercel.json"), "w").write('{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n')
open(os.path.join(OUT, "netlify.toml"), "w").write('[build]\n  publish = "."\n\n[[redirects]]\n  from = "/*"\n  to = "/404.html"\n  status = 404\n')
print("built", len(pages), "pages")
