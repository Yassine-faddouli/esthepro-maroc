# Shared building blocks for the Esthé-PRO static site
SITE = "https://www.esthepro-maroc.com"
IMG = {
 "logo":"e0ab45e4381948b2b233db7ac9686936~mv2.png",
 "ciefec":"a328c9c43240487b894a99fa6f72a808~mv2.png",
 "25ans":"d0d1cb98b6df43bcae0a56e67d1031aa~mv2.png",
 "lab":"b288142ef0ec410c9c246eea5877f4d5~mv2.webp",
 "soin1":"4693d82516a44207aebe0733407d1ce4~mv2.webp",
 "cabine":"61c2287095634af8979623a4540b721d~mv2.webp",
 "conseil1":"d9e5ae3252f14318b78c0d48f903cf58~mv2.webp",
 "conseil2":"fe29f8f533c246da91a9fb5d83cabbd0~mv2.webp",
 "classe":"08fc20ade99443ad8298daa7392583b5~mv2.webp",
 "blouse":"788b87ddb3a14b358d14b60a56990562~mv2.webp",
 "soin-gants":"057106351c3647bc9d04e76a4e8eac9f~mv2.webp",
 "institut":"59c497c8ef544214b16f52094ccaf8f7~mv2.webp",
 "massage":"ca871be6ba0e474189f982d57362e122~mv2.webp",
 "visage":"968cc86b8a7f45a0aee6b6ff1b5486c7~mv2.webp",
 "eleves":"9e903a6d8b304bcb94c10ac37a8d7f2f~mv2.webp",
 "hydra":"85cdddebe74c497e904b6078a9a8c92b~mv2.webp",
 "comptoir":"2a30a33b33a64289bcf0b384c30e09d1~mv2.webp",
 "cabine2":"af87743765004c449a7a1e357bb26acf~mv2.webp",
 "visage2":"0d8e0a3e7f9f41718e9115e26422e669~mv2.webp",
 "adulte1":"7771659525584bfe9744b32220de0666~mv2.webp",
 "adulte2":"7fa7f368118b4a72b36291711b490cfe~mv2.webp",
 "adulte3":"63cdaf702ba0492faee801c2b637c45e~mv2.webp",
 "produits":"27362cf589204d85a10c14acc5f27986~mv2.webp",
 "dermo1":"2cfd8ff8d45e4cd287df6e08ae5aac2b~mv2.webp",
 "produits2":"8cce95c9b9244bf3b7997b65100fab89~mv2.webp",
 "distance":"b2d8a7d73f0b4ef59031ffed27cb272f~mv2.jpg",
 "dermo2":"8c82f4d4e7ce49ca99cc6475006b5046~mv2.webp",
}

def src(key, w, h=None, fit=False):
    f = IMG[key]
    mode = f"fit/w_{w},h_{h or w}" if fit else f"fill/w_{w},h_{h},al_c"
    return f"https://static.wixstatic.com/media/76852a_{f}/v1/{mode},q_85,enc_auto/{key}.webp"

def img(key, w, h, alt, cls="", eager=False, extra=""):
    s1, s2 = src(key, w, h), src(key, w*2 if w < 1000 else w, h*2 if w < 1000 else h)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{s1}" srcset="{s1} 1x, {s2} 2x" width="{w}" height="{h}" alt="{alt}" {load} {extra}>'

