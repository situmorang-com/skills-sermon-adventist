// ============================================================================
// WORKED EXAMPLE — the Q3 2026 Lesson 10 teaching deck, Indonesian, adults.
//
// Copy this and replace the content. The parts worth keeping are the helpers
// (kick / head / card / divider / ask) and the constants: they encode the
// layout decisions in references/teaching-deck.md, including the 20pt floor,
// the labelled-card motif, and the text-fit maths.
//
// Two traps this file already avoids, both of which shipped once:
//   1. `card()` RETURNS the next free y. Use it. Hardcoding a position after a
//      variable-height card prints captions through source lines.
//   2. No zero-height shapes. One renders as a hairline rule under the title,
//      which is the accent-line antipattern the pptx skill bans.
//
// Setup in the working directory:
//   npm install pptxgenjs
//   python3 -m venv .venv && .venv/bin/pip install defusedxml lxml Pillow "markitdown[pptx]"
// Then validate and LOOK at every slide before shipping.
//
// TWO THINGS TO CHANGE FIRST, or it writes the wrong file from missing data:
//   - the writeFile path at the bottom still points at 2026-09-05's folder
//   - it requires ./slide-verses.json, a flat {"2Kor3:2": "text", ...} map you
//     build by fetching the week's verses (bolls.life for TB and KJV; strip
//     <sup>...</sup> INCLUDING its contents, or KJV marginal notes leak in)
// ============================================================================
// Lesson 10 — day-by-day teaching deck, Indonesian.
// Every quote is verbatim with a verified refcode. Nothing invented.
// Projector-first: no run below 20pt.
const pptxgen = require('pptxgenjs');
const V = require('./slide-verses.json');

const CLAY="B85042", GOLD="8A6410", SAGE="4F6F5E", INK="2B2B2B", MUTE="6B6B6B",
      CREAM="F4EFE7", PALE="F6DCD5";
const HEAD="Cambria", BODY="Calibri";

const p = new pptxgen();
p.layout = "LAYOUT_WIDE";
p.author = "Edmund Situmorang";
p.title  = "Pelajaran 10 — Pelayanan Kristen yang Sejati";

const W=13.3, M=0.7, CW=W-2*M;

const dark = s => { s.background = { color: CLAY }; };
function kick(s, t, c){
  s.addText(t, { x:M, y:0.42, w:CW, h:0.4, isTextBox:true, margin:0, fontFace:BODY,
    fontSize:20, bold:true, charSpacing:2, color:c||CLAY });
}
function head(s, t, size){
  s.addText(t, { x:M, y:0.95, w:CW, h:0.85, isTextBox:true, margin:0, fontFace:HEAD,
    fontSize:size||36, bold:true, color:INK, valign:"top" });
}
function lines(txt, fs, pad){
  const cpl = Math.max(20, Math.floor((CW-2*pad)*124/fs));
  return Math.max(1, Math.ceil(txt.length/cpl));
}
// One labelled card. The label is the motif; no edge stripes, no rules.
function card(s, y, label, labelColor, txt, source, fs){
  fs = fs||24; const pad=0.34;
  const n = lines(txt, fs, pad);
  const lh = (fs*1.42)/72;
  const h = Math.min(n*lh + pad + 0.52, 7.5 - y - 1.05);
  s.addShape(p.ShapeType.roundRect, { x:M, y, w:CW, h, fill:{color:CREAM}, rectRadius:0.08 });
  s.addText(label, { x:M+pad, y:y+0.2, w:CW-2*pad, h:0.34, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:20, bold:true, charSpacing:2, color:labelColor });
  s.addText(txt, { x:M+pad, y:y+0.62, w:CW-2*pad, h:h-0.85, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:fs, color:INK, lineSpacing:Math.round(fs*1.42), valign:"top" });
  if (source)
    s.addText(source, { x:M+pad, y:y+h+0.14, w:CW-2*pad, h:0.4, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:20, bold:true, color:labelColor });
  return y + h + (source?0.62:0.28);
}
function divider(s, day, date, title, minutes){
  dark(s);
  s.addText(day.toUpperCase() + "  ·  " + date, { x:M, y:2.0, w:CW, h:0.5, isTextBox:true,
    margin:0, fontFace:BODY, fontSize:22, bold:true, charSpacing:3, color:PALE });
  s.addText(title, { x:M, y:2.65, w:CW, h:1.7, isTextBox:true, margin:0, fontFace:HEAD,
    fontSize:46, bold:true, color:"FFFFFF", lineSpacing:54 });
  s.addText(minutes, { x:M, y:4.7, w:CW, h:0.5, isTextBox:true, margin:0, fontFace:BODY,
    fontSize:24, color:PALE });
}
function ask(s, label, q, sub){
  dark(s); kick(s, label, PALE);
  s.addText(q, { x:M, y:1.5, w:CW, h:2.4, isTextBox:true, margin:0, fontFace:HEAD,
    fontSize:36, bold:true, color:"FFFFFF", lineSpacing:46 });
  if (sub) s.addText(sub, { x:M, y:4.2, w:CW, h:1.4, isTextBox:true, margin:0, fontFace:BODY,
    fontSize:26, color:PALE, lineSpacing:34 });
}
let s;

