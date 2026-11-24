from parts import *

def home():
    F = [
     ("L'école est-elle reconnue ?", "Oui. Esthé-PRO est un établissement privé de formation professionnelle <b>autorisé et agréé par l'État</b> (autorisation n° 4/07/9/2003) et membre de la Confédération Internationale des Écoles de Formation d'Esthétique-Cosmétique (C.I.E.F.EC) depuis 2003."),
     ("Quelle formation choisir ?", "Vous voulez faire de l'esthétique votre métier à temps plein : la <b>Formation Esthéticienne</b> (1 an, diplômante). Vous travaillez déjà ou vous êtes en reconversion : <b>l'Esthétique pour Adultes</b> (6 mois, le samedi). Vous travaillez ou souhaitez travailler en pharmacie ou parapharmacie : la <b>Dermo-Cosmétique</b> (100 % à distance). En cas de doute, notre conseiller vous oriente gratuitement."),
     ("Faut-il un diplôme pour s'inscrire ?", "Pour la Formation Esthétique pour Adultes, <b>aucun diplôme n'est requis</b>. Pour les autres parcours, votre dossier est étudié avec vous lors de la pré-inscription afin de vérifier les conditions d'admission."),
     ("Quels sont les tarifs ?", "Les frais dépendent de la formation choisie. Notre conseiller pédagogique vous communique le programme détaillé, le calendrier et les tarifs dès votre pré-inscription — gratuite et sans engagement."),
     ("Où se trouve l'école ?", "Au cœur d'Agdal, à Rabat : angle Avenue Michlifen et Rue Jabal Al Ayachi, Imm. 49, 3ème étage, n°8 — à cinq minutes de la station de tramway Avenue de France."),
    ]
    c = COURSES
    body = f'''
<body>
{header('home')}
<main>
<section class="home-hero">
  <div class="bgimg">{img("hydra", 1920, 1080, "Élève esthéticienne réalisant un soin du visage à l'école Esthé-PRO", eager=True)}</div>
  <div class="wrap intro-anim">
    <span class="eyebrow">École agréée par l'État · Agdal, Rabat</span>
    <h1>Faites de votre passion pour la beauté un <em>métier d'excellence</em>.</h1>
    <p class="lead">Soins du visage, Hydrafacial, lumière pulsée, dermo-cosmétique : depuis 25 ans, Esthé-PRO forme des professionnelles précises dans leurs gestes, solides dans leurs connaissances et sûres d'elles face à la clientèle.</p>
    <div class="hero-actions">
      <a class="btn btn-sky" href="/inscription" data-track="hero_cta">Je me pré-inscris {A}</a>
      <a class="btn btn-light" href="#formations">Découvrir les formations</a>
    </div>
    <div class="hero-proof">
      <div><b><span data-count="25">25</span> ans</b><span>d'expertise pédagogique</span></div>
      <div><b>2003</b><span>agréée par l'État</span></div>
      <div><b><span data-count="3">3</span></b><span>formations certifiantes</span></div>
    </div>
  </div>
  <a href="#ecole" class="scroll-cue" aria-label="Défiler"></a>
</section>

<div class="marquee" aria-hidden="true"><div class="track">{''.join(f'<span>{w}</span>' for w in ["Dermocosmétique","Formation","Esthétique","Innovation","Excellence","Rigueur","Expertise","Professionnalisme"]*2)}</div></div>

<div class="trust" data-stagger>
  <div><span class="ic">{ICON['shield']}</span><p><b>Agréée par l'État</b><span>Autorisation n° 4/07/9/2003</span></p></div>
  <div><img src="https://static.wixstatic.com/media/76852a_{IMG['ciefec']}" width="56" height="31" alt="Logo CIEFEC" loading="lazy"><p><b>Membre C.I.E.F.EC</b><span>Réseau international depuis 2003</span></p></div>
  <div><img src="https://static.wixstatic.com/media/76852a_{IMG['25ans']}/v1/fit/w_120,h_120/25ans.png" width="56" height="56" alt="25 ans" loading="lazy"><p><b>25 ans d'expertise</b><span>Pédagogique et professionnelle</span></p></div>
  <div><span class="ic">{ICON['tram']}</span><p><b>Agdal, Rabat</b><span>À 5 min du tram Avenue de France</span></p></div>
</div>

<section id="ecole">
  <div class="wrap split">
    <div class="split-media rv l">
      {img("institut", 640, 800, "Salle de soins de l'école Esthé-PRO", cls="main img-rv")}
      {img("eleves", 360, 360, "Élèves de l'école Esthé-PRO en atelier pratique", cls="float rv")}
      <div class="badge rv" style="--d:.3s"><b><span data-count="25">25</span></b><span>ans d'expertise</span></div>
    </div>
    <div class="rv r">
      <span class="eyebrow">Expertise &amp; Excellence</span>
      <h2>Le geste d'une esthéticienne, <em>la rigueur</em> d'un pharmacien.</h2>
      <div class="divider"></div>
      <div class="body">
        <p>La force d'Esthé-PRO, c'est la rencontre de deux expertises. <b>Mme Touria F. Cherkaoui</b>, esthéticienne diplômée de l'Académie Internationale Edith Serei à Montréal, et <b>Dr B. Cherkaoui</b>, docteur en pharmacie et professeur de dermo-cosmétologie.</p>
        <p>Ensemble, ils ont construit une école où l'on apprend autant à réaliser un soin qu'à comprendre la peau : théorie, pratique encadrée et études de cas, avec une exigence constante d'hygiène, de sécurité et d'éthique.</p>
      </div>
      <ul class="checks">
        <li>Ateliers pratiques en petits groupes</li>
        <li>Formatrices permanentes et intervenants experts en dermo-cosmétologie</li>
        <li>Accompagnement personnalisé de chaque élève jusqu'au diplôme</li>
      </ul>
      <div class="hero-actions"><a class="link" href="/ecole-esthe-pro">Découvrir l'école {A}</a></div>
    </div>
  </div>
</section>

<section class="bg-soft" id="formations">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow rv">Nos formations</span>
      <h2 class="rv">Trois parcours, <em>un même niveau</em> d'exigence</h2>
      <p class="lead rv">Que vous débutiez, que vous changiez de voie ou que vous travailliez déjà en pharmacie, il y a une formation Esthé-PRO conçue pour votre projet.</p>
    </div>
    <div class="courses" data-stagger>
      <a class="course" href="{c['estheticienne']['url']}">
        <div class="img">{img("visage", 640, 480, "Soin du visage en formation esthéticienne")}<span class="tag sky">Diplômante</span></div>
        <div class="body">
          <h3>Formation Esthéticienne</h3>
          <p>Du diagnostic de peau à la création de votre institut : devenez une esthéticienne complète, prête à exercer.</p>
          <div class="meta"><div><b>1 an</b>Durée</div><div><b>Présentiel</b>Agdal, Rabat</div></div>
          <span class="go">Voir le programme <i>{A}</i></span>
        </div>
      </a>
      <a class="course" href="{c['adultes']['url']}">
        <div class="img">{img("adulte2", 640, 480, "Formation esthétique pour adultes en reconversion")}<span class="tag">Certifiante</span></div>
        <div class="body">
          <h3>Esthétique pour Adultes</h3>
          <p>Pour les femmes en reconversion ou en activité : apprenez le métier le samedi, sans mettre votre emploi entre parenthèses.</p>
          <div class="meta"><div><b>6 mois</b>Durée</div><div><b>Le samedi</b>10h – 15h</div></div>
          <span class="go">Voir le programme <i>{A}</i></span>
        </div>
      </a>
      <a class="course" href="{c['dermo']['url']}">
        <div class="img">{img("comptoir", 640, 480, "Conseil dermo-cosmétique en parapharmacie")}<span class="tag">Certifiante</span></div>
        <div class="body">
          <h3>Dermo-Cosmétique</h3>
          <p>Maîtrisez la peau, décryptez les formules INCI et conseillez avec assurance en pharmacie et parapharmacie.</p>
          <div class="meta"><div><b>À distance</b>Live sur Zoom</div><div><b>Cas réels</b>Comptoir &amp; TD</div></div>
          <span class="go">Voir le programme <i>{A}</i></span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow rv">Pourquoi Esthé-PRO</span>
      <h2 class="rv">Une formation qui prépare <em>vraiment</em> au métier</h2>
    </div>
    <div class="pillars" data-stagger>
      <div class="pillar"><span class="n">01 — Notre mission</span><h3>Un savoir-faire d'exception</h3><p>Transmettre des gestes précis, fondés sur la science, la sécurité et le respect de l'harmonie naturelle de la peau.</p></div>
      <div class="pillar"><span class="n">02 — Notre pédagogie</span><h3>La pratique au centre</h3><p>Ateliers en petits groupes, encadrés par des experts reconnus. On apprend en faisant, on progresse en étant corrigée.</p></div>
      <div class="pillar"><span class="n">03 — Nos certifications</span><h3>Exercer avec confiance</h3><p>Des formations certifiantes et diplômantes pour exercer avec professionnalisme dès la fin du cursus.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow rv">La vie à l'école</span>
      <h2 class="rv">Apprendre dans un cadre <em>professionnel</em></h2>
    </div>
    <div class="gallery" data-stagger>
      <figure>{img("soin-gants", 800, 600, "Soin du visage en cabine")}</figure>
      <figure>{img("classe", 500, 500, "Salle de formation Esthé-PRO")}</figure>
      <figure>{img("conseil1", 500, 500, "Conseil dermo-cosmétique")}</figure>
      <figure>{img("lab", 500, 760, "Analyse de produits cosmétiques")}</figure>
      <figure>{img("adulte3", 500, 500, "Atelier de soins")}</figure>
      <figure>{img("cabine", 500, 500, "Cabine de soins")}</figure>
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow rv">Processus d'inscription</span>
      <h2 class="rv">Rejoindre Esthé-PRO en <em>3 étapes</em></h2>
    </div>
    <div class="steps" data-stagger>
      <div class="step"><div class="num">01</div><h3>Pré-inscription</h3><p>Remplissez le formulaire en ligne en 2 minutes. Un conseiller pédagogique vous rappelle pour comprendre votre projet.</p></div>
      <div class="step"><div class="num">02</div><h3>Étude de dossier</h3><p>Notre équipe vérifie avec vous que la formation choisie correspond à votre profil et aux conditions d'admission.</p></div>
      <div class="step"><div class="num">03</div><h3>Validation</h3><p>Vous recevez votre confirmation d'admission. L'inscription est définitive après remise des documents et règlement des frais.</p></div>
    </div>
    <div class="center rv" style="margin-top:50px"><a class="btn" href="/inscription" data-track="steps_cta">Commencer ma pré-inscription {A}</a></div>
  </div>
</section>

{session_box()}

<section class="bg-soft">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow rv">Questions fréquentes</span><h2 class="rv">Tout ce qu'il faut savoir <em>avant de vous lancer</em></h2></div>
    <div class="faq">{faq(F)}</div>
  </div>
</section>

{final_cta()}
</main>
{footer()}'''
    schema = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"EducationalOrganization","name":"École Internationale d'Esthétique et de Cosmétologie Esthé-PRO","url":"{SITE}","logo":"https://static.wixstatic.com/media/76852a_{IMG['logo']}","telephone":"+212762575813","email":"esthepro_ma@yahoo.fr","foundingDate":"2003","address":{{"@type":"PostalAddress","streetAddress":"Angle Avenue Michlifen et Rue Jabal Al Ayachi, Imm. 49, 3ème étage, n°8","addressLocality":"Rabat","addressRegion":"Agdal","addressCountry":"MA"}},"sameAs":["https://www.facebook.com/esthepro.ecole/","https://www.instagram.com/ecole.esthe.pro/"]}}</script>{faq_schema(F)}'''
    return head("École d'Esthétique et de Dermo-Cosmétique à Rabat | Esthé-PRO",
                "École agréée par l'État depuis 2003 à Agdal, Rabat. Formation Esthéticienne, Esthétique pour Adultes et Dermo-Cosmétique. 25 ans d'expertise. Pré-inscription gratuite.",
                "/", og="hydra", extra=schema) + body
