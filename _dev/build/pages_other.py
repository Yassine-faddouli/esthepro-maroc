from parts import *

CR = lambda *items: ' <span>/</span> '.join(items)
HOME = '<a href="/">Accueil</a>'

# ---------------------------------------------------------------- ÉCOLE
def ecole():
    body = f'''
<body>
{header('ecole')}
<main>
{page_hero("Héritage &amp; Excellence", "Une école où l'on apprend <em>le geste</em> et <em>la science</em>.",
  "Depuis plus de 25 ans, Esthé-PRO forme des professionnelles compétentes, autonomes et responsables, attachées à l'éthique de leur métier et prêtes à accompagner les transformations du secteur de la beauté.",
  "classe", CR(HOME, "L'école"),
  actions=f'<a class="btn btn-sky" href="/inscription" data-track="ecole_hero">Je me pré-inscris {A}</a><a class="btn btn-light" href="#fondateurs">Rencontrer les fondateurs</a>',
  alt="Salle de formation de l'école Esthé-PRO à Rabat")}

<div class="trust" data-stagger>
  <div><span class="ic">{ICON['shield']}</span><p><b>Agréée par l'État</b><span>Autorisation n° 4/07/9/2003</span></p></div>
  <div><img src="https://static.wixstatic.com/media/76852a_{IMG['ciefec']}" width="56" height="31" alt="Logo CIEFEC" loading="lazy"><p><b>Membre C.I.E.F.EC</b><span>Depuis 2003</span></p></div>
  <div><span class="ic">{ICON['users']}</span><p><b>Petits groupes</b><span>Pratique encadrée</span></p></div>
  <div><span class="ic">{ICON['tram']}</span><p><b>Agdal, Rabat</b><span>5 min du tram Avenue de France</span></p></div>
</div>

<section>
  <div class="wrap split">
    <div class="rv l">
      <span class="eyebrow">Notre institution</span>
      <h2>Une école <em>reconnue</em>, ouverte sur le monde</h2>
      <div class="divider"></div>
      <div class="body">
        <p>L'École Internationale d'Esthétique et de Cosmétologie « Esthé-PRO » est un établissement privé de formation professionnelle spécialisé dans les métiers de l'esthétique et de la cosmétique, <b>autorisé et agréé par l'État</b> (autorisation n° 4/07/9/2003).</p>
        <p>Membre de la Confédération Internationale des Écoles de Formation d'Esthétique-Cosmétique (C.I.E.F.EC) depuis 2003, l'école inscrit sa mission dans une dynamique de transmission, d'exigence professionnelle et d'ouverture sur le monde.</p>
        <p>Cette vocation internationale ouvre nos apprenantes à la diversité des approches esthétiques et aux évolutions de la cosmétologie, pour répondre aux attentes d'une clientèle variée et envisager leur avenir au-delà des frontières.</p>
      </div>
    </div>
    <div class="split-media rv r">
      {img("soin1", 640, 800, "Soin du visage à l'école Esthé-PRO", cls="main img-rv")}
      {img("lab", 360, 360, "Formulation et analyse cosmétique", cls="float rv")}
      <div class="badge rv" style="--d:.3s"><b>2003</b><span>Agréée par l'État</span></div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow rv">L'excellence pédagogique</span>
      <h2 class="rv">Des fondements scientifiques, une maîtrise technique, <em>une pratique encadrée</em></h2>
      <p class="lead rv">Notre démarche accorde une place essentielle à l'écoute, au conseil personnalisé et au respect des règles d'hygiène et de sécurité. Elle développe autant la précision du geste que la compréhension des soins et la qualité de la relation client.</p>
    </div>
    <div class="pillars" data-stagger>
      <div class="pillar"><span class="n">01 — Notre mission</span><h3>Transmettre l'exception</h3><p>Un savoir-faire fondé sur la science, la sécurité et le respect de l'harmonie naturelle.</p></div>
      <div class="pillar"><span class="n">02 — Notre pédagogie</span><h3>Apprendre en pratiquant</h3><p>Des ateliers pratiques en petits groupes, encadrés par des experts reconnus.</p></div>
      <div class="pillar"><span class="n">03 — Nos certifications</span><h3>Exercer en confiance</h3><p>Des formations certifiantes reconnues, pour exercer avec professionnalisme dès la fin du cursus.</p></div>
    </div>
  </div>
</section>

<section class="bg-soft" id="fondateurs">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow rv">Les fondateurs</span>
      <h2 class="rv">Une vision portée <em>par des experts</em></h2>
    </div>
    <div class="founders" data-stagger>
      <article class="founder">
        <div class="mono">TC</div>
        <h3>Mme Touria F. Cherkaoui</h3>
        <p class="role">Esthéticienne · Fondatrice · Formatrice permanente</p>
        <ul><li>Académie Internationale Edith Serei, Montréal</li><li>25 ans d'expérience</li></ul>
        <p>Son parcours au Canada nourrit la vocation internationale de l'école. Sa pédagogie privilégie la pratique encadrée, la précision du geste et l'acquisition progressive de l'autonomie, avec une attention particulière au conseil personnalisé. Son ambition : former des esthéticiennes compétentes et responsables, capables d'affirmer leur identité professionnelle.</p>
        <blockquote>« J'ai créé cette école pour que chaque passion puisse devenir une vocation. »</blockquote>
      </article>
      <article class="founder">
        <div class="mono">BC</div>
        <h3>Dr B. Cherkaoui, Pharm.D.</h3>
        <p class="role">Docteur en pharmacie · Professeur de dermo-cosmétologie</p>
        <ul><li>36 ans en pharmacie</li><li>25 ans d'enseignement</li><li>Membre de la Société Française de Cosmétologie</li></ul>
        <p>Il relie biologie cutanée, étude des actifs et analyse des compositions à des cas pratiques, pour développer le discernement, l'esprit critique et l'autonomie des apprenants. Sa conviction : la qualité du conseil et des soins exige un savoir solide, une pratique réfléchie et une éthique rigoureuse.</p>
        <blockquote>« L'avenir de la cosmétologie se construit avec science, conscience et passion. »</blockquote>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow rv">Nos formations</span><h2 class="rv">Choisissez <em>votre parcours</em></h2></div>
    <div class="courses" data-stagger>
      <a class="course" href="/formation-estheticienne"><div class="img">{img("visage2", 640, 480, "Formation esthéticienne")}<span class="tag sky">Diplômante</span></div><div class="body"><h3>Formation Esthéticienne</h3><p>Une année complète pour devenir esthéticienne et créer votre propre activité.</p><span class="go">Découvrir <i>{A}</i></span></div></a>
      <a class="course" href="/formation-esthetique-pour-adultes"><div class="img">{img("adulte1", 640, 480, "Esthétique pour adultes")}<span class="tag">Certifiante</span></div><div class="body"><h3>Esthétique pour Adultes</h3><p>6 mois, le samedi, pour une reconversion concrète sans quitter votre emploi.</p><span class="go">Découvrir <i>{A}</i></span></div></a>
      <a class="course" href="/formation-dermocosmetique-appliquee-a-la-parapharmacie"><div class="img">{img("dermo2", 640, 480, "Dermo-cosmétique")}<span class="tag">Certifiante</span></div><div class="body"><h3>Dermo-Cosmétique</h3><p>À distance, en live : devenez une dermo-conseillère experte en parapharmacie.</p><span class="go">Découvrir <i>{A}</i></span></div></a>
    </div>
  </div>
</section>

{final_cta("institut")}
</main>
{footer()}'''
    return head("L'école Esthé-PRO — Agréée par l'État depuis 2003 | Rabat",
      "Découvrez Esthé-PRO : école d'esthétique et de cosmétologie agréée par l'État, membre de la C.I.E.F.EC, fondée par une esthéticienne diplômée à Montréal et un docteur en pharmacie.",
      "/ecole-esthe-pro", og="classe") + body