/* ── 1 title ─────────────────────────────────────────── */
s = p.addSlide(); dark(s);
s.addText("PELAJARAN 10  ·  TRIWULAN III 2026", { x:M, y:1.6, w:CW, h:0.5, isTextBox:true,
  margin:0, fontFace:BODY, fontSize:22, bold:true, charSpacing:3, color:PALE });
s.addText("Pelayanan Kristen\nyang Sejati", { x:M, y:2.2, w:CW, h:2.2, isTextBox:true,
  margin:0, fontFace:HEAD, fontSize:54, bold:true, color:"FFFFFF", lineSpacing:60 });
s.addText("2 Korintus 3–7   ·   Sabat, 5 September 2026", { x:M, y:4.8, w:CW, h:0.5,
  isTextBox:true, margin:0, fontFace:BODY, fontSize:24, color:PALE });
s.addNotes("Deck ini berjalan HARI DEMI HARI, sekitar 7 menit per hari, berbeda dari rencana di penuntun (yang memusatkan pada dua pertanyaan panjang). Pilih salah satu, jangan campur.\n\nProfil kelas dewasa: musuhnya PENGENALAN, bukan ketidakmengertian. Ada pengurus di ruangan, jadi minta BACAAN sebelum minta PUTUSAN.\n\nSemua kutipan di deck ini verbatim dengan sumber yang sudah diperiksa. Boleh dibacakan keras-keras.");

/* ── 2 memory text ───────────────────────────────────── */
s = p.addSlide(); kick(s, "AYAT HAFALAN"); head(s, "2 Korintus 4:8-10", 34);
card(s, 1.85, "TERJEMAHAN BARU", CLAY,
  V["2Kor4:8"]+" "+V["2Kor4:9"]+" "+V["2Kor4:10"], "2 Korintus 4:8-10", 22);
s.addNotes("Bacakan bersama. Empat pasang: ditindas/tidak terjepit, habis akal/tidak putus asa, dianiaya/tidak ditinggalkan, dihempaskan/tidak binasa.\n\nYang TIDAK dikatakan: penindasannya berhenti.");

/* ── 3 the week at a glance ──────────────────────────── */
s = p.addSlide(); kick(s, "PETA PEKAN INI"); head(s, "Lima hari, satu pertanyaan", 36);
const map = [
  ["Minggu","Buah pelayanan yang sejati","Bukti pelayanan adalah orang, bukan kertas"],
  ["Senin","Penderitaan dan kemuliaan","Harta di dalam bejana tanah liat"],
  ["Selasa","Pelayanan pendamaian","Allah mendamaikan, lalu menyerahkannya ke tangan kita"],
  ["Rabu","Panggilan kepada kekudusan","Keterpisahan, dan alasannya"],
  ["Kamis","Penghiburan dan sukacita","Lingkaran yang dibuka pasal 1 ditutup di pasal 7"],
];
let y = 1.9;
map.forEach((r,i)=>{
  s.addShape(p.ShapeType.ellipse, { x:M, y:y+0.02, w:0.44, h:0.44, fill:{color:CLAY} });
  s.addText(String(i+1), { x:M, y:y+0.02, w:0.44, h:0.44, isTextBox:true, margin:0,
    align:"center", valign:"middle", fontFace:HEAD, fontSize:20, bold:true, color:"FFFFFF" });
  s.addText(r[0], { x:M+0.62, y:y+0.03, w:1.5, h:0.42, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:21, bold:true, color:CLAY });
  s.addText(r[1], { x:M+2.15, y:y+0.03, w:4.0, h:0.42, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:22, bold:true, color:INK });
  s.addText(r[2], { x:M+6.3, y:y+0.05, w:CW-6.3, h:0.42, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:20, color:MUTE });
  y += 0.78;
});
s.addNotes("Tunjukkan peta ini sekali di awal supaya kelas tahu ke mana pekan ini pergi. Jangan dibahas, cukup dibacakan cepat.\n\nRabu adalah hari yang menanggung beban. Kalau waktu habis, hari itu yang tidak boleh dipotong.");

