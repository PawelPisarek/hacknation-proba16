// Makieta Prześwit R2 — UDAWANE DANE (spec §7.2), bez backendu. R1 (P31) + poprawki P32–P37; kolejność obrazów wg §7.3.
const TYPY = ["plandeka", "chłodnia", "kontener na podwoziu", "cysterna", "skrzyniowa"];
const POWODY = ["element konstrukcji", "ładunek zgodny z deklaracją", "cień lub zakłócenie obrazu", "inne"];
const STREFY = { podloga: "podwójna podłoga", sciana: "ściana przy kabinie" };
const RANGA = { wysoki: 0, "średni": 1, niski: 2 };
// miejsca: [x0,y0,x1,y1] w układzie 1000×400; strefa (ryzyka) albo opis „co” + krótki opis „kr” na obraz (P36); stopień (P30 A)
const OBRAZY = {
  b: { plik: "naczepa_017.bmp", opis: "(b) podwójna podłoga", dobrany: "chłodnia", towar: [[420, 200, 560, 300]], miejsca: { "chłodnia": [
    { r: [300, 296, 640, 326], strefa: "podloga", st: "wysoki" },
    { r: [760, 150, 800, 200], co: "pod dachem przy drzwiach", kr: "pod dachem", st: "średni" }] } },
  c: { plik: "naczepa_024.bmp", opis: "(c) ściana przy kabinie i towar", dobrany: "skrzyniowa", towar: [[300, 170, 460, 318], [520, 210, 700, 318]], miejsca: { skrzyniowa: [
    { r: [226, 100, 262, 318], strefa: "sciana", st: "wysoki" },
    { r: [560, 230, 610, 270], co: "w ładunku (paczka o innej gęstości)", kr: "paczka w ładunku", st: "wysoki" },
    { r: [880, 110, 930, 140], co: "pod dachem", kr: "pod dachem", st: "niski" },
    { r: [960, 220, 978, 280], co: "przy drzwiach", kr: "przy drzwiach", st: "niski" }] } },
  d: { plik: "naczepa_031.bmp", opis: "(d) zły typ wzorca", dobrany: "plandeka", poprawny: "chłodnia", towar: [[400, 150, 820, 318]], miejsca: {
    plandeka: [{ r: [222, 84, 300, 326], co: "cała ściana przednia (agregat)", kr: "ściana przednia", st: "wysoki" },
               { r: [222, 84, 978, 104], co: "dach (izolacja)", kr: "dach", st: "wysoki" },
               { r: [960, 84, 978, 326], co: "drzwi (izolacja)", kr: "drzwi", st: "średni" }],
    "chłodnia": [{ r: [600, 296, 720, 326], strefa: "podloga", st: "średni" }] } },
  a: { plik: "naczepa_003.bmp", opis: "(a) czysta", dobrany: "plandeka", miejsca: { plandeka: [] } },
};
for (const o of Object.values(OBRAZY)) for (const t in o.miejsca) o.miejsca[t].sort((a, b) => RANGA[a.st] - RANGA[b.st]);
const S = { obraz: OBRAZY[location.hash.slice(1)] ? location.hash.slice(1) : "b", typ: {}, dec: {}, wyb: 0, odrz: null };
function typ(k = S.obraz) { return S.typ[k] || OBRAZY[k].dobrany; }
function miejsca(k = S.obraz) { return OBRAZY[k].miejsca[typ(k)] || []; }
function klucz(i, k = S.obraz) { return k + "|" + typ(k) + "|" + i; }
function decyzja(i) { return S.dec[klucz(i)]; }
function przejrzane() { return miejsca().filter((_, i) => decyzja(i)).length; }
function nazwa(m) { return m.strefa ? STREFY[m.strefa] : m.co; }
function krotko(m) { return m.strefa ? STREFY[m.strefa] : m.kr; }

