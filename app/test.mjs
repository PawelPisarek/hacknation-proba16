// Test ekranu bez przeglądarki: logika app.js na danych z karty (public/dane). node app/test.mjs
import fs from "node:fs"; import path from "node:path"; import vm from "node:vm";
const K = path.join(import.meta.dirname, "public"), wyn = [];
const ok = (n, w) => { wyn.push(w); console.log((w ? "  OK  " : "  BŁĄD ") + n); };
const ctx = { location: { hash: "" }, console, URLSearchParams, document: { getElementById: () => ({ value: "x (dane sztuczne)", innerHTML: "" }), querySelectorAll: () => [], body: { classList: { add() {} }, dataset: {} } },
  fetch: async u => ({ ok: true, json: async () => u.startsWith("api") ? { wgrywanie: false } : JSON.parse(fs.readFileSync(path.join(K, u), "utf8")) }) };
vm.createContext(ctx); vm.runInContext(fs.readFileSync(path.join(K, "app.js"), "utf8").replace(/^const /gm, "var ") + "\n;globalThis.S=S;", ctx);
await new Promise(r => setTimeout(r, 200));
const c = ctx, spis = c.S.spis;
for (const o of spis.obrazy) {
  await c.laduj(o.id);
  for (const [t, r] of Object.entries(c.S.dane[o.id])) {
    const st = r.miejsca.map(m => c.RANGA[m.stopien]);
    if (!(st.every(x => x !== undefined) && st.join() === [...st].sort().join() && r.miejsca.every(m => !/\d/.test(m.opis))))
      ok(`P30 ${o.id}/${t}: stopień słownie, od wysokiego, bez liczb w opisie`, false);
  }
}
ok(`P30: ${spis.obrazy.length} obrazów × 6 wyników — stopień ∈ {niski, średni, wysoki}, lista od wysokiego, opisy bez liczb`, !wyn.includes(false));
c.S.obraz = "b"; c.S.dec = {}; await c.laduj("b");
ok("P34: (b) porównano z „chłodnia”", c.typ() === "chłodnia");
ok("§7.3: (b) 2 miejsca, jedno w strefie „podwójna podłoga”", c.miejsca().length === 2 && c.miejsca().some(m => m.strefa === "podwójna podłoga"));
ok("P32: lista powodów = A7 (4 pozycje z „inne”)", c.POWODY.join("|") === "element konstrukcji|ładunek zgodny z deklaracją|cień lub zakłócenie obrazu|inne");
c.odrzuc(1); ok("P32: samo „Odrzuć” nie zapisuje decyzji", !c.decyzja(1));
c.powod(1, ""); ok("P32: bez powodu nie odrzuca", !c.decyzja(1));
c.zatwierdz(0); c.powod(1, "inne");
let z = c.zestawienie().json;
ok("P35/A7: zestawienie — miejsce i przedmiot kontroli, dane sztuczne, ramka, decyzja i powód przy każdym", z.miejsce_kontroli && z.przedmiot_kontroli && /dane sztuczne/.test(z.dane_sztuczne)
  && z.obraz_z_zaznaczeniami.endsWith(".png") && z.miejsca.every(m => m.ramka.length === 4) && z.miejsca[0].decyzja === "zatwierdzone" && z.miejsca[1].decyzja === "odrzucone" && z.miejsca[1].powod === "inne");
ok("P38: po decyzjach przy wszystkich — 0 nieprzejrzanych (brak ostrzeżenia)", c.nieprzejrzane() === 0);
delete c.S.dec[c.klucz(1)]; z = c.zestawienie().json;
ok("P38: miejsce bez decyzji zapisane jako „nieprzejrzane”", c.nieprzejrzane() === 1 && z.miejsca[1].decyzja === "nieprzejrzane" && z.miejsca[1].powod === null);
ok("P38: odmiana 1 miejsce / 2, 4, 22 miejsca / 5, 12, 25 miejsc", [1, 2, 4, 22, 5, 12, 25].map(c.formaMiejsc).join() === "miejsce,miejsca,miejsca,miejsca,miejsc,miejsc,miejsc");
c.S.obraz = "d"; await c.laduj("d"); ok("P34/A6: (d) system dobiera „plandeka”", c.typ() === "plandeka");
await c.zmienTyp("chłodnia"); ok("A6: (d) po wyborze „chłodnia” porównano z „chłodnia”, nowy wzorzec", c.typ() === "chłodnia" && c.wynik().wzorzec !== c.S.dane.d.auto.wzorzec);
c.S.obraz = "a"; await c.laduj("a"); ok("§7.2: (a) 0 miejsc", c.miejsca().length === 0);
const teksty = fs.readFileSync(path.join(K, "app.js"), "utf8") + fs.readFileSync(path.join(K, "index.html"), "utf8");
ok("P37/A9: brak „WZORZEC:” i zdań o skuteczności w tekstach ekranu", !/WZORZEC:/.test(teksty) && !/skuteczn|wykryj(e|emy) (wszystk|każd)/i.test(teksty));
const n = wyn.filter(Boolean).length; console.log(`TEST EKRANU: ${n}/${wyn.length} OK`); process.exit(n === wyn.length ? 0 : 1);