/* ══════════════════ MINGGU ══════════════════ */
s = p.addSlide(); divider(s, "Minggu", "30 Agustus", "Buah Pelayanan\nyang Sejati", "2 Korintus 3:1-9   ·   sekitar 7 menit");
s.addNotes("Tesis pekan ini. Paulus mendefinisikan ulang apa yang dihitung sebagai BUKTI.");

s = p.addSlide(); kick(s, "MINGGU · BACALAH BERSAMA"); head(s, "2 Korintus 3:1-3", 34);
card(s, 1.85, "TERJEMAHAN BARU", CLAY, V["2Kor3:1"]+" "+V["2Kor3:2"]+" "+V["2Kor3:3"],
  "2 Korintus 3:1-3", 22);
s.addNotes("Ayat 2 adalah kalimatnya: KAMULAH SURAT PUJIAN KAMI.\n\nAyat 5 adalah pagarnya: kesanggupan itu dari Allah. Tanpa ayat 5, ayat 2 bisa dibaca sebagai pujian bagi pelayan.");

s = p.addSlide(); kick(s, "MINGGU · LATAR"); head(s, "Surat rekomendasi adalah alat kuasa", 32);
card(s, 1.85, "DUNIA YUNANI-ROMAWI", SAGE,
  "Seorang pengembara membawa surat dari sahabatnya untuk meminta kebaikan: penginapan, pertolongan, pekerjaan. Penulis surat menjamin watak si pembawa, dan penerima surat merasa BERKEWAJIBAN memperlakukan si pembawa seperti ia akan memperlakukan si penulis. Surat itu memindahkan kehormatan.",
  "Komentar Guru resmi, mengutip Lexham Research Commentary pada 2 Kor. 3:1-3", 23);
s.addNotes("Ini mengubah bobot ayat 2. Paulus TIDAK sedang merendah. Ia menolak seluruh sistem: ia tidak punya surat, dan ia mengatakan orang yang berubah adalah mata uang yang lebih tinggi.\n\nKorintus menghargai kehormatan, status, dan pembicara fasih. Para penentang Paulus cocok dengan pola itu.");

s = p.addSlide(); kick(s, "MINGGU · ROH NUBUAT"); head(s, "Buktinya tertulis pada hati", 34);
card(s, 1.8, "ROH NUBUAT", GOLD,
  "“Pertobatan orang berdosa dan pengudusan mereka melalui kebenaran adalah bukti terkuat yang dapat dimiliki seorang pelayan bahwa Allah telah memanggilnya kepada pelayanan. Bukti kerasulannya tertulis pada hati orang-orang yang bertobat, dan disaksikan oleh hidup mereka yang diperbarui.”",
  "Ellen G. White, The Acts of the Apostles, hlm. 328  ·  terjemahan kerja", 23);
s.addNotes("Pelajaran mencetak kutipan ini di bagian Sabat Sore. Ia mengatakan hal yang sama dengan 2 Kor 3:2 dengan kata lain.\n\nBerhenti setelah 'hidup mereka yang diperbarui'. Kalimat berikutnya tentang pelayan yang dikuatkan, dan itu mengalihkan perhatian dari orangnya kembali ke pelayannya.");

s = p.addSlide(); kick(s, "MINGGU · ILUSTRASI"); head(s, "Perempuan yang meninggalkan tempayannya", 30);
card(s, 1.75, "ILUSTRASI", CLAY,
  "“Meninggalkan tempayannya, ia kembali ke kota untuk membawa berita itu kepada orang lain. Yesus tahu mengapa ia pergi. Meninggalkan tempayan itu berbicara dengan jelas tentang akibat kata-kata-Nya... Dengan hati yang melimpah kegembiraan, ia bergegas pergi untuk menyampaikan kepada orang lain terang berharga yang telah ia terima.”",
  "Ellen G. White, The Desire of Ages, hlm. 191  ·  terjemahan kerja", 23);
s.addNotes("Inilah gambar 'surat pujian' yang hidup. Perempuan Samaria itu TIDAK punya kredensial: bukan orang Israel, hidup dalam dosa terbuka. Tetapi hidupnya yang berubah dapat dibaca oleh seluruh kota.\n\nHubungkan langsung: Paulus tidak punya surat, ia punya orang. Yesus tidak memberi perempuan itu surat, Ia memberinya air hidup, dan kota itu membacanya.");

s = p.addSlide();
ask(s, "PERTANYAAN · MINGGU", "Siapa surat pujian Anda?",
  "Kalau bukti pelayanan adalah orang dan bukan kertas — sebutkan satu nama dalam hati. Jangan disebut keras.");
