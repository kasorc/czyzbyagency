<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Social AI – Panel zarządzania</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
<style>
:root {
  --bg:#F7F6F3; --surface:#FFFFFF; --border:#E4E2DC; --border-light:#EEECE8;
  --text:#1A1916; --text-2:#5C5A54; --text-3:#9E9B93;
  --accent:#2D6A4F; --accent-light:#EAF3EE; --accent-border:#A8D5BC;
  --danger:#C0392B; --danger-light:#FCECEA; --danger-border:#F0B9B4;
  --warn:#B7791F; --warn-light:#FEF3CD; --warn-border:#F6D860;
  --info:#1A5F8A; --info-light:#E8F3FB; --info-border:#A3CDE8;
  --dw:#4BA6F0; --d3:#E2632A; --db:#2BB57C;
  --radius:8px; --radius-sm:5px;
  --shadow:0 1px 3px rgba(0,0,0,.07); --shadow-md:0 2px 8px rgba(0,0,0,.10);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--text);font-size:14px}
button{font-family:'DM Sans',sans-serif;cursor:pointer}
input,select,textarea{font-family:'DM Sans',sans-serif;font-size:13px;color:var(--text)}
select,input[type=text],input[type=date]{padding:7px 10px;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);width:100%;outline:none;transition:border-color .15s}
select:focus,input:focus{border-color:var(--accent)}
textarea{padding:8px 10px;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);width:100%;resize:vertical;line-height:1.6;outline:none;transition:border-color .15s}
textarea:focus{border-color:var(--accent)}
.app{display:flex;height:100vh;overflow:hidden}

/* SIDEBAR */
.sb{width:220px;flex-shrink:0;background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow-y:auto}
.sb-logo{padding:1.1rem 1.1rem .9rem;border-bottom:1px solid var(--border-light);margin-bottom:.5rem}
.sb-logo-name{font-size:15px;font-weight:600;color:var(--text);letter-spacing:-.2px}
.sb-logo-sub{font-size:11px;color:var(--text-3);margin-top:2px;font-family:'DM Mono',monospace}
.sb-sec{font-size:10px;color:var(--text-3);padding:.7rem 1.1rem .25rem;letter-spacing:.07em;text-transform:uppercase;font-weight:500}
.sb-btn{display:flex;align-items:center;gap:9px;padding:.45rem 1.1rem;border:none;background:none;width:100%;text-align:left;font-size:13px;color:var(--text-2);transition:background .1s,color .1s}
.sb-btn:hover{background:var(--bg);color:var(--text)}
.sb-btn.on{background:var(--accent-light);color:var(--accent);font-weight:500}
.sb-btn .ti{font-size:16px;opacity:.7}
.sb-btn.on .ti{opacity:1}
.dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;display:inline-block}
.badge-count{margin-left:auto;font-size:10px;font-weight:600;background:var(--danger-light);color:var(--danger);border-radius:10px;padding:1px 6px}