# ---------------------------------------------------------------- FORMATION TEMPLATE
def formation(d):
    infos = "".join(f'<div class="info">{ICON[i]}<span>{k}</span><b>{v}</b></div>' for i,k,v in d["infos"])
    prog = "".join(f"<li>{p}</li>" for p in d["programme"]) if d.get("programme") else ""
    modules = "".join(f'<div class="module rv"><span class="n">{n:02d}</span><div><h3>{t}</h3><p>{x}</p></div></div>' for n,(t,x) in enumerate(d.get("modules",[]),1))
    publics = "".join(f"<li>{p}</li>" for p in d["public"])
    debouches = "".join(f'<div class="tile">{ICON[i]}<b>{t}</b><span>{s}</span></div>' for i,t,s in d["debouches"])
    objectifs = "".join(f"<li>{o}</li>" for o in d["objectifs"])
    href = f"/inscription?formation={d['q']}"
    prog_block = f'<ul class="prog" data-stagger>{prog}</ul>' if prog else f'<div class="modules">{modules}</div>'
    body = f'''
<body data-course="{d['name']}">
{header(d['active'])}
<main>
{page_hero(d['eyebrow'], d['h1'], d['lead'], d['hero'],
  CR(HOME, '<a href="/#formations">Formations</a>', d['short']),
  actions=f'<a class="btn btn-sky" href="{href}" data-track="course_hero">{d["cta"]} {A}</a><a class="btn btn-light" href="#programme">Voir le programme</a>',
  facts="".join(fact(i,t) for i,t in d["facts"]), alt=d['hero_alt'])}

<section class="bg-soft" style="padding:60px 0">
  <div class="wrap"><div class="infos" data-stagger>{infos}</div></div>
</section>

<section>
  <div class="wrap split">
    <div class="split-media rv l">
      {img(d['img1'], 640, 800, d['img1_alt'], cls="main img-rv")}
      {img(d['img2'], 360, 360, d['img2_alt'], cls="float rv")}
    </div>
    <div class="rv r">
      <span class="eyebrow">{d['about_eyebrow']}</span>
      <h2>{d['about_h2']}</h2>
      <div class="divider"></div>
      <div class="body">{d['about']}</div>
      <ul class="checks">{objectifs}</ul>
    </div>
  </div>
</section>

<section class="bg-soft" id="programme">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow rv">Programme</span><h2 class="rv">{d['prog_h2']}</h2><p class="lead rv">{d['prog_lead']}</p></div>
    {prog_block}
    <div class="center rv" style="margin-top:44px"><a class="btn" href="{href}" data-track="course_prog">{d['cta']} {A}</a></div>
  </div>
</section>

<section>
  <div class="wrap cols2">
    <div class="card rv l">
      <span class="eyebrow">Pour qui ?</span>
      <h3 style="margin-top:12px">{d['public_h']}</h3>
      <ul class="checks">{publics}</ul>
    </div>
    <div class="card rv r">
      <span class="eyebrow">Encadrement</span>
      <h3 style="margin-top:12px">{d['team_h']}</h3>
      <ul class="checks">{"".join(f"<li>{t}</li>" for t in d['team'])}</ul>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow rv">Débouchés</span><h2 class="rv">{d['deb_h2']}</h2></div>
    <div class="tiles" data-stagger>{debouches}</div>
  </div>
</section>

{session_box(d['session_img'], d['session_title'], d['session_text'], href)}

<section class="bg-soft">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow rv">Questions fréquentes</span><h2 class="rv">Vos questions sur la <em>{d['short']}</em></h2></div>
    <div class="faq">{faq(d['faq'])}</div>
  </div>
</section>

{final_cta(d['final_img'], preset=d['name'])}
</main>
{footer()}'''
    course_schema = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Course","name":"{d['name']}","description":"{d['desc']}","provider":{{"@type":"EducationalOrganization","name":"École Esthé-PRO","sameAs":"{SITE}"}}}}</script>{faq_schema(d['faq'])}'''
    return head(d['title'], d['desc'], d['url'], og=d['hero'], extra=course_schema) + body