s.addNotes("Di ruangan ini ada orang yang sudah memegang jabatan puluhan tahun. Pertanyaan ini tidak bisa dijawab dengan riwayat jabatan.\n\nKebanyakan akan diam. Sebagian menyebut anak atau cucu, itu sah. Sebagian sadar mereka tidak punya nama — itu BUKAN kegagalan pertanyaan, itu pelajarannya. Jangan buru-buru menghibur.\n\nKalau ada yang menutup dengan 'yang penting kita setia melayani', buka lagi: 'Paulus bisa menyebut satu jemaat. Bukan kesetiaannya, tetapi mereka.'");

/* ══════════════════ SENIN ══════════════════ */
s = p.addSlide(); divider(s, "Senin", "31 Agustus", "Penderitaan\ndan Kemuliaan", "2 Korintus 4:7-18   ·   sekitar 7 menit");
s.addNotes("Harga pertama. Bejana tanah liat, dan empat pasang yang tidak pernah mengatakan penderitaannya berhenti.");

s = p.addSlide(); kick(s, "SENIN · BACALAH BERSAMA"); head(s, "2 Korintus 4:7", 34);
const a47 = card(s, 1.85, "TERJEMAHAN BARU", CLAY, V["2Kor4:7"], "2 Korintus 4:7", 26);
s.addText("Hartanya bukan Paulus. Bejananya memang tanah liat.", { x:M, y:a47+0.2, w:CW, h:0.7,
  isTextBox:true, margin:0, fontFace:HEAD, fontSize:28, bold:true, italic:true, color:CLAY });
s.addNotes("SDABC pada 4:7: hartanya adalah pengenalan akan kemuliaan Allah di dalam wajah Yesus Kristus. Tanpa pengenalan dan kuasa itu, bejana manusia yang lemah akan hancur.");

s = p.addSlide(); kick(s, "SENIN · EMPAT PASANG"); head(s, "Perhatikan apa yang tidak dikatakan", 34);
const four = [["Ditindas","tidak terjepit"],["Habis akal","tidak putus asa"],
               ["Dianiaya","tidak ditinggalkan"],["Dihempaskan","tidak binasa"]];
y = 2.0;
four.forEach((f,i)=>{
  s.addShape(p.ShapeType.roundRect, { x:M, y, w:CW, h:0.72, fill:{color:CREAM}, rectRadius:0.06 });
  s.addText(f[0], { x:M+0.35, y:y+0.14, w:4.2, h:0.44, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:24, bold:true, color:INK });
  s.addText("namun  " + f[1], { x:M+4.7, y:y+0.15, w:CW-5.1, h:0.44, isTextBox:true,
    margin:0, fontFace:BODY, fontSize:24, color:CLAY });
  y += 0.85;
});
s.addText("Paulus tidak berkata penindasannya berhenti.", { x:M, y:5.65, w:CW, h:0.6,
  isTextBox:true, margin:0, fontFace:HEAD, fontSize:26, bold:true, italic:true, color:CLAY });
s.addNotes("SDABC pada 4:8: keempat pasang ini menggambarkan kelemahan bejana tanah di satu sisi, dan keunggulan kuasa Allah di sisi lain. Setiap orang Kristen berada di tengah peperangan panjang antara Kristus dan Setan.\n\nAda jarak antara 'tidak binasa' dan 'baik-baik saja', dan sebagian anggota hidup di jarak itu bertahun-tahun.");

s = p.addSlide(); kick(s, "SENIN · SUARA DARI SEJARAH"); head(s, "John Huss, dari dalam penjara", 32);
card(s, 1.75, "KUTIPAN", SAGE,
  "“Ia adalah Allah, dan kita ciptaan-Nya; Ia Tuhan, dan kita hamba-Nya; Ia Penguasa dunia, dan kita manusia yang hina — namun Ia menderita! Mengapa kita tidak boleh menderita juga, terutama ketika penderitaan itu memurnikan kita?”",
  "John Huss, surat kepada sahabat-sahabatnya di Praha, 1414  ·  dikutip dalam The Great Controversy, hlm. 105", 24);
s.addNotes("PENTING: ini perkataan HUSS, bukan perkataan Ellen G. White. Ia mengutipnya dari Bonnechose. Katakan 'Huss berkata, sebagaimana dikutip dalam The Great Controversy'.\n\nKonteksnya: Huss menulis surat ini sebelum berangkat ke Konsili Konstanz, tahu ia mungkin tidak kembali. Ia dibakar di tiang pancang tahun 1415. Jadi ini bukan teori tentang penderitaan; ini ditulis oleh orang yang sedang berjalan ke arahnya.\n\nPelajaran hari Senin sendiri mengutip kalimat ini.");

s = p.addSlide();
ask(s, "PERTANYAAN · SENIN", "Di mana batas antara “tidak binasa” dan “baik-baik saja”?",
  "Pernahkah orang mengatakan Anda baik-baik saja, padahal Anda hanya belum binasa?");
