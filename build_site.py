import os

BASE = r'c:\Users\JLOW0\OneDrive\Área de Trabalho\IRSET'

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CONCUR-IR 2026 — Consensus Criteria for Uniform Reporting in Interventional Radiology</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:"Poppins",system-ui,sans-serif;color:#1a1a1a;background:#fff;font-size:15px;line-height:1.7;}
a{color:#1C3A6E;text-decoration:underline;}
a:hover{color:#2E75B6;}

/* NAV */
nav{
  background:#1C3A6E;
  padding:0 52px;
  display:flex;align-items:center;gap:32px;
  height:62px;
  position:sticky;top:0;z-index:100;
  box-shadow:0 4px 24px rgba(0,0,0,0.35);
}
.nav-logo img{height:32px;display:block;}
.nav-links{display:flex;gap:0;margin-left:auto;}
.nav-links a{
  color:rgba(255,255,255,0.78);font-size:13px;font-weight:500;
  text-decoration:none;padding:0 15px;height:62px;
  display:flex;align-items:center;
  border-bottom:3px solid transparent;transition:all 0.15s;
}
.nav-links a:hover{color:#fff;background:rgba(255,255,255,0.07);border-bottom-color:rgba(255,255,255,0.4);}
.nav-links a.cta{background:rgba(255,255,255,0.12);color:#fff;font-weight:600;margin-left:10px;height:36px;padding:0 18px;border:1.5px solid rgba(255,255,255,0.3);border-bottom:1.5px solid rgba(255,255,255,0.3);}
.nav-links a.cta:hover{background:rgba(255,255,255,0.22);}
/* DROPDOWN */
.nav-dropdown{position:relative;}
.nav-dropdown>a::after{content:'▾';margin-left:5px;font-size:10px;opacity:0.7;}
.nav-dropdown-menu{
  display:none;position:absolute;top:100%;left:0;
  background:#1C3A6E;min-width:210px;
  box-shadow:0 8px 24px rgba(0,0,0,0.35);
  border-top:2px solid rgba(255,255,255,0.15);
  z-index:200;
}
.nav-dropdown:hover .nav-dropdown-menu{display:block;}
.nav-dropdown-menu a{
  display:flex;align-items:center;gap:10px;
  color:rgba(255,255,255,0.82);font-size:12.5px;font-weight:500;
  text-decoration:none;padding:11px 18px;
  border-bottom:1px solid rgba(255,255,255,0.07);
  white-space:nowrap;height:auto;transition:background 0.12s;
}
.nav-dropdown-menu a:last-child{border-bottom:none;}
.nav-dropdown-menu a:hover{background:rgba(255,255,255,0.1);color:#fff;}
.nav-dropdown-menu a .dm-icon{font-size:14px;opacity:0.7;flex-shrink:0;}
.nav-dropdown-menu a .dm-sub{display:block;font-size:10px;opacity:0.55;margin-top:1px;}

/* PAGE HEADER */
.page-header{
  background:linear-gradient(160deg,#132952 0%,#1C3A6E 55%,#1e4d8c 100%);
  padding:52px 52px 48px;
  box-shadow:0 8px 40px rgba(0,0,0,0.3), inset 0 -1px 0 rgba(255,255,255,0.08);
  position:relative;overflow:hidden;
}
.page-header::before{
  content:"";position:absolute;right:-80px;top:-80px;
  width:500px;height:500px;border-radius:50%;
  border:1px solid rgba(255,255,255,0.04);
}
.page-header::after{
  content:"";position:absolute;left:-120px;bottom:-120px;
  width:600px;height:600px;border-radius:50%;
  border:1px solid rgba(255,255,255,0.03);
}
.ph-inner{max-width:960px;margin:0 auto;display:flex;align-items:center;gap:44px;position:relative;z-index:1;}
.ph-logo img{height:90px;display:block;}
.ph-text h1{font-size:27px;font-weight:700;color:#fff;line-height:1.25;margin-bottom:10px;letter-spacing:-0.3px;}
.ph-text p{font-size:14px;color:rgba(255,255,255,0.65);line-height:1.65;max-width:540px;font-weight:300;}
.ph-badge{display:inline-block;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.22);color:rgba(255,255,255,0.72);font-size:10.5px;font-weight:600;letter-spacing:1px;text-transform:uppercase;padding:3px 11px;margin-bottom:12px;}

/* LAYOUT */
.wrap{max-width:960px;margin:0 auto;padding:0 52px;}
section{padding:52px 0;border-bottom:1px solid #e8e8e8;}
section:last-of-type{border-bottom:none;}

h2{font-size:21px;font-weight:700;color:#1C3A6E;margin-bottom:20px;padding-bottom:11px;border-bottom:2px solid #1C3A6E;}
h3{font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:10px;}
p{margin-bottom:14px;color:#333;}
p:last-child{margin-bottom:0;}

/* TABS */
.tabs{display:flex;border-bottom:2px solid #d8dde8;margin-bottom:28px;gap:0;}
.tab-btn{
  padding:10px 22px;font-size:13.5px;font-weight:600;color:#888;
  background:none;border:none;cursor:pointer;
  border-bottom:3px solid transparent;margin-bottom:-2px;
  font-family:inherit;transition:all 0.15s;
}
.tab-btn:hover{color:#1C3A6E;}
.tab-btn.active{color:#1C3A6E;border-bottom-color:#1C3A6E;}
.tab-pane{display:none;}
.tab-pane.active{display:block;}

/* DOCS GRID */
.docs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:1px;background:#d5dce8;border:1px solid #d5dce8;margin-top:4px;}
.doc-item{background:#fff;padding:22px;display:flex;flex-direction:column;gap:9px;transition:background 0.12s;}
.doc-item:hover{background:#f5f7fc;}
.doc-type{font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:#999;}
.doc-name{font-size:13px;font-weight:600;color:#1C3A6E;line-height:1.4;}
.doc-links{display:flex;gap:8px;margin-top:4px;flex-wrap:wrap;}
.doc-dl{font-size:11.5px;font-weight:600;color:#1C3A6E;text-decoration:none;background:#EEF3FA;padding:4px 10px;border:1px solid #c4d0e8;}
.doc-dl:hover{background:#d6e4f7;}
.doc-soon{font-size:11.5px;color:#bbb;font-style:italic;}

/* DOWNLOAD AREA */
.dl-section{margin-top:8px;}
.dl-card{border:1px solid #d5dce8;padding:24px 28px;background:#fafbfd;margin-bottom:16px;}
.dl-card h3{color:#1C3A6E;margin-bottom:6px;}
.dl-card p{font-size:13.5px;margin-bottom:16px;color:#555;}
.dl-btns{display:flex;gap:10px;flex-wrap:wrap;}
.dlb{display:inline-flex;align-items:center;gap:8px;padding:9px 20px;background:#1C3A6E;color:#fff;text-decoration:none;font-size:13px;font-weight:600;font-family:inherit;border:none;cursor:pointer;transition:background 0.15s;}
.dlb:hover{background:#2E75B6;color:#fff;}
.dlb.outline{background:#fff;color:#1C3A6E;border:1.5px solid #1C3A6E;}
.dlb.outline:hover{background:#EEF3FA;}

/* DOMAIN TABLE */
.dtable{width:100%;border-collapse:collapse;margin-top:20px;font-size:13px;}
.dtable th{background:#1C3A6E;color:#fff;text-align:left;padding:10px 14px;font-weight:600;font-size:12px;letter-spacing:0.3px;}
.dtable td{padding:9px 14px;border-bottom:1px solid #e8e8e8;vertical-align:top;}
.dtable tr:last-child td{border-bottom:none;}
.dtable tr:hover td{background:#f7f9fd;}
.dtable .did{font-weight:700;color:#1C3A6E;white-space:nowrap;}
.dtable .nitems{text-align:right;color:#888;white-space:nowrap;}
.dtable .cond{color:#2E75B6;font-size:11px;font-style:italic;}

/* FLOW DIAGRAM ELEMENTS */
.flow-elements{margin-top:20px;}
.fe-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid #d5dce8;background:#d5dce8;}
.fe-item{background:#fff;padding:16px 20px;display:flex;gap:12px;align-items:flex-start;}
.fe-item:hover{background:#f5f7fc;}
.fe-num{flex-shrink:0;width:24px;height:24px;background:#1C3A6E;color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;margin-top:1px;}
.fe-txt h4{font-size:13px;font-weight:600;color:#1C3A6E;margin-bottom:3px;}
.fe-txt p{font-size:12.5px;color:#555;margin-bottom:0;line-height:1.55;}

/* STEPS */
.steps{margin-top:20px;}
.step-item{display:flex;gap:18px;margin-bottom:24px;padding-bottom:24px;border-bottom:1px solid #ececec;}
.step-item:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0;}
.step-num{flex-shrink:0;width:30px;height:30px;background:#1C3A6E;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;margin-top:2px;}
.step-body h3{margin-bottom:5px;}
.step-body p{margin-bottom:0;font-size:14px;color:#444;}

/* INSTITUTIONS */
.inst-list{margin-top:20px;}
.inst-item{display:flex;align-items:flex-start;gap:16px;padding:15px 0;border-bottom:1px solid #ececec;}
.inst-item:last-child{border-bottom:none;}
.inst-name{font-weight:600;color:#1a1a1a;font-size:14px;margin-bottom:2px;}
.inst-city{font-size:12.5px;color:#777;}
.inst-role{font-size:12px;color:#2E75B6;margin-top:3px;font-style:italic;}
.inst-icon{font-size:22px;flex-shrink:0;margin-top:2px;}

/* DELPHI INFO */
.delphi-info{margin-bottom:0;}
.delphi-info p{font-size:14px;color:#333;}
.rounds{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#d5dce8;border:1px solid #d5dce8;margin-top:20px;}
.round-item{background:#fff;padding:18px 20px;text-align:center;}
.round-num{font-size:22px;font-weight:800;color:#1C3A6E;margin-bottom:4px;}
.round-label{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:0.6px;}
.round-desc{font-size:12px;color:#666;margin-top:6px;line-height:1.5;}

/* DELPHI FORM */
.dform{border:1px solid #d5dce8;padding:28px;background:#fafbfd;}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;}
.fg{display:flex;flex-direction:column;gap:5px;}
.fg.full{grid-column:1/-1;}
label{font-size:12px;font-weight:600;color:#444;}
.fi,.fsel,.fta{background:#fff;border:1px solid #ccc;padding:9px 12px;font-size:13px;color:#1a1a1a;font-family:inherit;transition:border 0.15s;border-radius:0;}
.fi:focus,.fsel:focus,.fta:focus{outline:none;border-color:#1C3A6E;}
.fta{resize:vertical;min-height:90px;}
.fsub{background:#1C3A6E;color:#fff;border:none;padding:10px 26px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit;transition:background 0.15s;border-radius:0;}
.fsub:hover{background:#2E75B6;}
.fnote{font-size:11.5px;color:#999;margin-top:10px;line-height:1.55;}

/* CITE */
.cblock{background:#1a1e2e;padding:16px 18px;font-family:"JetBrains Mono",monospace;font-size:12px;color:#a8b4d0;line-height:1.85;position:relative;margin-top:10px;margin-bottom:22px;border-left:3px solid #2E75B6;overflow:auto;}
.cpbtn{position:absolute;top:10px;right:10px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);color:#a8b4d0;padding:3px 10px;font-size:10px;cursor:pointer;font-family:inherit;transition:all 0.15s;border-radius:0;}
.cpbtn:hover{background:rgba(255,255,255,0.18);color:#fff;}

/* FOOTER */
footer{background:#111827;padding:30px 52px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;}
.fl img{height:26px;display:block;opacity:0.6;}
.ft{font-size:12px;color:rgba(255,255,255,0.3);}
.flinks{display:flex;gap:22px;}
.flinks a{font-size:12px;color:rgba(255,255,255,0.3);text-decoration:none;}
.flinks a:hover{color:rgba(255,255,255,0.7);}

.toast{position:fixed;bottom:20px;right:20px;background:#1C3A6E;color:#fff;padding:10px 18px;font-size:13px;transform:translateY(60px);opacity:0;transition:all 0.3s;z-index:9999;box-shadow:0 4px 16px rgba(0,0,0,0.2);}
.toast.show{transform:translateY(0);opacity:1;}

@media(max-width:720px){
  nav{padding:0 20px;}
  .wrap{padding:0 20px;}
  .page-header{padding:32px 20px;}
  .ph-inner{flex-direction:column;gap:20px;}
  .frow{grid-template-columns:1fr;}
  footer{padding:22px 20px;flex-direction:column;align-items:flex-start;}
  .nav-links a:not(.cta){display:none;}
  .fe-grid{grid-template-columns:1fr;}
  .rounds{grid-template-columns:1fr;}
}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-logo"><img src="FUNDO_VAZIO.png" alt="CONCUR-IR"></div>
  <div class="nav-links">
    <a href="#about">About</a>
    <div class="nav-dropdown">
      <a href="#documents">Documents</a>
      <div class="nav-dropdown-menu">
        <a href="CONCUR-IR.html">
          <span class="dm-icon">&#9776;</span>
          <span>Interactive Checklist<span class="dm-sub">Fill out online</span></span>
        </a>
        <a href="CONCUR-IR_Checklist.docx" download>
          <span class="dm-icon">&#8984;</span>
          <span>Download Word<span class="dm-sub">.docx — editable checklist</span></span>
        </a>
        <a href="CONCUR-IR_Checklist.pdf" download>
          <span class="dm-icon">&#8599;</span>
          <span>Download PDF<span class="dm-sub">.pdf — print-ready</span></span>
        </a>
      </div>
    </div>
    <a href="#checklist">Checklist</a>
    <a href="#flowdiagram">Flow Diagram</a>
    <a href="#extensions">Extensions</a>
    <a href="#institutions">Institutions</a>
    <a href="#endorsement">Endorsement</a>
    <a href="#cite">Cite</a>
    <a href="#delphi" class="cta">Join Delphi Panel</a>
  </div>
</nav>

<!-- PAGE HEADER -->
<div class="page-header">
  <div class="ph-inner">
    <div class="ph-logo"><img src="FUNDO_VAZIO.png" alt="CONCUR-IR"></div>

    <div class="ph-text">
      <div class="ph-badge">CONCUR-IR 2026 &nbsp;·&nbsp; Delphi Validation Phase</div>
      <h1>Consensus Criteria for Uniform Reporting<br>in Interventional Radiology</h1>
      <p>The first universal reporting framework for primary IR studies — designed to complement procedure-specific CIRSE and SIR standards across all study designs.</p>
    </div>
  </div>
</div>

<!-- ABOUT -->
<section id="about">
  <div class="wrap">
    <h2>About CONCUR-IR</h2>
    <p>CONCUR-IR is the first universal reporting guideline for primary studies in interventional radiology. It was built to fill a structural gap: existing CIRSE and SIR reporting standards define outcome terminology for specific procedures, but none address the full methodological scope that a primary IR study must cover to be reproducible, comparable, and clinically credible.</p>
    <p>CONCUR-IR does not compete with procedure-specific standards — it complements them. Where CIRSE and SIR define <em>what counts as success</em> for a given technique, CONCUR-IR defines <em>how to report the study itself</em>: eligibility criteria, operator characteristics, imaging guidance, device specification, dose delivery, adverse event classification, statistical methods, and outcome taxonomy. Together, they form a complete reporting ecosystem for IR research.</p>
    <p>CONCUR-IR 2026 spans <strong>12 reporting domains</strong> and <strong>93 core items</strong>, with conditional item blocks activated by study design — covering case series, cohort studies, RCTs, registries, and case-control studies. All items are best-practice recommendations. An explanation and elaboration document is currently under development.</p>
    <p>CONCUR-IR is undergoing multi-round Delphi validation with IR experts across four international institutions. The statement is currently under review for publication.</p>
    <h3 style="margin-top:22px;margin-bottom:8px;">Development and methodology</h3>
    <p>CONCUR-IR was developed through a structured process combining systematic review of existing IR reporting practices, cross-referencing with established guidelines (CONSORT, STROBE, TREND, IDEAL), and iterative expert input across four international IR centers. Item generation, domain structuring, and conditional branching logic were developed over multiple review cycles before formal Delphi validation.</p>
    <h3 style="margin-top:18px;margin-bottom:8px;">Funding</h3>
    <p>CONCUR-IR was developed without external funding or industry sponsorship. No commercial entity had any role in item development, domain structure, or publication planning. The project is supported entirely by academic contributions from the four collaborating institutions.</p>
  </div>
</section>

<!-- DOCUMENTS -->
<section id="documents">
  <div class="wrap">
    <h2>Documents</h2>
    <div class="tabs">
      <button class="tab-btn active" onclick="switchTab(this,'docs-overview')">Overview</button>
      <button class="tab-btn" onclick="switchTab(this,'docs-download')">Download</button>
    </div>

    <div class="tab-pane active" id="docs-overview">
      <p>The CONCUR-IR 2026 reporting package includes a reporting checklist, an abstract checklist, a patient/procedure flow diagram template, a statement paper, and an explanation &amp; elaboration document. All materials are freely available under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0</a>.</p>
      <div class="docs-grid">
        <div class="doc-item">
          <div class="doc-type">Reporting Checklist</div>
          <div class="doc-name">CONCUR-IR 2026 Checklist</div>
          <div class="doc-links">
            <a class="doc-dl" href="CONCUR-IR_Checklist.docx" download>Word (.docx)</a>
            <a class="doc-dl" href="CONCUR-IR.html" target="_blank">Interactive</a>
          </div>
        </div>
        <div class="doc-item">
          <div class="doc-type">Abstract Checklist</div>
          <div class="doc-name">CONCUR-IR 2026 Abstract Checklist</div>
          <div class="doc-links"><span class="doc-soon">Under development</span></div>
        </div>
        <div class="doc-item">
          <div class="doc-type">Flow Diagram</div>
          <div class="doc-name">CONCUR-IR Patient/Procedure Flow Diagram</div>
          <div class="doc-links"><span class="doc-soon">Word template — coming</span></div>
        </div>
        <div class="doc-item">
          <div class="doc-type">Statement Paper</div>
          <div class="doc-name">CONCUR-IR 2026 Statement</div>
          <div class="doc-links"><span class="doc-soon">Under review</span></div>
        </div>
        <div class="doc-item">
          <div class="doc-type">Explanation &amp; Elaboration</div>
          <div class="doc-name">CONCUR-IR 2026 E&amp;E Document</div>
          <div class="doc-links"><span class="doc-soon">Under development</span></div>
        </div>
      </div>
    </div>

    <div class="tab-pane" id="docs-download">
      <div class="dl-section">
        <div class="dl-card">
          <h3>CONCUR-IR Checklist</h3>
          <p>The complete reporting checklist with all 12 domains and 93 core items. Use the Word file to fill in page numbers and submit with your manuscript. Use the interactive version to check off items online and export as PDF.</p>
          <div class="dl-btns">
            <a class="dlb" href="CONCUR-IR_Checklist.docx" download>&#8659;&nbsp; Download Word (.docx)</a>
            <a class="dlb outline" href="CONCUR-IR.html" target="_blank">&#9654;&nbsp; Open Interactive Version</a>
          </div>
        </div>
        <div class="dl-card">
          <h3>CONCUR-IR Checklist — PDF</h3>
          <p>To obtain a PDF version, open the interactive checklist in your browser and use your browser's print function (File → Print → Save as PDF). All formatting is optimized for print output.</p>
          <div class="dl-btns">
            <a class="dlb outline" href="CONCUR-IR.html" target="_blank" onclick="setTimeout(()=>window.open('CONCUR-IR.html'),100)">Open &amp; Print as PDF</a>
          </div>
        </div>
        <div class="dl-card" style="background:#fff8f0;border-color:#e0c090;">
          <h3 style="color:#7a4a00;">Coming soon</h3>
          <p style="color:#7a4a00;">Flow Diagram Word template, Statement paper, and Explanation &amp; Elaboration document will be available here upon completion of Delphi validation.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CHECKLIST -->
<section id="checklist">
  <div class="wrap">
    <h2>CONCUR-IR Checklist</h2>
    <p>The checklist is organized into 12 reporting domains. Each domain contains core items applicable to all study designs, plus conditional items activated by the declared study design. Conditional blocks cover five designs: <strong>Case Series</strong>, <strong>Cohort</strong>, <strong>RCT</strong>, <strong>Registry</strong>, and <strong>Case-Control</strong>.</p>
    <p>Authors should complete all core items and the conditional items for their design, record the manuscript page number for each, and submit the completed checklist as a supplementary file. Download the <a href="CONCUR-IR_Checklist.docx" download>Word checklist (.docx)</a> or use the <a href="CONCUR-IR.html" target="_blank">interactive browser version</a>.</p>
    <table class="dtable">
      <thead>
        <tr><th>Domain</th><th>Title</th><th style="text-align:right">Core items</th><th>Conditional designs</th></tr>
      </thead>
      <tbody>
        <tr><td class="did">D1</td><td>Study Design &amp; Pre-Registration</td><td class="nitems">5</td><td class="cond">RCT, Registry, Case Series</td></tr>
        <tr><td class="did">D2</td><td>Patient Selection &amp; Eligibility</td><td class="nitems">4</td><td class="cond">Case Series, Cohort, RCT, Registry</td></tr>
        <tr><td class="did">D3a</td><td>Baseline Clinical Characterization</td><td class="nitems">6</td><td class="cond">Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D3b</td><td>Baseline Anatomical &amp; Radiological Characterization</td><td class="nitems">5</td><td class="cond">Cohort/RCT, Registry</td></tr>
        <tr><td class="did">D4</td><td>Intervention Indication &amp; Alternatives</td><td class="nitems">5</td><td class="cond">Case Series, Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D5</td><td>Operator &amp; Center Characteristics</td><td class="nitems">5</td><td class="cond">Case Series, Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D6a</td><td>Procedure Description — Technical Execution</td><td class="nitems">7</td><td class="cond">Case Series, Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D6b</td><td>Procedure Description — Imaging Guidance</td><td class="nitems">5</td><td class="cond">Case Series, RCT</td></tr>
        <tr><td class="did">D6c</td><td>Procedure Description — Devices &amp; Materials</td><td class="nitems">5</td><td class="cond">Case Series, RCT, Registry</td></tr>
        <tr><td class="did">D7</td><td>Periprocedural Management</td><td class="nitems">6</td><td class="cond">Case Series, Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D8</td><td>Radiation, Contrast &amp; Dose Delivery</td><td class="nitems">7</td><td class="cond">Case Series, Cohort/RCT, Registry</td></tr>
        <tr><td class="did">D9</td><td>Outcome Definition &amp; Taxonomy</td><td class="nitems">11</td><td class="cond">Case Series, Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D10</td><td>Adverse Events</td><td class="nitems">8</td><td class="cond">Case Series, Cohort/RCT, RCT, Registry</td></tr>
        <tr><td class="did">D11</td><td>Follow-up &amp; Statistical Analysis</td><td class="nitems">9</td><td class="cond">Case Series, Cohort, RCT, Registry</td></tr>
        <tr><td class="did">D12</td><td>Funding, Conflicts of Interest &amp; Data Availability</td><td class="nitems">5</td><td class="cond">—</td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FLOW DIAGRAM -->
<section id="flowdiagram">
  <div class="wrap">
    <h2>CONCUR-IR Flow Diagram</h2>
    <p>The CONCUR-IR flow diagram tracks patients and procedures from initial identification through final analysis, adapted for IR-specific exclusion points such as procedural failure and technical non-eligibility. It is mandatory for cohort studies and RCTs, and strongly recommended for case series with formal eligibility criteria.</p>
    <p>A Word template will be made available when finalized. The diagram must include the following stages and elements:</p>

    <div class="flow-elements">
      <div class="fe-grid">
        <div class="fe-item">
          <div class="fe-num">1</div>
          <div class="fe-txt">
            <h4>Identification</h4>
            <p>Total number of patients or procedures identified as potentially eligible, with source (e.g., institutional database, referral list, registry query).</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">2</div>
          <div class="fe-txt">
            <h4>Screening exclusions</h4>
            <p>Number excluded at screening with specific reasons itemized (failed inclusion criteria, declined participation, other). Each reason reported as n.</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">3</div>
          <div class="fe-txt">
            <h4>Enrollment</h4>
            <p>Number formally enrolled after screening. In RCTs: number randomized per arm must be shown at this stage.</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">4</div>
          <div class="fe-txt">
            <h4>Post-enrollment exclusions</h4>
            <p>Exclusions after enrollment but before or during the procedure: procedure not performed, technical failure, withdrawal of consent. Reported separately from screening exclusions.</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">5</div>
          <div class="fe-txt">
            <h4>Procedure completion</h4>
            <p>Number in whom the procedure was performed as planned. This is the denominator for technical success and immediate outcome reporting.</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">6</div>
          <div class="fe-txt">
            <h4>Follow-up losses</h4>
            <p>Number lost before the primary endpoint assessment timepoint, with reason where known. Distinguish deaths from drop-outs and administrative censoring.</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">7</div>
          <div class="fe-txt">
            <h4>Final analysis</h4>
            <p>Number included in the primary analysis. In RCTs: confirm ITT/modified ITT/per-protocol population here. Any discrepancy from enrolled n must be explained.</p>
          </div>
        </div>
        <div class="fe-item">
          <div class="fe-num">8</div>
          <div class="fe-txt">
            <h4>Denominators at each stage</h4>
            <p>All figures must be reported as absolute numbers (n), not percentages alone. The denominator at each stage must be stated explicitly and must reflect the actual population at risk.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- HOW TO USE -->
<section id="howto">
  <div class="wrap">
    <h2>How to use CONCUR-IR</h2>
    <div class="steps">
      <div class="step-item">
        <div class="step-num">1</div>
        <div class="step-body">
          <h3>Select your study design</h3>
          <p>Identify whether your study is a case series, cohort, RCT, registry-based study, or case-control study. In the Word checklist or interactive tool, activate the corresponding design to reveal conditional items relevant to your design.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">2</div>
        <div class="step-body">
          <h3>Complete all core items across D1–D12</h3>
          <p>Work through all 12 domains. Core items apply to all study types. Items marked <em>(recommended)</em> are strongly encouraged but represent best practice rather than mandatory requirements.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">3</div>
        <div class="step-body">
          <h3>Address all conditional items for your design</h3>
          <p>Conditional items appear within relevant domains for your study design — for example, randomization and allocation concealment items in RCTs, or learning-curve acknowledgment in case series.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">4</div>
        <div class="step-body">
          <h3>Record manuscript page numbers and submit</h3>
          <p>For each reported item, enter the page, section, or figure number where that information appears. Submit the completed checklist as a supplementary file. Most IR journals now require a reporting checklist at submission.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">5</div>
        <div class="step-body">
          <h3>Include the flow diagram</h3>
          <p>Complete the CONCUR-IR flow diagram showing patient and procedure flow from identification through analysis. Include it as a manuscript figure or supplementary material with explicit denominators at each stage.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- INSTITUTIONS -->
<section id="institutions">
  <div class="wrap">
    <h2>Collaborating institutions</h2>
    <p>CONCUR-IR was developed through a multi-center international collaboration. Delphi validation is being conducted with expert panels at the following institutions.</p>
    <div class="inst-list">
      <div class="inst-item">
        <div class="inst-icon">&#127963;</div>
        <div>
          <div class="inst-name">Massachusetts General Hospital — Harvard Medical School</div>
          <div class="inst-city">Boston, Massachusetts, USA</div>
          <div class="inst-role">Delphi validation partner · Methodology review</div>
        </div>
      </div>
      <div class="inst-item">
        <div class="inst-icon">&#127963;</div>
        <div>
          <div class="inst-name">Hospital Israelita Albert Einstein (HIAE)</div>
          <div class="inst-city">São Paulo, Brazil</div>
          <div class="inst-role">Delphi validation partner · Latin America coordination</div>
        </div>
      </div>
      <div class="inst-item">
        <div class="inst-icon">&#127963;</div>
        <div>
          <div class="inst-name">Institut Curie</div>
          <div class="inst-city">Paris, France</div>
          <div class="inst-role">Delphi validation partner · Oncologic IR expertise</div>
        </div>
      </div>
      <div class="inst-item">
        <div class="inst-icon">&#127963;</div>
        <div>
          <div class="inst-name">University of Arizona</div>
          <div class="inst-city">Tucson, Arizona, USA</div>
          <div class="inst-role">Delphi validation partner · Methodology review</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- EXTENSIONS -->
<section id="extensions">
  <div class="wrap">
    <h2>CONCUR-IR Extensions</h2>
    <p>CONCUR-IR is designed as a universal framework applicable to all IR primary studies. Procedure-specific extensions are planned to complement the core checklist with items tailored to individual IR domains — analogous to the PRISMA extension model. Extensions will not replace the core CONCUR-IR checklist; they will add domain-specific conditional items on top of it.</p>
    <p>The following extensions are under consideration for future development:</p>
    <ul style="margin:16px 0 0 20px;line-height:2;color:#333;font-size:14px;">
      <li>CONCUR-IR Embolization (transarterial embolization and chemoembolization)</li>
      <li>CONCUR-IR Ablation (thermal ablation: RFA, MWA, cryoablation, IRE)</li>
      <li>CONCUR-IR Radioembolization (SIRT/TARE with Y-90 and other radionuclides)</li>
      <li>CONCUR-IR Vascular Access (central venous access, PICC, ports)</li>
      <li>CONCUR-IR Peripheral Arterial Disease (angioplasty, stenting, atherectomy)</li>
      <li>CONCUR-IR Venous Interventions (thrombolysis, IVC filter, venoplasty)</li>
      <li>CONCUR-IR Biliary &amp; GI Interventions</li>
      <li>CONCUR-IR Vertebral Augmentation</li>
    </ul>
    <p style="margin-top:16px;">If you are interested in leading or collaborating on an extension, contact us at <a href="mailto:delphi@concur-ir.org">delphi@concur-ir.org</a>.</p>
  </div>
</section>

<!-- ENDORSEMENT -->
<section id="endorsement">
  <div class="wrap">
    <h2>Endorsement</h2>
    <p>Journals, societies, and institutions are invited to formally endorse CONCUR-IR 2026 and encourage its use in primary IR research submissions. Endorsement means that your journal recommends or requires authors of IR primary studies to consult CONCUR-IR and submit a completed checklist as a supplementary file.</p>
    <h3 style="margin-top:22px;margin-bottom:10px;">How to endorse CONCUR-IR</h3>
    <p><strong>Step 1.</strong> Add a reference to CONCUR-IR in your journal's instructions to authors for interventional radiology manuscripts. Suggested language:</p>
    <div style="background:#f5f7fc;border-left:3px solid #2E75B6;padding:14px 18px;margin:14px 0;font-size:13.5px;color:#333;font-style:italic;">
      "Authors submitting primary interventional radiology studies are encouraged to consult the CONCUR-IR 2026 reporting guideline (concur-ir.org) and submit a completed CONCUR-IR checklist as a supplementary file."
    </div>
    <p><strong>Step 2.</strong> Notify us at <a href="mailto:delphi@concur-ir.org">delphi@concur-ir.org</a> so we can list your journal or society among endorsing institutions.</p>
    <h3 style="margin-top:24px;margin-bottom:10px;">Endorsing institutions</h3>
    <p style="color:#888;font-style:italic;">Endorsements will be listed here upon formal publication of the CONCUR-IR 2026 statement. Delphi validation is currently in progress.</p>
  </div>
</section>

<!-- DELPHI -->
<section id="delphi">
  <div class="wrap">
    <h2>Delphi Expert Panel</h2>
    <div class="tabs">
      <button class="tab-btn active" onclick="switchTab(this,'delphi-about')">About the Panel</button>
      <button class="tab-btn" onclick="switchTab(this,'delphi-apply')">Apply</button>
    </div>

    <div class="tab-pane active" id="delphi-about">
      <div class="delphi-info">
        <p>CONCUR-IR is being validated through a structured Delphi consensus process. A panel of interventional radiology experts across multiple countries will evaluate each checklist item for relevance, completeness, and feasibility in real-world IR research settings.</p>
        <p>The process follows established Delphi methodology: panelists complete structured questionnaires in two or three sequential rounds. After each round, results are aggregated and fed back to the panel. Items reaching predefined consensus thresholds are retained; items below threshold are revised or removed. Panelists are blinded to each other's identities throughout.</p>
        <p>Participation requires approximately 45–60 minutes per round. Panelists who complete all rounds will be listed as Delphi contributors in the final publication.</p>
        <div class="rounds">
          <div class="round-item">
            <div class="round-num">Round 1</div>
            <div class="round-label">Item Rating</div>
            <div class="round-desc">Rate each item for relevance and feasibility on a 1–9 Likert scale.</div>
          </div>
          <div class="round-item">
            <div class="round-num">Round 2</div>
            <div class="round-label">Revision &amp; Consensus</div>
            <div class="round-desc">Review aggregated Round 1 results and re-rate items below consensus threshold.</div>
          </div>
          <div class="round-item">
            <div class="round-num">Round 3</div>
            <div class="round-label">Final Confirmation</div>
            <div class="round-desc">Confirm final item set. Conducted only if ≥15% of items remain below threshold after Round 2.</div>
          </div>
        </div>
      </div>
    </div>

    <div class="tab-pane" id="delphi-apply">
      <p style="margin-bottom:20px;font-size:14px;">To apply for the Delphi panel, complete the form below. Applications are reviewed on a rolling basis. We are particularly seeking panelists from under-represented IR subspecialties and geographic regions.</p>
      <div class="dform">
        <form onsubmit="submitDelphi(event)">
          <div class="frow">
            <div class="fg"><label>Full name *</label><input class="fi" type="text" placeholder="First and last name" required></div>
            <div class="fg"><label>Email address *</label><input class="fi" type="email" placeholder="your@institution.edu" required></div>
          </div>
          <div class="frow">
            <div class="fg"><label>Institution *</label><input class="fi" type="text" placeholder="Hospital or University" required></div>
            <div class="fg"><label>Country *</label><input class="fi" type="text" placeholder="Country" required></div>
          </div>
          <div class="frow">
            <div class="fg">
              <label>Years of IR experience</label>
              <select class="fsel">
                <option value="">Select</option>
                <option>1–5 years</option><option>6–10 years</option><option>11–20 years</option><option>20+ years</option>
              </select>
            </div>
            <div class="fg"><label>Primary IR subspecialty</label><input class="fi" type="text" placeholder="e.g. Oncology, Vascular, Neuro"></div>
          </div>
          <div class="fg full" style="margin-bottom:18px;"><label>Statement of interest (optional)</label><textarea class="fta" placeholder="Why you wish to participate in the Delphi process..."></textarea></div>
          <button type="submit" class="fsub">Submit application</button>
          <p class="fnote">Your information will be used solely to contact you regarding CONCUR-IR Delphi rounds and will not be shared with third parties.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- CITE -->
<section id="cite">
  <div class="wrap">
    <h2>Cite CONCUR-IR</h2>
    <p>If you use CONCUR-IR in your work, please cite the working document as follows. The citation will be updated upon formal publication.</p>
    <h3>Vancouver / ICMJE</h3>
    <div class="cblock" id="cvan">CONCUR-IR Working Group. Consensus Criteria for Uniform Reporting in Interventional Radiology (CONCUR-IR) 2026: a reporting guideline for primary interventional radiology studies. 2026. Available at: https://concur-ir.org<button class="cpbtn" onclick="copyCite('cvan')">Copy</button></div>
    <h3>BibTeX</h3>
    <div class="cblock" id="cbib">@misc&#123;concurir2026,<br>&nbsp; title&nbsp;&nbsp; = &#123;CONCUR-IR 2026: Consensus Criteria for Uniform Reporting in Interventional Radiology&#125;,<br>&nbsp; author&nbsp; = &#123;&#123;CONCUR-IR Working Group&#125;&#125;,<br>&nbsp; year&nbsp;&nbsp;&nbsp; = &#123;2026&#125;,<br>&nbsp; url&nbsp;&nbsp;&nbsp;&nbsp; = &#123;https://concur-ir.org&#125;<br>&#125;<button class="cpbtn" onclick="copyCite('cbib')">Copy</button></div>
    <p style="font-size:13px;color:#777;">All materials are distributed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0</a>. Citation will be updated upon journal publication.</p>
  </div>
</section>

<footer>
  <div class="fl"><img src="FUNDO_VAZIO.png" alt="CONCUR-IR"></div>
  <div class="ft">CONCUR-IR 2026 &nbsp;·&nbsp; <a href="mailto:delphi@concur-ir.org" style="color:rgba(255,255,255,0.3);text-decoration:none;">delphi@concur-ir.org</a> &nbsp;·&nbsp; CC BY 4.0</div>
  <div class="flinks">
    <a href="#about">About</a>
    <a href="#documents">Documents</a>
    <a href="#extensions">Extensions</a>
    <a href="#endorsement">Endorsement</a>
    <a href="#delphi">Delphi Panel</a>
    <a href="#cite">Cite</a>
  </div>
</footer>

<div class="toast" id="toast"></div>

<script>
function switchTab(btn, paneId) {
  const section = btn.closest('section') || btn.closest('.wrap') || document.body;
  const tabGroup = btn.closest('.tabs');
  const paneGroup = tabGroup.nextElementSibling.id ? tabGroup.parentElement : tabGroup.parentElement;
  tabGroup.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  paneGroup.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.getElementById(paneId).classList.add('active');
}
function copyCite(id) {
  const el = document.getElementById(id);
  const btn = el.querySelector('.cpbtn');
  const text = el.innerText.replace('Copy','').replace('Copied!','').trim();
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 2000);
  });
}
function submitDelphi(e) {
  e.preventDefault();
  const f = e.target;
  const inputs = f.querySelectorAll('input[type=text]');
  const name = inputs[0].value;
  const email = f.querySelector('input[type=email]').value;
  const inst = inputs[1].value;
  const country = inputs[2].value;
  const exp = f.querySelector('select').value;
  const spec = inputs[3]?.value || '';
  const msg = f.querySelector('textarea').value;
  const body = `Name: ${name}%0AInstitution: ${inst}%0ACountry: ${country}%0AExperience: ${exp}%0ASubspecialty: ${spec}%0A%0AStatement of interest:%0A${encodeURIComponent(msg)}`;
  window.location.href = `mailto:delphi@concur-ir.org?subject=Delphi Panel Application — ${encodeURIComponent(name)}&body=${body}`;
  const t = document.getElementById('toast');
  t.textContent = 'Opening email client...';
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}
</script>
</body>
</html>"""

out = os.path.join(BASE, 'CONCUR-IR-site.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f'Done — {len(HTML):,} chars — {os.path.getsize(out):,} bytes')
