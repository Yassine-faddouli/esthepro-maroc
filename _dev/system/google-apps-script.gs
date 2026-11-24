/**
 * ESTHÉ-PRO — Mini-CRM des leads (Google Sheets + Apps Script)
 * ------------------------------------------------------------
 * Ce que fait ce script :
 *  1. Reçoit chaque pré-inscription / demande de rappel envoyée par le site
 *  2. L'ajoute dans l'onglet « Leads » avec un statut, un lien WhatsApp en 1 clic et une date de relance
 *  3. Envoie une alerte e-mail à l'école à chaque nouveau lead
 *  4. Envoie un e-mail de confirmation à la personne (si elle a donné son e-mail)
 *  5. Envoie chaque matin un récapitulatif des leads non traités
 *  6. Alimente un onglet « Tableau de bord » (leads par statut, formation, source)
 *
 * INSTALLATION (10 minutes) :
 *  a) Créez un Google Sheet vide → Extensions → Apps Script → collez ce fichier → Enregistrer.
 *  b) Renseignez SCHOOL_EMAIL ci-dessous.
 *  c) Menu Exécuter → choisissez la fonction « setup » → Exécuter → acceptez les autorisations.
 *  d) Déployer → Nouveau déploiement → type « Application Web »
 *       Exécuter en tant que : Moi    |    Accès : Tout le monde
 *  e) Copiez l'URL qui se termine par /exec dans site/assets/js/config.js → endpoint.
 */

const SCHOOL_EMAIL = "esthepro_ma@yahoo.fr";   // reçoit les alertes et le récap du matin
const SCHOOL_WA = "212762575813";
const SEND_CONFIRMATION_TO_LEAD = true;
const STATUTS = ["Nouveau", "Contacté", "À relancer", "RDV / visite", "Dossier en cours", "Inscrit", "Pas intéressé"];
const COLS = ["ID","Date","Statut","Type","Prénom","Nom","Téléphone","WhatsApp","Lien WhatsApp","E-mail","Ville","Niveau d'études","Formation","Message","Prochaine relance","Notes conseiller","Source","Campagne","Annonce","Page d'arrivée","Page du formulaire"];

