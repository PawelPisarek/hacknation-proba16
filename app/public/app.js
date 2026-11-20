// Prześwit — ekran aplikacji (zadanie 01): układ i zachowanie z makiety R3 (P29–P38), wyniki z rdzenia policzone na karcie OMENa.
const POWODY = ["element konstrukcji", "ładunek zgodny z deklaracją", "cień lub zakłócenie obrazu", "inne"];   // spec A7 (P32)
const RANGA = { wysoki: 0, "średni": 1, niski: 2 };
const S = { spis: null, dane: {}, obraz: "b", typ: {}, dec: {}, wyb: 0, odrz: null, licze: "", blad: "", wgrywanie: false };

function wynikiObrazu(k = S.obraz) { return S.dane[k]; }
function wynik(k = S.obraz) {   // wybrany typ albo dobór automatyczny; wybór typu równego dobranemu = wynik doboru
  const w = wynikiObrazu(k); if (!w) return null;
  const t = S.typ[k]; return !t || t === w.auto.porownano_z || !w[t] ? w.auto : w[t];
}
function typ(k = S.obraz) { const r = wynik(k); return r ? r.porownano_z : ""; }
function miejsca(k = S.obraz) { const r = wynik(k); return r ? r.miejsca : []; }
function formaMiejsc(n) { const d = n % 10, s = n % 100; return n === 1 ? "miejsce" : d >= 2 && d <= 4 && (s < 12 || s > 14) ? "miejsca" : "miejsc"; }
function klucz(i, k = S.obraz) { return k + "|" + typ(k) + "|" + i; }
function decyzja(i) { return S.dec[klucz(i)]; }
function przejrzane() { return miejsca().filter((_, i) => decyzja(i)).length; }
function nieprzejrzane() { return miejsca().length - przejrzane(); }
function plik(k = S.obraz) { const o = S.spis.obrazy.find(o => o.id === k); return o ? o.plik : k; }
function adres(x) { return x.startsWith("data:") ? x : "dane/" + x; }

