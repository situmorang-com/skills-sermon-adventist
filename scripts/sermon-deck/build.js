#!/usr/bin/env node
// sermon-deck — build a sermon PowerPoint from a deck.json.
//
//   sermon-deck <deck.json> [out.pptx]      # default: <deck.json's folder>/<file or slug of title>.pptx
//   sermon-deck --example                   # print a small deck.json to start from
//
// The content is data; the layout decisions live here, so every sermon deck
// reads as one series: five layouts, a dark theme, a gold badge as the motif,
// nothing under 16pt. First use: `npm install` in this folder (scripts/install.sh
// does it). Afterwards check the deck with the pptx skill's validate.py and look
// at the slides; this script only warns about text likely to overflow.
//
// deck.json
//   { "title": "...", "author": "...", "file": "optional-name.pptx",
//     "bigIdea": ["line", "a line with **gold words**", "line"],
//     "theme": { "name": "...", "colors": { ...twelve slots... } },      // optional
//     "slides": [
//       { "section": "Pembukaan" },                                      // starts a PowerPoint section
//       { "type": "title",    "title": "...", "lines": ["...", "..."], "glyph": "♪" },
//       { "type": "verse",    "title": "...", "text": "...", "ref": "Wahyu 15:3 (TB)", "note": "...", "size": 28 },
//       { "type": "point",    "title": "...", "lines": ["...", "..."], "glyph": "1", "note": "...", "size": 28 },
//       { "type": "movement", "no": 1, "title": "...", "sub": "...", "note": "..." },   // also starts a section
//       { "type": "idea",     "title": "...", "lines": ["..."], "note": "..." }         // lines default to bigIdea
//     ] }
// "note" becomes the speaker note. "size" overrides the automatic font size.
// A verse longer than about 300 characters will not fit at 24pt: split it over two slides.
const fs = require("fs");
const path = require("path");

const EXAMPLE = {
  title: "Judul Khotbah", author: "Nama Pengkhotbah",
  bigIdea: ["Kalimat gagasan utama,", "dengan **kata kunci** berwarna emas."],
  slides: [
    { section: "Pembukaan" },
    { type: "title", title: "Judul Khotbah", lines: ["Wahyu 15:3", "Jemaat · Sabat, tanggal"], glyph: "♪" },
    { type: "verse", title: "Ayat Inti", text: "Teks ayat, kata demi kata dari Alkitab.", ref: "Wahyu 15:3 (TB)" },
    { type: "idea", title: "Satu kalimat untuk hari Senin" },
    { type: "movement", no: 1, title: "Gerakan pertama", sub: "Satu kalimat yang merangkum gerakan ini." },
    { type: "point", title: "Pokok", lines: ["Baris pertama.", "Baris kedua."], glyph: "1", note: "Catatan pembicara." },
  ],
};

const args = process.argv.slice(2);
if (args[0] === "--example") { console.log(JSON.stringify(EXAMPLE, null, 2)); process.exit(0); }
if (!args[0] || args[0].startsWith("-")) {
  console.error("usage: sermon-deck <deck.json> [out.pptx]   |   sermon-deck --example");
  process.exit(64);
}

let pptxgen, JSZip;
try {
  pptxgen = require("pptxgenjs");
  JSZip = require("jszip");
} catch {
  console.error(`pptxgenjs is not installed. Run:  npm install --prefix "${__dirname}"`);
  process.exit(2);
}

const fail = (msg) => { console.error(msg); process.exit(1); };
let deck;
try { deck = JSON.parse(fs.readFileSync(args[0], "utf8")); } catch (e) { fail(`Cannot read ${args[0]}: ${e.message}`); }
if (!deck.title || !Array.isArray(deck.slides) || !deck.slides.length) fail("deck.json needs a title and a non-empty slides array.");