ESTH = dict(
  name="Formation Esthéticienne", short="Formation Esthéticienne", q="estheticienne", active="f-esth", url="/formation-estheticienne",
  title="Formation Esthéticienne à Rabat — 1 an, diplômante | Esthé-PRO",
  desc="Formation esthéticienne diplômante d'un an en présentiel à Agdal, Rabat : soins du visage, Hydrafacial, épilation, lumière pulsée, massages, dermo-cosmétique. École agréée par l'État.",
  eyebrow="Formation diplômante · 1 an", h1="Devenez <em>esthéticienne</em> professionnelle en une année.",
  lead="Du diagnostic de peau à la création de votre institut : une formation complète en présentiel pour maîtriser les soins, les techniques et les technologies du métier — et être prête à exercer.",
  hero="hydra", hero_alt="Élève esthéticienne réalisant un soin Hydrafacial",
  cta="Réserver ma place",
  facts=[("cal","Durée : 1 an"),("home","100 % présentiel"),("cap","Diplôme remis"),("pin","Agdal, Rabat")],
  infos=[("cal","Durée","Une année"),("home","Format","100 % en présentiel"),("cap","Validation","Diplôme de fin de formation"),("users","Accompagnement","Personnalisé, en petits groupes")],
  img1="visage", img1_alt="Soin du visage en cabine", img2="conseil2", img2_alt="Conseil dermo-cosmétique",
  about_eyebrow="La formation", about_h2="Une formation solide, pensée pour <em>le marché du travail</em>",
  about="<p>À l'école Esthé-PRO, vous apprendrez à examiner la peau et poser un diagnostic dermo-esthétique, à réaliser des soins du visage dont l'Hydrafacial, et à construire des ordonnances dermo-cosmétiques en vous appuyant sur la cosmétologie.</p><p>Vous maîtriserez aussi l'épilation et la lumière pulsée, les massages relaxants et amincissants, l'amincissement Tech, les soins des mains et des pieds — ainsi que la vente et la création de projet pour lancer votre activité.</p>",
  objectifs=["Acquérir des connaissances fondamentales fiables","Maîtriser les techniques, outils et technologies du métier","Adopter une démarche professionnelle rigoureuse","Développer autonomie, sens des responsabilités et qualités relationnelles","Favoriser l'insertion professionnelle et l'évolution de carrière"],
  prog_h2="15 compétences pour <em>exercer dès la sortie</em>", prog_lead="Un programme qui couvre l'ensemble du métier, du soin à la gestion de votre future activité.",
  programme=["Soins du visage","Examen de la peau","Diagnostic dermo-esthétique","Hydrafacial","Ordonnances dermo-cosmétiques","Cosmétologie","Épilation","Lumière pulsée","Massage relaxant vital","Massage amincissant","Amincissement Tech","Soins des mains","Soins des pieds","Techniques de vente","Création de projet"],
  public_h="Cette formation est faite pour vous si…", public=["Vous êtes une jeune femme qui souhaite entrer dans les métiers de l'esthétique","Vous êtes en reconversion professionnelle","Vous êtes passionnée d'esthétique et de bien-être"],
  team_h="Des professionnelles à vos côtés", team=["Esthéticiennes professionnelles à la longue expérience pédagogique","Intervenants spécialisés en dermo-cosmétologie","Accompagnement personnalisé de chaque élève"],
  deb_h2="Les métiers qui <em>vous attendent</em>",
  debouches=[("store","Créatrice d'institut","Ouvrez votre propre institut de beauté"),("flask","Créatrice de parapharmacie","Lancez votre parapharmacie"),("spark","Esthéticienne en institut ou spa","Rejoignez une équipe professionnelle"),("home","Esthéticienne indépendante","À domicile ou à votre compte"),("heart","Cabinet de dermatologie","Collaborez avec des dermatologues"),("brief","Conseillère, animatrice, gérante","Pharmacie, marque cosmétique, institut ou spa")],
  session_img="soin-gants", session_title="Rentrée : réservez votre place", session_text="Les ateliers se déroulent en petits groupes pour que chaque élève soit suivie de près. Les places sont donc limitées à chaque session.",
  final_img="eleves",
  faq=[("La formation est-elle diplômante ?","Oui, un <b>diplôme</b> vous est remis à la fin de la formation. Esthé-PRO est une école agréée par l'État (autorisation n° 4/07/9/2003)."),
       ("Combien de temps dure la formation ?","Une année, <b>100 % en présentiel</b> dans nos locaux d'Agdal, à Rabat."),
       ("Apprend-on vraiment l'Hydrafacial et la lumière pulsée ?","Oui. Ces techniques font partie du programme, aux côtés des soins du visage, de l'épilation, des massages et de l'amincissement Tech."),
       ("Pourrai-je ouvrir mon propre institut ?","C'est l'un des objectifs : le programme inclut des techniques de vente et de création de projet pour vous préparer à lancer votre activité."),
       ("Quels sont les tarifs et les conditions d'admission ?","Notre conseiller pédagogique vous les communique lors de votre pré-inscription, gratuite et sans engagement, après un échange sur votre projet.")])