s.addNotes("Kelas ini akan menjawab dengan kesaksian. Minta BACAAN dulu, pengalaman kemudian.\n\nKalau ada yang membawa 2 Kor 4:17 ('penderitaan ringan yang sekejap'): Paulus tidak berkata penderitaannya kecil, ia berkata ringan DIBANDINGKAN. Dan yang menulis kalimat itu dicambuk lima kali. Tanyakan: siapa yang berhak mengatakan kalimat itu kepada orang lain?");

/* ══════════════════ SELASA ══════════════════ */
s = p.addSlide(); divider(s, "Selasa", "1 September", "Pelayanan\nPendamaian", "2 Korintus 5:11-21   ·   sekitar 7 menit");
s.addNotes("Memberi nama pada pekerjaannya. Bukan sekadar memberitakan, melainkan mendamaikan.");

s = p.addSlide(); kick(s, "SELASA · BACALAH BERSAMA"); head(s, "2 Korintus 5:18-20", 34);
card(s, 1.85, "TERJEMAHAN BARU", CLAY, V["2Kor5:18"]+" "+V["2Kor5:19"]+" "+V["2Kor5:20"],
  "2 Korintus 5:18-20", 22);
s.addNotes("Urutannya penting: Allah mendamaikan LEBIH DAHULU, lalu MEMBERIKAN pelayanan pendamaian itu kepada kita. Kita tidak menciptakan pendamaian; kita meneruskannya.");

s = p.addSlide(); kick(s, "SELASA · SATU KATA"); head(s, "Utusan", 40);
const aPre = card(s, 1.7, "BAHASA YUNANI · presbeuō", SAGE,
  "Secara harfiah “menjadi lebih tua”, lalu “menjadi tua-tua”, lalu “menjadi utusan”. Kata ini menandai utusan sebagai orang yang dibedakan oleh kehormatan dan pengalaman, dan karena itu diberi wewenang. Utusan Kristus menjadi utusan karena keterikatannya lebih dahulu kepada Dia.",
  "SDA Bible Commentary, jilid 6, pada 2 Korintus 5:20  ·  parafrase", 23);
s.addText("Wibawa seorang utusan bukan miliknya sendiri.", { x:M, y:aPre+0.2, w:CW, h:0.7,
  isTextBox:true, margin:0, fontFace:HEAD, fontSize:26, bold:true, italic:true, color:CLAY });
s.addNotes("Ini jawaban untuk anggota yang merasa tidak cukup layak untuk melayani. Wibawa utusan datang dari yang mengutus, bukan dari dirinya.\n\nKalau seorang utusan salah berbicara, yang tercemar adalah nama yang mengutusnya. Itu sisi beratnya.");

s = p.addSlide(); kick(s, "SELASA · ROH NUBUAT"); head(s, "Pekerjaan itu diserahkan kepada kita", 32);
card(s, 1.8, "ROH NUBUAT", GOLD,
  "“Sebagai gereja, kita telah menerima terang yang besar. Terang ini dipercayakan Tuhan kepada kita untuk kebaikan dan berkat dunia. Kepada kita telah diberikan pelayanan pendamaian. Dengan kuasa dari tempat tinggi kita harus memohon kepada manusia supaya diperdamaikan dengan Allah.”",
  "Ellen G. White, Letter 32, 1903  ·  dikutip dalam pelajaran hari Jumat  ·  terjemahan kerja", 23);
s.addNotes("Kutipan ini ada di bagian Pendalaman hari Jumat, jadi kelas mungkin sudah membacanya.\n\nPerhatikan kata 'memohon' — sama dengan 2 Kor 5:20. Pendamaian bukan pengumuman, melainkan permohonan.");

s = p.addSlide();
ask(s, "PERTANYAAN · SELASA", "Kalau kita utusan, siapa yang sedang menunggu dijemput?",
  "Sebutkan satu hubungan yang rusak — di jemaat atau di rumah — yang menunggu seseorang memulai langkah pertama.");
s.addNotes("Pendamaian di pasal ini punya dua arah: vertikal (manusia dengan Allah) dan horizontal (manusia dengan manusia). Komentar Guru resmi menyebut bukti orang sudah diperdamaikan dengan Allah adalah bahwa mereka mencari pendamaian satu dengan yang lain.\n\nJangan biarkan jawabannya berhenti pada 'orang di luar gereja'. Tanyakan tentang di dalam.");

/* ══════════════════ RABU ══════════════════ */
s = p.addSlide(); divider(s, "Rabu", "2 September", "Panggilan\nkepada Kekudusan", "2 Korintus 6:11–7:1   ·   sekitar 10 menit  ·  hari yang menanggung beban");
s.addNotes("Hari yang paling mungkin diperdebatkan, karena kelas sudah punya jawaban sebelum ayatnya dibuka. Beri hari ini waktu paling banyak. Kalau harus memotong, potong hari lain.");