const slug = (s) => s.normalize("NFKD").replace(/[^\x00-\x7F]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const OUT = path.resolve(args[1] || path.join(path.dirname(args[0]), deck.file || slug(deck.title) + ".pptx"));

const THEME = {
  name: "Lautan Kaca", headFontFace: "Cambria", bodyFontFace: "Calibri",
  colors: { dk1: "0B1026", lt1: "EEF1F7", dk2: "172048", lt2: "AAB4CC", accent1: "E8B44A", accent2: "71CDF4",
            accent3: "BC7AF5", accent4: "F2707A", accent5: "8593AD", accent6: "2A3566", hlink: "71CDF4", folHlink: "BC7AF5" },
  ...(deck.theme || {}),
};
const SLOTS = ["dk1", "lt1", "dk2", "lt2", "accent1", "accent2", "accent3", "accent4", "accent5", "accent6", "hlink", "folHlink"];
for (const k of SLOTS) if (!/^[0-9A-Fa-f]{6}$/.test(String(THEME.colors[k]))) fail(`theme.colors.${k} must be six hex digits with no "#".`);

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = deck.title;
if (deck.author) pres.author = deck.author;
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const BG = C.text1, INK = C.background1, CARD = C.text2, MUTED = C.background2, GOLD = C.accent1, BLUE = C.accent2;
const num = { x: 9.0, y: 5.15, w: 0.6, h: 0.3, fontSize: 10, color: MUTED, align: "right" };
const ph = (name, o) => ({ placeholder: { options: { name, type: name, ...o }, text: "" } });
pres.defineSlideMaster({ title: "Judul", background: { color: BG }, objects: [
  ph("title", { x: 0.8, y: 1.55, w: 8.4, h: 1.9, fontSize: 40, bold: true, color: INK, align: "center", valign: "middle" }),
  ph("body", { x: 0.8, y: 3.6, w: 8.4, h: 1.1, fontSize: 18, color: GOLD, align: "center", valign: "top" }) ] });
pres.defineSlideMaster({ title: "Gerakan", background: { color: CARD }, slideNumber: num, objects: [
  ph("title", { x: 3.7, y: 1.5, w: 5.7, h: 1.6, fontSize: 38, bold: true, color: INK, align: "left", valign: "bottom" }),
  ph("body", { x: 3.7, y: 3.25, w: 5.7, h: 1.4, fontSize: 18, color: MUTED, align: "left", valign: "top" }) ] });
pres.defineSlideMaster({ title: "Ayat", background: { color: BG }, slideNumber: num, objects: [
  { rect: { x: 0.6, y: 1.3, w: 8.8, h: 3.25, fill: { color: CARD } } },
  ph("title", { x: 0.6, y: 0.4, w: 8.8, h: 0.75, fontSize: 28, bold: true, color: GOLD, align: "left", valign: "middle" }),
  ph("body", { x: 1.75, y: 1.45, w: 7.4, h: 2.95, fontSize: 24, color: INK, align: "left", valign: "middle" }) ] });
pres.defineSlideMaster({ title: "Pokok", background: { color: BG }, slideNumber: num, objects: [
  ph("title", { x: 0.6, y: 0.4, w: 8.8, h: 0.95, fontSize: 30, bold: true, color: GOLD, align: "left", valign: "middle" }),
  ph("body", { x: 1.75, y: 1.6, w: 7.6, h: 3.0, fontSize: 26, color: INK, align: "left", valign: "middle" }) ] });
pres.defineSlideMaster({ title: "Gagasan", background: { color: CARD }, slideNumber: num, objects: [
  ph("title", { x: 0.8, y: 0.5, w: 8.4, h: 0.6, fontSize: 18, bold: true, color: GOLD, align: "center", valign: "middle" }),
  ph("body", { x: 0.9, y: 1.3, w: 8.2, h: 3.4, fontSize: 32, color: INK, align: "center", valign: "middle" }) ] });

let sec = null;
const warnings = [];
const add = (masterName) => pres.addSlide(sec ? { masterName, sectionTitle: sec } : { masterName });
const section = (t) => { sec = t; pres.addSection({ title: t }); };
const badge = (s, txt, x, y, d, fs_, name) => {
  s.addShape(pres.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color: GOLD }, objectName: name + " lingkaran" });
  s.addText(String(txt), { x, y, w: d, h: d, align: "center", valign: "middle", fontSize: fs_, bold: true, color: BG, fontFace: "Cambria", margin: 0, isTextBox: true, objectName: name });
};
// Sizes are passed on the runs: a placeholder's own font size wins over a string's options.
const plain = (arr, size) => arr.map((t, i) => ({ text: t, options: { breakLine: i < arr.length - 1, paraSpaceAfter: 12, fontSize: size } }));
// "**words**" inside a line come out bold and gold.
const rich = (arr, size) => arr.flatMap((line, i) => {
  const parts = line.split(/\*\*(.+?)\*\*/).map((t, k) => ({ t, gold: k % 2 === 1 })).filter((p) => p.t);
  return parts.map((p, k) => ({ text: p.t, options: {
    fontFace: "Cambria", fontSize: size, ...(p.gold ? { bold: true, color: GOLD } : {}),
    ...(k === parts.length - 1 && i < arr.length - 1 ? { breakLine: true, paraSpaceAfter: 12 } : {}) } }));
});
const need = (sl, i, ...keys) => { for (const k of keys) if (sl[k] === undefined || sl[k] === "") fail(`Slide ${i + 1} (${sl.type}) has no "${k}".`); };