ADU = dict(
  name="Formation Esthétique pour Adultes", short="Esthétique pour Adultes", q="adultes", active="f-adu", url="/formation-esthetique-pour-adultes",
  title="Formation Esthétique pour Adultes — Le samedi, 6 mois | Esthé-PRO Rabat",
  desc="Reconversion en esthétique à Rabat : formation certifiante de 6 mois, chaque samedi de 10h à 15h, en petits groupes, sans diplôme requis. 100 % pratique.",
  eyebrow="Formation certifiante · 6 mois", h1="Changez de vie, <em>le samedi</em>.",
  lead="Une formation 100 % pratique pensée pour les femmes en reconversion, en recherche d'emploi ou qui veulent ajouter une compétence — sans mettre leur emploi entre parenthèses.",
  hero="adulte3", hero_alt="Formatrice et élève adulte pendant un soin",
  cta="Réserver ma place",
  facts=[("cal","6 mois"),("clock","Samedi 10h – 15h"),("users","Petits groupes"),("cap","Aucun diplôme requis")],
  infos=[("cal","Durée","06 mois"),("clock","Horaire","Chaque samedi, 10h – 15h"),("users","Format","Présentiel, petits groupes"),("cap","Prérequis","Aucun diplôme requis")],
  img1="adulte2", img1_alt="Atelier pratique de soin du visage", img2="adulte1", img2_alt="Formatrices Esthé-PRO",
  about_eyebrow="Une reconversion concrète", about_h2="Apprenez à votre rythme, <em>gagnez en confiance</em>",
  about="<p>Cette formation offre une reconversion concrète et progressive vers les métiers de l'esthétique. Vous acquérez les bases essentielles des soins du visage et du corps, de l'épilation, ainsi que les règles d'hygiène et la relation client.</p><p>Grâce à une approche 100 % pratique, chaque apprenante développe des gestes professionnels et gagne en confiance pour construire son projet dans l'univers de l'esthétique.</p>",
  objectifs=["Maîtriser les soins essentiels du visage et du corps","Pratiquer chaque semaine sur de vrais gestes professionnels","Appliquer les règles d'hygiène et soigner la relation client","Construire votre projet : institut, domicile ou activité indépendante"],
  prog_h2="Les gestes <em>essentiels</em> du métier", prog_lead="Un programme ciblé sur les soins les plus demandés en institut.",
  programme=["Soins du visage / Hydrafacial","Examen de la peau et diagnostic dermo-esthétique","Ordonnances dermo-cosmétiques","Massage relaxant vital","Massage amincissant","Épilation","Lumière pulsée"],
  public_h="Cette formation est faite pour vous si…", public=["Vous êtes en reconversion professionnelle","Vous êtes en recherche d'emploi","Vous travaillez et souhaitez développer une nouvelle compétence","Vous n'avez pas de diplôme : aucun n'est requis"],
  team_h="Une formatrice qui vous accompagne pas à pas", team=["25 ans d'expérience professionnelle et pédagogique","Corrections individuelles pendant chaque atelier","Un groupe réduit pour progresser plus vite"],
  deb_h2="Où exercer <em>après la formation</em>",
  debouches=[("spark","Institut de beauté","Rejoindre une équipe en institut"),("heart","Spa","Soins et bien-être"),("store","Parfumerie","Conseil et soins en boutique"),("home","Esthétique à domicile","Travailler à votre rythme"),("brief","Votre propre activité","Créer votre entreprise"),("users","Nouvelle compétence","Valoriser votre profil actuel")],
  session_img="adulte1", session_title="Le prochain groupe du samedi démarre bientôt", session_text="Les groupes sont volontairement réduits pour que chaque apprenante pratique et soit corrigée. Réservez votre place pour la prochaine session.",
  final_img="adulte2",
  faq=[("Je travaille la semaine, est-ce compatible ?","Oui, c'est le principe : la formation a lieu <b>chaque samedi de 10h à 15h</b>, pendant 6 mois."),
       ("Faut-il un diplôme ?","Non, <b>aucun diplôme n'est requis</b>. La formation part des bases et progresse pas à pas."),
       ("La formation est-elle certifiante ?","Oui, il s'agit d'une formation certifiante délivrée par Esthé-PRO, école agréée par l'État."),
       ("Est-ce vraiment pratique ?","Oui, la formation est 100 % pratique et accompagnée, en petits groupes, avec une formatrice qui corrige vos gestes."),
       ("Quels sont les tarifs ?","Notre conseiller pédagogique vous les communique lors de votre pré-inscription, gratuite et sans engagement.")])