s = p.addSlide();
ask(s, "RABU · PEMBUKA", "“Jangan menjadi pasangan yang tidak seimbang.”",
  "Satu kalimat saja: selama ini, ayat itu tentang apa, dalam setiap khotbah yang pernah Anda dengar?");
s.addNotes("JANGAN jawab sendiri. Biarkan empat atau lima orang menjawab. Hampir pasti: pernikahan.\n\nItu memang SALAH SATU penerapannya, jadi jangan dibantah. Lanjut ke slide berikutnya.");

s = p.addSlide(); kick(s, "RABU · 2 KORINTUS 6:14-16"); head(s, "Lima pertentangan Paulus", 36);
const pairs=[["Kebenaran","Kedurhakaan"],["Terang","Gelap"],["Kristus","Belial"],
             ["Orang percaya","Orang tak percaya"],["Bait Allah","Berhala"]];
y = 1.95;
pairs.forEach((pr,i)=>{
  s.addShape(p.ShapeType.ellipse, { x:M, y, w:0.5, h:0.5, fill:{color:CLAY} });
  s.addText(String(i+1), { x:M, y, w:0.5, h:0.5, isTextBox:true, margin:0, align:"center",
    valign:"middle", fontFace:HEAD, fontSize:22, bold:true, color:"FFFFFF" });
  s.addText(pr[0], { x:M+0.72, y:y+0.02, w:3.7, h:0.45, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:24, bold:true, color:INK });
  s.addText("—", { x:M+4.45, y:y+0.02, w:0.5, h:0.45, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:24, color:MUTE, align:"center" });
  s.addText(pr[1], { x:M+5.05, y:y+0.02, w:4.4, h:0.45, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:24, color:MUTE });
  y += 0.7;
});
s.addText("Semuanya tentang kepada siapa Anda berpihak.", { x:M, y:5.6, w:CW, h:0.6,
  isTextBox:true, margin:0, fontFace:HEAD, fontSize:26, bold:true, italic:true, color:CLAY });
s.addNotes("Tidak satu pun dari lima ini tentang urusan rumah tangga. TAPI jangan berlebihan ke arah sebaliknya — lihat slide 'Dua kesalahan'.\n\nCameron (ssnet): 'orang tak percaya' TIDAK berarti 'bukan anggota gereja kita'. Paulus menyandingkannya dengan Belial. Yang dipersoalkan keberpihakan kepada Kristus, bukan kesepakatan pada setiap butir ajaran.");

s = p.addSlide(); kick(s, "RABU · ASAL GAMBARANNYA"); head(s, "Lembu dan keledai, satu bajak", 34);
const aUl = card(s, 1.8, "ULANGAN 22:10", SAGE, "“"+V["Ul22:10"]+"”", "Ulangan 22:10  ·  Terjemahan Baru", 26);
s.addText("Dua binatang dengan langkah dan kekuatan berbeda, terikat pada satu bajak. Itu bukan soal kebencian. Itu soal langkah yang tidak sama.",
  { x:M, y:aUl+0.2, w:CW, h:1.2, isTextBox:true, margin:0, fontFace:BODY, fontSize:26,
    color:INK, lineSpacing:34 });
s.addNotes("'Memikul kuk' adalah istilah pertanian, dan Ulangan 22:10 adalah asalnya. Cameron (ssnet) menunjukkan kaitan ini.\n\nGambaran ini menolong kelas melihat bahwa masalahnya bukan permusuhan, melainkan arah dan langkah yang tidak bisa disatukan.");

s = p.addSlide(); kick(s, "RABU · ALASANNYA"); head(s, "Kenapa harus terpisah", 34);
const a616 = card(s, 1.8, "TERJEMAHAN BARU", CLAY, V["2Kor6:16"], "2 Korintus 6:16", 24);
s.addText("Keterpisahan bukan aturan. Itu akibat dari siapa mereka.", { x:M, y:a616+0.2, w:CW, h:0.7,
  isTextBox:true, margin:0, fontFace:HEAD, fontSize:26, bold:true, italic:true, color:CLAY });
s.addNotes("Urutan seluruh bagian: hati yang terbuka (ayat 11), lima pertentangan (14-16), ALASANNYA (16b), janji (17-18), baru tuntutan (7:1).\n\nKeterpisahan datang SESUDAH keterbukaan dan SESUDAH janji, bukan sebelumnya. Itu yang membuatnya bukan daftar larangan.");

