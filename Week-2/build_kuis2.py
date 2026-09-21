# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, PageBreak)

NAVY = colors.HexColor("#1F3864")
GREY = colors.HexColor("#595959")
BOXBG = colors.HexColor("#EDF1F8")
KEYBG = colors.HexColor("#FBEEE6")
KEYBORDER = colors.HexColor("#C0742E")
NEWG = colors.HexColor("#2E7D32")

styles = getSampleStyleSheet()
def S(name, **kw): styles.add(ParagraphStyle(name, **kw))

S("Inst", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=11, textColor=NAVY, alignment=1, spaceAfter=1, leading=13)
S("Sub", parent=styles["Normal"], fontName="Helvetica", fontSize=9, textColor=GREY, alignment=1, spaceAfter=1, leading=11)
S("KuisTitle", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=15, textColor=NAVY, alignment=1, spaceBefore=5, spaceAfter=2, leading=18)
S("KuisScope", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=9, textColor=colors.HexColor("#2E5496"), alignment=1, spaceAfter=4, leading=11)
S("SecHead", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=11.5, textColor=colors.white, leading=15)
S("Meta", parent=styles["Normal"], fontName="Helvetica", fontSize=9, textColor=colors.black, leading=13)
S("Petunjuk", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, textColor=colors.black, leading=12, leftIndent=2)
S("QNum", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5, textColor=NAVY, leading=13, spaceBefore=6, spaceAfter=2)
S("QText", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, textColor=colors.black, leading=14)
S("Opt", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, textColor=colors.black, leading=13.5, leftIndent=10)
S("Field", parent=styles["Normal"], fontName="Helvetica", fontSize=10, textColor=colors.black, leading=16)
S("KeyHead", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=12, textColor=KEYBORDER, leading=15, spaceAfter=2)
S("KeyNote", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=9, textColor=KEYBORDER, leading=12, spaceAfter=6)
S("KeyRow", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, textColor=colors.black, leading=13)

def code(t): return '<font name="Courier">%s</font>' % t

def section_bar(text):
    tbl = Table([[Paragraph(text, styles["SecHead"])]], colWidths=[170*mm])
    tbl.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),("LEFTPADDING",(0,0),(-1,-1),8),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
    return tbl

