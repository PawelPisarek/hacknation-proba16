// Prześwit — aplikacja (zadanie 01). Ekran statyczny + wyniki rdzenia policzone na karcie OMENa (public/dane).
// Wgrany .bmp idzie do usługi na karcie (OMEN_URL, np. http://192.168.1.112:8716); bez niej gotowe obrazy działają dalej.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
const PORT = +process.env.PORT || 3000, OMEN = process.env.OMEN_URL || "", KAT = path.join(import.meta.dirname, "public");
const TYP = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css", ".json": "application/json; charset=utf-8", ".jpg": "image/jpeg", ".png": "image/png" };
http.createServer(async (req, res) => {
  const u = new URL(req.url, "http://x");
  if (u.pathname === "/api/analiza" && req.method === "POST") {
    if (!OMEN) { res.writeHead(503, { "Content-Type": "application/json; charset=utf-8" }); return res.end(JSON.stringify({ blad: "liczenie na karcie jest teraz wyłączone — gotowe obrazy działają" })); }
    const cz = []; for await (const c of req) cz.push(c);
    try {
      const r = await fetch(OMEN + "/analiza" + u.search, { method: "POST", body: Buffer.concat(cz), signal: AbortSignal.timeout(120000) });
      res.writeHead(r.status, { "Content-Type": "application/json; charset=utf-8" }); return res.end(Buffer.from(await r.arrayBuffer()));
    } catch (e) { res.writeHead(503, { "Content-Type": "application/json; charset=utf-8" }); return res.end(JSON.stringify({ blad: "karta OMENa nie odpowiada — gotowe obrazy działają" })); }
  }
  if (u.pathname === "/api/stan") { res.writeHead(200, { "Content-Type": "application/json" }); return res.end(JSON.stringify({ wgrywanie: !!OMEN })); }
  const p = path.normalize(path.join(KAT, decodeURIComponent(u.pathname === "/" ? "/index.html" : u.pathname)));
  if (!p.startsWith(KAT)) { res.writeHead(403); return res.end(); }
  fs.readFile(p, (e, d) => { if (e) { res.writeHead(404); return res.end("brak"); } res.writeHead(200, { "Content-Type": TYP[path.extname(p)] || "application/octet-stream", "Cache-Control": "no-cache" }); res.end(d); });
}).listen(PORT, () => console.log("Prześwit na porcie " + PORT + (OMEN ? ", karta: " + OMEN : ", bez usługi na karcie")));