/* MAIN */
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}
.topbar{background:var(--surface);border-bottom:1px solid var(--border);padding:.65rem 1.25rem;display:flex;align-items:center;justify-content:space-between;gap:8px}
.badge{font-size:11px;font-weight:500;padding:2px 9px;border-radius:20px;border:1px solid}
.bw{background:#EBF4FD;color:#1557A0;border-color:#BAD8F5}
.b3{background:#FBECe8;color:#8B3112;border-color:#F4C0A8}
.bb{background:#E8F5EE;color:#1A5C35;border-color:#A7D8BB}
.view{display:none;flex:1;overflow-y:auto;padding:1.1rem;flex-direction:column;gap:.8rem}
.view.on{display:flex}

/* CARDS */
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:.9rem 1rem;box-shadow:var(--shadow)}
.card-title{font-size:13.5px;font-weight:600;color:var(--text);margin-bottom:.75rem;display:flex;align-items:center;gap:7px}
.card-title .ti{color:var(--text-3);font-size:16px}
.r2{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:9px}
.fg{display:flex;flex-direction:column;gap:4px;margin-bottom:9px}
.fg label{font-size:11.5px;color:var(--text-2);font-weight:500}

/* BUTTONS */
.btn{font-size:12.5px;padding:6px 13px;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);color:var(--text-2);display:inline-flex;align-items:center;gap:5px;transition:all .12s;white-space:nowrap}
.btn:hover{background:var(--bg);color:var(--text);border-color:#ccc}
.btn.pr{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn.pr:hover{background:#245C42;border-color:#245C42}
.btn.rd{background:var(--danger-light);color:var(--danger);border-color:var(--danger-border)}
.btn.rd:hover{background:#FBDBD9}
.btn:disabled{opacity:.4;cursor:default}
.spin{display:inline-block;width:12px;height:12px;border:1.5px solid transparent;border-top-color:currentColor;border-radius:50%;animation:sp .65s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}

/* TABS */
.ptabs{display:flex;gap:4px;margin-bottom:.75rem}
.tab{padding:4px 12px;font-size:12px;border-radius:var(--radius-sm);border:1px solid var(--border);background:none;color:var(--text-2)}
.tab:hover{background:var(--bg)}
.tab.on{background:var(--text);color:#fff;border-color:var(--text);font-weight:500}
.pc{display:none}.pc.on{display:block}
.rbox{background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-sm);padding:.85rem;min-height:80px;font-size:12.5px;line-height:1.75;color:var(--text);white-space:pre-wrap;font-family:'DM Mono',monospace}
.htags{color:var(--info);font-size:11.5px;margin-top:5px;line-height:1.7;font-family:'DM Mono',monospace}
.sep{border:none;border-top:1px solid var(--border-light);margin:.8rem 0}
.arow{display:flex;gap:6px;flex-wrap:wrap;margin-top:7px}

/* COUNTDOWN */
.evp{display:none;margin-bottom:9px;padding:8px 10px;background:var(--info-light);border-radius:var(--radius-sm);font-size:12px;color:var(--info);line-height:1.6;border:1px solid var(--info-border)}
.cnt{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;font-weight:500;padding:3px 9px;border-radius:20px;border:1px solid}
.cnt-hot{background:var(--danger-light);color:var(--danger);border-color:var(--danger-border)}
.cnt-warn{background:var(--warn-light);color:var(--warn);border-color:var(--warn-border)}
.cnt-ok{background:var(--accent-light);color:var(--accent);border-color:var(--accent-border)}
.cnt-gone{background:var(--bg);color:var(--text-3);border-color:var(--border)}

/* FEEDBACK */
.fb-bar{background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-sm);padding:.85rem;margin-top:.8rem}
.stars{display:flex;gap:4px;margin-bottom:7px}
.star{font-size:20px;color:var(--border);background:none;border:none;padding:0;line-height:1;transition:color .1s}
.star:hover,.star.on{color:#F5A623}
.fbtags{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:7px}
.fbt{font-size:11.5px;padding:3px 9px;border:1px solid var(--border);border-radius:20px;background:none;color:var(--text-2)}
.fbt:hover{background:var(--bg)}
.fbt.on{background:var(--info-light);color:var(--info);border-color:var(--info-border);font-weight:500}

/* EVENTS */
.ev-pill{display:flex;align-items:flex-start;gap:9px;padding:9px 10px;background:var(--bg);border-radius:var(--radius-sm);border:1px solid var(--border);margin-bottom:6px;transition:border-color .12s}
.ev-pill:hover{border-color:#ccc}
.ep-n{font-weight:500;color:var(--text);font-size:13px}
.ep-d{font-size:11.5px;color:var(--text-3);margin-top:2px}
.ep-del{background:none;border:none;color:var(--text-3);font-size:15px;padding:2px 3px;flex-shrink:0}
.ep-del:hover{color:var(--danger)}

/* KB */
.kb-wrap{display:flex;gap:.8rem;flex:1}
.kb-cats{width:160px;flex-shrink:0;display:flex;flex-direction:column;gap:4px}
.kb-cat{display:flex;align-items:center;gap:8px;padding:.5rem .75rem;border-radius:var(--radius-sm);border:1px solid var(--border);background:var(--surface);font-size:12.5px;color:var(--text-2);text-align:left;width:100%}
.kb-cat:hover{background:var(--bg)}
.kb-cat.on{border-color:var(--accent-border);background:var(--accent-light);color:var(--accent);font-weight:500}
.tw{display:flex;flex-wrap:wrap;gap:5px;padding:7px 9px;border:1px solid var(--border);border-radius:var(--radius-sm);min-height:38px;cursor:text;background:var(--surface)}
.tw:focus-within{border-color:var(--accent)}
.tg{display:inline-flex;align-items:center;gap:3px;font-size:12px;padding:2px 8px;border-radius:20px;font-weight:500}
.tg-b{background:var(--info-light);color:var(--info)}
.tg-g{background:var(--accent-light);color:var(--accent)}
.tg-r{background:var(--danger-light);color:var(--danger)}
.tg-del{background:none;border:none;color:inherit;opacity:.6;font-size:13px;line-height:1;padding:0}
.tg-del:hover{opacity:1}
.tg-in{border:none;outline:none;background:transparent;font-size:12.5px;color:var(--text);font-family:'DM Sans',sans-serif;min-width:80px;flex:1}

/* LEARN */
.learn-card{border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;margin-bottom:.65rem;background:var(--surface);box-shadow:var(--shadow)}
.lc-hdr{display:flex;align-items:flex-start;gap:10px;padding:.85rem 1rem}
.lc-num{width:26px;height:26px;border-radius:50%;background:var(--bg);color:var(--text-3);font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;border:1px solid var(--border);font-family:'DM Mono',monospace}
.lc-num.ok{background:var(--accent-light);color:var(--accent);border-color:var(--accent-border)}
.lc-num.bad{background:var(--danger-light);color:var(--danger);border-color:var(--danger-border)}
.lc-meta{font-size:11px;color:var(--text-3);margin-bottom:5px;font-family:'DM Mono',monospace}
.lc-txt{font-size:13px;line-height:1.7;color:var(--text);white-space:pre-wrap}
.lc-body{padding:.75rem 1rem;border-top:1px solid var(--border-light);background:var(--bg)}
.vrow{display:flex;gap:6px}
.vbtn{flex:1;padding:7px;border-radius:var(--radius-sm);border:1px solid var(--border);background:var(--surface);font-size:13px;font-weight:500;display:flex;align-items:center;justify-content:center;gap:5px;transition:all .12s}
.vbtn.ok-v{border-color:var(--accent-border);color:var(--accent)}
.vbtn.ok-v:hover,.vbtn.ok-v.sel{background:var(--accent-light)}
.vbtn.bad-v{border-color:var(--danger-border);color:var(--danger)}
.vbtn.bad-v:hover,.vbtn.bad-v.sel{background:var(--danger-light)}
.prog{height:4px;background:var(--border);border-radius:2px;overflow:hidden;margin:.6rem 0;display:none}
.prog-fill{height:100%;background:var(--accent);border-radius:2px;transition:width .3s}

/* INBOX */
.ib-item{border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;margin-bottom:.6rem;background:var(--surface);box-shadow:var(--shadow)}
.ib-hdr{display:flex;align-items:center;gap:8px;padding:.75rem 1rem;cursor:pointer}
.ib-hdr:hover{background:var(--bg)}
.ib-body{padding:.875rem 1rem;border-top:1px solid var(--border-light);background:var(--bg);display:none}
.ib-body.op{display:block}
.ndot{width:7px;height:7px;border-radius:50%;background:var(--danger);flex-shrink:0}
.oq{font-size:12px;color:var(--text-2);border-left:2px solid var(--border);padding-left:9px;margin-bottom:.75rem;line-height:1.6;font-style:italic}
.rw-box{border:1px solid var(--accent-border);border-radius:var(--radius-sm);overflow:hidden;margin-bottom:.75rem}
.rw-hdr{padding:.5rem .875rem;background:var(--accent-light);font-size:12px;color:var(--accent);font-weight:500}
.rw-body{padding:.75rem .875rem}

/* HISTORY */
.mr{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:.75rem}
.mc{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:.85rem}
.mv{font-size:22px;font-weight:600;color:var(--text);font-family:'DM Mono',monospace}
.ml{font-size:11.5px;color:var(--text-3);margin-top:3px}
.hi{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);padding:.8rem;margin-bottom:6px}
.hh{display:flex;align-items:center;gap:6px;margin-bottom:4px;flex-wrap:wrap}
.es{color:var(--text-3);font-size:13px;font-style:italic;padding:.5rem 0}
.tr-btn{display:inline-flex;align-items:center;gap:6px;padding:6px 13px;border-radius:var(--radius-sm);background:var(--accent-light);color:var(--accent);border:1px solid var(--accent-border);font-size:12.5px;font-weight:500}
.tr-btn:hover{background:#d1eadb}
.notif{position:fixed;bottom:20px;right:20px;background:var(--text);color:#fff;padding:10px 16px;border-radius:var(--radius);font-size:13px;display:none;align-items:center;gap:7px;box-shadow:var(--shadow-md);z-index:999}
.notif.show{display:flex}
.save-bar{display:flex;align-items:center;gap:8px;padding:.75rem 0 0;border-top:1px solid var(--border-light);margin-top:.75rem}

/* API STATUS */
.api-status{display:flex;align-items:center;gap:6px;font-size:12px;font-family:'DM Mono',monospace}
.api-dot{width:7px;height:7px;border-radius:50%;background:var(--text-3)}
.api-dot.ok{background:var(--accent)}
.api-dot.err{background:var(--danger)}
</style>
</head>
<body>
<div class="app">

<!-- SIDEBAR -->
<nav class="sb">
  <div class="sb-logo">
    <div class="sb-logo-name">Social AI</div>
    <div class="sb-logo-sub">v5 · backend mode</div>
  </div>
  <div class="sb-sec">Marki</div>
  <button class="sb-btn on" onclick="selBrand('winter',this)"><span class="dot" style="background:var(--dw)"></span>Zimowa Akademia</button>
  <button class="sb-btn" onclick="selBrand('3x3',this)"><span class="dot" style="background:var(--d3)"></span>3x3 Koszykówka</button>
  <button class="sb-btn" onclick="selBrand('bdb',this)"><span class="dot" style="background:var(--db)"></span>bdb event</button>
  <div class="sb-sec" style="margin-top:.5rem">Narzędzia</div>
  <button class="sb-btn on" id="nav-gen" onclick="selView('gen',this)"><i class="ti ti-wand"></i> Generator postów</button>
  <button class="sb-btn" id="nav-learn" onclick="selView('learn',this)"><i class="ti ti-brain"></i> Uczenie agenta</button>
  <button class="sb-btn" id="nav-events" onclick="selView('events',this)"><i class="ti ti-calendar-plus"></i> Baza eventów</button>
  <button class="sb-btn" id="nav-kb" onclick="selView('kb',this)"><i class="ti ti-database"></i> Baza wiedzy</button>
  <button class="sb-btn" id="nav-hist" onclick="selView('hist',this)"><i class="ti ti-history"></i> Historia</button>
  <button class="sb-btn" id="nav-inbox" onclick="selBrand('bdb',document.querySelectorAll('.sb-btn')[2]);selView('inbox',this)">
    <i class="ti ti-inbox"></i> Skrzynka bdb
    <span class="badge-count" id="inbox-bc" style="display:none">0</span>
  </button>
</nav>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:9px">
      <span id="top-badge" class="badge bw">Zimowa Akademia</span>
      <span id="top-view" style="font-size:12.5px;color:var(--text-3)">Generator postów</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px">
      <div class="api-status"><span class="api-dot" id="api-dot"></span><span id="api-txt">Sprawdzam backend...</span></div>
      <span style="font-size:12px;color:var(--text-3);font-family:'DM Mono',monospace" id="td"></span>
    </div>
  </div>

  <!-- GENERATOR -->
  <div id="v-gen" class="view on">
    <div class="card">
      <div class="card-title"><i class="ti ti-wand"></i> Ustawienia posta</div>
      <div class="r2">
        <div class="fg" style="margin:0">
          <label>Cel kampanii</label>
          <select id="goal-sel" onchange="onGoalChange()">
            <option value="promocja">Promocja eventu</option>
            <option value="informacje">Informacje o evencie</option>
            <option value="wspomnienia">Wspomnienia z eventu</option>
          </select>
        </div>
        <div class="fg" style="margin:0">
          <label>Format treści</label>
          <select id="fmt-sel" onchange="onFmtChange()">
            <option value="social">Post social media</option>
            <option value="blog">Wpis na bloga</option>
          </select>
        </div>
      </div>
      <div id="soc-opts" style="margin-bottom:9px">
        <label style="font-size:11.5px;color:var(--text-2);font-weight:500;display:block;margin-bottom:5px">Platformy</label>
        <div style="display:flex;gap:14px">
          <label style="display:flex;align-items:center;gap:5px;font-size:13px;cursor:pointer"><input type="checkbox" id="chk-fb" checked> Facebook</label>
          <label style="display:flex;align-items:center;gap:5px;font-size:13px;cursor:pointer"><input type="checkbox" id="chk-ig" checked> Instagram</label>
        </div>
      </div>
      <div id="blog-opts" style="display:none;margin-bottom:9px">
        <label style="font-size:11.5px;color:var(--text-2);font-weight:500;display:block;margin-bottom:5px">Posty promujące wpis</label>
        <div style="display:flex;gap:14px">
          <label style="display:flex;align-items:center;gap:5px;font-size:13px;cursor:pointer"><input type="checkbox" id="chk-bfb" checked> Facebook</label>
          <label style="display:flex;align-items:center;gap:5px;font-size:13px;cursor:pointer"><input type="checkbox" id="chk-big" checked> Instagram</label>
        </div>
      </div>
      <div class="fg">
        <label>Wybierz event z bazy</label>
        <select id="ev-sel" onchange="onEvSel()"><option value="">— brak / wpisz temat ręcznie —</option></select>
      </div>
      <div class="evp" id="evp"></div>
      <div id="cnt-row" style="display:none;margin-bottom:9px"></div>
      <div class="fg">
        <label>Dodatkowy kontekst / wskazówki</label>
        <textarea id="topic-in" rows="2" placeholder="Np. podkreśl nagrodę główną..."></textarea>
      </div>
      <div style="display:flex;gap:7px">
        <button class="btn pr" id="gen-btn" onclick="genPost()"><i class="ti ti-sparkles"></i> Generuj</button>
        <button class="btn" onclick="clearGen()">Wyczyść</button>
      </div>
    </div>

    <div class="card" id="res-card" style="display:none">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:6px;margin-bottom:.75rem">
        <div class="card-title" style="margin:0">Wygenerowany content</div>
        <div class="ptabs" id="p-tabs" style="margin:0"></div>
      </div>
      <div id="res-cont"></div>
      <div class="arow">
        <span style="font-size:11.5px;color:var(--text-3);align-self:center">Popraw:</span>
        <button class="btn" onclick="refine('casual')">Luźniejszy ton</button>
        <button class="btn" onclick="refine('short')">Skróć</button>
        <button class="btn" onclick="refine('emoji')">Dodaj emoji</button>
        <button class="btn" onclick="copyPost()" style="margin-left:auto"><i class="ti ti-copy"></i> Kopiuj</button>
      </div>
      <div id="tr-row" style="display:none">
        <div class="sep"></div>
        <div style="display:flex;align-items:center;gap:9px;flex-wrap:wrap">
          <span style="font-size:12.5px;color:var(--text-2)">Przekaż do bdb event:</span>
          <button class="tr-btn" onclick="transferToBdb()"><i class="ti ti-send"></i> Przenieś – wersja organizatorska</button>
          <span id="tr-ok" style="font-size:12px;color:var(--accent);display:none"><i class="ti ti-check"></i> Wysłano</span>
        </div>
      </div>
      <div class="sep"></div>
      <div class="fb-bar">
        <div style="font-size:13px;font-weight:500;color:var(--text);margin-bottom:7px"><i class="ti ti-message-circle" style="color:var(--text-3)"></i> Oceń post – agent się uczy</div>
        <div class="stars">
          <button class="star" onclick="setStar(1)" aria-label="1">★</button><button class="star" onclick="setStar(2)" aria-label="2">★</button><button class="star" onclick="setStar(3)" aria-label="3">★</button><button class="star" onclick="setStar(4)" aria-label="4">★</button><button class="star" onclick="setStar(5)" aria-label="5">★</button>
        </div>
        <div class="fbtags">
          <button class="fbt" onclick="togFbt(this,'dobry ton')">Dobry ton</button>
          <button class="fbt" onclick="togFbt(this,'za długi')">Za długi</button>
          <button class="fbt" onclick="togFbt(this,'za krótki')">Za krótki</button>
          <button class="fbt" onclick="togFbt(this,'brak CTA')">Brak CTA</button>
          <button class="fbt" onclick="togFbt(this,'świetne emoji')">Świetne emoji</button>
          <button class="fbt" onclick="togFbt(this,'zły ton marki')">Zły ton marki</button>
          <button class="fbt" onclick="togFbt(this,'kreatywny')">Kreatywny</button>
          <button class="fbt" onclick="togFbt(this,'za ogólny')">Za ogólny</button>
        </div>
        <textarea id="fb-note" rows="2" placeholder="Notatka dla agenta..."></textarea>
        <div style="display:flex;align-items:center;gap:8px;margin-top:7px">
          <button class="btn pr" onclick="saveFb()" id="fb-btn">Zapisz feedback</button>
          <span id="fb-ok" style="font-size:12px;color:var(--accent);display:none"><i class="ti ti-check"></i> Zapisano</span>
        </div>
      </div>
    </div>
  </div>

  <!-- UCZENIE -->
  <div id="v-learn" class="view">
    <div class="card">
      <div class="card-title"><i class="ti ti-brain"></i> Szybkie uczenie agenta</div>
      <div style="font-size:13px;color:var(--text-2);margin-bottom:.75rem;line-height:1.7">
        Agent wygeneruje <strong>10 różnych postów</strong> w różnych stylach. Oceń każdy jako <strong style="color:var(--accent)">Dobry</strong> lub <strong style="color:var(--danger)">Do poprawy</strong> i opisz co zmienić. Agent zapamiętuje wszystkie oceny.
      </div>
      <div class="fg">
        <label>Temat / kontekst (opcjonalnie)</label>
        <textarea id="learn-topic" rows="2" placeholder="Np. promocja turnieju, post wizerunkowy, relacja z eventu..."></textarea>
      </div>
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
        <button class="btn pr" id="learn-btn" onclick="startLearning()"><i class="ti ti-player-play"></i> Generuj 10 postów do oceny</button>
        <span id="learn-prog-txt" style="font-size:12px;color:var(--text-3)"></span>
      </div>
      <div class="prog" id="learn-prog"><div class="prog-fill" id="learn-fill" style="width:0%"></div></div>
    </div>
    <div id="learn-list"></div>
    <div id="learn-summary" style="display:none"></div>
  </div>

  <!-- EVENTY -->
  <div id="v-events" class="view">
    <div class="card">
      <div class="card-title"><i class="ti ti-calendar-plus"></i> Dodaj nowy event</div>
      <div class="r2">
        <div class="fg" style="margin:0"><label>Marka</label>
          <select id="ev-brand"><option value="winter">Zimowa Akademia</option><option value="3x3">3x3 Koszykówka</option><option value="bdb">bdb event</option></select>
        </div>
        <div class="fg" style="margin:0"><label>Data eventu</label><input type="date" id="ev-date"></div>
      </div>
      <div class="fg"><label>Nazwa eventu</label><input type="text" id="ev-name" placeholder="Np. Turniej 3x3 Wisła – edycja letnia"></div>
      <div class="fg"><label>Lokalizacja</label><input type="text" id="ev-loc" placeholder="Np. Wisła, amfiteatr miejski"></div>
      <div class="fg"><label>Szczegóły dla AI (nagrody, atrakcje, limity, cennik...)</label>
        <textarea id="ev-desc" rows="3" placeholder="Np. Pula nagród 5000 zł, wstęp wolny, 16 drużyn, food trucki..."></textarea>
      </div>
      <button class="btn pr" onclick="addEvent()"><i class="ti ti-plus"></i> Zapisz event</button>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> Zapisane eventy</div>
      <div style="display:flex;gap:5px;margin-bottom:.75rem;flex-wrap:wrap">
        <button class="tab on" onclick="filterEv('all',this)">Wszystkie</button>
        <button class="tab" onclick="filterEv('winter',this)"><span class="dot" style="background:var(--dw);margin-right:3px"></span>Zimowa</button>
        <button class="tab" onclick="filterEv('3x3',this)"><span class="dot" style="background:var(--d3);margin-right:3px"></span>3x3</button>
        <button class="tab" onclick="filterEv('bdb',this)"><span class="dot" style="background:var(--db);margin-right:3px"></span>bdb</button>
      </div>
      <div id="ev-list"><div class="es">Brak eventów.</div></div>
    </div>
  </div>

  <!-- BAZA WIEDZY -->
  <div id="v-kb" class="view">
    <div class="kb-wrap">
      <div class="kb-cats" id="kb-cats"></div>
      <div class="kb-ed" id="kb-ed" style="flex:1;min-width:0"></div>
    </div>
    <div class="save-bar">
      <button class="btn pr" onclick="saveKb()"><i class="ti ti-device-floppy"></i> Zapisz bazę wiedzy</button>
      <button class="btn" onclick="resetKbCat()"><i class="ti ti-refresh"></i> Przywróć domyślne</button>
      <span id="kb-ok" style="font-size:12px;color:var(--accent);display:none"><i class="ti ti-check"></i> Zapisano</span>
    </div>
  </div>

  <!-- HISTORIA -->
  <div id="v-hist" class="view">
    <div class="mr">
      <div class="mc"><div class="mv" id="st-p">0</div><div class="ml">Wygenerowanych postów</div></div>
      <div class="mc"><div class="mv" id="st-a">–</div><div class="ml">Średnia ocena</div></div>
      <div class="mc"><div class="mv" id="st-f">0</div><div class="ml">Feedbacków</div></div>
    </div>
    <div class="card"><div class="card-title"><i class="ti ti-history"></i> Historia postów</div><div id="hist-list"><div class="es">Brak historii.</div></div></div>
  </div>

  <!-- INBOX BDB -->
  <div id="v-inbox" class="view">
    <div class="card">
      <div class="card-title"><i class="ti ti-inbox"></i> Skrzynka bdb event</div>
      <div style="font-size:13px;color:var(--text-2);margin-bottom:.75rem">Posty z Zimowej i 3x3 – przepisz na język organizatora / B2B.</div>
      <div id="inbox-list"><div class="es">Skrzynka pusta.</div></div>
    </div>
  </div>
</div>
</div>

<div class="notif" id="notif"><i class="ti ti-check"></i><span id="notif-txt">OK</span></div>

<script>
// ─── KONFIGURACJA ───────────────────────────────────────────
// Adres backendu – zmień na swój serwer gdy wdrażasz produkcyjnie
const API_BASE = window.location.origin;  // automatycznie ten sam host

// ─── STAŁE MARKI ────────────────────────────────────────────
const BRAND_NAMES = { winter:'Zimowa Akademia','3x3':'3x3 Koszykówka',bdb:'bdb event' };
const BRAND_BADGES = { winter:'bw','3x3':'b3',bdb:'bb' };
const BRAND_DOTS = { winter:'var(--dw)','3x3':'var(--d3)',bdb:'var(--db)' };
const GOALS = {
  promocja:    { name:'Promocja eventu',      cta_fb:'Kliknij w link i zapisz się!',           cta_ig:'Zapisz się przez link w bio!',  blog:'zachęcający do udziału z jasnym CTA' },
  informacje:  { name:'Informacje o evencie', cta_fb:'Masz pytania? Zostaw komentarz!',         cta_ig:'Szczegóły – link w bio.',        blog:'informacyjny i edukacyjny' },
  wspomnienia: { name:'Wspomnienia z eventu', cta_fb:'Podziel się wspomnieniami w komentarzu!', cta_ig:'Oznacz znajomych którzy byli!', blog:'nostalgiczny, opisujący atmosferę' }
};

const KB_CATS = [
  {id:'identity',label:'Tożsamość marki',icon:'ti-building'},
  {id:'tone',label:'Ton głosu (ToV)',icon:'ti-message-dots'},
  {id:'audience',label:'Grupy docelowe',icon:'ti-users'},
  {id:'offer',label:'Oferta i USP',icon:'ti-list-check'},
  {id:'keywords',label:'Słowa kluczowe',icon:'ti-hash'}
];
const KB_FIELDS = {
  identity:[{k:'name',l:'Nazwa marki',t:'input'},{k:'tagline',l:'Tagline / slogan',t:'input'},{k:'mission',l:'Misja i opis (bazowy kontekst AI)',t:'ta',r:4}],
  tone:[{k:'main',l:'Główny ton głosu',t:'ta',r:2},{k:'examples',l:'Przykładowe frazy',t:'ta',r:3},{k:'forbidden',l:'Czego AI nie może pisać',t:'ta',r:2}],
  audience:[{k:'primary',l:'Główna grupa docelowa',t:'ta',r:2},{k:'secondary',l:'Grupy dodatkowe',t:'ta',r:2},{k:'geo',l:'Lokalizacje i zasięg',t:'input'}],
  offer:[{k:'services',l:'Lista usług',t:'ta',r:4},{k:'usp',l:'Główny wyróżnik (USP)',t:'ta',r:2},{k:'pricing',l:'Model cenowy',t:'ta',r:2}],
  keywords:[{k:'must',l:'Słowa must-use',t:'tags',c:'tg-b'},{k:'hashtags',l:'Hashtagi',t:'tags',c:'tg-g'},{k:'forbidden_words',l:'Słowa zakazane',t:'tags',c:'tg-r'}]
};
const KB_DEF = {
  winter:{identity:{name:'Zimowa Akademia',tagline:'Mobilna skocznia narciarska dla każdego',mission:'Przybliżamy emocje sportów zimowych przez bezpieczne, mobilne skocznie narciarskie na eventach w całej Polsce.'},tone:{main:'Ekscytujący, rodzinny, bezpieczny, zimowy',examples:'Poczuj dreszczyk emocji! / Zimowa przygoda czeka!',forbidden:'Nie strasz trudnością, unikaj słowa "ryzyko"'},audience:{primary:'Gminy i samorządy organizujące eventy rodzinne',secondary:'Szkoły, organizatorzy eventów, rodzice z dziećmi 5-15 lat',geo:'Cała Polska, szczególnie małe i średnie miasta'},offer:{services:'Mobilna skocznia narciarska na wynajem\nPokazy narciarskie\nEdukacja sportów zimowych',usp:'Jedyna mobilna skocznia narciarska dostępna przez cały rok',pricing:'Wycena indywidualna, minimum 4h wynajmu'},keywords:{must:'zimowa, skocznia, śnieg, przygoda, rodzina, emocje',hashtags:'#ZimowaAkademia, #SkoczniaNarciarska, #SportDlaWszystkich, #FamilyFun',forbidden_words:'ryzyko, trudne, wyczynowe'}},
  '3x3':{identity:{name:'3x3 Koszykówka',tagline:'Streetball na najwyższym poziomie',mission:'Organizujemy dynamiczne turnieje 3x3 łącząc lokalne społeczności przez sport uliczny.'},tone:{main:'Dynamiczny, młodzieżowy, hip-hopowy, streetwearowy',examples:'Jesteś gotowy?! / Real ballers show up',forbidden:'Unikaj korporacyjnego języka, nie pisz "zapraszamy uprzejmie"'},audience:{primary:'Młodzi koszykarze 16-30 lat',secondary:'Kibice streetballu, sponsorzy lokalni',geo:'Wisła, Kołobrzeg, Bielsko-Biała'},offer:{services:'Turnieje 3x3\nEventy streetball\nStrefa kibica z DJ',usp:'Jedyne turnieje 3x3 łączące sport z kulturą uliczną',pricing:'Wstęp wolny dla kibiców, opłata startowa dla drużyn'},keywords:{must:'3x3, streetball, turniej, ballers, rywalizacja',hashtags:'#3x3Basketball, #Streetball, #3x3Polska, #HoopLife',forbidden_words:'nudne, formalne, zapraszamy uprzejmie'}},
  bdb:{identity:{name:'bdb event',tagline:'Tworzymy z pasją',mission:'Agencja eventowa z Cieszyna tworząca kompleksowe doświadczenia sportowe dla samorządów i firm.'},tone:{main:'Profesjonalny, kreatywny, biznesowy, case-study',examples:'Zrealizowaliśmy ponad 50 eventów / Kompleksowa obsługa od A do Z',forbidden:'Unikaj pustych frazesów, zawsze podawaj liczby'},audience:{primary:'Samorządy i gminy szukające organizatorów eventów',secondary:'Sponsorzy korporacyjni, marki sportowe',geo:'Ogólnopolski zasięg, headquarter w Cieszynie'},offer:{services:'Organizacja imprez sportowych (Plaża Open, Beskidzka Plaża)\nWynajem sprzętu eventowego\nObsługa i zabezpieczenie imprez\nTransport eventowy\nProdukcja odzieży eventowej',usp:'Jedyna agencja łącząca eventy z własną produkcją odzieży i logistyką',pricing:'Oferty B2B, wycena projektowa'},keywords:{must:'pasja, profesjonalizm, skala, B2B, event, case study',hashtags:'#bdbEvent, #TwórzymyZPasją, #EventMarketing, #Cieszyn',forbidden_words:'najtańsi, rewolucyjni, najlepsi bez uzasadnienia'}}
};

// ─── STATE & LOCALSTORAGE ────────────────────────────────────
function lsGet(k,d){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d;}catch(e){return d;}}
function lsSet(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}

let DATA = {
  events:      lsGet('sa5_events',[]),
  feedbacks:   lsGet('sa5_feedbacks',[]),
  postHistory: lsGet('sa5_history',[]),
  inbox:       lsGet('sa5_inbox',[]),
  kb:          lsGet('sa5_kb',JSON.parse(JSON.stringify(KB_DEF)))
};
function save(key){const map={events:'sa5_events',feedbacks:'sa5_feedbacks',postHistory:'sa5_history',inbox:'sa5_inbox',kb:'sa5_kb'};lsSet(map[key],DATA[key]);}

function showNotif(msg){const n=document.getElementById('notif');document.getElementById('notif-txt').textContent=msg;n.classList.add('show');clearTimeout(window._nt);window._nt=setTimeout(()=>n.classList.remove('show'),2200);}

// ─── NAWIGACJA ───────────────────────────────────────────────
let curBrand='winter',curView='gen',curPlat='facebook',isBlog=false;
let curStar=0,selFbTags=[],genData=null,curEvId=null,curKbCat='identity';

document.getElementById('td').textContent=new Date().toLocaleDateString('pl-PL',{day:'numeric',month:'long',year:'numeric'});

function selBrand(b,btn){
  curBrand=b;
  document.querySelectorAll('.sb-btn').forEach(x=>{if(['Zimowa','3x3','bdb'].some(s=>x.textContent.includes(s)))x.classList.remove('on');});
  btn.classList.add('on');
  document.getElementById('top-badge').textContent=BRAND_NAMES[b];
  document.getElementById('top-badge').className='badge '+BRAND_BADGES[b];
  genData=null;document.getElementById('res-card').style.display='none';
  document.getElementById('tr-row').style.display='none';
  refreshEvSel();if(curView==='kb')renderKb();
}

function selView(v,btn){
  curView=v;
  document.querySelectorAll('.sb-btn').forEach(x=>x.classList.remove('on'));
  if(btn)btn.classList.add('on');
  ['gen','learn','events','kb','hist','inbox'].forEach(id=>{const el=document.getElementById('v-'+id);if(el){el.style.display=id===v?'flex':'none';el.classList.toggle('on',id===v);}});
  const labels={gen:'Generator postów',learn:'Uczenie agenta',events:'Baza eventów',kb:'Baza wiedzy',hist:'Historia',inbox:'Skrzynka bdb event'};
  document.getElementById('top-view').textContent=labels[v]||'';
  if(v==='hist')renderHist();if(v==='events')renderEvList();if(v==='kb')renderKb();if(v==='inbox')renderInbox();
}

// ─── API CALL – przez backend ────────────────────────────────
async function callAPI(prompt, maxTokens=1200){
  const r=await fetch(`${API_BASE}/api/generate`,{
    method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({prompt,max_tokens:maxTokens})
  });
  if(!r.ok){const err=await r.json();throw new Error(err.detail||'Błąd serwera');}
  const d=await r.json();
  return JSON.parse(d.content.replace(/```json|```/g,'').trim());
}

async function callAPIRaw(prompt, maxTokens=600){
  const r=await fetch(`${API_BASE}/api/generate`,{
    method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({prompt,max_tokens:maxTokens})
  });
  if(!r.ok){const err=await r.json();throw new Error(err.detail||'Błąd serwera');}
  const d=await r.json();
  return d.content.trim();
}

// ─── HEALTH CHECK ────────────────────────────────────────────
async function checkHealth(){
  try{
    const r=await fetch(`${API_BASE}/api/health`);
    const d=await r.json();
    const dot=document.getElementById('api-dot'),txt=document.getElementById('api-txt');
    if(d.api_key_set){dot.className='api-dot ok';txt.textContent='Backend OK · '+d.api_key_preview;}
    else{dot.className='api-dot err';txt.textContent='Brak klucza API!';}
  }catch(e){
    document.getElementById('api-dot').className='api-dot err';
    document.getElementById('api-txt').textContent='Backend niedostępny';
  }
}
checkHealth();

// ─── GENERATOR UTILS ─────────────────────────────────────────
function onGoalChange(){const ph={promocja:'Np. podkreśl nagrodę, limit miejsc...',informacje:'Np. harmonogram, zasady uczestnictwa...',wspomnienia:'Np. wspomnij zwycięzców, frekwencję...'};document.getElementById('topic-in').placeholder=ph[document.getElementById('goal-sel').value]||'';}
function onFmtChange(){isBlog=document.getElementById('fmt-sel').value==='blog';document.getElementById('soc-opts').style.display=isBlog?'none':'block';document.getElementById('blog-opts').style.display=isBlog?'block':'none';}

function daysTo(ds){if(!ds)return null;const ev=new Date(ds+'T00:00:00'),now=new Date();now.setHours(0,0,0,0);return Math.ceil((ev-now)/86400000);}
function cntBadge(d){
  if(d===null)return'';
  if(d<0)return`<span class="cnt cnt-gone"><i class="ti ti-calendar-off"></i> Event minął ${Math.abs(d)} dni temu</span>`;
  if(d===0)return`<span class="cnt cnt-hot"><i class="ti ti-flame"></i> DZIŚ – event trwa!</span>`;
  if(d===1)return`<span class="cnt cnt-hot"><i class="ti ti-alarm"></i> JUTRO!</span>`;
  if(d<=3)return`<span class="cnt cnt-hot"><i class="ti ti-clock"></i> Zostały tylko ${d} dni!</span>`;
  if(d<=14)return`<span class="cnt cnt-warn"><i class="ti ti-calendar"></i> Za ${d} dni</span>`;
  return`<span class="cnt cnt-ok"><i class="ti ti-calendar"></i> Za ${d} dni</span>`;
}
function cntCtx(ev){
  if(!ev||!ev.date)return'';const d=daysTo(ev.date);if(d===null)return'';
  if(d<0)return`\nCzas: Event odbył się ${Math.abs(d)} dni temu – pisz z perspektywy wspomnień.`;
  if(d===0)return`\nCzas: Event DZIŚ – pisz w czasie teraźniejszym, wzbudzaj FOMO!`;
  if(d===1)return`\nCzas: Event JUTRO – buduj napięcie, CTA: ostatnia szansa!`;
  if(d<=3)return`\nCzas: Do eventu tylko ${d} dni – wyraź pilność, wpleć "tylko ${d} dni!"`;
  if(d<=7)return`\nCzas: Za ${d} dni – buduj oczekiwanie i zachęcaj do zapisów.`;
  return`\nCzas: Za ${d} dni – promuj i informuj.`;
}

function onEvSel(){
  const id=parseInt(document.getElementById('ev-sel').value)||0;curEvId=id||null;
  const prev=document.getElementById('evp'),cntRow=document.getElementById('cnt-row');
  if(!id){prev.style.display='none';cntRow.style.display='none';return;}
  const ev=DATA.events.find(e=>e.id===id);if(!ev){prev.style.display='none';cntRow.style.display='none';return;}
  const dStr=ev.date?new Date(ev.date+'T00:00:00').toLocaleDateString('pl-PL',{day:'numeric',month:'long',year:'numeric'}):'';
  prev.style.display='block';prev.innerHTML=`<strong>${ev.name}</strong>${dStr?' · '+dStr:''}${ev.loc?' · '+ev.loc:''}${ev.desc?`<br><span style="font-size:11.5px">${ev.desc}</span>`:''}`;
  const days=ev.date?daysTo(ev.date):null;
  if(days!==null){cntRow.style.display='block';cntRow.innerHTML=cntBadge(days);}else cntRow.style.display='none';
}

function refreshEvSel(){
  const sel=document.getElementById('ev-sel');sel.innerHTML='<option value="">— brak / wpisz temat ręcznie —</option>';
  DATA.events.filter(e=>e.brand===curBrand).forEach(e=>{const opt=document.createElement('option');opt.value=e.id;const dStr=e.date?new Date(e.date+'T00:00:00').toLocaleDateString('pl-PL',{day:'numeric',month:'short'}):'';opt.textContent=(dStr?dStr+' – ':'')+e.name+(e.loc?' ('+e.loc+')':'');sel.appendChild(opt);});
  document.getElementById('evp').style.display='none';document.getElementById('cnt-row').style.display='none';curEvId=null;
}

function buildKbPrompt(brand){
  const kb=DATA.kb[brand]||KB_DEF[brand];
  return`PROFIL MARKI Z BAZY WIEDZY:
Marka: ${kb.identity?.name||BRAND_NAMES[brand]}
Tagline: ${kb.identity?.tagline||''}
Misja: ${kb.identity?.mission||''}
Ton głosu: ${kb.tone?.main||''}
Przykładowe frazy: ${kb.tone?.examples||''}
ZAKAZANE (ton): ${kb.tone?.forbidden||''}
Główna grupa: ${kb.audience?.primary||''}
Grupy dodatkowe: ${kb.audience?.secondary||''}
Zasięg: ${kb.audience?.geo||''}
Usługi: ${kb.offer?.services||''}
USP: ${kb.offer?.usp||''}
Cennik: ${kb.offer?.pricing||''}
Słowa kluczowe (używaj): ${kb.keywords?.must||''}
Hashtagi: ${kb.keywords?.hashtags||''}
Słowa zakazane: ${kb.keywords?.forbidden_words||''}`;
}

function buildFbCtx(brand){
  const bf=DATA.feedbacks.filter(f=>f.brand===brand);if(!bf.length)return'';
  const avg=(bf.reduce((s,f)=>s+(f.stars||0),0)/bf.length).toFixed(1);
  const tc={};bf.flatMap(f=>f.tags||[]).forEach(t=>{tc[t]=(tc[t]||0)+1;});
  const top=Object.entries(tc).sort((a,b)=>b[1]-a[1]).slice(0,5).map(([t])=>t);
  const notes=bf.filter(f=>f.note).map(f=>'• '+f.note).join('\n');
  return`\n\nPREFERENCJE WYUCZONE Z FEEDBACKU (zastosuj bezwzględnie):\n- Średnia ocena: ${avg}/5\n- Najczęstsze uwagi: ${top.join(', ')}\n${notes?'- Notatki:\n'+notes:''}`;
}

function evCtxStr(ev){
  if(!ev)return'';
  const dStr=ev.date?new Date(ev.date+'T00:00:00').toLocaleDateString('pl-PL',{day:'numeric',month:'long',year:'numeric'}):'';
  return`\n\nDANE EVENTU:\nNazwa: ${ev.name}\n${dStr?'Data: '+dStr+'\n':''}${ev.loc?'Lokalizacja: '+ev.loc+'\n':''}${ev.desc?'Szczegóły: '+ev.desc:''}${cntCtx(ev)}`;
}

// ─── GENERATOR ───────────────────────────────────────────────
async function genPost(){
  const ev=curEvId?DATA.events.find(e=>e.id===curEvId):null;
  const goal=GOALS[document.getElementById('goal-sel').value];
  const topic=document.getElementById('topic-in').value.trim();
  const btn=document.getElementById('gen-btn');
  btn.disabled=true;btn.innerHTML='<span class="spin"></span> Generuję...';
  const base=`Jesteś profesjonalnym agentem social media.\n${buildKbPrompt(curBrand)}${evCtxStr(ev)}${buildFbCtx(curBrand)}\nCel: ${goal.name}\n${topic?'Wskazówki: '+topic:''}`;
  try{
    let parsed;
    if(isBlog){
      const bfb=document.getElementById('chk-bfb').checked,big=document.getElementById('chk-big').checked;
      const p=`${base}\n\nNapisz wpis blogowy (min 400 słów): tytuł, wstęp, 3+ sekcje, CTA.${bfb||big?`\nDodatkowo posty promujące:${bfb?'\n- Facebook CTA: '+goal.cta_fb:''}${big?'\n- Instagram bez hashtagów CTA: '+goal.cta_ig:''}`:''}\n\nOdpowiedz TYLKO samym JSON:\n{"blog":"pełny wpis"${bfb?',"facebook":"post FB"':''}${big?',"instagram":"post IG"':''}}`;
      parsed=await callAPI(p,2000);
    }else{
      const fb=document.getElementById('chk-fb').checked,ig=document.getElementById('chk-ig').checked;
      if(!fb&&!ig){btn.disabled=false;btn.innerHTML='<i class="ti ti-sparkles"></i> Generuj';return;}
      const p=`${base}\n\nOdpowiedz TYLKO samym JSON:\n{${fb?`"facebook":"post FB z CTA: ${goal.cta_fb}"`:''}${fb&&ig?',':''}${ig?`"instagram":"post IG bez hashtagów z CTA: ${goal.cta_ig}"`:''}}`;
      parsed=await callAPI(p,1000);
    }
    genData=parsed;renderGenResult();
    const ev2=curEvId?DATA.events.find(e=>e.id===curEvId):null;
    DATA.postHistory.unshift({id:Date.now(),brand:curBrand,brandName:BRAND_NAMES[curBrand],badge:BRAND_BADGES[curBrand],eventName:ev2?ev2.name:null,goal:goal.name,isBlog,text:parsed.blog||parsed.facebook||'',stars:0,tags:[],note:'',date:new Date().toLocaleDateString('pl-PL')});
    save('postHistory');updateStats();
  }catch(e){
    document.getElementById('res-cont').innerHTML=`<div class="rbox" style="color:var(--danger)">Błąd: ${e.message}</div>`;
    document.getElementById('res-card').style.display='block';
  }
  btn.disabled=false;btn.innerHTML='<i class="ti ti-sparkles"></i> Generuj';
}

function renderGenResult(){
  const tabs=document.getElementById('p-tabs'),cont=document.getElementById('res-cont');
  tabs.innerHTML='';cont.innerHTML='';
  const order=isBlog?['blog','facebook','instagram']:['facebook','instagram'];
  const labels={blog:'Blog',facebook:'Facebook',instagram:'Instagram'};
  let first=null;
  order.forEach(k=>{
    if(!genData[k])return;if(!first)first=k;
    const b=document.createElement('button');b.className='tab'+(k===first?' on':'');b.textContent=labels[k];b.onclick=()=>swPlat(k,b);tabs.appendChild(b);
    const w=document.createElement('div');w.id='p-'+k;w.className='pc'+(k===first?' on':'');
    const box=document.createElement('div');box.className='rbox';box.id='r-'+k;box.textContent=genData[k];if(k==='blog')box.style.minHeight='200px';
    w.appendChild(box);
    if(k==='instagram'){const h=document.createElement('div');h.className='htags';h.textContent=(DATA.kb[curBrand]?.keywords?.hashtags||KB_DEF[curBrand].keywords.hashtags).replace(/,\s*/g,' ');w.appendChild(h);}
    cont.appendChild(w);
  });
  if(first)curPlat=first;
  document.getElementById('res-card').style.display='block';
  document.getElementById('tr-row').style.display=curBrand!=='bdb'?'block':'none';
  document.getElementById('tr-ok').style.display='none';
  resetFb();
}

function swPlat(p,btn){curPlat=p;document.querySelectorAll('.pc').forEach(x=>x.classList.remove('on'));document.querySelectorAll('#p-tabs .tab').forEach(x=>x.classList.remove('on'));const el=document.getElementById('p-'+p);if(el)el.classList.add('on');if(btn)btn.classList.add('on');}
function copyPost(){const el=document.getElementById('r-'+curPlat);if(el&&navigator.clipboard){navigator.clipboard.writeText(el.textContent);showNotif('Skopiowano!');}}
function clearGen(){document.getElementById('topic-in').value='';document.getElementById('ev-sel').value='';document.getElementById('evp').style.display='none';document.getElementById('cnt-row').style.display='none';document.getElementById('res-card').style.display='none';genData=null;curEvId=null;}

async function refine(type){
  if(!genData)return;const el=document.getElementById('r-'+curPlat);if(!el)return;const txt=el.textContent;if(!txt)return;
  const blog=curPlat==='blog';
  const instr={casual:'Przepisz luźniejszym tonem. Zachowaj sens i CTA.',short:blog?'Skróć o 1/3, zachowaj nagłówki i kluczowe fakty.':'Skróć o połowę. Zachowaj CTA.',emoji:blog?'Dodaj 1 emoji przy każdym nagłówku.':'Dodaj 4-5 emoji w naturalnych miejscach.'};
  document.querySelectorAll('.btn').forEach(b=>b.disabled=true);
  try{const refined=await callAPIRaw(instr[type]+'\n\nTekst:\n'+txt,blog?1500:600);el.textContent=refined;genData[curPlat]=refined;}catch(e){}
  document.querySelectorAll('.btn').forEach(b=>b.disabled=false);
}

function setStar(n){curStar=n;document.querySelectorAll('.star').forEach((s,i)=>s.classList.toggle('on',i<n));}
function togFbt(btn,tag){btn.classList.toggle('on');if(btn.classList.contains('on'))selFbTags.push(tag);else selFbTags=selFbTags.filter(t=>t!==tag);}
function resetFb(){curStar=0;selFbTags=[];document.querySelectorAll('.star').forEach(s=>s.classList.remove('on'));document.querySelectorAll('.fbt').forEach(t=>t.classList.remove('on'));document.getElementById('fb-note').value='';document.getElementById('fb-ok').style.display='none';document.getElementById('fb-btn').disabled=false;}

function saveFb(){
  const note=document.getElementById('fb-note').value.trim();
  if(!curStar&&!selFbTags.length&&!note)return;
  DATA.feedbacks.push({brand:curBrand,stars:curStar,tags:[...selFbTags],note,date:new Date().toLocaleDateString('pl-PL')});
  if(DATA.postHistory.length){DATA.postHistory[0].stars=curStar;DATA.postHistory[0].tags=[...selFbTags];DATA.postHistory[0].note=note;}
  save('feedbacks');save('postHistory');
  document.getElementById('fb-ok').style.display='inline-flex';document.getElementById('fb-btn').disabled=true;
  updateStats();showNotif('Feedback zapisany!');
}

function transferToBdb(){
  if(!genData)return;const ev=curEvId?DATA.events.find(e=>e.id===curEvId):null;
  DATA.inbox.push({id:Date.now(),fromBrand:curBrand,fromName:BRAND_NAMES[curBrand],fromBadge:BRAND_BADGES[curBrand],eventName:ev?ev.name:null,eventData:ev||null,origFb:genData.facebook||'',origIg:genData.instagram||'',origBlog:genData.blog||'',date:new Date().toLocaleDateString('pl-PL'),unread:true,rewritten:null,open:false});
  save('inbox');document.getElementById('tr-ok').style.display='inline-flex';updateInboxBadge();showNotif('Wysłano do skrzynki bdb!');
}

function updateInboxBadge(){const n=DATA.inbox.filter(i=>i.unread).length;const b=document.getElementById('inbox-bc');b.textContent=n;b.style.display=n>0?'inline-block':'none';}
function updateStats(){document.getElementById('st-p').textContent=DATA.postHistory.length;document.getElementById('st-f').textContent=DATA.feedbacks.length;const rated=DATA.feedbacks.filter(f=>f.stars>0);document.getElementById('st-a').textContent=rated.length?(rated.reduce((s,f)=>s+f.stars,0)/rated.length).toFixed(1)+'/5':'–';}

// ─── UCZENIE ─────────────────────────────────────────────────
let learnPosts=[],learnVerdicts={};

async function startLearning(){
  const topic=document.getElementById('learn-topic').value.trim();
  const btn=document.getElementById('learn-btn');
  btn.disabled=true;btn.innerHTML='<span class="spin"></span> Generuję posty...';
  document.getElementById('learn-prog').style.display='block';
  document.getElementById('learn-list').innerHTML='';document.getElementById('learn-summary').style.display='none';document.getElementById('learn-summary').innerHTML='';
  learnPosts=[];learnVerdicts={};
  const kbCtx=buildKbPrompt(curBrand),fbCtx=buildFbCtx(curBrand);
  const goals=['promocja','informacje','wspomnienia'];
  const styles=['krótki i energiczny z emoji','storytellingowy – zacznij od historii','oparty na faktach i liczbach','z pytaniem otwartym do odbiorców','wzbudzający FOMO i pilność','ciepły i rodzinny','dynamiczny z wyliczeniem punktów','humorystyczny i lekki','motywacyjny i inspirujący','bezpośredni – tylko konkrety'];
  for(let i=0;i<10;i++){
    document.getElementById('learn-fill').style.width=((i/10)*100)+'%';
    document.getElementById('learn-prog-txt').textContent=`Post ${i+1}/10...`;
    const goal=GOALS[goals[i%3]],style=styles[i];
    try{
      const p=`Jesteś agentem social media.\n${kbCtx}${fbCtx}\nCel: ${goal.name}\nStyl: ${style}\n${topic?'Temat: '+topic:''}\n\nWygeneruj JEDEN post na Facebook. Odpowiedz TYLKO samym tekstem posta.`;
      const txt=await callAPIRaw(p,500);
      learnPosts.push({id:i,text:txt,goal:goal.name,style});appendLearnCard(i,txt,goal.name,style);
    }catch(e){learnPosts.push({id:i,text:'Błąd generowania.',goal:goal.name,style});appendLearnCard(i,'Błąd generowania.',goal.name,style);}
  }
  document.getElementById('learn-fill').style.width='100%';
  document.getElementById('learn-prog-txt').textContent='✓ Gotowe! Oceń każdy post.';
  btn.disabled=false;btn.innerHTML='<i class="ti ti-refresh"></i> Generuj nowe 10';
}

function appendLearnCard(i,txt,goal,style){
  const list=document.getElementById('learn-list');
  const div=document.createElement('div');div.className='learn-card';div.id='lc-'+i;
  div.innerHTML=`<div class="lc-hdr"><div class="lc-num" id="lcn-${i}">${i+1}</div><div style="flex:1;min-width:0"><div class="lc-meta">${goal} · ${style}</div><div class="lc-txt">${txt}</div></div></div>
  <div class="lc-body"><div class="vrow"><button class="vbtn ok-v" onclick="setVerdict(${i},'ok',this)"><i class="ti ti-thumb-up"></i> Dobry</button><button class="vbtn bad-v" onclick="setVerdict(${i},'bad',this)"><i class="ti ti-thumb-down"></i> Do poprawy</button></div>
  <div id="lc-note-${i}" style="display:none;margin-top:8px"><textarea id="lc-txt-${i}" rows="2" placeholder="Co wymaga poprawy? (np. zbyt formalny, brak CTA, za długi...)" style="font-size:13px;margin-bottom:6px"></textarea><button class="btn pr" onclick="saveLearnVerdict(${i})"><i class="ti ti-check"></i> Zapisz uwagę</button></div>
  <div id="lc-saved-${i}" style="display:none;font-size:12px;color:var(--accent);margin-top:6px"><i class="ti ti-check"></i> Zapisano do pamięci agenta</div></div>`;
  list.appendChild(div);
}

function setVerdict(i,v,btn){
  learnVerdicts[i]=learnVerdicts[i]||{};learnVerdicts[i].verdict=v;
  btn.closest('.vrow').querySelectorAll('.vbtn').forEach(b=>b.classList.remove('sel'));btn.classList.add('sel');
  const num=document.getElementById('lcn-'+i);num.className='lc-num '+(v==='ok'?'ok':'bad');num.textContent=v==='ok'?'✓':'✗';
  document.getElementById('lc-note-'+i).style.display=v==='bad'?'block':'none';
  if(v==='ok'){DATA.feedbacks.push({brand:curBrand,stars:5,tags:['dobry ton','kreatywny'],note:'',date:new Date().toLocaleDateString('pl-PL'),fromLearn:true});save('feedbacks');updateStats();checkLearnDone();}
}

function saveLearnVerdict(i){
  const note=document.getElementById('lc-txt-'+i)?.value.trim()||'';
  DATA.feedbacks.push({brand:curBrand,stars:2,tags:['do poprawy'],note,date:new Date().toLocaleDateString('pl-PL'),fromLearn:true});
  save('feedbacks');updateStats();
  document.getElementById('lc-saved-'+i).style.display='block';
  document.getElementById('lc-note-'+i).style.display='none';
  learnVerdicts[i]=learnVerdicts[i]||{};learnVerdicts[i].note=note;
  checkLearnDone();
}

function checkLearnDone(){const rated=Object.values(learnVerdicts).filter(v=>v.verdict).length;if(rated>=learnPosts.length&&learnPosts.length>0)showLearnSummary();}

function showLearnSummary(){
  const good=Object.values(learnVerdicts).filter(v=>v.verdict==='ok').length;
  const bad=Object.values(learnVerdicts).filter(v=>v.verdict==='bad').length;
  const notes=Object.values(learnVerdicts).filter(v=>v.note).map(v=>v.note);
  const sumDiv=document.getElementById('learn-summary');sumDiv.style.display='block';
  sumDiv.innerHTML=`<div class="card"><div class="card-title"><i class="ti ti-chart-bar"></i> Podsumowanie sesji</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:.875rem">
    <div class="mc" style="border-color:var(--accent-border)"><div class="mv" style="color:var(--accent)">${good}</div><div class="ml">Dobrych postów</div></div>
    <div class="mc" style="border-color:var(--danger-border)"><div class="mv" style="color:var(--danger)">${bad}</div><div class="ml">Do poprawy</div></div>
  </div>
  <div style="font-size:13px;color:var(--text-2);line-height:1.7">Agent zapisał <strong>${good+bad} ocen</strong> dla <strong>${BRAND_NAMES[curBrand]}</strong>. Przy kolejnym generowaniu automatycznie uwzględni Twoje preferencje.
  ${notes.length?`<br><br><strong>Zapisane instrukcje:</strong>${notes.map(n=>`<div style="margin-top:5px;padding:6px 10px;background:var(--bg);border-radius:var(--radius-sm);border:1px solid var(--border);font-style:italic">"${n}"</div>`).join('')}`:''}</div></div>`;
  showNotif(`Zapisano ${good+bad} ocen!`);
}

// ─── EVENTY ──────────────────────────────────────────────────
let evFilter='all';
function filterEv(f,btn){evFilter=f;document.querySelectorAll('#v-events .tab').forEach(x=>x.classList.remove('on'));btn.classList.add('on');renderEvList();}

function addEvent(){
  const name=document.getElementById('ev-name').value.trim();if(!name){document.getElementById('ev-name').focus();return;}
  DATA.events.push({id:Date.now(),brand:document.getElementById('ev-brand').value,name,date:document.getElementById('ev-date').value,loc:document.getElementById('ev-loc').value.trim(),desc:document.getElementById('ev-desc').value.trim()});
  ['ev-name','ev-date','ev-loc','ev-desc'].forEach(id=>document.getElementById(id).value='');
  save('events');renderEvList();refreshEvSel();showNotif('Event zapisany!');
}
function delEvent(id){DATA.events=DATA.events.filter(e=>e.id!==id);save('events');renderEvList();refreshEvSel();}

function renderEvList(){
  const list=document.getElementById('ev-list');
  const filtered=evFilter==='all'?DATA.events:DATA.events.filter(e=>e.brand===evFilter);
  if(!filtered.length){list.innerHTML='<div class="es">Brak eventów.</div>';return;}
  list.innerHTML=filtered.map(e=>{
    const days=e.date?daysTo(e.date):null;
    const dStr=e.date?new Date(e.date+'T00:00:00').toLocaleDateString('pl-PL',{day:'numeric',month:'short',year:'numeric'}):'';
    return`<div class="ev-pill"><span class="dot" style="background:${BRAND_DOTS[e.brand]};margin-top:3px;flex-shrink:0"></span>
    <div style="flex:1;min-width:0"><div class="ep-n">${e.name}</div>
    <div style="display:flex;align-items:center;gap:7px;flex-wrap:wrap;margin-top:3px">${dStr?'<span style="font-size:11.5px;color:var(--text-3)">'+dStr+'</span>':''}${e.loc?'<span style="font-size:11.5px;color:var(--text-3)">· '+e.loc+'</span>':''}${days!==null?cntBadge(days):''}</div>
    ${e.desc?`<div style="font-size:12px;color:var(--text-3);margin-top:3px">${e.desc.substring(0,100)}${e.desc.length>100?'…':''}</div>`:''}</div>
    <button class="ep-del" onclick="delEvent(${e.id})" aria-label="Usuń"><i class="ti ti-trash"></i></button></div>`;
  }).join('');
}

// ─── BAZA WIEDZY ─────────────────────────────────────────────
function renderKb(){
  document.getElementById('kb-cats').innerHTML=KB_CATS.map(c=>`<button class="kb-cat${curKbCat===c.id?' on':''}" onclick="selKbCat('${c.id}')"><i class="ti ${c.icon}"></i><span>${c.label}</span></button>`).join('');
  renderKbFields();
}
function selKbCat(c){curKbCat=c;renderKb();}
function renderKbFields(){
  const ed=document.getElementById('kb-ed');
  if(!DATA.kb[curBrand])DATA.kb[curBrand]=JSON.parse(JSON.stringify(KB_DEF[curBrand]));
  const data=DATA.kb[curBrand][curKbCat]||KB_DEF[curBrand][curKbCat]||{};
  const cat=KB_CATS.find(x=>x.id===curKbCat);
  ed.innerHTML=`<div class="card" style="flex:1"><div class="card-title"><i class="ti ${cat.icon}"></i>${cat.label} – ${BRAND_NAMES[curBrand]}</div>
  ${KB_FIELDS[curKbCat].map(f=>{const val=data[f.k]||'';
    if(f.t==='tags'){const tags=val?val.split(',').map(t=>t.trim()).filter(Boolean):[];return`<div class="fg"><label>${f.l}</label><div class="tw" id="tw-${f.k}" onclick="document.getElementById('ti-${f.k}').focus()">${tags.map(t=>`<span class="tg ${f.c}">${t}<button class="tg-del" onclick="delKbTag('${f.k}','${t.replace(/'/g,"\\'")}',event)">×</button></span>`).join('')}<input class="tg-in" id="ti-${f.k}" placeholder="Dodaj, zatwierdź Enterem..." onkeydown="kbTagKey(event,'${f.k}','${f.c}')"></div></div>`;}
    if(f.t==='ta')return`<div class="fg"><label>${f.l}</label><textarea rows="${f.r||3}" id="kf-${f.k}" oninput="updKb('${f.k}',this.value)">${val}</textarea></div>`;
    return`<div class="fg"><label>${f.l}</label><input type="text" id="kf-${f.k}" value="${val.replace(/"/g,'&quot;')}" oninput="updKb('${f.k}',this.value)"></div>`;
  }).join('')}</div>`;
}
function updKb(k,v){if(!DATA.kb[curBrand])DATA.kb[curBrand]={};if(!DATA.kb[curBrand][curKbCat])DATA.kb[curBrand][curKbCat]={};DATA.kb[curBrand][curKbCat][k]=v;}
function kbTagKey(e,k,c){
  if(e.key==='Enter'||e.key===','){e.preventDefault();const v=e.target.value.trim().replace(/,$/,'');if(!v)return;
    if(!DATA.kb[curBrand])DATA.kb[curBrand]={};if(!DATA.kb[curBrand][curKbCat])DATA.kb[curBrand][curKbCat]={};
    const cur=DATA.kb[curBrand][curKbCat][k]||'';const tags=cur?cur.split(',').map(t=>t.trim()).filter(Boolean):[];
    if(!tags.includes(v)){tags.push(v);DATA.kb[curBrand][curKbCat][k]=tags.join(', ');}
    e.target.value='';const wrap=document.getElementById('tw-'+k);const sp=document.createElement('span');sp.className='tg '+c;
    sp.innerHTML=`${v}<button class="tg-del" onclick="delKbTag('${k}','${v.replace(/'/g,"\\'")}',event)">×</button>`;wrap.insertBefore(sp,e.target);
  }
}
function delKbTag(k,v,e){e.stopPropagation();const cur=DATA.kb[curBrand]?.[curKbCat]?.[k]||'';const tags=cur.split(',').map(t=>t.trim()).filter(t=>t&&t!==v);updKb(k,tags.join(', '));renderKbFields();}
function saveKb(){save('kb');const ok=document.getElementById('kb-ok');ok.style.display='inline-flex';setTimeout(()=>ok.style.display='none',2500);showNotif('Baza wiedzy zapisana!');}
function resetKbCat(){if(!DATA.kb[curBrand])DATA.kb[curBrand]={};DATA.kb[curBrand][curKbCat]=JSON.parse(JSON.stringify(KB_DEF[curBrand][curKbCat]));renderKbFields();}