function doPost(e) {
  const lock = LockService.getScriptLock(); lock.waitLock(10000);
  try {
    const d = JSON.parse((e && e.postData && e.postData.contents) || "{}");
    if (d.website) return json_({ ok: true });                       // anti-spam
    const sh = leads_();
    const id = "EP-" + Utilities.formatDate(new Date(), "Africa/Casablanca", "yyMMdd-HHmmss");
    const now = new Date();
    const relance = new Date(now.getTime() + 24 * 3600 * 1000);
    const wa = (d.whatsapp || d.telephone || "").replace(/\D/g, "");
    const hello = encodeURIComponent("Bonjour " + (d.prenom || "") + ", ici l'école Esthé-PRO. Merci pour votre demande concernant la " + (d.formation || "formation") + ". Avez-vous quelques minutes pour en parler ?");
    sh.appendRow([
      id, now, "Nouveau", d.type || "Pré-inscription", d.prenom || "", d.nom || "", d.telephone || "", d.whatsapp || "",
      wa ? '=HYPERLINK("https://wa.me/' + wa + '?text=' + hello + '","Ouvrir WhatsApp")' : "",
      d.email || "", d.ville || "", d.niveau || "", d.formation || "", d.message || "", relance, "",
      d.utm_source || (d.fbclid ? "facebook" : (d.referrer ? d.referrer : "direct")), d.utm_campaign || "", d.utm_content || "", d.landing || "", d.page || ""
    ]);
    notifySchool_(d, id, wa, hello);
    if (SEND_CONFIRMATION_TO_LEAD && d.email) confirmLead_(d);
    return json_({ ok: true, id: id });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally { lock.releaseLock(); }
}

function doGet() { return json_({ ok: true, service: "Esthé-PRO leads" }); }

/* ---------- Installation : onglets, mise en forme, tableau de bord, déclencheur ---------- */
function setup() {
  const ss = SpreadsheetApp.getActive();
  const sh = leads_();
  sh.getRange(1, 1, 1, COLS.length).setValues([COLS]).setFontWeight("bold").setBackground("#002D62").setFontColor("#FFFFFF");
  sh.setFrozenRows(1); sh.setFrozenColumns(3);
  sh.getRange("B:B").setNumberFormat("dd/MM/yyyy HH:mm");
  sh.getRange("O:O").setNumberFormat("dd/MM/yyyy");
  const rule = SpreadsheetApp.newDataValidation().requireValueInList(STATUTS, true).build();
  sh.getRange(2, 3, 2000, 1).setDataValidation(rule);
  const colors = { "Nouveau": "#FDECEA", "Contacté": "#E8F1FB", "À relancer": "#FFF4D6", "RDV / visite": "#E3F4FC", "Dossier en cours": "#EDE7F6", "Inscrit": "#DFF3E6", "Pas intéressé": "#EEEEEE" };
  const rng = sh.getRange(2, 1, 2000, COLS.length);
  sh.setConditionalFormatRules(Object.keys(colors).map(s =>
    SpreadsheetApp.newConditionalFormatRule().whenFormulaSatisfied('=$C2="' + s + '"').setBackground(colors[s]).setRanges([rng]).build()));
  sh.setColumnWidths(1, COLS.length, 140); sh.setColumnWidth(14, 260); sh.setColumnWidth(16, 260);

  // Tableau de bord
  let db = ss.getSheetByName("Tableau de bord") || ss.insertSheet("Tableau de bord");
  db.clear();
  db.getRange("A1").setValue("ESTHÉ-PRO — Suivi des leads").setFontSize(16).setFontWeight("bold").setFontColor("#002D62");
  db.getRange("A3:B3").setValues([["Indicateur", "Valeur"]]).setFontWeight("bold").setBackground("#002D62").setFontColor("#fff");
  db.getRange("A4:B8").setFormulas([
    ['="Total leads"', '=COUNTA(Leads!A2:A)'],
    ['="Leads des 7 derniers jours"', '=COUNTIF(Leads!B2:B,">="&TODAY()-7)'],
    ['="À traiter (Nouveau)"', '=COUNTIF(Leads!C2:C,"Nouveau")'],
    ['="Inscrits"', '=COUNTIF(Leads!C2:C,"Inscrit")'],
    ['="Taux de conversion lead → inscrit"', '=IFERROR(B7/B4,0)']
  ]);
  db.getRange("B8").setNumberFormat("0.0%");
  db.getRange("A10:B10").setValues([["Statut", "Leads"]]).setFontWeight("bold").setBackground("#009BE3").setFontColor("#fff");
  db.getRange(11, 1, STATUTS.length, 2).setFormulas(STATUTS.map((s, i) => ['="' + s + '"', '=COUNTIF(Leads!C2:C,A' + (11 + i) + ')']));
  db.getRange("D3:E3").setValues([["Formation", "Leads"]]).setFontWeight("bold").setBackground("#002D62").setFontColor("#fff");
  db.getRange("D4").setFormula('=QUERY(Leads!M2:M,"select M, count(M) where M is not null group by M order by count(M) desc label count(M) \'\'",0)');
  db.getRange("G3:H3").setValues([["Source", "Leads"]]).setFontWeight("bold").setBackground("#002D62").setFontColor("#fff");
  db.getRange("G4").setFormula('=QUERY(Leads!Q2:Q,"select Q, count(Q) where Q is not null group by Q order by count(Q) desc label count(Q) \'\'",0)');
  db.setColumnWidth(1, 260); db.setColumnWidth(4, 260); db.setColumnWidth(7, 200);

  // Récap chaque matin à 9h
  ScriptApp.getProjectTriggers().filter(t => t.getHandlerFunction() === "dailyDigest").forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger("dailyDigest").timeBased().atHour(9).everyDays(1).inTimezone("Africa/Casablanca").create();
  SpreadsheetApp.getUi && ss.toast("Installation terminée ✔");
}

/* ---------- Récap quotidien des leads à traiter ---------- */
function dailyDigest() {
  const sh = leads_(); const v = sh.getDataRange().getValues(); v.shift();
  const today = new Date(); today.setHours(23, 59, 59);
  const todo = v.filter(r => r[2] === "Nouveau" || ((r[2] === "À relancer" || r[2] === "Contacté") && r[14] && new Date(r[14]) <= today));
  if (!todo.length) return;
  const rows = todo.map(r => "<tr><td>" + [r[2], r[4] + " " + r[5], r[6], r[12], Utilities.formatDate(new Date(r[1]), "Africa/Casablanca", "dd/MM")].join("</td><td>") + "</td></tr>").join("");
  MailApp.sendEmail({ to: SCHOOL_EMAIL, subject: "Esthé-PRO — " + todo.length + " lead(s) à traiter aujourd'hui",
    htmlBody: "<p>Bonjour,</p><p>Voici les personnes à contacter ou relancer aujourd'hui :</p><table border='1' cellpadding='6' style='border-collapse:collapse;font-family:Arial;font-size:13px'><tr style='background:#002D62;color:#fff'><th>Statut</th><th>Nom</th><th>Téléphone</th><th>Formation</th><th>Reçu le</th></tr>" + rows + "</table><p><a href='" + SpreadsheetApp.getActive().getUrl() + "'>Ouvrir le suivi des leads</a></p>" });
}

/* ---------- E-mails ---------- */
function notifySchool_(d, id, wa, hello) {
  if (!SCHOOL_EMAIL) return;
  const waUrl = wa ? "https://wa.me/" + wa + "?text=" + hello : "";
  MailApp.sendEmail({
    to: SCHOOL_EMAIL,
    subject: "🔔 Nouveau lead — " + (d.prenom || "") + " " + (d.nom || "") + " · " + (d.formation || ""),
    htmlBody: "<div style='font-family:Arial;font-size:14px;color:#14233A'>" +
      "<h2 style='color:#002D62;font-family:Georgia'>Nouvelle demande (" + (d.type || "Pré-inscription") + ")</h2>" +
      "<p><b>" + (d.prenom || "") + " " + (d.nom || "") + "</b> — " + (d.formation || "") + "</p>" +
      "<p>📞 " + (d.telephone || "") + "<br>✉️ " + (d.email || "—") + "<br>📍 " + (d.ville || "—") + "<br>🎓 " + (d.niveau || "—") + "</p>" +
      (d.message ? "<p>💬 " + d.message + "</p>" : "") +
      "<p>Source : " + (d.utm_source || "direct") + (d.utm_campaign ? " / " + d.utm_campaign : "") + "</p>" +
      (waUrl ? "<p><a href='" + waUrl + "' style='background:#1FA855;color:#fff;padding:12px 18px;text-decoration:none;border-radius:20px'>Répondre sur WhatsApp</a></p>" : "") +
      "<p style='color:#597799'>Réf. " + id + " · À contacter idéalement dans l'heure.</p></div>"
  });
}

function confirmLead_(d) {
  MailApp.sendEmail({
    to: d.email, name: "École Esthé-PRO", replyTo: SCHOOL_EMAIL,
    subject: "Votre pré-inscription à l'école Esthé-PRO",
    htmlBody: "<div style='font-family:Arial;font-size:15px;color:#14233A;max-width:560px'>" +
      "<div style='background:#002D62;color:#fff;padding:24px;font-family:Georgia;font-size:22px'>Esthé-PRO</div>" +
      "<div style='padding:24px;border:1px solid #D3DEE8'>" +
      "<p>Bonjour " + (d.prenom || "") + ",</p>" +
      "<p>Merci pour votre intérêt pour la <b>" + (d.formation || "formation") + "</b>. Votre demande a bien été reçue.</p>" +
      "<p>Notre conseiller pédagogique vous contactera très prochainement pour vous présenter le programme, le calendrier et les modalités d'inscription.</p>" +
      "<p>Pour aller plus vite, vous pouvez aussi nous écrire directement :</p>" +
      "<p><a href='https://wa.me/" + SCHOOL_WA + "' style='background:#1FA855;color:#fff;padding:12px 18px;text-decoration:none;border-radius:20px'>Nous écrire sur WhatsApp</a></p>" +
      "<p style='color:#597799;font-size:13px'>École Internationale d'Esthétique et de Cosmétologie Esthé-PRO<br>Angle Av. Michlifen et Rue Jabal Al Ayachi, Imm. 49, 3ème étage, n°8 — Agdal, Rabat<br>+212 7 62 57 58 13</p>" +
      "</div></div>"
  });
}

/* ---------- Utilitaires ---------- */
function leads_() {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName("Leads");
  if (!sh) { sh = ss.getSheets()[0]; sh.setName("Leads"); }
  if (sh.getLastRow() === 0) sh.appendRow(COLS);
  return sh;
}
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
