// Makieta Prześwit — UDAWANE DANE (spec §7.2), bez backendu. Wspólne dla wariantów 1–3.
const TYPY = ["plandeka", "chłodnia", "kontener na podwoziu", "cysterna", "skrzyniowa"];
const POWODY = ["element konstrukcji", "ładunek zgodny z deklaracją", "cień lub zakłócenie obrazu", "inne"];
const STREFY = { podloga: "podwójna podłoga", sciana: "ściana przy kabinie" };
// miejsca: [x0,y0,x1,y1] w układzie 1000×400, strefa (ryzyka) albo opis, stopień różnicy
const OBRAZY = {
  a: { plik: "naczepa_003.bmp", opis: "(a) czysta", dobrany: "plandeka", miejsca: { plandeka: [] } },
  b: { plik: "naczepa_017.bmp", opis: "(b) podwójna podłoga", dobrany: "plandeka", towar: [[420, 200, 560, 300]], miejsca: { plandeka: [
    { r: [300, 296, 640, 326], strefa: "podloga", st: "wysoki" },
    { r: [760, 150, 800, 200], co: "pod dachem przy drzwiach", st: "średni" }] } },
  c: { plik: "naczepa_024.bmp", opis: "(c) ściana przy kabinie i towar", dobrany: "skrzyniowa", towar: [[300, 170, 460, 318], [520, 210, 700, 318]], miejsca: { skrzyniowa: [
    { r: [226, 100, 262, 318], strefa: "sciana", st: "wysoki" },
    { r: [560, 230, 610, 270], co: "w ładunku (paczka o innej gęstości)", st: "wysoki" },
    { r: [880, 90, 930, 120], co: "pod dachem", st: "niski" },
    { r: [960, 200, 978, 260], co: "przy drzwiach", st: "niski" }] } },
  d: { plik: "naczepa_031.bmp", opis: "(d) zły typ wzorca", dobrany: "plandeka", poprawny: "chłodnia", towar: [[400, 150, 820, 318]], miejsca: {
    plandeka: [{ r: [222, 84, 300, 326], co: "cała ściana przednia (agregat)", st: "wysoki" },
               { r: [222, 84, 978, 104], co: "dach (izolacja)", st: "wysoki" },
               { r: [960, 84, 978, 326], co: "drzwi (izolacja)", st: "średni" }],
    "chłodnia": [{ r: [600, 296, 720, 326], strefa: "podloga", st: "średni" }] } },
};
const S = { obraz: "b", typ: {}, dec: {}, wyb: 0 };
function typ(k = S.obraz) { return S.typ[k] || OBRAZY[k].dobrany; }
function miejsca(k = S.obraz) { const o = OBRAZY[k]; return o.miejsca[typ(k)] || []; }
function klucz(i) { return S.obraz + "|" + typ() + "|" + i; }
function decyzja(i) { return S.dec[klucz(i)]; }
function przejrzane() { return miejsca().filter((_, i) => decyzja(i)).length; }
function nazwa(m) { return m.strefa ? STREFY[m.strefa] : m.co; }