// ─── HISTORIA ────────────────────────────────────────────────
function renderHist(){
  const list=document.getElementById('hist-list');
  if(!DATA.postHistory.length){list.innerHTML='<div class="es">Brak historii.</div>';return;}
  list.innerHTML=DATA.postHistory.slice(0,30).map(p=>{
    const stars=p.stars?[1,2,3,4,5].map(i=>`<span style="color:${i<=p.stars?'#F5A623':'var(--border)'}">★</span>`).join(''):'<span style="font-size:12px;color:var(--text-3)">Brak oceny</span>';
    return`<div class="hi"><div class="hh"><span class="badge ${p.badge}" style="font-size:10.5px;padding:1px 8px">${p.brandName}</span>${p.isBlog?'<span style="font-size:11px;color:var(--text-3)">Blog</span>':''}${p.eventName?`<span style="font-size:11.5px;color:var(--info)"><i class="ti ti-calendar"></i> ${p.eventName}</span>`:''}<span style="margin-left:auto;font-size:11.5px;color:var(--text-3)">${p.date}</span></div><div style="font-size:11.5px;color:var(--text-3);margin-bottom:4px">${p.goal}</div><div style="color:var(--text-2);font-size:13px;line-height:1.6;margin-bottom:5px">${p.text.substring(0,160)}${p.text.length>160?'…':''}</div><div style="display:flex;align-items:center;gap:8px;font-size:14px">${stars}${p.tags&&p.tags.length?'<span style="font-size:11.5px;color:var(--text-3)">'+p.tags.join(', ')+'</span>':''}</div>${p.note?`<div style="font-size:12px;color:var(--text-3);margin-top:3px;font-style:italic">"${p.note}"</div>`:''}</div>`;
  }).join('');
}