ICON = {
 "arrow":'<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "wa":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.2-.2-.2-.5-.3z"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "cal":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
 "cap":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
 "home":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>',
 "screen":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
 "spark":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.9 5.8L20 10l-6.1 1.2L12 17l-1.9-5.8L4 10l6.1-1.2z"/><path d="M19 17l.7 2.3L22 20l-2.3.7L19 23l-.7-2.3L16 20l2.3-.7z"/></svg>',
 "store":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l1.5-5h15L21 9M3 9v11h18V9M3 9h18M9 20v-6h6v6"/></svg>',
 "flask":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2h6M10 2v6L4 19a2 2 0 0 0 1.8 3h12.4A2 2 0 0 0 20 19L14 8V2M7 15h10"/></svg>',
 "brief":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
 "mic":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>',
 "heart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
 "tram":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="4" width="14" height="14" rx="3"/><path d="M5 12h14M9 18l-2 3M15 18l2 3M9 4l1-2h4l1 2"/></svg>',
 "lock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 "fb":'<svg viewBox="0 0 24 24"><path d="M14 8h3V4h-3c-2.8 0-4 1.8-4 4.3V10H7v4h3v8h4v-8h3l1-4h-4V8.6c0-.4.3-.6.6-.6z"/></svg>',
 "ig":'<svg viewBox="0 0 24 24"><path d="M12 7.3A4.7 4.7 0 1 0 16.7 12 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 3-3 3 3 0 0 1-3 3zm6-7.9a1.1 1.1 0 1 1-1.1-1.1A1.1 1.1 0 0 1 18 7.1zM21 7a5.4 5.4 0 0 0-1.5-3.9A5.4 5.4 0 0 0 15.6 1.6C14.1 1.5 9.9 1.5 8.4 1.6A5.4 5.4 0 0 0 4.5 3.1 5.4 5.4 0 0 0 3 7c-.1 1.5-.1 5.7 0 7.2a5.4 5.4 0 0 0 1.5 3.9 5.4 5.4 0 0 0 3.9 1.5c1.5.1 5.7.1 7.2 0a5.4 5.4 0 0 0 3.9-1.5A5.4 5.4 0 0 0 21 14.2c.1-1.5.1-5.7 0-7.2z"/></svg>',
}
A = ICON["arrow"]

COURSES = {
 "estheticienne": dict(name="Formation Esthéticienne", short="Esthéticienne", url="/formation-estheticienne", q="estheticienne"),
 "adultes": dict(name="Formation Esthétique pour Adultes", short="Esthétique pour Adultes", url="/formation-esthetique-pour-adultes", q="adultes"),
 "dermo": dict(name="Formation Dermo-Cosmétique", short="Dermo-Cosmétique", url="/formation-dermocosmetique-appliquee-a-la-parapharmacie", q="dermo"),
}

def head(title, desc, path, og="classe", noindex=False, extra=""):
    rob = '<meta name="robots" content="noindex">' if noindex else ""
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
{rob}
<meta name="theme-color" content="#002D62">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_MA">
<meta property="og:site_name" content="École Esthé-PRO">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{src(og,1200,630)}">
<link rel="icon" href="https://static.wixstatic.com/media/76852a_{IMG['logo']}/v1/fit/w_64,h_64/favicon.png">
<link rel="preconnect" href="https://static.wixstatic.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Spinnaker&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
<script>(function(d){{d.classList.add('js');try{{if(!sessionStorage.getItem('ep_seen')&&!matchMedia('(prefers-reduced-motion: reduce)').matches){{d.classList.add('first');sessionStorage.setItem('ep_seen','1')}}}}catch(e){{}}}})(document.documentElement)</script>
<script src="/assets/js/config.js"></script>
{extra}
</head>'''

def header(active=""):
    def cur(k): return ' aria-current="page"' if active == k else ""
    fa = " active" if active.startswith("f-") else ""
    return f'''
