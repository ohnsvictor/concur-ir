"""
Restyles CONCUR-IR.html to match the main site design system:
- Poppins font
- No rounded corners
- Same color/button/table styles as CONCUR-IR-site.html
- Version: 2026
"""
import re

BASE = r'c:\Users\JLOW0\OneDrive\Área de Trabalho\IRSET'
src = BASE + r'\CONCUR-IR.html'

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

NEW_HEAD_OPEN = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CONCUR-IR 2026 — Interactive Checklist</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">"""

NEW_STYLE = """<style>
:root{
  --navy:#1C3A6E;--blue:#2E75B6;--teal:#1A7FAA;
  --condbg:#EEF3FA;--condhdr:#2E75B6;
  --gray:#6B7A99;--border:#D0D8E8;--white:#FFFFFF;
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:"Poppins",system-ui,sans-serif;background:#fff;color:#1a1a1a;font-size:14px;line-height:1.6;}

/* NAV */
nav{background:var(--navy);padding:0 48px;display:flex;align-items:center;gap:24px;height:60px;position:sticky;top:0;z-index:100;box-shadow:0 4px 20px rgba(0,0,0,0.3);}
.nav-logo{display:flex;align-items:center;gap:14px;}
.nav-logo img{height:32px;filter:brightness(0) invert(1);}
.nav-logo-text{color:white;font-size:15px;font-weight:700;letter-spacing:-0.2px;}
.nav-logo-sub{color:rgba(255,255,255,0.5);font-size:11px;font-weight:400;display:block;margin-top:-2px;}
.nav-badge{margin-left:auto;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);color:rgba(255,255,255,0.65);font-size:10.5px;font-weight:600;letter-spacing:0.8px;text-transform:uppercase;padding:3px 10px;}
.nav-back{color:rgba(255,255,255,0.6);font-size:12.5px;font-weight:500;text-decoration:none;margin-left:12px;padding:6px 14px;border:1px solid rgba(255,255,255,0.2);}
.nav-back:hover{background:rgba(255,255,255,0.08);color:white;}

/* SETUP BAR */
.setup-panel{background:#f7f9fd;border-bottom:2px solid var(--border);padding:14px 48px;position:sticky;top:60px;z-index:90;}
.setup-row{display:flex;align-items:flex-start;gap:32px;flex-wrap:wrap;}
.setup-section{flex:1;min-width:220px;}
.setup-label{font-size:10px;font-weight:700;color:var(--gray);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}
.design-pills{display:flex;flex-wrap:wrap;gap:6px;}
.pill{padding:5px 14px;border:1.5px solid var(--border);background:white;color:var(--navy);font-size:12px;font-weight:600;cursor:pointer;transition:all 0.15s;user-select:none;font-family:inherit;}
.pill:hover{border-color:var(--blue);color:var(--blue);}
.pill.active{background:var(--navy);border-color:var(--navy);color:white;}

/* PROGRESS */
.progress-wrap{min-width:200px;}
.progress-numbers{display:flex;justify-content:space-between;font-size:12px;color:var(--gray);margin-bottom:6px;}
.progress-numbers strong{color:var(--navy);font-size:14px;}
.progress-bar-bg{background:var(--condbg);height:6px;overflow:hidden;}
.progress-bar-fill{height:100%;background:linear-gradient(90deg,var(--blue),var(--teal));width:0%;transition:width 0.3s;}

/* BUTTONS */
.action-btns{display:flex;gap:8px;align-items:flex-end;padding-bottom:2px;}
.btn{padding:7px 16px;border:none;font-size:12px;font-weight:600;cursor:pointer;transition:all 0.15s;white-space:nowrap;font-family:inherit;}
.btn-primary{background:var(--navy);color:white;}
.btn-primary:hover{background:var(--blue);}
.btn-outline{background:white;color:var(--navy);border:1.5px solid var(--border);}
.btn-outline:hover{border-color:var(--blue);color:var(--blue);}
.btn-danger{background:white;color:#c0392b;border:1.5px solid #f0c0bb;}
.btn-danger:hover{background:#fff5f5;}

/* INSTRUCTIONS */
.instructions{background:var(--condbg);border-left:3px solid var(--blue);padding:10px 16px;font-size:12.5px;color:var(--gray);margin:14px 48px;}
.instructions strong{color:var(--navy);}

/* CHECKLIST */
.checklist{padding:0 48px 48px;max-width:1100px;margin:0 auto;}

/* DOMAIN */
.domain{margin-bottom:12px;border:1px solid var(--border);overflow:hidden;}
.domain-header{background:var(--navy);color:white;padding:10px 18px;font-size:13px;font-weight:700;display:flex;align-items:center;gap:10px;cursor:pointer;user-select:none;}
.domain-id{background:rgba(255,255,255,0.15);padding:2px 8px;font-size:10px;font-weight:700;letter-spacing:1px;}
.domain-toggle{margin-left:auto;font-size:14px;opacity:0.7;}
.domain-body{background:white;}

/* COLUMN HEADERS */
.col-headers{display:grid;grid-template-columns:56px 1fr 110px;padding:6px 16px;background:#f4f7fc;border-bottom:1px solid var(--border);font-size:10px;font-weight:700;color:var(--gray);text-transform:uppercase;letter-spacing:0.6px;}

/* ITEM ROW */
.item-row{display:grid;grid-template-columns:56px 1fr 110px;padding:9px 16px;border-bottom:1px solid #eef2f9;transition:background 0.1s;align-items:start;}
.item-row:hover{background:#fafcff;}
.item-row.checked-row{background:#f2fbf8;}
.item-id{font-size:11px;color:var(--gray);font-weight:600;padding-top:2px;}
.item-content{padding-right:14px;}
.item-check-wrap{display:flex;align-items:flex-start;gap:10px;}
.custom-cb{width:17px;height:17px;border:2px solid var(--border);flex-shrink:0;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.15s;margin-top:2px;background:white;}
.custom-cb:hover{border-color:var(--blue);}
.custom-cb.checked{background:var(--teal);border-color:var(--teal);}
.custom-cb.checked::after{content:'✓';color:white;font-size:11px;font-weight:700;}
.item-text{font-size:13px;color:#222;line-height:1.5;}
.item-text.checked-text{color:var(--gray);text-decoration:line-through;}
.rec-tag{font-size:10px;color:var(--teal);font-style:italic;font-weight:500;margin-left:5px;white-space:nowrap;}
.sub-items{margin-top:5px;padding-left:4px;}
.sub-item{font-size:11.5px;color:var(--gray);padding:2px 0 2px 10px;border-left:2px solid var(--border);margin-bottom:2px;font-style:italic;line-height:1.4;}
.sub-item::before{content:'→ ';color:#5B9BD5;font-style:normal;font-weight:600;}

/* PAGE INPUT */
.page-input{border:1px solid var(--border);padding:4px 8px;font-size:12px;width:90px;color:var(--navy);background:white;font-family:inherit;}
.page-input:focus{outline:none;border-color:var(--blue);}
.page-input::placeholder{color:#ccc;}

/* CONDITIONAL */
.cond-block{display:none;}
.cond-block.visible{display:block;}
.cond-header{background:var(--condhdr);color:white;padding:7px 16px 7px 22px;font-size:11.5px;font-weight:700;display:flex;align-items:center;gap:8px;}
.cond-header::before{content:'▼';font-size:9px;opacity:0.8;}
.cond-note{background:#f5f7fa;padding:8px 16px 8px 22px;font-size:11px;color:var(--gray);font-style:italic;border-bottom:1px solid var(--border);line-height:1.5;}
.cond-block .item-row{background:var(--condbg);}
.cond-block .item-row:hover{background:#e4edfa;}
.cond-block .item-id{color:var(--blue);}

/* FOOTER */
.footer{background:#111827;color:rgba(255,255,255,0.4);font-size:11.5px;padding:20px 48px;margin-top:24px;}

/* TOAST */
.toast{position:fixed;bottom:20px;right:20px;background:var(--navy);color:white;padding:10px 18px;font-size:13px;transform:translateY(60px);opacity:0;transition:all 0.3s;z-index:999;box-shadow:0 4px 16px rgba(0,0,0,0.2);}
.toast.show{transform:translateY(0);opacity:1;}

@media print{
  nav,.setup-panel,.action-btns,.footer{display:none!important;}
  .checklist{padding:0 10px!important;}
  .instructions{margin:0 10px 12px!important;}
  .cond-block{display:block!important;}
  .domain{margin-bottom:6px!important;box-shadow:none!important;}
}
@media(max-width:700px){
  nav,.setup-panel,.checklist,.instructions{padding-left:16px;padding-right:16px;}
  .setup-panel{top:60px;}
}
</style>"""