# (topik, teks, [opsi], kunci, sumber, pembahasan)
Q = [
 ("Penulisan Variabel",
  "Manakah dari nama variabel berikut yang menerapkan gaya penulisan standar snake_case secara benar dalam konvensi Python?",
  [code("NilaiUjianMahasiswa"), code("nilaiUjianMahasiswa"), code("nilai_ujian_mahasiswa"), code("nilai-ujian-mahasiswa")],
  "C","M2",
  "Konvensi %s menggunakan huruf kecil semua yang dipisahkan underscore. A = PascalCase, B = camelCase, D memakai tanda minus yang tidak valid." % code("snake_case")),

 ("Penulisan Variabel",
  "Apa yang akan terjadi jika seorang mahasiswa mendeklarasikan variabel dengan nama kata kunci bawaan (reserved keyword) seperti %s?" % code("for = 25"),
  ["Nilai 25 otomatis diubah menjadi tipe data string",
   "Program menghasilkan %s" % code("SyntaxError: invalid syntax"),
   "Variabel berhasil dibuat tetapi tidak bisa dicetak",
   "Python membuat variabel baru bernama %s" % code("_for")],
  "B","M2",
  "Kata kunci seperti %s sudah punya fungsi internal di Python sehingga tidak boleh dipakai sebagai nama variabel." % code("for, if, class, import, def")),

 ("Penulisan Variabel",
  "Python bersifat case-sensitive dalam penulisan variabel. Pernyataan manakah yang paling tepat?",
  ["Nama variabel harus selalu ditulis dengan huruf kapital",
   "Variabel %s, %s, dan %s mengacu pada 3 objek memori berbeda" % (code("Beban"), code("beban"), code("BEBAN")),
   "Huruf kapital hanya boleh digunakan pada tipe data string",
   "Python otomatis mengubah huruf kapital menjadi huruf kecil"],
  "B","M2",
  "Case-sensitive berarti Python membedakan huruf besar dan kecil, sehingga %s, %s, dan %s dianggap tiga variabel terpisah." % (code("Beban"), code("beban"), code("BEBAN"))),

 ("Penulisan Variabel",
  "Mengapa penulisan %s akan menyebabkan error pada Python?" % code("suhu-boiler = 540.5"),
  ["Angka desimal 540.5 harus diapit tanda kutip",
   "Tanda minus (-) dianggap Python sebagai operator pengurangan",
   "Nama variabel tidak boleh menggunakan huruf kecil",
   "Tipe data float tidak bisa disimpan dalam variabel"],
  "B","M2",
  "Karakter %s diartikan sebagai operator pengurangan, sehingga Python mencoba mengurangkan variabel %s dengan %s." % (code("-"), code("suhu"), code("boiler"))),

 ("Penulisan Variabel",
  "Manakah perintah assignment yang benar untuk menyimpan nilai logika bahwa generator sedang beroperasi?",
  [code("status_aktif = \"True\""), code("status_aktif = true"), code("status_aktif = True"), code("status_aktif = (TRUE)")],
  "C","M2",
  "Tipe boolean memakai kata kunci khusus %s dan %s (diawali huruf kapital, tanpa tanda kutip)." % (code("True"), code("False"))),

 ("Multiple Assignment",
  "Perhatikan kode berikut:<br/>%s<br/>%s<br/>Setelah dijalankan, berapakah nilai %s dan %s?" % (
      code("v_a, v_b = 220, 380"), code("v_a, v_b = v_b, v_a"), code("v_a"), code("v_b")),
  ["220 dan 380", "380 dan 220", "380 dan 380", "220 dan 220"],
  "B","BARU",
  "Python menukar kedua nilai sekaligus (multiple assignment): %s menjadi 380 dan %s menjadi 220." % (code("v_a"), code("v_b"))),

 ("Dynamic Typing",
  "Python menganut dynamic typing. Manakah pernyataan yang BENAR terkait sifat ini?",
  ["Tipe data variabel harus dideklarasikan sebelum digunakan",
   "Variabel yang tadinya bertipe %s boleh diisi ulang dengan nilai bertipe %s" % (code("int"), code("str")),
   "Sebuah variabel hanya boleh menyimpan satu tipe data selama program berjalan",
   "Python menolak perubahan tipe data dan menghasilkan error"],
  "B","BARU",
  "Dynamic typing: tipe ditentukan otomatis dari nilainya, dan variabel yang sama boleh diisi ulang dengan tipe berbeda, mis. %s lalu %s." % (code("daya = 100"), code("daya = \"tinggi\""))),

 ("Tipe Data Primitif",
  "Diberikan pernyataan kode: %s. Apakah hasil dari %s?" % (code("x = \"100\""), code("type(x)")),
  [code("&lt;class 'int'&gt;"), code("&lt;class 'float'&gt;"), code("&lt;class 'str'&gt;"), code("&lt;class 'bool'&gt;")],
  "C","M2",
  "Nilai %s diapit tanda kutip, sehingga dikategorikan sebagai string (%s), bukan integer." % (code("\"100\""), code("str"))),

 ("Tipe Data Primitif",
  "Di antara nilai berikut, manakah yang bertipe data %s?" % code("float"),
  [code("50"), code("\"50\""), code("50.0"), code("True")],
  "C","BARU",
  "Angka dengan titik desimal (%s) bertipe %s. %s adalah %s, %s adalah %s, %s adalah %s." % (
      code("50.0"), code("float"), code("50"), code("int"), code("\"50\""), code("str"), code("True"), code("bool"))),

 ("Tipe Data Primitif",
  "Perhatikan kode: %s. Apakah hasil dari %s?" % (code("impedansi = complex(4, 3)"), code("type(impedansi)")),
  [code("&lt;class 'int'&gt;"), code("&lt;class 'float'&gt;"), code("&lt;class 'complex'&gt;"), code("&lt;class 'tuple'&gt;")],
  "C","BARU",
  "Fungsi %s membuat bilangan kompleks (4+3j) bertipe %s &mdash; berguna merepresentasikan impedansi Z = R + jX." % (code("complex()"), code("complex"))),

 ("Immutability Data",
  "Sifat immutability pada tipe data primitif seperti Integer dan String berarti bahwa...",
  ["Nilai variabel tidak bisa dicetak ke layar konsol",
   "Isi/elemen di dalam alamat memori objek tidak dapat diubah setelah dibuat",
   "Variabel tersebut hanya bisa digunakan satu kali di dalam kode",
   "Tipe datanya bisa berubah secara otomatis saat program berjalan"],
  "B","M2",
  "Immutable berarti objek di alamat memori tidak bisa diubah langsung; mengubah nilai berarti menciptakan objek baru di memori berbeda."),

 ("Struktur Koleksi Data",
  "Struktur koleksi data Python manakah yang menyimpan elemen menggunakan pasangan kunci dan nilai (key-value pairs)?",
  ["List", "Tuple", "Set", "Dictionary"],
  "D","M2",
  "Dictionary (%s) menyimpan pasangan key-value dalam kurung kurawal, mis. %s." % (code("dict"), code("{\"unit\": \"PLTU 1\", \"mw\": 150}"))),

 ("List vs Tuple",
  "Manakah pernyataan berikut yang BENAR mengenai perbedaan List dan Tuple?",
  ["List immutable memakai %s, Tuple mutable memakai %s" % (code("()"), code("[]")),
   "List mutable memakai %s, Tuple immutable memakai %s" % (code("[]"), code("()")),
   "List tidak mendukung duplikasi, Tuple mendukung duplikasi",
   "List hanya bisa menyimpan angka, Tuple hanya bisa menyimpan teks"],
  "B","M2",
  "List memakai kurung siku %s dan mutable; Tuple memakai kurung biasa %s dan immutable." % (code("[]"), code("()"))),

 ("Set Unik",
  "Jika dijalankan kode %s, berapakah jumlah elemen dalam variabel %s?" % (code("data = {10, 20, 20, 30, 30, 30}"), code("data")),
  ["6 elemen", "5 elemen", "3 elemen", "1 elemen"],
  "C","M2",
  "Kurung kurawal tanpa key-value bertipe Set. Set mengeliminasi duplikasi sehingga hasilnya %s (3 elemen)." % code("{10, 20, 30}")),

 ("Struktur Koleksi Data",
  "Manakah pernyataan yang BENAR mengenai isi sebuah %s di Python?" % code("list"),
  ["Sebuah list hanya boleh berisi elemen dengan tipe data yang sama",
   "Sebuah list boleh berisi campuran %s, %s, dan %s sekaligus" % (code("int"), code("float"), code("str")),
   "Sebuah list tidak boleh berisi lebih dari 10 elemen",
   "Sebuah list otomatis mengubah semua elemen menjadi tipe %s" % code("str")],
  "B","BARU",
  "List bersifat heterogen &mdash; boleh menyimpan berbagai tipe sekaligus, mis. %s." % code("[150, 3.5, \"PLTU\"]")),
]