<div class="loader" aria-hidden="true"><div class="lg"><div class="row"><span class="esthe">Esthé</span><span class="pro">PRO</span></div><div class="ln"></div><small>École Internationale d'Esthétique et de Cosmétologie</small></div></div>
<div class="sessionbar" data-session>Prochaine rentrée le <b data-session-label></b><span class="cd" data-cd="short"></span>· Places limitées <a href="/inscription" data-track="topbar">Réserver ma place</a></div>
<header class="site">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Esthé-PRO, accueil">
      <img src="https://static.wixstatic.com/media/76852a_{IMG['logo']}/v1/fit/w_240,h_188,q_90/logo-esthe-pro.png" width="76" height="59" alt="Logo Esthé PRO, école d'esthétique et de dermo-cosmétique à Rabat">
      <small>École Internationale d'Esthétique et de Cosmétologie</small>
    </a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul class="menu">
      <li><a href="/"{cur('home')}>Accueil</a></li>
      <li><a href="/ecole-esthe-pro"{cur('ecole')}>L'école</a></li>
      <li>
        <button class="dd{fa}" aria-haspopup="true">Nos formations <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M6 9l6 6 6-6"/></svg></button>
        <ul class="sub">
          <li><a href="/formation-estheticienne"{cur('f-esth')}>Formation Esthéticienne<span>1 an · présentiel · diplômante</span></a></li>
          <li><a href="/formation-esthetique-pour-adultes"{cur('f-adu')}>Esthétique pour Adultes<span>6 mois · le samedi · sans prérequis</span></a></li>
          <li><a href="/formation-dermocosmetique-appliquee-a-la-parapharmacie"{cur('f-dermo')}>Dermo-Cosmétique<span>100 % à distance · live sur Zoom</span></a></li>
        </ul>
      </li>
      <li><a href="/contact"{cur('contact')}>Contact</a></li>
      <li class="cta"><a href="/inscription"{cur('insc')} data-track="nav_cta">S'inscrire</a></li>
    </ul>
  </div>
</header>'''

def footer(mbar=True):
    mb = f'''
<div class="mbar">
  <a class="btn btn-sky" href="/inscription" data-track="mbar_cta">Je m'inscris</a>
  <a class="btn btn-wa sq" data-wa data-place="mbar" aria-label="WhatsApp">{ICON['wa']}</a>
  <a class="btn sq" href="tel:+212762575813" aria-label="Appeler">{ICON['phone']}</a>
</div>''' if mbar else ""
    return f'''
<footer class="site">
  <div class="wrap">
    <div class="foot">
      <div>
        <img src="https://static.wixstatic.com/media/76852a_{IMG['logo']}/v1/fit/w_240,h_188,q_90/logo-esthe-pro.png" width="96" height="75" alt="Esthé-PRO" loading="lazy">
        <p>École Internationale d'Esthétique et de Cosmétologie. Établissement privé de formation professionnelle autorisé et agréé par l'État — n° 4/07/9/2003.</p>
        <div class="socials">
          <a href="https://www.facebook.com/esthepro.ecole/" target="_blank" rel="noopener" aria-label="Facebook">{ICON['fb']}</a>
          <a href="https://www.instagram.com/ecole.esthe.pro/" target="_blank" rel="noopener" aria-label="Instagram">{ICON['ig']}</a>
        </div>
      </div>
      <div>
        <h4>Formations</h4>
        <ul>
          <li><a href="/formation-estheticienne">Formation Esthéticienne</a></li>
          <li><a href="/formation-esthetique-pour-adultes">Esthétique pour Adultes</a></li>
          <li><a href="/formation-dermocosmetique-appliquee-a-la-parapharmacie">Dermo-Cosmétique</a></li>
        </ul>
      </div>
      <div>
        <h4>L'école</h4>
        <ul>
          <li><a href="/ecole-esthe-pro">Notre histoire</a></li>
          <li><a href="/ecole-esthe-pro#fondateurs">Les fondateurs</a></li>
          <li><a href="/inscription">Pré-inscription</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <p>Angle Avenue Michlifen et Rue Jabal Al Ayachi<br>Imm. 49, 3ème étage, n°8 — Agdal, Rabat<br>
        <a href="tel:+212762575813">+212 7 62 57 58 13</a><br>
        <a data-wa data-place="footer">WhatsApp</a> · <a href="mailto:esthepro_ma@yahoo.fr">esthepro_ma@yahoo.fr</a></p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span data-year>2026</span> École Internationale d'Esthétique et de Cosmétologie Esthé-PRO. Tous droits réservés.</span>
      <span>Membre de la C.I.E.F.EC depuis 2003</span>
    </div>
  </div>
