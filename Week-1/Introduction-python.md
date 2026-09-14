# Materi Pertemuan — Minggu 1
## RPE311 Dasar Pemrograman — Introduction to Python & Coding Environment

**CLO:** CLO-1 (menerapkan konsep dasar pemrograman menggunakan Python untuk soal-soal rekayasa pembangkit/energi)
**Durasi:** 270 menit (± 4 x 50 menit + jeda)
**Metode:** Interactive lecture, demonstration, live coding practice di Google Colab
**Asesmen pertemuan ini:** Diagnostik awal (non-nilai) + Journal + Coding practice
**Sub-topik (sesuai RPS):** Intro Python & Google Colab · Running the first code · Variables & assignment · Input/output · Comments

---

## 1. Tujuan Pembelajaran (Indikator Capaian Pertemuan)

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. Menjelaskan peran Python sebagai alat bantu analisis di bidang rekayasa pembangkit energi (mengapa dipelajari di prodi RPE, bukan sekadar "belajar coding").
2. Menjelaskan sejarah singkat Python serta kelebihan dan kekurangannya dibanding bahasa pemrograman lain (C/C++, MATLAB).
3. Menggunakan Google Colab (membuat notebook, cell code vs cell text, menjalankan cell, menyimpan ke Google Drive).
4. Menulis dan menjalankan program Python pertama (`print()`).
5. Mendeklarasikan variabel dan memahami aturan penamaan serta tipe data dasar (int, float, str) melalui data pembangkit sederhana.
6. Menggunakan `input()` dan `print()` untuk pertukaran data sederhana.
7. Menulis komentar kode yang jelas (`#` dan docstring `""" """`).

---

## 2. Rencana Waktu (270 menit)

| Segmen | Durasi | Aktivitas |
|---|---|---|
| A. Pembukaan & Diagnostik | 20 menit | Perkenalan, apersepsi, diagnostik logika dasar (non-nilai) |
| B. Mengapa Python untuk Rekayasa Pembangkit? + Sejarah & Perbandingan Python | 25 menit | Kontekstualisasi mata kuliah, sejarah singkat, kelebihan/kekurangan vs bahasa lain |
| C. Tur Google Colab | 20 menit | Demo lingkungan kerja |
| D. Program Pertama: `print()` | 15 menit | Live coding bersama |
| E. Variabel & Tipe Data | 45 menit | Live coding + latihan mandiri |
| — Istirahat — | 10 menit | |
| F. Input/Output | 40 menit | Live coding + latihan mandiri |
| G. Komentar Kode | 15 menit | Live coding singkat |
| H. Studi Kasus Terpadu: Kalkulator Efisiensi Termal Sederhana | 50 menit | Latihan berpasangan |
| I. Penutup, Rangkuman, Journal Reflection | 15 menit | Refleksi tertulis singkat |

---

## 3. Materi & Aktivitas

### A. Pembukaan & Diagnostik (20 menit)

- Perkenalan dosen, silabus singkat, dan gambaran besar mata kuliah: *"Semester ini kita akan belajar Python selama 7 minggu pertama, lalu memakainya untuk menganalisis data operasional pembangkit listrik di 7 minggu berikutnya."*
- **Diagnostik non-nilai** (5–7 soal singkat, bisa lisan/Mentimeter/kertas) untuk memetakan kemampuan logika dasar mahasiswa sebelum masuk materi, contoh soal:
  - Urutkan langkah membuat kopi menjadi langkah-langkah bernomor (mengukur pemahaman *sequence*).
  - Jika suhunya > 100°C maka air mendidih, jika tidak maka belum mendidih — mahasiswa diminta menyatakan ulang dengan kalimat "jika... maka..." untuk kasus lain (mengukur pemahaman *kondisional* dasar).
  - Tanya siapa yang sudah pernah menulis kode (bahasa apa saja) — untuk pemetaan kelompok bantu-sebaya nantinya.
- Hasil diagnostik **tidak dinilai**, hanya dipakai dosen untuk menyesuaikan kecepatan mengajar dan membentuk kelompok kerja berpasangan yang heterogen.

### B. Mengapa Python untuk Rekayasa Pembangkit? + Sejarah & Perbandingan Python (25 menit)

**B.1 Konteks industri (5-menit)**

Poin diskusi singkat (bisa disertai gambar/contoh dashboard):