// rysunek „RTG”: jasne tło, ciemniejsze = gęstsze
function svgNaczepa(k, { ramki = true, wzorzec = false, tylkoTyp = null, kadr = null, wybrane = -1 } = {}) {
  const o = OBRAZY[k], t = tylkoTyp || (wzorzec ? typ(k) : (o.poprawny || typ(k)));
  const ch = t === "chłodnia", cy = t === "cysterna", vb = kadr ? kadr.join(" ") : "0 0 1000 400";
  let s = `<svg class="rtg" viewBox="${vb}" xmlns="http://www.w3.org/2000/svg">`;
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
  if (ramki && !wzorzec) miejsca(k).forEach((m, i) => {
    const r = m.r, kol = m.strefa ? "#d0021b" : "#2b6cb0", d = S.dec[k + "|" + typ(k) + "|" + i];
    s += `<rect x="${r[0] - 4}" y="${r[1] - 4}" width="${r[2] - r[0] + 8}" height="${r[3] - r[1] + 8}" fill="none" stroke="${kol}" stroke-width="${i === wybrane ? 7 : 4}" ${d ? 'stroke-dasharray="10 6"' : ""}/>`;
    s += `<rect x="${r[0] - 4}" y="${r[1] - 30}" width="${m.strefa ? 200 : 30}" height="24" fill="${kol}"/><text x="${r[0] + 2}" y="${r[1] - 12}" fill="#fff" font-size="17" font-family="sans-serif">${i + 1}${m.strefa ? " " + STREFY[m.strefa] : ""}${d ? (d.d === "z" ? " ✓" : " ✗") : ""}</text>`;
  });
  if (wzorzec) s += `<text x="30" y="40" font-size="22" fill="#566" font-family="sans-serif">WZORZEC: ${t}</text>`;
  return s + "</svg>";
}
function htmlPasek() {
  const n = miejsca().length, p = przejrzane();
  return n ? `Przejrzano ${p} z ${n}<div class="pasek"><i style="width:${100 * p / n}%"></i></div>` : `0 miejsc — brak różnic od wzorca<div class="pasek"></div>`;
}
const OSTR = `<span class="ostr">Narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz.</span>`;
function htmlTyp() {
  return `porównano z: <select onchange="S.typ[S.obraz]=this.value;S.wyb=0;rysuj()">${TYPY.map(t => `<option ${t === typ() ? "selected" : ""}>${t}</option>`).join("")}</select>`;
}
function htmlObrazy() {
  return `<div class="obrazy">Gotowe obrazy (dane udawane): ${Object.keys(OBRAZY).map(k => `<button class="${k === S.obraz ? "akt" : ""}" onclick="S.obraz='${k}';S.wyb=0;rysuj()">${OBRAZY[k].opis}</button>`).join("")}</div>`;
}
function zatwierdz(i) { S.dec[klucz(i)] = { d: "z" }; nastepne(i); }
function odrzuc(i) { S.dec[klucz(i)] = { d: "o", powod: null }; S.wyb = i; rysuj(); }
function powod(i, p) { S.dec[klucz(i)].powod = p; nastepne(i); }
function nastepne(i) { const n = miejsca().findIndex((_, j) => !decyzja(j)); S.wyb = n < 0 ? i : n; rysuj(); }
function htmlDecyzja(i) {
  const d = decyzja(i);
  if (d && d.d === "z") return `<div class="dec">✓ Zatwierdzone — sprawdzone, podejrzane, do kontroli <a href="#" onclick="delete S.dec[klucz(${i})];rysuj();return false">cofnij</a></div>`;
  if (d && d.d === "o") return d.powod ? `<div class="dec">✗ Odrzucone — pomyłka systemu: ${d.powod} <a href="#" onclick="delete S.dec[klucz(${i})];rysuj();return false">cofnij</a></div>`
    : `<div class="dec">Powód odrzucenia:<br><select class="powod" onchange="powod(${i},this.value)"><option value="">— wybierz —</option>${POWODY.map(p => `<option>${p}</option>`).join("")}</select></div>`;
  return `<div class="dec"><button class="btn zatw" onclick="zatwierdz(${i})">Zatwierdź</button> <button class="btn odrz" onclick="odrzuc(${i})">Odrzuć</button></div>`;
}
function raport() {
  const o = OBRAZY[S.obraz], ms = miejsca();
  const w = document.createElement("div"); w.className = "modal";
  w.innerHTML = `<div><h3 style="margin-top:0">Raport z kontroli — ${o.plik}</h3>${svgNaczepa(S.obraz)}
  <p>Porównano z wzorcem: <b>${typ()}</b></p>
  <label>Miejsce kontroli<input id="mk" value="Przejście graniczne Koroszczyn, stanowisko RTG 2"></label>
  <label>Przedmiot kontroli<input id="pk" value="Naczepa WGM 4521X, ciągnik WGM 1187C"></label>
  <ol>${ms.map((m, i) => { const d = decyzja(i); return `<li>${nazwa(m)} — ${!d ? "nieprzejrzane" : d.d === "z" ? "zatwierdzone (do kontroli)" : "odrzucone: " + (d.powod || "bez powodu")}</li>`; }).join("") || "<li>brak miejsc różnych od wzorca</li>"}</ol>
  <button class="btn gl" onclick="pobierz()">Zapisz raport (plik)</button> <button class="btn odrz" onclick="this.closest('.modal').remove()">Zamknij</button>
  <p class="ostr" style="font-size:12px">Makieta: dane udawane.</p></div>`;
  document.body.appendChild(w);
}
function pobierz() {
  const o = OBRAZY[S.obraz], r = { obraz: o.plik, wzorzec: typ(), miejsce_kontroli: document.getElementById("mk").value,
    przedmiot_kontroli: document.getElementById("pk").value,
    miejsca: miejsca().map((m, i) => ({ nr: i + 1, ramka: m.r, strefa: m.strefa ? STREFY[m.strefa] : null, opis: nazwa(m), stopien: m.st, decyzja: decyzja(i) || null })) };
  const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([JSON.stringify(r, null, 2)], { type: "application/json" }));
  a.download = "raport_" + o.plik.replace(".bmp", ".json"); a.click();
}