DERMO = dict(
  name="Formation Dermo-Cosmétique", short="Dermo-Cosmétique", q="dermo", active="f-dermo", url="/formation-dermocosmetique-appliquee-a-la-parapharmacie",
  title="Formation Dermo-Cosmétique appliquée à la Parapharmacie — en ligne | Esthé-PRO",
  desc="Formation dermo-cosmétique certifiante 100 % à distance, en live sur Zoom : physiologie de la peau, actifs, analyse INCI, ordonnances et cas de comptoir. Pour pharmaciens, préparateurs, conseillers.",
  eyebrow="Formation certifiante · 100 % à distance", h1="Conseillez en <em>dermo-cosmétique</em> avec assurance.",
  lead="Maîtrisez la peau, décryptez les formules, construisez des ordonnances adaptées à chaque client — en pharmacie comme en parapharmacie. En live sur Zoom, depuis chez vous.",
  hero="dermo1", hero_alt="Conseillère dermo-cosmétique avec une cliente en parapharmacie",
  cta="Réserver ma place",
  facts=[("screen","Live sur Zoom"),("mic","Échanges en direct"),("flask","Cas de comptoir"),("cap","Certifiante")],
  infos=[("screen","Format","100 % à distance"),("mic","Cours","Live sur Zoom"),("flask","Pratique","TD, cas de comptoir, synthèses"),("cap","Supports","Fournis à chaque module")],
  img1="conseil1", img1_alt="Conseil dermo-cosmétique au comptoir", img2="produits2", img2_alt="Produits dermo-cosmétiques",
  about_eyebrow="La formation", about_h2="De la physiologie de la peau <em>au conseil au comptoir</em>",
  about="<p>Cette formation vous apprend la physiologie de la peau, les actifs cosmétiques et l'analyse des compositions INCI. À travers des cas de comptoir et des travaux dirigés, vous apprenez à construire des ordonnances dermo-cosmétiques et à conseiller avec assurance.</p><p>Elle est conçue et animée sous la direction de Dr B. Cherkaoui, docteur en pharmacie et professeur de dermo-cosmétologie, membre de la Société Française de Cosmétologie.</p>",
  objectifs=["Comprendre la structure et la physiologie de la peau","Connaître les actifs, leurs propriétés et leurs indications","Lire et interpréter une liste INCI","Maîtriser les 4 niveaux de conseil : Basique, Plus, Extra et Ultra"],
  prog_h2="5 modules pour devenir <em>dermo-conseiller(e)</em>", prog_lead="Un parcours progressif, de la biologie cutanée aux cas réels de comptoir.",
  modules=[("Biologie de la peau","Comprendre sa structure et sa physiologie."),("Cosmétologie et actifs cosmétiques","Connaître les ingrédients, leurs propriétés et leurs indications."),("Analyse des produits dermo-cosmétiques","Décortiquer et interpréter les compositions selon la nomenclature INCI."),("Conseil et ordonnances dermo-cosmétiques","Maîtriser les niveaux de conseil : le Basique, le Plus, l'Extra et l'Ultra."),("Cas de comptoir et études de cas","Travaux dirigés, exercices d'application et activités de synthèse.")],
  public_h="Cette formation s'adresse à…", public=["Pharmaciens et pharmaciennes d'officine qui veulent développer leur parapharmacie","Préparateurs en pharmacie souhaitant se perfectionner en conseil","Vendeurs et conseillers en parapharmacie","Esthéticiennes et passionnées de cosmétique","Personnes en reconversion passionnées par la dermo-cosmétique"],
  team_h="Comment se déroulent les cours", team=["Cours en direct sur Zoom, avec échanges en temps réel","Supports pédagogiques fournis","Travaux dirigés, exercices d'application et travaux de synthèse","Responsable : Dr B. Cherkaoui, Pharm.D."],
  deb_h2="Ce que cette formation <em>vous ouvre</em>",
  debouches=[("store","Projet de parapharmacie","Créer et développer votre espace"),("flask","Conseiller(e) dermo-cosmétique","En pharmacie ou parapharmacie"),("spark","Animateur(trice) de marque","Pour une marque dermo-cosmétique"),("brief","Délégué(e) commercial(e)","Chez un distributeur de cosmétiques"),("mic","Formateur(trice) produits","Former les équipes de vente"),("heart","Entrepreneur(e)","Dans le secteur cosmétique")],
  session_img="distance", session_title="Votre futur métier, depuis chez vous", session_text="Une formation en live sur Zoom pour devenir dermo-conseillère experte. Places limitées : réservez la vôtre dès maintenant.",
  final_img="produits",
  faq=[("La formation se fait-elle entièrement en ligne ?","Oui, elle est <b>100 % à distance</b>, en live sur l'application Zoom, avec des échanges en direct avec le formateur."),
       ("Faut-il être pharmacien pour suivre la formation ?","Non. Elle s'adresse aussi aux préparateurs, conseillers en parapharmacie, esthéticiennes et personnes en reconversion passionnées par la dermo-cosmétique."),
       ("Y a-t-il de la pratique ?","Oui : cas de comptoir, études de cas, travaux dirigés, exercices d'application et travaux de synthèse."),
       ("Qui anime la formation ?","Dr B. Cherkaoui, docteur en pharmacie, professeur de dermo-cosmétologie et membre de la Société Française de Cosmétologie."),
       ("Quels sont les tarifs et le calendrier ?","Notre conseiller pédagogique vous les communique lors de votre pré-inscription, gratuite et sans engagement.")])