- Python banyak dipakai industri energi untuk: pemrosesan data SCADA, analisis efisiensi unit pembangkit, prediksi beban, monitoring sensor real-time.
- Alternatif terhadap Excel/SPSS/Minitab ketika data besar (ribuan baris log sensor per hari).
- Alur besar mata kuliah: **Python dasar (Minggu 1–7) → Analisis data energi (Minggu 8–14)** — dataset yang dipakai nanti adalah data operasional pembangkit (akan diperkenalkan di Minggu 8).

**B.2 Sejarah Singkat Python (10 menit)**

- Diciptakan oleh **Guido van Rossum**, seorang programmer asal Belanda, mulai dikembangkan akhir 1980-an dan **dirilis pertama kali tahun 1991** (Python 0.9.0).
- Nama "Python" **bukan** diambil dari nama ular, melainkan dari acara komedi favorit Guido, *Monty Python's Flying Circus* — salah satu alasan komunitas Python suka memakai istilah jenaka di dokumentasi/contoh kode.
- Filosofi desainnya dirangkum dalam **"The Zen of Python"** (bisa diketik `import this` di Colab) — intinya: kode harus mudah dibaca, sederhana lebih baik daripada rumit.
- Milestone penting:
  - **1991** — Python 1.0 dirilis publik.
  - **2000** — Python 2.0, membawa fitur seperti list comprehension.
  - **2008** — Python 3.0 dirilis (tidak backward-compatible dengan Python 2), memperbaiki banyak inkonsistensi bahasa.
  - **2020** — Python 2 resmi *end-of-life*; seluruh industri & mata kuliah ini memakai **Python 3**.
  - **2010-an–sekarang** — Python meledak popularitasnya seiring booming data science, machine learning, dan otomasi — termasuk di sektor energi & industri.
- Saat ini Python konsisten menjadi salah satu bahasa pemrograman paling populer di dunia (survei TIOBE/Stack Overflow), terutama untuk analisis data dan AI.

**B.3 Kelebihan & Kekurangan Python Dibanding Bahasa Lain (10 menit)**

Diskusi terbuka: bandingkan dengan bahasa yang mungkin sudah pernah didengar mahasiswa (C/C++, Java, MATLAB — MATLAB relevan karena umum dipakai di rekayasa/teknik).

*Kelebihan Python:*

- **Sintaks mudah dibaca** — mendekati bahasa manusia, tanpa banyak tanda kurung kurawal/titik koma seperti C/Java, sehingga cocok untuk pemula dan non-programmer (mis. engineer pembangkit yang fokusnya bukan software).
- **Gratis & open-source** — berbeda dengan MATLAB yang berbayar/berlisensi, sehingga bisa dipakai bebas di kampus maupun setelah lulus bekerja.
- **Ekosistem library data science sangat kuat** — Pandas, NumPy, Matplotlib, Scikit-learn — akan langsung dipakai mulai Minggu 8 untuk analisis data pembangkit.
- **Interpreted language** — kode langsung dijalankan baris per baris tanpa proses compile, sehingga cepat untuk mencoba-coba (prototyping) dan cocok untuk pembelajaran interaktif di Colab.
- **Komunitas besar & dokumentasi melimpah** — mudah mencari solusi ketika error (Stack Overflow, dokumentasi resmi).
- **Multi-platform** — berjalan di Windows/Mac/Linux, dan bisa diakses lewat cloud (Google Colab) tanpa instalasi.

*Kekurangan Python:*

- **Lebih lambat** dibanding bahasa compiled seperti C/C++ untuk komputasi berat atau sistem real-time — karena itu untuk kontrol embedded/PLC pada unit pembangkit, C/C++ (atau ladder logic) masih lebih umum dipakai.
- **Indentasi (spasi) menentukan struktur kode** — berbeda dari bahasa lain yang pakai kurung kurawal `{}`; ini memudahkan pembacaan tapi bisa jadi sumber error tersembunyi bagi pemula (`IndentationError`).
- **Global Interpreter Lock (GIL)** — membatasi Python menjalankan banyak thread secara paralel penuh, kurang ideal untuk aplikasi yang butuh komputasi paralel berat.
- **Kurang umum untuk aplikasi mobile/embedded** — dibanding Java (Android) atau C (mikrokontroler/PLC).
- **Manajemen versi & dependency (library) bisa membingungkan** bagi pemula — perlu konsep virtual environment yang tidak dibahas mendalam di mata kuliah ini.

> **Simpulan diskusi:** Python bukan bahasa "terbaik" untuk semua kasus — tapi untuk kebutuhan mata kuliah ini (belajar logika pemrograman lalu langsung dipakai analisis data energi), Python adalah pilihan paling praktis: mudah dipelajari, gratis, dan ekosistem data science-nya terkuat dibanding alternatif lain.