// ─── INBOX BDB ───────────────────────────────────────────────
async function rewriteForBdb(id){
  const item=DATA.inbox.find(i=>i.id===id);if(!item)return;
  const btn=document.getElementById('rw-btn-'+id);btn.disabled=true;btn.innerHTML='<span class="spin"></span> Przepisuję...';
  const plat=document.getElementById('rw-plat-'+id)?.value||'facebook';
  const orig=plat==='blog'?item.origBlog:plat==='instagram'?item.origIg:item.origFb;
  const extra=document.getElementById('rw-extra-'+id)?.value.trim()||'';
  const p=`Jesteś agentem dla agencji bdb event.\n${buildKbPrompt('bdb')}${item.eventData?evCtxStr(item.eventData):''}${buildFbCtx('bdb')}\n${extra?'Wskazówki: '+extra:''}\n\nPost z perspektywy uczestnika (${item.fromName}):\n---\n${orig}\n---\n\nPrzepisz z perspektywy ORGANIZATORA bdb event. Pokaż profesjonalizm, skalę, B2B, CTA do samorządów/sponsorów.\n\nOdpowiedz TYLKO samym JSON:\n{"facebook":"wersja FB","instagram":"wersja IG bez hashtagów","blog":"wpis blogowy min 300 słów"}`;
  try{const parsed=await callAPI(p,2000);item.rewritten=parsed;item.unread=false;save('inbox');updateInboxBadge();renderInbox();showNotif('Przepisano dla bdb!');}
  catch(e){btn.disabled=false;btn.innerHTML='<i class="ti ti-wand"></i> Przepisz dla bdb';}
}