s = p.addSlide(); kick(s, "RABU · DUA KESALAHAN"); head(s, "Dua kesalahan yang sama besarnya", 34);
[["Terlalu sempit","“Ayat ini hanya tentang pernikahan.”"],
 ["Terlalu jauh","“Ayat ini bukan tentang pernikahan.”"]].forEach((c,i)=>{
  const x = M + i*(CW/2+0.15);
  s.addShape(p.ShapeType.roundRect, { x, y:1.85, w:CW/2-0.15, h:1.6, fill:{color:CREAM}, rectRadius:0.08 });
  s.addText(c[0], { x:x+0.3, y:2.0, w:CW/2-0.75, h:0.42, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:20, bold:true, charSpacing:1, color:CLAY });
  s.addText(c[1], { x:x+0.3, y:2.45, w:CW/2-0.75, h:0.9, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:23, color:INK, lineSpacing:30 });
});
s.addText("Larangan ini mencakup hubungan pernikahan, tetapi sama sekali tidak terbatas pada itu.",
  { x:M, y:3.95, w:CW, h:0.95, isTextBox:true, margin:0, fontFace:HEAD, fontSize:26,
    bold:true, color:INK, lineSpacing:34 });
s.addText("SDA Bible Commentary, jilid 6, pada 2 Korintus 6:14  ·  parafrase", { x:M, y:4.95,
  w:CW, h:0.4, isTextBox:true, margin:0, fontFace:BODY, fontSize:20, bold:true, color:CLAY });
s.addText("Pernikahan adalah satu penerapan, bukan batasnya.", { x:M, y:5.55, w:CW, h:0.6,
  isTextBox:true, margin:0, fontFace:BODY, fontSize:24, italic:true, color:MUTE });
s.addNotes("Bacakan sesudah kelas sempat menyempitkannya ke pernikahan, dan SEBELUM ada yang menyimpulkan bahwa pernikahan tidak termasuk.\n\nSDABC menjaga Anda dari dua kesalahan sekaligus. Ini kalimat yang paling berguna pekan ini.");

s = p.addSlide(); kick(s, "RABU · ROH NUBUAT"); head(s, "Kekudusan menghasilkan perbuatan", 32);
card(s, 1.8, "ROH NUBUAT", GOLD,
  "“Kekudusan hati dan kemurnian hidup adalah pokok-pokok besar pengajaran Kristus... Kekudusan akan membawa pemiliknya menjadi berbuah, dan berlimpah dalam segala perbuatan baik. Ia tidak akan pernah menjadi lelah dalam berbuat baik.”",
  "Ellen G. White, The Review and Herald, 7 September 1886  ·  terjemahan kerja", 23);
s.addNotes("Ini menyeimbangkan hari Rabu supaya keterpisahan tidak terdengar hanya sebagai daftar larangan. Kekudusan di sini BERBUAH, bukan menarik diri.\n\nSumber aslinya Review and Herald 1886. Pelajaran mencetak kalimat yang sama lewat buku susunan; yang di slide ini sumber aslinya.");

s = p.addSlide();
ask(s, "PERTANYAAN · RABU", "Kalau alasannya adalah bahwa kamu bait Allah — keterpisahan itu melindungi apa?",
  "Dan sebutkan satu hal dalam pekan Anda sendiri yang benar-benar akan tersentuh olehnya.");
s.addNotes("Ini pertanyaan terpenting pekan ini. Diamlah empat sampai enam detik.\n\nYang akan muncul: pernikahan dulu, lalu usaha bersama, lalu hiburan. Yang jarang muncul dan paling dekat dengan teksnya: IBADAH, kepada siapa saya berpihak.\n\nKalau ada yang menyempitkannya kembali ke pernikahan, JANGAN Anda yang memperbaiki. Minta orang kedua membacakan ayat 16 dan mengatakan alasan apa yang diberikan di sana.\n\nKeberatan yang akan datang: 'kalau harus terpisah, bagaimana kita menginjili? Yesus makan bersama orang berdosa.' Jawabnya: lima pertentangan itu soal PERSEKUTUAN dan KEBERPIHAKAN, bukan soal kehadiran. Paulus sendiri tinggal 18 bulan di Korintus.");

/* ══════════════════ KAMIS ══════════════════ */
s = p.addSlide(); divider(s, "Kamis", "3 September", "Penghiburan\ndan Sukacita", "2 Korintus 7:2-16   ·   sekitar 6 menit");
s.addNotes("Menutup lingkaran yang dibuka pasal 1. Titus datang, kabarnya baik, dan Paulus meledak.");

s = p.addSlide(); kick(s, "KAMIS · BACALAH BERSAMA"); head(s, "2 Korintus 7:5-7", 34);
card(s, 1.85, "TERJEMAHAN BARU", CLAY, V["2Kor7:5"]+" "+V["2Kor7:6"]+" "+V["2Kor7:7"],
  "2 Korintus 7:5-7", 22);