| Kriteria | Python | C/C++ | MATLAB |
|---|---|---|---|
| Kemudahan dipelajari | Tinggi | Rendah–Sedang | Sedang |
| Kecepatan eksekusi | Sedang (interpreted) | Tinggi (compiled) | Sedang |
| Ekosistem data science | Sangat kuat | Terbatas | Kuat (berbayar) |
| Biaya lisensi | Gratis | Gratis | Berbayar |
| Umum untuk real-time/embedded control | Jarang | Umum | Jarang |
| Umum untuk analisis data pembangkit di industri saat ini | Meningkat pesat | Jarang (kecuali firmware) | Umum (legacy) |


### C. Tur Google Colab (20 menit)

Demo langsung oleh dosen, mahasiswa mengikuti di laptop masing-masing:

1. Buka https://colab.research.google.com, login dengan akun Google.
2. Buat notebook baru, ganti nama file (mis. `RPE311_W1_NamaMahasiswa.ipynb`).
3. Perbedaan **code cell** vs **text cell** (Markdown).
4. Menjalankan cell (`Shift+Enter`), menyisipkan cell baru, menghapus cell.
5. Menyimpan otomatis ke Google Drive; cara membagikan (share) notebook ke dosen untuk pengumpulan.

> **Catatan dosen:** siapkan notebook template kosong dengan struktur judul + sub-heading sesuai sub-topik pertemuan agar mahasiswa tinggal mengisi.

### D. Program Pertama: `print()` (15 menit)

Live coding bersama, mahasiswa mengetik ulang di Colab masing-masing:

```python
# Program pertama saya di RPE311
print("Selamat datang di Dasar Pemrograman - Teknik Rekayasa Pembangkit Energi")
print("Nama saya:", "Isi nama Anda")
```

Latihan cepat (individu, 5 menit): mahasiswa mengubah teks agar menampilkan nama dan NIM masing-masing, lalu satu kalimat tentang cita-cita profesional di bidang energi.

### E. Variabel & Tipe Data (45 menit)

**Konsep inti:** variabel sebagai "wadah" nilai; aturan penamaan (huruf/underscore di awal, case-sensitive, tidak boleh pakai spasi/keyword); tipe data dasar `int`, `float`, `str`, `bool`.

Contoh dikaitkan langsung ke konteks pembangkit (bukan `x = 5` generik):

```python
# Data operasi sederhana satu unit pembangkit
nama_unit = "Unit 1 - PLTU"          # str
suhu_boiler = 540.5                   # float, satuan: derajat Celcius
tekanan_turbin = 12.4                 # float, satuan: MPa
output_daya = 250                     # int, satuan: MW
status_operasi = True                 # bool

print(nama_unit, "menghasilkan", output_daya, "MW pada suhu boiler", suhu_boiler, "°C")
print("Tipe data suhu_boiler:", type(suhu_boiler))
```

Jelaskan juga operasi assignment gabungan (`+=`, dst.) dengan contoh menaikkan output daya:

```python
output_daya = output_daya + 10   # unit dinaikkan 10 MW
output_daya += 10                # cara singkat, hasil sama
print("Output setelah penyesuaian:", output_daya, "MW")
```

**Latihan mandiri (10 menit, dikerjakan di Colab):**
Mahasiswa membuat 5 variabel yang merepresentasikan data operasi unit pembangkit pilihan mereka sendiri (boleh direka-reka): nama unit, jenis bahan bakar, suhu, tekanan, output daya — lalu menampilkannya dengan `print()` dalam satu kalimat naratif.

### — Istirahat (10 menit) —

### F. Input/Output (40 menit)

**Konsep inti:** fungsi `input()` selalu mengembalikan `str`, perlu `int()`/`float()` untuk konversi jika dipakai perhitungan.

```python
nama_unit = input("Masukkan nama unit pembangkit: ")
suhu_boiler = float(input("Masukkan suhu boiler (°C): "))
output_daya = int(input("Masukkan output daya (MW): "))

print(f"Unit {nama_unit} beroperasi pada suhu {suhu_boiler}°C dengan output {output_daya} MW")
```

Perkenalkan **f-string** sebagai cara modern memformat output (akan dipakai terus sepanjang semester).

Contoh perhitungan sederhana yang menggabungkan input + variabel + operator dasar (preview ringan untuk Minggu 3, tidak perlu dibahas dalam-dalam):