def build():
    doc = SimpleDocTemplate("/mnt/user-data/outputs/Kuis-Minggu-2-Variabel-dan-Tipe-Data.pdf",
        pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=12*mm, bottomMargin=16*mm,
        title="Kuis Minggu 2 - Variabel dan Tipe Data", author="Muhammad Veven, S.Kom., M.Eng.")
    story = []
    story.append(Paragraph("POLITEKNIK NEGERI BATAM", styles["Inst"]))
    story.append(Paragraph("D4 Teknologi Rekayasa Pembangkit Energi (TRPE)", styles["Sub"]))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.4, color=NAVY, spaceAfter=6))
    story.append(Paragraph("KUIS MINGGU 2 &mdash; Variabel &amp; Tipe Data", styles["KuisTitle"]))
    story.append(Paragraph("Mata Kuliah: Pemrograman Dasar (RPE311) &middot; Materi: Variabel &amp; Tipe Data (belum mencakup slicing)", styles["KuisScope"]))
    story.append(Spacer(1, 4))

    meta = [[Paragraph("<b>Dosen:</b> Muhammad Veven, S.Kom., M.Eng.", styles["Meta"]),
             Paragraph("<b>Jumlah Soal:</b> 15 Pilihan Ganda", styles["Meta"])]]
    mt = Table(meta, colWidths=[105*mm, 65*mm])
    mt.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),2)]))
    story.append(mt)

    idata = [[Paragraph("Nama&nbsp;: ______________________________", styles["Field"]),
              Paragraph("Kelas&nbsp;: ____________", styles["Field"])],
             [Paragraph("NIM&nbsp;&nbsp;&nbsp;&nbsp;: ______________________________", styles["Field"]),
              Paragraph("Nilai&nbsp;: ____________", styles["Field"])]]
    itbl = Table(idata, colWidths=[105*mm, 65*mm])
    itbl.setStyle(TableStyle([("BOX",(0,0),(-1,-1),0.8,NAVY),("INNERGRID",(0,0),(-1,-1),0.3,colors.HexColor("#B8C4DA")),
        ("BACKGROUND",(0,0),(-1,-1),BOXBG),("LEFTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
    story.append(itbl)
    story.append(Spacer(1, 5))

    story.append(section_bar("PETUNJUK PENGERJAAN"))
    story.append(Spacer(1, 3))
    for i, p in enumerate([
        "Kuis terdiri dari <b>15 soal pilihan ganda</b>. Setiap soal bernilai <b>+/- 6,67 poin</b> (total 100).",
        "Pilih jawaban paling tepat dengan memberi tanda silang (X) pada huruf A, B, C, atau D.",
        "Seluruh soal berada pada lingkup variabel &amp; tipe data; materi slicing belum diujikan.",
        "Kerjakan mandiri, tanpa membuka catatan maupun gawai. Selamat mengerjakan."], 1):
        story.append(Paragraph("%d.&nbsp;&nbsp;%s" % (i, p), styles["Petunjuk"]))
    story.append(Spacer(1, 5))

    story.append(section_bar("SOAL PILIHAN GANDA"))
    letters = ["A","B","C","D"]
    for i, (topik, q, opts, key, src, why) in enumerate(Q, 1):
        block = [Paragraph("Soal %d&nbsp;&nbsp;<font size=8 color='#595959'>[%s]</font>" % (i, topik), styles["QNum"]),
                 Paragraph(q, styles["QText"]), Spacer(1, 1)]
        for L, opt in zip(letters, opts):
            block.append(Paragraph("<b>%s.</b>&nbsp;&nbsp;%s" % (L, opt), styles["Opt"]))
        story.append(KeepTogether(block))

    # Answer key
    story.append(PageBreak())
    kbar = Table([[Paragraph("KUNCI JAWABAN &amp; PEMBAHASAN &mdash; DOSEN ONLY", styles["KeyHead"])]], colWidths=[170*mm])
    kbar.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),KEYBG),("BOX",(0,0),(-1,-1),1,KEYBORDER),
        ("LEFTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    story.append(kbar)
    story.append(Spacer(1, 2))
    story.append(Paragraph('Kolom "Sumber": M2 = soal lama Minggu 2, BARU = soal baru pengganti slicing. Hapus halaman ini sebelum dibagikan.', styles["KeyNote"]))

    rows = [[Paragraph("<b>No</b>", styles["KeyRow"]), Paragraph("<b>Kunci</b>", styles["KeyRow"]),
             Paragraph("<b>Sumber</b>", styles["KeyRow"]), Paragraph("<b>Pembahasan</b>", styles["KeyRow"])]]
    for i, (topik, q, opts, key, src, why) in enumerate(Q, 1):
        srccol = ('<font color="#2E7D32"><b>BARU</b></font>' if src == "BARU" else "M2")
        rows.append([Paragraph(str(i), styles["KeyRow"]), Paragraph("<b>%s</b>" % key, styles["KeyRow"]),
                     Paragraph(srccol, styles["KeyRow"]), Paragraph(why, styles["KeyRow"])])
    ktbl = Table(rows, colWidths=[10*mm, 14*mm, 18*mm, 128*mm], repeatRows=1)
    ktbl.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#B8C4DA")),
        ("VALIGN",(0,0),(-1,-1),"TOP"),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, BOXBG]),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),("ALIGN",(0,0),(2,-1),"CENTER")]))
    story.append(ktbl)

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8); canvas.setFillColor(GREY)
        canvas.drawString(20*mm, 10*mm, "Kuis Minggu 2 \u2014 Pemrograman Dasar RPE311 \u00b7 Politeknik Negeri Batam")
        canvas.drawRightString(190*mm, 10*mm, "Hal. %d" % doc.page)
        canvas.setStrokeColor(colors.HexColor("#B8C4DA")); canvas.setLineWidth(0.4)
        canvas.line(20*mm, 12*mm, 190*mm, 12*mm)
        canvas.restoreState()
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("PDF built")

build()