</footer>
<a class="wa-float" data-wa data-place="float" aria-label="Nous écrire sur WhatsApp">{ICON['wa']}</a>{mb}
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''

def faq(items):
    return "\n".join(f'<details class="rv"><summary>{q}<i></i></summary><div class="ans">{a}</div></details>' for q, a in items)

def faq_schema(items):
    import json, re
    data = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in items]}
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'

def session_box(key="soin-gants", title="La prochaine rentrée approche", text="Les groupes sont volontairement réduits pour garantir un accompagnement personnalisé. Pré-inscrivez-vous dès maintenant pour réserver votre place.", href="/inscription"):
    return f'''
<section data-session>
  <div class="wrap">
    <div class="session rv z">
      <div class="l">
        <span class="eyebrow">Prochaine session · <span data-session-label></span></span>
        <h2>{title}</h2>
        <p class="lead">{text}</p>
        <div class="countdown" data-cd>
          <div><b data-u="d">00</b><span>Jours</span></div>
          <div><b data-u="h">00</b><span>Heures</span></div>
          <div><b data-u="m">00</b><span>Min</span></div>
          <div><b data-u="s">00</b><span>Sec</span></div>
        </div>
        <a class="btn btn-sky" href="{href}" data-track="session_box">Réserver ma place {A}</a>
      </div>
      <div class="r">{img(key, 800, 800, "Élève en pratique à l'école Esthé-PRO")}</div>
    </div>
  </div>
</section>'''

def final_cta(key="eleves", title="Votre avenir dans la beauté commence <em>ici</em>.", text="Laissez-nous votre numéro : un conseiller pédagogique vous rappelle pour répondre à vos questions et vous guider vers la formation qui vous correspond.", preset=""):
    opts = "".join(f'<option{" selected" if preset==c["name"] else ""}>{c["name"]}</option>' for c in COURSES.values())
    return f'''
<section class="final">
  <div class="bgimg">{img(key, 1600, 900, "", extra='aria-hidden="true"')}</div>
  <div class="wrap">
    <span class="eyebrow rv">Être rappelé(e) gratuitement</span>
    <h2 class="rv">{title}</h2>
    <p class="lead rv">{text}</p>
    <form class="quick rv" data-lead="quick" novalidate style="margin-top:40px;text-align:left">
      <div class="field"><label for="q-prenom">Prénom</label><input id="q-prenom" name="prenom" autocomplete="given-name" data-req><p class="err">Indiquez votre prénom.</p></div>
      <div class="field"><label for="q-tel">Téléphone / WhatsApp</label><div class="tel"><span>+212</span><input id="q-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="6 12 34 56 78" data-req="phone"></div><p class="err">Numéro invalide.</p></div>
      <div class="field"><label for="q-f">Formation</label><select id="q-f" name="formation"><option value="">Je ne sais pas encore</option>{opts}</select></div>
      <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-sky" type="submit">Être rappelé(e) {A}</button>
    </form>
    <p class="legal" style="color:#9fb8d4">{ICON['lock']} Gratuit, sans engagement. Ou écrivez-nous directement sur <a data-wa data-place="final" style="color:#fff;margin-left:4px">WhatsApp</a>.</p>
  </div>
</section>'''

def page_hero(eyebrow, h1, lead, key, crumbs, actions="", facts="", alt=""):
    return f'''
<section class="page-hero">
  <div class="wrap inner">
    <div class="txt intro-anim">
      <nav class="crumbs" aria-label="Fil d'Ariane">{crumbs}</nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {f'<div class="facts">{facts}</div>' if facts else ''}
      {f'<div class="hero-actions">{actions}</div>' if actions else ''}
    </div>
    <div class="media">{img(key, 1100, 900, alt, eager=True)}</div>
  </div>
</section>'''

def fact(icon, text):
    return f'<span class="fact">{ICON[icon]}{text}</span>'