function delInboxItem(id){DATA.inbox=DATA.inbox.filter(i=>i.id!==id);save('inbox');updateInboxBadge();renderInbox();}
function toggleInboxItem(id){const item=DATA.inbox.find(i=>i.id===id);if(item){item.open=!item.open;item.unread=false;save('inbox');updateInboxBadge();renderInbox();}}

function swIbPlat(id,p,btn){['facebook','instagram','blog'].forEach(x=>{const el=document.getElementById('irw-'+x+'-'+id);if(el)el.style.display=x===p?'block':'none';});btn.closest('.ptabs').querySelectorAll('.tab').forEach(t=>t.classList.remove('on'));btn.classList.add('on');}
function copyIbPost(id){['facebook','instagram','blog'].forEach(p=>{const el=document.getElementById('irw-'+p+'-'+id);if(el&&el.style.display!=='none'){const b=el.querySelector('.rbox');if(b&&navigator.clipboard){navigator.clipboard.writeText(b.textContent);showNotif('Skopiowano!');}}}); }

function renderInbox(){
  const list=document.getElementById('inbox-list');
  if(!DATA.inbox.length){list.innerHTML='<div class="es">Skrzynka pusta.</div>';return;}
  list.innerHTML=DATA.inbox.map(item=>{const rw=item.rewritten;return`<div class="ib-item">
    <div class="ib-hdr" onclick="toggleInboxItem(${item.id})">${item.unread?'<span class="ndot"></span>':'<span style="width:7px;flex-shrink:0"></span>'}
      <span class="badge ${item.fromBadge}" style="font-size:10.5px;padding:1px 8px">${item.fromName}</span>
      <span style="font-size:13px;font-weight:500;color:var(--text)">${item.eventName||'Post bez eventu'}</span>
      <span style="margin-left:auto;font-size:12px;color:var(--text-3)">${item.date}</span>
      ${rw?'<span style="font-size:11px;color:var(--accent);margin-left:8px;font-weight:500"><i class="ti ti-check"></i> Gotowy</span>':''}
    </div>
    <div class="ib-body${item.open?' op':''}" id="ib-${item.id}">
      ${item.origFb||item.origBlog?`<div class="oq">${(item.origFb||item.origBlog).substring(0,200)}…</div>`:''}
      ${rw?`<div class="rw-box"><div class="rw-hdr"><i class="ti ti-building"></i> Wersja bdb event</div><div class="rw-body">
        <div class="ptabs"><button class="tab on" onclick="swIbPlat(${item.id},'facebook',this)">Facebook</button><button class="tab" onclick="swIbPlat(${item.id},'instagram',this)">Instagram</button><button class="tab" onclick="swIbPlat(${item.id},'blog',this)">Blog</button></div>
        <div id="irw-facebook-${item.id}"><div class="rbox">${rw.facebook||''}</div></div>
        <div id="irw-instagram-${item.id}" style="display:none"><div class="rbox">${rw.instagram||''}</div></div>
        <div id="irw-blog-${item.id}" style="display:none"><div class="rbox" style="min-height:150px">${rw.blog||''}</div></div>
        <button class="btn" style="margin-top:7px" onclick="copyIbPost(${item.id})"><i class="ti ti-copy"></i> Kopiuj</button>
      </div></div>`:''}
      <div class="fg"><label>Źródło do przepisania</label><select id="rw-plat-${item.id}">${item.origFb?'<option value="facebook">Post Facebook</option>':''}${item.origIg?'<option value="instagram">Post Instagram</option>':''}${item.origBlog?'<option value="blog">Wpis blogowy</option>':''}</select></div>
      <div class="fg"><label>Wskazówki (opcjonalnie)</label><textarea id="rw-extra-${item.id}" rows="2" placeholder="Np. podkreśl transport eventowy..."></textarea></div>
      <div style="display:flex;gap:7px"><button class="btn pr" onclick="rewriteForBdb(${item.id})" id="rw-btn-${item.id}"><i class="ti ti-wand"></i> ${rw?'Przepisz ponownie':'Przepisz dla bdb'}</button><button class="btn rd" onclick="delInboxItem(${item.id})" style="margin-left:auto"><i class="ti ti-trash"></i> Usuń</button></div>
    </div></div>`;
  }).join('');
}

// ─── INIT ────────────────────────────────────────────────────
updateStats();updateInboxBadge();refreshEvSel();
</script>
</body>
</html>