# ---------------------------------------------------------------- INSCRIPTION
def inscription():
    picks = "".join(f'''<div class="opt"><input type="radio" name="formation" id="p{i}" value="{n}"><label for="p{i}"><b>{s}</b><small>{d}</small><em>{m}</em></label></div>''' for i,(n,s,d,m) in enumerate([
      ("Formation Esthéticienne","Esthéticienne","Le parcours complet pour devenir esthéticienne professionnelle.","1 an · présentiel · diplômante"),
      ("Formation Esthétique pour Adultes","Esthétique pour Adultes","Reconversion ou nouvelle compétence, sans quitter votre emploi.","6 mois · le samedi"),
      ("Formation Dermo-Cosmétique","Dermo-Cosmétique","Conseil en pharmacie et parapharmacie : peau, actifs, INCI.","100 % à distance · Zoom")],1))
    body = f'''
<body>
{header('insc')}
<main>
<section class="page-hero" style="padding:0">
  <div class="wrap" style="padding:64px 0 120px;text-align:center">
    <div class="intro-anim">
      <nav class="crumbs" style="justify-content:center">{CR(HOME, "Pré-inscription")}</nav>
      <h1 style="color:#fff;margin:16px auto 16px">Formulaire de <em>pré-inscription</em></h1>
      <p class="lead" style="margin:0 auto;max-width:720px">Donnez vie à votre avenir dans l'esthétique ou la dermo-cosmétique. Remplissez ce formulaire en 2 minutes : notre conseiller pédagogique vous contacte pour vous présenter le programme et les modalités d'inscription.</p>
    </div>
  </div>
</section>
<section style="padding-top:0;margin-top:-80px">
  <div class="wrap insc-grid">
    <div class="form-wrap rv z">
      <form data-lead="full" novalidate>
        <fieldset class="block">
          <legend class="f-title"><span class="num-c">1</span>Choix de formation <span style="color:var(--sky)">*</span></legend>
          <p class="f-sub">Sélectionnez la formation qui vous intéresse.</p>
          <div class="pick">{picks}</div>
          <label class="check unsure"><input type="radio" name="formation" value="Je ne sais pas encore"> Je ne sais pas encore, je souhaite être conseillé(e)</label>
          <p class="group-err">Veuillez choisir une formation.</p>
        </fieldset>
        <fieldset class="block">
          <legend class="f-title"><span class="num-c">2</span>Vos informations</legend>
          <p class="f-sub">Les champs marqués d'un * sont obligatoires.</p>
          <div class="grid2">
            <div class="field"><label for="prenom">Prénom <i>*</i></label><input id="prenom" name="prenom" autocomplete="given-name" data-req><p class="err">Veuillez indiquer votre prénom.</p></div>
            <div class="field"><label for="nom">Nom <i>*</i></label><input id="nom" name="nom" autocomplete="family-name" data-req><p class="err">Veuillez indiquer votre nom.</p></div>
            <div class="field"><label for="ville">Ville <i>*</i></label><input id="ville" name="ville" list="villes" autocomplete="address-level2" data-req><datalist id="villes"><option value="Rabat"><option value="Salé"><option value="Témara"><option value="Kénitra"><option value="Skhirat"><option value="Casablanca"></datalist><p class="err">Veuillez indiquer votre ville.</p></div>
            <div class="field"><label for="niveau">Niveau d'études <i>*</i></label><select id="niveau" name="niveau" data-req><option value="">Sélectionnez</option><option>Niveau collège</option><option>Niveau lycée</option><option>Baccalauréat</option><option>Bac+2</option><option>Bac+3 et plus</option><option>Autre</option></select><p class="err">Veuillez sélectionner votre niveau d'études.</p></div>
            <div class="field"><label for="tel">Numéro de téléphone <i>*</i></label><div class="tel"><span>+212</span><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel-national" placeholder="6 12 34 56 78" data-req="phone"></div><p class="err">Numéro invalide (ex : 06 12 34 56 78).</p></div>
            <div class="field"><label for="email">E-mail <i>*</i></label><input id="email" name="email" type="email" inputmode="email" autocomplete="email" placeholder="vous@exemple.com" data-req="email"><p class="err">Adresse e-mail invalide.</p></div>
            <label class="check full"><input type="checkbox" name="sameWa" checked> Mon numéro WhatsApp est le même que mon numéro de téléphone</label>
            <div class="field full f-wa" hidden><label for="wa">Numéro de WhatsApp <i>*</i></label><div class="tel"><span>+212</span><input id="wa" name="wa" type="tel" inputmode="tel" placeholder="6 12 34 56 78" data-req="phone"></div><p class="err">Numéro WhatsApp invalide.</p></div>
            <div class="field full"><label for="message">Message <small>(facultatif)</small></label><textarea id="message" name="message" placeholder="Une question sur les horaires, la rentrée, les modalités…"></textarea></div>
          </div>
          <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
        </fieldset>
        <button class="btn btn-block" type="submit">Envoyer ma pré-inscription {A}</button>
        <p class="legal">{ICON['lock']} Gratuit et sans engagement. Vos informations restent confidentielles.</p>
      </form>
    </div>
    <aside class="form-aside">
      <div class="aside-card rv r">
        <h3>Et ensuite ?</h3>
        <ol>
          <li><p><b>Appel du conseiller</b>Nous vous contactons pour comprendre votre projet.</p></li>
          <li><p><b>Étude de dossier</b>Nous vérifions avec vous les conditions d'admission.</p></li>
          <li><p><b>Validation</b>Confirmation d'admission et finalisation de l'inscription.</p></li>
        </ol>
      </div>
      <div class="aside-help rv r" style="--d:.1s">
        <h3 style="font-size:22px">Une question ?</h3>
        <p>Notre équipe vous répond directement sur WhatsApp ou par téléphone.</p>
        <a class="btn btn-wa btn-block btn-sm" data-wa data-place="inscription">{ICON['wa']} Écrire sur WhatsApp</a>
        <a class="btn btn-ghost btn-block btn-sm" href="tel:+212762575813" style="margin-top:10px">{ICON['phone']} 07 62 57 58 13</a>
      </div>
      <div class="aside-help rv r" data-session style="--d:.2s">
        <span class="eyebrow">Prochaine rentrée</span>
        <h3 style="font-size:24px;margin:10px 0 4px" data-session-label></h3>
        <p style="margin:0">Places limitées · <b data-cd="short" style="color:var(--blue)"></b></p>
      </div>
    </aside>
  </div>
</section>
</main>
{footer(mbar=False)}'''
    return head("S'inscrire — Pré-inscription | École Esthé-PRO",
      "Pré-inscription gratuite à l'école Esthé-PRO : Formation Esthéticienne, Esthétique pour Adultes ou Dermo-Cosmétique. Un conseiller pédagogique vous rappelle.",
      "/inscription", og="eleves") + body