s.addNotes("Kata parakaleo dan paraklesis muncul TUJUH kali di pasal 7. Pasal 1 dibuka dengan penghiburan; pasal 7 menutup dengan penghiburan.\n\nDan perhatikan: Allah menghibur Paulus lewat KEDATANGAN SEORANG ORANG, bukan lewat penglihatan. Penghiburan-Nya datang dengan kaki.");

s = p.addSlide(); kick(s, "KAMIS · ROH NUBUAT"); head(s, "Siapa yang paling bisa menghibur", 32);
card(s, 1.8, "ROH NUBUAT", GOLD,
  "“Mereka yang telah menanggung dukacita terbesar sering kali adalah orang yang membawa penghiburan terbesar bagi orang lain, membawa sinar matahari ke mana pun mereka pergi. Orang-orang seperti itu telah ditempa dan dilembutkan oleh penderitaan mereka.”",
  "Ellen G. White, dikutip dalam God’s Amazing Grace, hlm. 122  ·  terjemahan kerja", 23);
s.addNotes("Hubungkan kembali ke hari Senin: bejana tanah liat yang pecah adalah bejana yang bisa menghibur.\n\nCatatan atribusi: God's Amazing Grace adalah buku renungan SUSUNAN, disusun setelah Ellen White meninggal. Kalimat ini aslinya dari In Heavenly Places, hlm. 273. Katakan 'dikutip dalam', bukan 'ditulis dalam'.");

s = p.addSlide();
ask(s, "PERTANYAAN · KAMIS", "Allah menghibur Paulus dengan mengirim seseorang.",
  "Siapa yang pernah dikirim kepada Anda? Dan kepada siapa Anda mungkin sedang dikirim minggu ini?");
s.addNotes("Ini pertanyaan yang paling mudah dijawab pekan ini, jadi bagus untuk mengangkat suasana sebelum penerapan.\n\nSambungkan ke penerapan: nama yang muncul di sini sering kali nama yang sama untuk 'siapa surat pujian Anda'.");

/* ══════════════════ PENUTUP ══════════════════ */
s = p.addSlide(); kick(s, "PENERAPAN");
s.addText("Satu nama.", { x:M, y:1.3, w:CW, h:1.0, isTextBox:true, margin:0, fontFace:HEAD,
  fontSize:48, bold:true, color:CLAY });
s.addText([
  { text:"Orang yang hidupnya berubah karena Anda pernah ada di sana.", options:{bullet:true, breakLine:true} },
  { text:"Kalau tidak ada namanya: satu orang yang minggu depan bisa mulai menjadi nama itu.", options:{bullet:true, breakLine:true} },
  { text:"Hubungi dia sebelum Sabat depan.", options:{bullet:true} },
], { x:M, y:2.5, w:CW, h:2.5, isTextBox:true, margin:0, fontFace:BODY, fontSize:26,
     color:INK, lineSpacing:36, paraSpaceAfter:14 });
s.addNotes("Cukup konkret untuk DITOLAK. Sebagian akan berkata mereka tidak punya nama. Itu jawaban jujur, dan itu pelajaran pekan ini.\n\nJangan tutup dengan ringkasan. Tutup dengan ayatnya.");

s = p.addSlide(); dark(s); kick(s, "AYAT KUNCI", PALE);
s.addText("“"+V["2Kor3:2"]+"”", { x:M, y:1.5, w:CW, h:2.6, isTextBox:true, margin:0,
  fontFace:HEAD, fontSize:32, color:"FFFFFF", lineSpacing:44, italic:true });
s.addText("2 Korintus 3:2", { x:M, y:4.4, w:CW, h:0.5, isTextBox:true, margin:0,
  fontFace:BODY, fontSize:22, bold:true, color:PALE });
s.addText("Paulus tidak punya surat rekomendasi. Ia punya orang.", { x:M, y:5.2, w:CW, h:0.8,
  isTextBox:true, margin:0, fontFace:BODY, fontSize:28, color:"FFFFFF" });
s.addNotes("Bacakan pelan. Lalu satu kalimat, tidak lebih:\n\n'Paulus tidak punya surat rekomendasi. Ia punya orang. Pertanyaannya bukan apakah Anda layak, tetapi siapa yang bisa dibaca orang lain.'\n\nLalu doa. Jangan meringkas pelajaran dalam doa.");

p.writeFile({ fileName:"/Users/edmundsitumorang/DEV/skills-sermon-adventist/output/2026-09-05-ss-authentic-christian-ministry/slides/pelajaran-10-hari-demi-hari.pptx" })
 .then(f=>console.log("wrote", f));