```python
kalori_input = float(input("Energi input bahan bakar (MJ): "))
energi_output = float(input("Energi listrik dihasilkan (MJ): "))
efisiensi = (energi_output / kalori_input) * 100
print(f"Efisiensi termal unit ini sekitar {efisiensi:.2f}%")
```

**Latihan mandiri (10 menit):** mahasiswa membuat program kecil yang meminta 3 input data operasi (bebas, mis. suhu, tekanan, jam operasi) lalu menampilkannya dalam satu ringkasan kalimat menggunakan f-string.

### G. Komentar Kode (15 menit)

```python
# Ini komentar satu baris - dipakai untuk penjelasan singkat

"""
Ini adalah docstring / komentar multi-baris.
Biasa dipakai untuk menjelaskan tujuan program,
nama pembuat, dan tanggal.
"""

suhu_boiler = 540.5  # satuan: derajat Celcius
```

Tekankan **kebiasaan baik**: setiap program yang dikumpulkan sepanjang semester wajib punya komentar header (nama, NIM, tanggal, tujuan program) — ini akan jadi bagian penilaian portofolio/journal ke depannya.

### H. Studi Kasus Terpadu: Kalkulator Efisiensi Termal Sederhana (50 menit)

Dikerjakan **berpasangan** (memakai hasil pemetaan diagnostik di awal agar tiap pasangan heterogen).

**Instruksi:**

> Buatlah program Python di Colab yang:
> 1. Meminta pengguna memasukkan nama unit pembangkit, energi input bahan bakar (MJ), dan energi listrik yang dihasilkan (MJ).
> 2. Menghitung efisiensi termal = (energi output / energi input) × 100.
> 3. Menampilkan hasil dalam kalimat naratif menggunakan f-string, dibulatkan 2 angka desimal.
> 4. Program diberi komentar header (nama kedua anggota, tanggal, tujuan program).

Dosen berkeliling membimbing; pasangan yang selesai lebih cepat diminta menambahkan variasi (mis. menampilkan status "Efisiensi baik" jika > 35%, "Perlu evaluasi" jika ≤ 35% — sekadar pancingan konsep percabangan untuk Minggu 4, tidak wajib berhasil).

**Luaran:** setiap pasangan mengumpulkan link Colab (di-share ke dosen) sebagai bagian dari *coding practice* pertemuan ini.

### I. Penutup, Rangkuman & Journal Reflection (15 menit)

Rangkuman lisan: Python & Colab, program pertama, variabel & tipe data, input/output, komentar — semuanya adalah fondasi yang akan langsung dipakai untuk memroses data pembangkit mulai Minggu 8.

**Journal reflection (ditulis di akhir notebook Colab masing-masing, 3–5 kalimat):**
1. Apa satu hal baru yang paling menarik dari pertemuan hari ini?
2. Bagian mana yang masih terasa sulit?
3. Menurutmu, di bagian pekerjaan seorang engineer pembangkit yang mana Python bisa membantu?

---

## 4. Latihan Mandiri / Tugas Rumah (opsional, dibahas sekilas di Minggu 2)

Mahasiswa diminta mencoba di rumah: membuat program yang meminta 4 data operasi pembangkit (bebas dipilih sendiri, misalnya suhu, tekanan, kelembapan, output daya), menyimpannya di variabel dengan tipe data yang sesuai, lalu menampilkan ringkasan naratif menggunakan f-string dan minimal 2 baris komentar penjelas.

---

## 5. Rubrik Penilaian Singkat (mengacu ke Bagian IX RPS, CLO-1/A-(A.3), Level 1–2)

| Level | Deskriptor | Indikator di pertemuan ini |
|---|---|---|
| 1 | Knows what Python is but has not used it | Bisa menjalankan cell tapi belum bisa memodifikasi kode sendiri |
| 2 | Actively uses Python with guidance, limited contribution | Bisa menyelesaikan latihan mandiri dengan bantuan pasangan/dosen |
| 3 (target minimum akhir pertemuan) | Understands and explains how to use Python for simple problems | Mampu menyelesaikan studi kasus kalkulator efisiensi termal secara mandiri berpasangan, dengan variabel, input/output, dan komentar yang benar |

---

## 6. Referensi Pertemuan

- [1] Python Software Foundation. *Python 3.x Official Documentation* — https://docs.python.org/3/
- [3] Matthes, E., *Python Crash Course*, 3rd Edition, Bab 1–2 (variabel & tipe data)
- [4] Raharjo, B., *Logika dan Algoritma Pemrograman Menggunakan Python*, Bab 1–2