# ---------------------------------------------------------------- CONTACT
def contact():
    body = f'''
<body>
{header('contact')}
<main>
{page_hero("Nos coordonnées", "Parlons de <em>votre projet</em>.",
  "Une question sur une formation, la rentrée ou les modalités d'inscription ? Notre équipe vous répond par téléphone, WhatsApp ou directement à l'école, au cœur d'Agdal.",
  "cabine2", CR(HOME, "Contact"),
  actions=f'<a class="btn btn-wa" data-wa data-place="contact_hero">{ICON["wa"]} Écrire sur WhatsApp</a><a class="btn btn-light" href="tel:+212762575813">Appeler l\'école</a>',
  alt="Cabine de soins de l'école Esthé-PRO")}
<section>
  <div class="wrap contact-grid">
    <div class="c-items" data-stagger>
      <a class="c-item" href="https://www.google.com/maps/search/?api=1&query=Avenue+Michlifen+Rue+Jabal+Al+Ayachi+Agdal+Rabat" target="_blank" rel="noopener"><span class="ic">{ICON['pin']}</span><div><span>Adresse</span><b>Angle Avenue Michlifen et Rue Jabal Al Ayachi, Imm. 49, 3ème étage, n°8 — Agdal, Rabat</b></div></a>
      <a class="c-item" href="tel:+212762575813"><span class="ic">{ICON['phone']}</span><div><span>Téléphone / WhatsApp</span><b>+212 7 62 57 58 13</b></div></a>
      <a class="c-item" href="mailto:esthepro_ma@yahoo.fr"><span class="ic">{ICON['mail']}</span><div><span>E-mail</span><b>esthepro_ma@yahoo.fr</b></div></a>
      <div class="c-item"><span class="ic">{ICON['tram']}</span><div><span>Accès</span><b>À 5 minutes de la station de tramway Avenue de France</b></div></div>
    </div>
    <div class="rv r"><iframe class="map" title="Plan d'accès Esthé-PRO" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Avenue+Michlifen+Rue+Jabal+Al+Ayachi+Agdal+Rabat&output=embed"></iframe></div>
  </div>
</section>
{final_cta("visage2", title="Vous préférez qu'on <em>vous rappelle</em> ?")}
</main>
{footer()}'''
    return head("Contact — École Esthé-PRO, Agdal Rabat",
      "Contactez l'école Esthé-PRO : angle Avenue Michlifen et Rue Jabal Al Ayachi, Agdal, Rabat. Tél./WhatsApp +212 7 62 57 58 13.",
      "/contact", og="cabine2") + body