// rysunek „RTG”: jasne tło, ciemniejsze = gęstsze. Wzorzec: to samo miejsce przerywaną ramką (P33), bez napisu w oknie (P37)
function svgNaczepa(k, { wzorzec = false, wybrane = -1 } = {}) {
  const o = OBRAZY[k], t = wzorzec ? typ(k) : (o.poprawny || typ(k));
  const ch = t === "chłodnia", cy = t === "cysterna";
  let s = `<svg class="rtg" viewBox="0 0 1000 400" xmlns="http://www.w3.org/2000/svg">`;
  s += `<rect x="20" y="150" width="180" height="180" rx="14" fill="#9aa"/><rect x="40" y="170" width="70" height="60" fill="#dde"/>`;
  for (const x of [70, 300, 360, 860, 920]) s += `<circle cx="${x}" cy="352" r="26" fill="#566"/><circle cx="${x}" cy="352" r="10" fill="#bbb"/>`;
  if (cy) s += `<rect x="220" y="110" width="760" height="210" rx="100" fill="none" stroke="#677" stroke-width="10"/>`;
  else {
    s += `<rect x="220" y="80" width="760" height="250" fill="none" stroke="#677" stroke-width="${ch ? 12 : 5}"/>`;
    s += `<rect x="220" y="318" width="760" height="12" fill="#566"/>`;
    if (t === "plandeka" || t === "skrzyniowa") for (let x = 320; x < 980; x += 110) s += `<line x1="${x}" y1="80" x2="${x}" y2="318" stroke="#9aa" stroke-width="3"/>`;
    if (ch) s += `<rect x="200" y="100" width="34" height="90" fill="#788"/>`;
  }
  if (!wzorzec) {
    for (const r of o.towar || []) s += `<rect x="${r[0]}" y="${r[1]}" width="${r[2] - r[0]}" height="${r[3] - r[1]}" fill="#b9c0b8" stroke="#99a"/>`;
    if (k === "b") s += `<rect x="300" y="300" width="340" height="16" fill="#8a9088"/><rect x="560" y="240" width="40" height="30" fill="#a0a69e"/>`;
    if (k === "c") s += `<rect x="232" y="100" width="24" height="218" fill="#8a9088"/><rect x="565" y="235" width="40" height="30" fill="#7d837b"/>`;
    if (k === "d") s += `<rect x="620" y="302" width="90" height="14" fill="#8a9088"/>`;
  }
  miejsca(k).forEach((m, i) => {
    if (wzorzec && i !== wybrane) return;
    const r = m.r, kol = m.strefa ? "#d0021b" : "#2b6cb0", d = S.dec[klucz(i, k)];
    s += `<rect x="${r[0] - 4}" y="${r[1] - 4}" width="${r[2] - r[0] + 8}" height="${r[3] - r[1] + 8}" fill="none" stroke="${kol}" stroke-width="${i === wybrane ? 7 : 4}" ${wzorzec ? 'stroke-dasharray="14 8"' : ""}/>`;
    const et = `${i + 1} ${krotko(m)}${!wzorzec && d ? (d.d === "z" ? " ✓" : " ✗") : ""}`, sz = et.length * 12 + 16;
    const lx = Math.max(2, Math.min(r[0] - 4, 998 - sz)), ly = r[1] - 38 < 2 ? r[3] + 6 : r[1] - 38;
    s += `<rect x="${lx}" y="${ly}" width="${sz}" height="32" rx="3" fill="${wzorzec ? "#fff" : kol}" stroke="${kol}" stroke-width="2"/><text x="${lx + 7}" y="${ly + 23}" fill="${wzorzec ? kol : "#fff"}" font-size="21" font-weight="700" font-family="sans-serif">${et}</text>`;
  });
  return s + "</svg>";
}
function htmlPasek() {   // P37: bez zdania ostrożności na pasku
  const n = miejsca().length, p = przejrzane();
  return n ? `Przejrzano ${p} z ${n}<div class="pasek"><i style="width:${100 * p / n}%"></i></div>` : `0 miejsc — brak różnic od wzorca<div class="pasek"></div>`;
}
function htmlTyp() {
  return `porównano z: <select onchange="S.typ[S.obraz]=this.value;S.wyb=0;S.odrz=null;rysuj()">${TYPY.map(t => `<option ${t === typ() ? "selected" : ""}>${t}</option>`).join("")}</select>`;
}
function htmlObrazy() {   // kolejność jak ścieżka pokazu §7.3: (b), raport, (c), (d), (a)
  return `<div class="obrazy">Gotowe obrazy (dane udawane): ${Object.keys(OBRAZY).map(k => `<button class="${k === S.obraz ? "akt" : ""}" onclick="S.obraz='${k}';S.wyb=0;S.odrz=null;rysuj()">${OBRAZY[k].opis}</button>`).join("")}</div>`;
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
function raport() {
  const o = OBRAZY[S.obraz], ms = miejsca();
  const w = document.createElement("div"); w.className = "modal";
  w.innerHTML = `<div><h3 style="margin-top:0">Raport z kontroli — ${o.plik}</h3>${svgNaczepa(S.obraz)}
  <p>Porównano z wzorcem: <b>${typ()}</b></p>
  <label>Miejsce kontroli <i class="szt">(dane sztuczne)</i><input id="mk" value="Przejście graniczne Koroszczyn, stanowisko RTG 2"></label>
  <label>Przedmiot kontroli <i class="szt">(dane sztuczne)</i><input id="pk" value="Naczepa WGM 4521X, ciągnik WGM 1187C"></label>
  <ol>${ms.map((m, i) => { const d = decyzja(i); return `<li>${nazwa(m)} (różnica: ${m.st}) — ${!d ? "nieprzejrzane" : d.d === "z" ? "zatwierdzone (do kontroli)" : "odrzucone: " + d.powod}</li>`; }).join("") || "<li>brak miejsc różnych od wzorca</li>"}</ol>
  <button class="btn gl" onclick="pobierz()">Zapisz raport (zestawienie + obraz PNG)</button> <button class="btn odrz" onclick="this.closest('.modal').remove()">Zamknij</button></div>`;
  document.body.appendChild(w);
}
function pobierzPlik(blob, nazwaPliku) { const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = nazwaPliku; a.click(); }
function pobierz() {   // P35: zestawienie (JSON) razem z obrazem PNG z zaznaczeniami
  const o = OBRAZY[S.obraz], baza = "raport_" + o.plik.replace(".bmp", "");
  const r = { obraz: o.plik, obraz_z_zaznaczeniami: baza + ".png", porownano_z: typ(), dane_sztuczne: "miejsce i przedmiot kontroli — przykładowe, dane sztuczne",
    miejsce_kontroli: document.getElementById("mk").value, przedmiot_kontroli: document.getElementById("pk").value,
    miejsca: miejsca().map((m, i) => ({ nr: i + 1, ramka: m.r, strefa: m.strefa ? STREFY[m.strefa] : null, opis: nazwa(m), stopien: m.st,
      decyzja: !decyzja(i) ? null : decyzja(i).d === "z" ? "zatwierdzone" : "odrzucone", powod: decyzja(i) && decyzja(i).powod || null })) };
  pobierzPlik(new Blob([JSON.stringify(r, null, 2)], { type: "application/json" }), baza + ".json");
  const img = new Image(), c = document.createElement("canvas"); c.width = 1000; c.height = 400;
  img.onload = () => { const g = c.getContext("2d"); g.fillStyle = "#f7f7f2"; g.fillRect(0, 0, 1000, 400); g.drawImage(img, 0, 0, 1000, 400); c.toBlob(b => pobierzPlik(b, baza + ".png")); };
  img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svgNaczepa(S.obraz));
}