NEW_TOPBAR = """<nav>
  <div class="nav-logo">
    <img src="Logo Concur.png" alt="CONCUR-IR">
    <div>
      <span class="nav-logo-text">CONCUR-IR 2026</span>
      <span class="nav-logo-sub">Interactive Reporting Checklist</span>
    </div>
  </div>
  <a class="nav-back" href="CONCUR-IR-site.html">&#8592; Back to site</a>
  <div class="nav-badge">CONCUR-IR 2026</div>
</nav>"""

NEW_FOOTER = """<div class="footer">
  CONCUR-IR 2026 &nbsp;·&nbsp; Consensus Criteria for Uniform Reporting in Interventional Radiology &nbsp;·&nbsp; delphi@concur-ir.org
</div>"""

# Replace head open
html = re.sub(
    r'<!DOCTYPE html>\s*<html[^>]*>\s*<head>\s*<meta charset[^>]*>\s*<meta name="viewport"[^>]*>\s*<title>[^<]*</title>',
    NEW_HEAD_OPEN,
    html, count=1
)

# Replace entire style block
html = re.sub(r'<style>.*?</style>', NEW_STYLE, html, count=1, flags=re.DOTALL)

# Replace topbar div
html = re.sub(
    r'<!-- ── TOP BAR.*?</div>\s*\n',
    NEW_TOPBAR + '\n',
    html, count=1, flags=re.DOTALL
)

# Replace footer div
html = re.sub(
    r'<div class="footer">.*?</div>',
    NEW_FOOTER,
    html, count=1, flags=re.DOTALL
)

# Version references
html = html.replace('Draft v0.1 · 2025', 'CONCUR-IR 2026')
html = html.replace('CONCUR-IR v0.1', 'CONCUR-IR 2026')
html = html.replace('v0.1', '2026')

with open(src, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done — {len(html):,} chars')