// obraz z ramkami (SVG nad zdjęciem). Wzorzec (wyrównany do badanego): to samo miejsce przerywaną ramką (P33), bez napisu (P37)
function htmlObraz(k, { wzorzec = false, wybrane = -1 } = {}) {
  const r = wynik(k); if (!r) return "";
  const fs = Math.max(16, Math.round(r.szer / 34)), mn = Math.round(r.szer / 60);   // P36: czytelny numer i opis także przy małych miejscach
  let s = `<div class="rtgw"><img src="${adres(wzorzec ? r.wzorzec : r.badany)}" alt="${wzorzec ? "wzorzec" : "badany"}"><svg viewBox="0 0 ${r.szer} ${r.wys}" xmlns="http://www.w3.org/2000/svg">`;
  r.miejsca.forEach((m, i) => {
    if (wzorzec && i !== wybrane) return;
    let [x0, y0, x1, y1] = m.ekran; const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    if (x1 - x0 < mn) [x0, x1] = [cx - mn / 2, cx + mn / 2]; if (y1 - y0 < mn) [y0, y1] = [cy - mn / 2, cy + mn / 2];
    const kol = m.strefa ? "#d0021b" : "#2b6cb0", d = S.dec[klucz(i, k)];
    s += `<rect x="${x0 - 4}" y="${y0 - 4}" width="${x1 - x0 + 8}" height="${y1 - y0 + 8}" fill="none" stroke="${kol}" stroke-width="${i === wybrane ? 6 : 3}" ${wzorzec ? 'stroke-dasharray="12 7"' : ""}/>`;
    const et = `${i + 1} ${m.opis}${!wzorzec && d ? (d.d === "z" ? " ✓" : " ✗") : ""}`, sz = et.length * fs * 0.6 + 14;   // P36: numer + krótki opis, także przy małych
    const lx = Math.max(2, Math.min(x0 - 4, r.szer - sz - 2)), ly = y0 - fs - 14 < 2 ? y1 + 6 : y0 - fs - 14;
    s += `<rect x="${lx}" y="${ly}" width="${sz}" height="${fs + 10}" rx="3" fill="${wzorzec ? "#fff" : kol}" stroke="${kol}" stroke-width="2"/><text x="${lx + 7}" y="${ly + fs + 2}" fill="${wzorzec ? kol : "#fff"}" font-size="${fs}" font-weight="700" font-family="sans-serif">${et}</text>`;
  });
  return s + "</svg></div>";
}
function htmlPasek() {   // P37: bez zdania ostrożności na pasku
  const n = miejsca().length, p = przejrzane();
  return n ? `Przejrzano ${p} z ${n}<div class="pasek"><i style="width:${100 * p / n}%"></i></div>` : `0 miejsc<div class="pasek"></div>`;
}
function htmlTyp() {   // P34: typ dobrany automatycznie, operator zmienia jednym wyborem (A6)
  return `porównano z: <select id="typ" onchange="zmienTyp(this.value)">${S.spis.typy.map(t => `<option ${t === typ() ? "selected" : ""}>${t}</option>`).join("")}</select>`;
}
function htmlObrazy() {   // kolejność ścieżki pokazu §7.3: (b), (c), (d), (a), potem inne obrazy sztuczne
  return `<div class="obrazy">Obrazy sztuczne: ${S.spis.obrazy.map(o => `<button class="${o.id === S.obraz ? "akt" : ""}" title="${o.opis}" onclick="wybierz('${o.id}')">${o.id.length === 1 ? "(" + o.id + ") " : ""}${o.plik}</button>`).join("")}
  <span class="wgraj">${S.wgrywanie ? `<label>wgraj .bmp: <input type="file" accept=".bmp,image/bmp" onchange="wgraj(this.files[0])"></label>` : ""}</span></div>`;
}
async function wybierz(k) { S.obraz = k; S.wyb = 0; S.odrz = null; S.blad = ""; await laduj(k); rysuj(); }
async function laduj(k) {
  if (S.dane[k]) return;
  const o = S.spis.obrazy.find(o => o.id === k);
  S.dane[k] = await (await fetch("dane/" + o.json)).json();
}
async function zmienTyp(t) {
  S.typ[S.obraz] = t; S.wyb = 0; S.odrz = null;
  const w = wynikiObrazu();
  if (w && !w[t] && t !== w.auto.porownano_z && w.wgrany) return liczNaKarcie(w.wgrany, t);   // wgrany obraz: nowe porównanie na karcie
  rysuj();
}
async function liczNaKarcie(bmp, t) {
  S.licze = "Liczę na karcie…"; S.blad = ""; rysuj();
  try {
    const r = await fetch("api/analiza" + (t ? "?typ=" + encodeURIComponent(t) : ""), { method: "POST", body: bmp });
    const j = await r.json(); if (!r.ok) throw new Error(j.blad || r.status);
    const w = S.dane.wgrany || (S.dane.wgrany = { wgrany: bmp });
    if (t) w[t] = j; else w.auto = j;
  } catch (e) { S.blad = "Nie policzono: " + e.message; }
  S.licze = ""; rysuj();
}
async function wgraj(f) {
  if (!f) return;
  delete S.dane.wgrany; Object.keys(S.dec).filter(x => x.startsWith("wgrany|")).forEach(x => delete S.dec[x]); delete S.typ.wgrany;
  S.spis.obrazy = S.spis.obrazy.filter(o => o.id !== "wgrany").concat([{ id: "wgrany", plik: f.name, opis: "wgrany plik" }]);
  S.obraz = "wgrany"; S.wyb = 0; await liczNaKarcie(f, null);
  if (!S.dane.wgrany || !S.dane.wgrany.auto) { S.spis.obrazy = S.spis.obrazy.filter(o => o.id !== "wgrany"); S.obraz = "b"; rysuj(); }
}
function zatwierdz(i) { S.dec[klucz(i)] = { d: "z" }; S.odrz = null; nastepne(i); }
function odrzuc(i) { S.odrz = klucz(i); S.wyb = i; rysuj(); }               // P32: samo „Odrzuć” niczego nie zapisuje
function powod(i, p) { if (!p) return; S.dec[klucz(i)] = { d: "o", powod: p }; S.odrz = null; nastepne(i); }
function nastepne(i) { const n = miejsca().findIndex((_, j) => !decyzja(j)); S.wyb = n < 0 ? i : n; rysuj(); }
function htmlDecyzja(i) {
  const d = decyzja(i);
  if (d && d.d === "z") return `<div class="dec">✓ Zatwierdzone — sprawdzone, podejrzane, do kontroli <a href="#" onclick="delete S.dec[klucz(${i})];rysuj();return false">cofnij</a></div>`;
  if (d && d.d === "o") return `<div class="dec">✗ Odrzucone — pomyłka systemu: ${d.powod} <a href="#" onclick="delete S.dec[klucz(${i})];rysuj();return false">cofnij</a></div>`;
  if (S.odrz === klucz(i)) return `<div class="dec">Odrzucenie wymaga powodu:<br><select class="powod" onchange="powod(${i},this.value)"><option value="">— wybierz powód —</option>${POWODY.map(p => `<option>${p}</option>`).join("")}</select> <a href="#" onclick="S.odrz=null;rysuj();return false">anuluj</a></div>`;
  return `<div class="dec"><button class="btn zatw" onclick="zatwierdz(${i})">Zatwierdź</button> <button class="btn odrz" onclick="odrzuc(${i})">Odrzuć</button></div>`;
}
function rysuj() {
  const r = wynik(), ms = miejsca(); if (S.wyb >= ms.length) S.wyb = 0;
  document.getElementById("app").innerHTML = `<header><b>Prześwit</b><span>${plik()}</span><span>${r ? htmlTyp() : ""}</span><button class="btn gl" onclick="raport()" ${r ? "" : "disabled"}>Zapisz raport</button></header>${htmlObrazy()}
  ${S.licze ? `<div class="licze">${S.licze}</div>` : ""}${S.blad ? `<div class="blad">${S.blad}</div>` : ""}
  ${r ? `<div class="uk"><div><div class="tyt"><b>WZORZEC</b> — typ: ${typ()}</div>${htmlObraz(S.obraz, { wzorzec: true, wybrane: S.wyb })}</div>
  <div><div class="tyt"><b>BADANY</b> — ${plik()}</div>${htmlObraz(S.obraz, { wybrane: S.wyb })}</div>
  <div class="lista"><b>Miejsca</b> <span style="font-size:13px">(od wysokiego stopnia różnicy)</span>
  ${ms.map((m, i) => `<div class="miejsce ${i === S.wyb ? "wyb" : ""}" onclick="if(event.target.tagName==='DIV'||event.target.tagName==='SPAN'){S.wyb=${i};rysuj()}"><span class="${m.strefa ? "ryzyko" : ""}">${i + 1}. ${m.opis}</span><br><span style="font-size:13px">różnica: <span class="st ${m.stopien}">${m.stopien}</span></span>${htmlDecyzja(i)}</div>`).join("") || `<div class="miejsce">0 miejsc</div>`}</div></div>
  <div class="stopka">${htmlPasek()}</div>
  <div class="info">Wynik policzony na karcie OMENa (${r.metoda}, ${r.czas_s} s); obrazy sztuczne z generatora.</div>` : ""}`;
}
function raport() {
  const ms = miejsca();
  const w = document.createElement("div"); w.className = "modal";
  w.innerHTML = `<div><h3 style="margin-top:0">Raport z kontroli — ${plik()}</h3>${htmlObraz(S.obraz)}
  <p>Porównano z wzorcem: <b>${typ()}</b></p>
  <label>Miejsce kontroli <i class="szt">(dane sztuczne)</i><input id="mk" value="Przejście graniczne Koroszczyn, stanowisko RTG 2"></label>
  <label>Przedmiot kontroli <i class="szt">(dane sztuczne)</i><input id="pk" value="Naczepa WGM 4521X, ciągnik WGM 1187C"></label>
  <ol>${ms.map((m, i) => { const d = decyzja(i); return `<li>${m.opis} (różnica: ${m.stopien}) — ${!d ? "nieprzejrzane" : d.d === "z" ? "zatwierdzone (do kontroli)" : "odrzucone: " + d.powod}</li>`; }).join("") || "<p>0 miejsc</p>"}</ol>
  <span id="zapis"><button class="btn gl" onclick="zapisz()">Zapisz raport (zestawienie + obraz PNG)</button></span> <button class="btn odrz" onclick="raportZamknij()">Zamknij</button></div>`;
  document.body.appendChild(w);
}
function raportZamknij() { document.querySelectorAll(".modal").forEach(m => m.remove()); }
function zapisz() {   // P38 B: jedno ostrzeżenie przy nieprzejrzanych, po potwierdzeniu zapis z „nieprzejrzane”
  const n = nieprzejrzane();
  if (!n) return pobierz();
  document.getElementById("zapis").innerHTML = `<div class="ostrz">Nieprzejrzane: ${n} ${formaMiejsc(n)}. Zapisać mimo to?</div>
    <button class="btn gl" onclick="pobierz()">Zapisz mimo to</button> <button class="btn odrz" onclick="raportZamknij();raport()">Wróć</button>`;
}
function zestawienie() {   // P35, A7: zestawienie razem z obrazem PNG
  const r = wynik(), baza = "raport_" + plik().replace(/\.bmp$/i, "");
  return { baza, json: { obraz: plik(), obraz_z_zaznaczeniami: baza + ".png", porownano_z: typ(), typ_wybrany_przez_operatora: S.typ[S.obraz] || null,
    metoda: r.metoda, policzono_na: "karta OMENa", czas_s: r.czas_s, dane_sztuczne: "miejsce i przedmiot kontroli — przykładowe, dane sztuczne",
    miejsce_kontroli: (document.getElementById("mk") || {}).value || null, przedmiot_kontroli: (document.getElementById("pk") || {}).value || null,
    miejsca: miejsca().map((m, i) => { const d = decyzja(i); return { nr: i + 1, ramka: m.ramka, strefa: m.strefa, opis: m.opis, stopien: m.stopien,
      decyzja: !d ? "nieprzejrzane" : d.d === "z" ? "zatwierdzone" : "odrzucone", powod: d && d.powod || null }; }) } };
}
function pobierzPlik(blob, nazwa) { const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = nazwa; document.body.appendChild(a); a.click(); a.remove(); }
function pobierz() {
  const { baza, json } = zestawienie(), r = wynik();
  pobierzPlik(new Blob([JSON.stringify(json, null, 2)], { type: "application/json" }), baza + ".json");
  const img = new Image(); img.onload = () => {
    const c = document.createElement("canvas"); c.width = r.szer; c.height = r.wys; const g = c.getContext("2d"); g.drawImage(img, 0, 0);
    const svg = new Image(); svg.onload = () => { g.drawImage(svg, 0, 0, r.szer, r.wys); c.toBlob(b => pobierzPlik(b, baza + ".png")); };
    svg.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(htmlObraz(S.obraz).replace(/^.*?(<svg)/s, "$1").replace(/<\/div>$/, "").replace("<svg ", `<svg width="${r.szer}" height="${r.wys}" `));
  };
  img.src = adres(r.badany);
  document.querySelectorAll(".modal").forEach(m => m.querySelector("#zapis").innerHTML = "<b>Zapisano: " + baza + ".json i " + baza + ".png</b>");
}

