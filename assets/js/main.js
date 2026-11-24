/* Esthé-PRO — interactions, animations, tracking & formulaires */
(function(){
  "use strict";
  const C = window.ESTHEPRO || {};
  const $ = (s, r=document) => r.querySelector(s);
  const $$ = (s, r=document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------- Tracking ---------------- */
  if (C.metaPixelId) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', C.metaPixelId); fbq('track','PageView');
  }
  if (C.ga4Id) {
    const s=document.createElement('script'); s.async=true; s.src='https://www.googletagmanager.com/gtag/js?id='+C.ga4Id; document.head.appendChild(s);
    window.dataLayer=window.dataLayer||[]; window.gtag=function(){dataLayer.push(arguments)}; gtag('js',new Date()); gtag('config',C.ga4Id);
  }
  const STD = {Lead:'generate_lead', ViewContent:'view_item', Contact:'contact', InitiateCheckout:'begin_checkout'};
  function track(name, params={}){
    try{ if(window.fbq){ STD[name] ? fbq('track',name,params) : fbq('trackCustom',name,params); } }catch(e){}
    try{ if(window.gtag){ gtag('event', STD[name]||name, params); } }catch(e){}
  }
  window.EPtrack = track;
  const course = document.body.dataset.course;
  if (course) track('ViewContent',{content_name:course});

  /* ---------------- Source (UTM first-touch) ---------------- */
  const qs = new URLSearchParams(location.search);
  let src = {};
  try { src = JSON.parse(localStorage.getItem('ep_src')||'{}'); } catch(e){}
  const keys = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','fbclid','gclid'];
  if (keys.some(k=>qs.get(k))) { src = {landing:location.pathname}; keys.forEach(k=>{ if(qs.get(k)) src[k]=qs.get(k); }); }
  if (!src.landing) src.landing = location.pathname;
  if (!src.referrer && document.referrer && !document.referrer.includes(location.host)) src.referrer = document.referrer;
  try { localStorage.setItem('ep_src', JSON.stringify(src)); } catch(e){}

  /* ---------------- WhatsApp / tel ---------------- */
  const waLink = t => `https://wa.me/${C.whatsapp}?text=${encodeURIComponent(t)}`;
  window.EPwa = waLink;
  $$('[data-wa]').forEach(a=>{
    a.href = waLink(a.dataset.wa || "Bonjour Esthé-PRO, j'aimerais avoir des informations sur vos formations.");
    a.target = '_blank'; a.rel = 'noopener';
    a.addEventListener('click',()=>track('Contact',{method:'whatsapp',place:a.dataset.place||''}));
  });
  $$('a[href^="tel:"]').forEach(a=>a.addEventListener('click',()=>track('Contact',{method:'phone'})));
  $$('[data-track]').forEach(a=>a.addEventListener('click',()=>track('cta_click',{id:a.dataset.track})));
  $$('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());

  /* ---------------- Header ---------------- */
  const header = $('header.site');
  const onScroll = () => {
    const y = scrollY;
    header && header.classList.toggle('scrolled', y > 40);
    const bar = $('.mbar');
    if (bar) {
      const form = $('.form-wrap');
      let hide = false;
      if (form) { const r = form.getBoundingClientRect(); hide = r.top < innerHeight && r.bottom > 0; }
      bar.classList.toggle('show', y > 520 && !hide);
    }
  };
  addEventListener('scroll', onScroll, {passive:true}); onScroll();
  const burger = $('#burger');
  if (burger) burger.addEventListener('click',()=>{
    const r = header.getBoundingClientRect(); document.documentElement.style.setProperty('--menu-top', r.bottom+'px');
    const o = document.body.classList.toggle('menu-open'); burger.setAttribute('aria-expanded',o);
    document.body.style.overflow = o ? 'hidden' : '';
  });
  $$('.menu a').forEach(a=>a.addEventListener('click',()=>{document.body.classList.remove('menu-open');document.body.style.overflow='';}));

  /* ---------------- Session countdowns ---------------- */
  const target = C.nextSession ? new Date(C.nextSession) : null;
  const sessionOn = target && target > new Date();
  $$('[data-session-label]').forEach(e=>e.textContent = C.nextSessionLabel || '');
  if (!sessionOn) $$('[data-session]').forEach(e=>e.remove());
  function tick(){
    if(!sessionOn) return;
    let s = Math.max(0, Math.floor((target - new Date())/1000));
    const d=Math.floor(s/86400); s%=86400; const h=Math.floor(s/3600); s%=3600; const m=Math.floor(s/60); s%=60;
    const pad=n=>String(n).padStart(2,'0');
    $$('[data-cd]').forEach(el=>{
      if (el.dataset.cd==='short') el.textContent = d>0 ? `J-${d}` : `${pad(h)}h${pad(m)}`;
      else { const set=(k,v)=>{const x=el.querySelector(`[data-u="${k}"]`); if(x) x.textContent=pad(v)}; set('d',d);set('h',h);set('m',m);set('s',s); }
    });
  }
  tick(); if (sessionOn) setInterval(tick,1000);

  /* ---------------- Reveal on scroll ---------------- */
  document.documentElement.classList.add('js');
  const io = new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }),{threshold:.14, rootMargin:'0px 0px -40px 0px'});
  $$('.rv,.img-rv').forEach(el=>io.observe(el));
  // Stagger children
  $$('[data-stagger]').forEach(p=>[...p.children].forEach((c,i)=>{ c.classList.add('rv'); c.style.setProperty('--d',(i*0.09)+'s'); io.observe(c); }));

  /* Counters */
  const cio = new IntersectionObserver(es=>es.forEach(e=>{
    if(!e.isIntersecting) return; cio.unobserve(e.target);
    const el=e.target, to=+el.dataset.count, dur=1600, t0=performance.now();
    if (reduce){ el.textContent=to; return; }
    const step=t=>{ const p=Math.min(1,(t-t0)/dur); el.textContent=Math.round(to*(1-Math.pow(1-p,3))); if(p<1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  }),{threshold:.6});
  $$('[data-count]').forEach(el=>cio.observe(el));

  /* Parallax */
  const px = $$('[data-parallax]');
  if (px.length && !reduce) {
    const run=()=>{ px.forEach(el=>{ const r=el.parentElement.getBoundingClientRect(); if(r.bottom<0||r.top>innerHeight) return; const k=+el.dataset.parallax||0.08; el.style.transform=`translate3d(0,${(r.top+r.height/2-innerHeight/2)*-k}px,0) scale(1.12)`; }); };
    addEventListener('scroll',()=>requestAnimationFrame(run),{passive:true}); run();
  }

  /* ---------------- Forms ---------------- */
  const norm = v => { let d=(v||'').replace(/\D/g,''); if(d.startsWith('00212')) d=d.slice(5); else if(d.startsWith('212')) d=d.slice(3); if(d.startsWith('0')) d=d.slice(1); return /^[5-7]\d{8}$/.test(d)?d:null; };
  const pre = {estheticienne:'Formation Esthéticienne', adultes:'Formation Esthétique pour Adultes', dermo:'Formation Dermo-Cosmétique'}[(qs.get('formation')||'').toLowerCase()];

  $$('form[data-lead]').forEach(form=>{
    const type = form.dataset.lead;
    if (pre) { const r=form.querySelector(`[name=formation][value="${pre}"]`); if(r){ r.checked=true; } const s=form.querySelector('select[name=formation]'); if(s) s.value=pre; }
    const same = form.querySelector('[name=sameWa]');
    if (same) same.addEventListener('change',()=>{ form.querySelector('.f-wa').hidden = same.checked; });
    let started=false;
    form.addEventListener('input',e=>{ const f=e.target.closest('.field'); if(f) f.classList.remove('invalid'); if(!started){ started=true; track('form_start',{form:type}); }});
    form.addEventListener('change',e=>{ if(e.target.name==='formation'){ const g=form.querySelector('.group-err'); g&&g.classList.remove('show'); } const f=e.target.closest('.field'); if(f) f.classList.remove('invalid'); });

    form.addEventListener('submit', async ev=>{
      ev.preventDefault();
      if (form.website && form.website.value) return;
      const errs=[];
      const bad=(el,b)=>{ const f=el.closest('.field'); if(f) f.classList.toggle('invalid',b); if(b) errs.push(el); };
      const fRadio = form.querySelector('[name=formation][type=radio]');
      if (fRadio) { const ok=!!form.querySelector('[name=formation]:checked'); const g=form.querySelector('.group-err'); g&&g.classList.toggle('show',!ok); if(!ok) errs.push(fRadio); }
      $$('[data-req]',form).forEach(el=>{
        if (el.closest('[hidden]')) return;
        const v=el.value.trim();
        if (el.dataset.req==='phone') bad(el,!norm(v));
        else if (el.dataset.req==='email') bad(el,!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v));
        else bad(el,!v);
      });
      if (errs.length){ const el=errs[0]; scrollTo({top:el.getBoundingClientRect().top+scrollY-170,behavior:'smooth'}); setTimeout(()=>el.focus({preventScroll:true}),400); return; }

      const btn = form.querySelector('[type=submit]'); const label=btn.innerHTML; btn.disabled=true; btn.textContent='Envoi en cours…';
      const fd = new FormData(form); const g=k=>(fd.get(k)||'').toString().trim();
      const tel = '+212'+norm(g('tel'));
      const data = {
        type: type==='quick' ? 'Rappel' : 'Pré-inscription',
        prenom:g('prenom'), nom:g('nom'), ville:g('ville'), telephone:tel,
        whatsapp: (same && !same.checked) ? '+212'+norm(g('wa')) : tel,
        email:g('email'), niveau:g('niveau'), formation:g('formation')||'À définir',
        message:g('message'), page:location.pathname, date:new Date().toISOString(), ...src
      };
      let sent=false;
      if (C.endpoint) {
        try { const r = await fetch(C.endpoint,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(data)}); sent = r.ok; } catch(e){}
      }
      track('Lead',{content_name:data.formation, form:type});
      try { sessionStorage.setItem('ep_lead', JSON.stringify({...data, sent})); } catch(e){}
      location.href = '/merci';
      setTimeout(()=>{ btn.disabled=false; btn.innerHTML=label; }, 4000);
    });
  });

  /* ---------------- Page Merci ---------------- */
  const thanks = $('#thanks');
  if (thanks) {
    let L=null; try{ L=JSON.parse(sessionStorage.getItem('ep_lead')||'null'); }catch(e){}
    const wa = $('#waConfirm');
    if (L) {
      $('#tName').textContent = L.prenom;
      const rows=[['Formation',L.formation],['Téléphone',L.telephone]]; if(L.email) rows.push(['E-mail',L.email]);
      const recap=$('#recap'); rows.forEach(([k,v])=>{ const d=document.createElement('div'); d.innerHTML='<span></span><b></b>'; d.children[0].textContent=k; d.children[1].textContent=v; recap.appendChild(d); });
      const msg=`Bonjour Esthé-PRO, je viens de faire ma ${L.type.toLowerCase()} sur le site.\n• Nom : ${L.prenom} ${L.nom}\n• Formation : ${L.formation}`+(L.niveau?`\n• Niveau d'études : ${L.niveau}`:'')+(L.ville?`\n• Ville : ${L.ville}`:'')+(L.message?`\n• Message : ${L.message}`:'');
      wa.href = waLink(msg);
      if (!L.sent) {
        $('#tTitle').innerHTML = `Merci <span id="tName"></span>, plus qu'une étape&nbsp;!`; $('#tName').textContent=L.prenom;
        $('#tText').textContent = "Envoyez maintenant votre demande sur WhatsApp : c'est ce qui permet à notre conseiller pédagogique de vous répondre rapidement.";
        $('#waLabel').textContent = 'Envoyer ma demande sur WhatsApp';
      }
    } else { $('#recap').hidden = true; $('#tName').textContent=''; wa.href = waLink("Bonjour Esthé-PRO, j'aimerais avoir des informations sur vos formations."); }
    wa.target='_blank'; wa.rel='noopener'; wa.addEventListener('click',()=>track('Contact',{method:'whatsapp',place:'merci'}));
  }
})();
