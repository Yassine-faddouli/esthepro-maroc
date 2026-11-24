# Esthé-PRO — Site web + système de conversion

## 1. Contenu du dossier

```
(racine)                    ← le site déployé (statique, aucun serveur requis)
  index.html                  Accueil
  ecole-esthe-pro/            L'école
  formation-estheticienne/    Formation Esthéticienne
  formation-esthetique-pour-adultes/
  formation-dermocosmetique-appliquee-a-la-parapharmacie/
  inscription/                Formulaire de pré-inscription
  contact/                    Contact + plan
  merci/                      Page de remerciement (conversion)
  404.html, sitemap.xml, robots.txt, vercel.json, netlify.toml
  assets/css/style.css        Design (charte Esthé-PRO)
  assets/js/config.js         ⚙️ LE SEUL FICHIER À CONFIGURER
  assets/js/main.js           Animations, formulaires, tracking
_dev/system/google-apps-script.gs  Mini-CRM Google Sheets (réception des leads)
_dev/build/                      Générateur des pages (Python) pour modifier les textes
```

Les URLs sont identiques à celles du site Wix actuel, donc le référencement Google est conservé.

## 2. Le système, du clic à l'inscription

```
Publicité Meta / Instagram / Google  ──►  Page formation (ViewContent)
                                             │
             ┌───────────────────────────────┼──────────────────────────────┐
             ▼                               ▼                              ▼
   Pré-inscription complète        Formulaire « Être rappelé(e) »     Bouton WhatsApp / Appel
   (/inscription)                  (bas de chaque page)               (Contact)
             └───────────────┬───────────────┘
                             ▼
                Page /merci  →  événement Lead (Pixel + GA4)
                             │   + bouton « Confirmer sur WhatsApp » (message pré-rempli)
                             ▼
             Google Sheet « Leads »  (statut, lien WhatsApp 1 clic, source de la pub)
                             │
             ├─ E-mail d'alerte immédiat à l'école
             ├─ E-mail de confirmation à la personne
             └─ Récap chaque matin à 9h des leads à traiter / relancer
```

**Points de conversion présents sur toutes les pages** : bouton « S'inscrire » dans le menu, barre « Prochaine rentrée » avec compte à rebours, bouton WhatsApp flottant, barre d'action fixe sur mobile (S'inscrire · WhatsApp · Appeler), formulaire court de rappel en bas de page.

**Aucun lead perdu** : si le Google Sheet n'est pas encore branché (ou en cas de panne), la page /merci invite la personne à envoyer sa demande sur WhatsApp, avec un message pré-rempli.

## 3. Mise en ligne (≈ 20 minutes)

1. **CRM** : suivre l'en-tête de `system/google-apps-script.gs` (créer le Sheet, coller, exécuter `setup`, déployer en Application Web). Copier l'URL `/exec`.
2. **Configurer** `assets/js/config.js` :
   - `endpoint` : l'URL `/exec`
   - `metaPixelId` / `ga4Id` : vos identifiants
   - `nextSession` / `nextSessionLabel` : la date de la prochaine rentrée (les comptes à rebours disparaissent seuls une fois la date passée)
3. **Déployer** le dépôt sur Vercel ou Netlify (glisser-déposer). Les fichiers `vercel.json` / `netlify.toml` sont déjà prêts.
4. **Domaine** : pointer esthepro-maroc.com vers Vercel/Netlify (DNS), puis désactiver le site Wix.
5. **Tester** : remplir le formulaire une fois, vérifier la ligne dans le Sheet, l'e-mail reçu et l'événement Lead dans le Gestionnaire d'événements Meta.

## 4. Process de suivi des leads (à donner à l'équipe)

| Délai | Action | Statut dans le Sheet |
|---|---|---|
| Dans l'heure | Appel ou WhatsApp (bouton « Ouvrir WhatsApp » dans le Sheet) | Contacté |
| Pas de réponse | Message WhatsApp + nouvelle date dans « Prochaine relance » (J+1, puis J+3) | À relancer |
| Intéressée | Proposer une visite de l'école ou un appel détaillé | RDV / visite |
| Dossier reçu | Vérifier les conditions d'admission | Dossier en cours |
| Paiement fait | — | Inscrit |
| Pas intéressée | Noter la raison dans « Notes conseiller » | Pas intéressé |

L'onglet **Tableau de bord** affiche les leads par statut, par formation et par source de publicité, ainsi que le taux de conversion lead → inscrit.

## 5. Tracking

| Événement | Quand | Meta Pixel | GA4 |
|---|---|---|---|
| PageView | chaque page | PageView | page_view |
| ViewContent | page d'une formation | ViewContent | view_item |
| form_start | 1er champ rempli | custom | form_start |
| Lead | formulaire envoyé | **Lead** | generate_lead |
| Contact | clic WhatsApp / téléphone | Contact | contact |

Les paramètres UTM et `fbclid` de la première visite sont mémorisés et enregistrés avec chaque lead (colonnes Source / Campagne / Annonce).

**Liens de pub pré-remplis** : `/inscription?formation=estheticienne`, `?formation=adultes`, `?formation=dermo` cochent automatiquement la bonne formation.

## 6. Images

Les photos sont celles du site actuel, servies depuis le CDN d'images de Wix (optimisées et redimensionnées automatiquement). **Avant de résilier l'abonnement Wix**, téléchargez-les dans `assets/img/` et remplacez la fonction `src()` dans `_dev/build/parts.py`, puis relancez la génération.

## 7. Modifier un texte

Les textes sont dans `_dev/build/pages_home.py` et `_dev/build/pages_other.py`. Après modification : `python3 _dev/build/build.py` régénère tout le dépôt.
Pour une petite correction, vous pouvez aussi éditer directement le fichier HTML concerné.

## 8. À valider avec l'école

- Les options du champ « Niveau d'études » (Collège → Bac+3 et plus, Autre).
- La date de la prochaine rentrée : 1er décembre 2026, reprise du site actuel.
- Les textes de l'e-mail de confirmation envoyé aux candidates (`confirmLead_` dans le script).
