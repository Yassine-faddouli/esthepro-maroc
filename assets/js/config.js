/* =====================================================================
   ESTHÉ-PRO — CONFIGURATION DU SITE (le seul fichier à modifier)
   ===================================================================== */
window.ESTHEPRO = {
  // 1) Réception des leads : URL /exec du Google Apps Script (voir system/google-apps-script.gs)
  //    Laisser vide = chaque demande est envoyée via WhatsApp uniquement.
  endpoint: "",

  // 2) Contact
  whatsapp: "212762575813",          // sans + ni espaces
  phone: "+212762575813",
  email: "esthepro_ma@yahoo.fr",

  // 3) Tracking publicitaire (laisser vide si non utilisé)
  metaPixelId: "",                  // ex : "123456789012345"
  ga4Id: "",                        // ex : "G-XXXXXXXXXX"

  // 4) Prochaine rentrée : pilote la barre du haut et les comptes à rebours.
  //    Après cette date, les comptes à rebours se masquent automatiquement.
  nextSession: "2026-12-01T09:00:00+01:00",
  nextSessionLabel: "1er décembre 2026"
};