# ---------------------------------------------------------------- MERCI
def merci():
    body = f'''
<body>
{header()}
<main>
<section class="bg-soft">
  <div class="wrap thanks" id="thanks">
    <div class="ok"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></div>
    <span class="eyebrow">Demande bien reçue</span>
    <h1 id="tTitle" style="font-size:clamp(34px,5vw,54px);margin:14px 0 16px">Merci <span id="tName"></span>&nbsp;!</h1>
    <p class="lead" id="tText">Votre demande a bien été transmise. Notre conseiller pédagogique vous contacte très prochainement pour vous présenter le programme et les modalités d'inscription.</p>
    <div class="recap" id="recap"></div>
    <a class="btn btn-wa" id="waConfirm" href="#">{ICON['wa']} <span id="waLabel">Accélérer : confirmer sur WhatsApp</span></a>
    <div class="next">
      <div><b>1. Appel du conseiller</b><span>Gardez votre téléphone à portée de main : nous vous contactons rapidement.</span></div>
      <div><b>2. Étude de dossier</b><span>Nous vérifions ensemble la formation adaptée à votre projet.</span></div>
      <div><b>3. Validation</b><span>Vous recevez la confirmation et les étapes pour finaliser.</span></div>
    </div>
    <p style="margin-top:40px;font-family:var(--spin);color:var(--slate)">En attendant, suivez la vie de l'école sur <a href="https://www.instagram.com/ecole.esthe.pro/" target="_blank" rel="noopener" style="color:var(--navy-2)">Instagram</a>.</p>
  </div>
</section>
</main>
{footer(mbar=False)}'''
    return head("Merci — Votre demande est envoyée | Esthé-PRO", "Merci pour votre pré-inscription à l'école Esthé-PRO.", "/merci", noindex=True) + body

def notfound():
    body = f'''
<body>
{header()}
<main><section class="bg-soft"><div class="wrap thanks">
  <span class="eyebrow">Erreur 404</span>
  <h1 style="margin:14px 0 16px">Cette page <em>n'existe pas</em>.</h1>
  <p class="lead">Elle a peut-être été déplacée. Découvrez nos formations ou faites votre pré-inscription.</p>
  <div class="hero-actions" style="justify-content:center"><a class="btn" href="/">Retour à l'accueil</a><a class="btn btn-ghost" href="/inscription">Pré-inscription</a></div>
</div></section></main>
{footer(mbar=False)}'''
    return head("Page introuvable | Esthé-PRO", "Page introuvable.", "/404", noindex=True) + body