// tryb zrzutu: #b&z=0&o=1:cień lub zakłócenie obrazu&odrz=1&typ=chłodnia&wyb=1&raport&ostrz&zrzut
async function start() {
  S.spis = await (await fetch("dane/spis.json")).json();
  try { S.wgrywanie = (await (await fetch("api/stan")).json()).wgrywanie; } catch (e) { S.wgrywanie = false; }
  const h = new URLSearchParams(location.hash.slice(1)), k0 = [...h.keys()][0];
  if (k0 && S.spis.obrazy.some(o => o.id === k0)) S.obraz = k0;
  await laduj(S.obraz);
  if (h.get("typ")) S.typ[S.obraz] = h.get("typ");
  for (const i of (h.get("z") || "").split(",").filter(Boolean)) S.dec[klucz(+i)] = { d: "z" };
  if (h.get("o")) { const [i, p] = h.get("o").split(":"); S.dec[klucz(+i)] = { d: "o", powod: p }; }
  if (h.get("odrz")) S.odrz = klucz(+h.get("odrz"));
  S.wyb = +(h.get("wyb") || 0); rysuj();
  if (h.has("raport")) raport();
  if (h.has("ostrz")) zapisz();
  if (h.has("zrzut")) document.body.classList.add("zrzut");
  document.body.dataset.gotowe = "1";
}
start();