const BUILD = {
  title(sl, i) {
    need(sl, i, "title");
    const s = add("Judul"); s.addText(sl.title, { placeholder: "title" });
    if (sl.lines) s.addText(plain(sl.lines, sl.size || 20), { placeholder: "body" });
    if (sl.glyph) badge(s, sl.glyph, 4.6, 0.55, 0.8, 34, "Not");
    return s;
  },
  verse(sl, i) {
    need(sl, i, "title", "text", "ref");
    const s = add("Ayat"); s.addText(sl.title, { placeholder: "title" });
    const size = sl.size || (sl.text.length < 150 ? 32 : sl.text.length < 215 ? 28 : 24);
    if (sl.text.length > 300 && !sl.size) warnings.push(`Slide ${i + 1}: the verse is ${sl.text.length} characters and will overflow at 24pt; split it over two slides.`);
    s.addText([{ text: sl.text, options: { fontFace: "Cambria", fontSize: size } }], { placeholder: "body" });
    badge(s, "“", 0.8, 1.5, 0.75, 40, "Tanda kutip");
    s.addText(sl.ref, { x: 0.6, y: 4.7, w: 8.2, h: 0.4, fontSize: 16, bold: true, color: BLUE, align: "left", margin: 0, isTextBox: true, objectName: "Rujukan" });
    return s;
  },
  point(sl, i) {
    need(sl, i, "title", "lines");
    const s = add("Pokok"); s.addText(sl.title, { placeholder: "title" });
    const size = sl.size || 28;
    if (sl.lines.join(" ").length > 170 && !sl.size) warnings.push(`Slide ${i + 1}: ${sl.lines.join(" ").length} characters of points at ${size}pt may overflow; shorten or set "size".`);
    s.addText(plain(sl.lines, size), { placeholder: "body" });
    if (sl.glyph) badge(s, sl.glyph, 0.7, 2.7, 0.8, 30, "Penanda");
    return s;
  },
  movement(sl, i) {
    need(sl, i, "no", "title");
    section(`${sl.no}. ${sl.title}`);
    const s = add("Gerakan"); s.addText(sl.title, { placeholder: "title" });
    if (sl.sub) s.addText([{ text: sl.sub, options: { fontSize: 22 } }], { placeholder: "body" });
    badge(s, sl.no, 0.9, 1.45, 2.3, 110, "Nomor gerakan");
    return s;
  },
  idea(sl, i) {
    need(sl, i, "title");
    const lines = sl.lines || deck.bigIdea;
    if (!lines) fail(`Slide ${i + 1} (idea) has no "lines" and the deck has no "bigIdea".`);
    const s = add("Gagasan"); s.addText(sl.title, { placeholder: "title" });
    s.addText(rich(lines, sl.size || 32), { placeholder: "body" });
    return s;
  },
};

let count = 0;
deck.slides.forEach((sl, i) => {
  if (sl.section) { section(sl.section); if (!sl.type) return; }
  const fn = BUILD[sl.type];
  if (!fn) fail(`Slide ${i + 1}: unknown type ${JSON.stringify(sl.type)}. Types: ${Object.keys(BUILD).join(", ")}.`);
  const s = fn(sl, i);
  if (sl.note) s.addNotes(sl.note);
  count++;
});

// pptxgenjs writes Office's stock palette; put the deck's own colors and name in the theme part.
async function applyTheme(file) {
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  const part = "ppt/theme/theme1.xml";
  const name = String(THEME.name).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const scheme = `<a:clrScheme name="${name}">` + SLOTS.map((k) => `<a:${k}><a:srgbClr val="${String(THEME.colors[k]).toUpperCase()}"/></a:${k}>`).join("") + "</a:clrScheme>";
  const xml = (await zip.file(part).async("string"))
    .replace(/<a:clrScheme\b[\s\S]*?<\/a:clrScheme>/, () => scheme)
    .replace(/(<a:(?:theme|fontScheme)\b[^>]*?\bname=")[^"]*"/g, (_, head) => `${head}${name}"`);
  if (!xml.includes(scheme)) throw new Error("the theme part has no color scheme to replace");
  // Rewritten without folder entries: decks carrying them have failed to open from a cloud drive.
  const out = new JSZip();
  for (const [name, entry] of Object.entries(zip.files)) {
    if (!entry.dir) out.file(name, name === part ? xml : await entry.async("nodebuffer"), { createFolders: false });
  }
  fs.writeFileSync(file, await out.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT);
  console.log(`${OUT}  (${count} slides)`);
  for (const w of warnings) console.error("WARNING: " + w);
})().catch((e) => fail(`Could not write ${OUT}: ${e.message}`));
