# Soal Pertemuan 3 — RPE311 Dasar Pemrograman
## Expressions & Operators

**CLO:** CLO-3 (Terkait SO-PI: A–(A.3))
**Sub-topik:** Types of expressions; Arithmetic, logical, relational, assignment operators; Operator precedence.
**Konteks energi:** menghitung efisiensi, capacity factor, dan heat rate dari data operasi harian menggunakan operator aritmatika; memvalidasi ambang batas pembangkit (mis. status efisiensi, peringatan maintenance) menggunakan operator relasional dan logika.

---

## A. Soal Esai — Mendorong Mahasiswa Mencari Materi Sendiri

**1.** Python mengenal beberapa jenis ekspresi (aritmatika, relasional, logika, assignment). Carilah referensi (dokumentasi resmi Python atau sumber lain) yang menjelaskan **urutan prioritas operator (operator precedence)** di Python, lalu jelaskan dengan kata-katamu sendiri: mengapa ekspresi `10 + 5 * 2` menghasilkan `20`, bukan `30`? Sertakan sumber yang kamu gunakan.

**2.** Jelaskan perbedaan mendasar antara **operator relasional** (`>`, `<`, `==`, dll.) dan **operator logika** (`and`, `or`, `not`) dalam Python. Berikan satu contoh situasi nyata (boleh di luar konteks pembangkit) di mana kedua jenis operator ini harus dipakai **bersamaan** dalam satu ekspresi untuk menghasilkan keputusan yang benar.

**3.** Cari satu contoh kasus nyata (artikel, forum programmer, atau dokumentasi) tentang **bug atau kesalahan perhitungan** yang terjadi akibat salah memahami *operator precedence* (misalnya lupa memberi tanda kurung). Ringkas kasus tersebut dalam 3–5 kalimat, lalu jelaskan bagaimana seharusnya kode itu diperbaiki.

---

## B. Soal Praktikum — Implementasi Materi Pertemuan 3

### B.1 Soal Umum

**1.** Buatlah program Python yang meminta pengguna memasukkan dua bilangan bulat, lalu tampilkan hasil dari operasi `+`, `-`, `*`, `/`, `//` (pembagian bulat), dan `%` (modulus) antara kedua bilangan tersebut.

**2.** Buatlah program yang meminta pengguna memasukkan nilai ujian (0–100), lalu gunakan **operator relasional** untuk menampilkan `True` atau `False` terhadap pernyataan: *"Nilai ini termasuk kategori lulus (≥ 60)"*.

**3.** Buatlah program yang meminta pengguna memasukkan umur dan status memiliki SIM (`True`/`False`), lalu gunakan **operator logika** (`and`) untuk menentukan apakah orang tersebut *"boleh mengemudi sendiri"* (syarat: umur ≥ 17 **dan** punya SIM). Tambahkan minimal satu ekspresi yang sengaja butuh tanda kurung agar hasilnya benar, sebagai latihan *operator precedence*.

### B.2 Soal Konteks Energi

**4.** Buatlah program Python yang menghitung **efisiensi termal** sebuah unit pembangkit menggunakan rumus:

```
efisiensi (%) = (energi output / energi input) * 100
```

Program meminta pengguna memasukkan nilai energi input dan energi output (dalam MJ), lalu menampilkan hasil efisiensi dengan f-string, dibulatkan 2 angka desimal. Pastikan penggunaan tanda kurung pada rumus sudah benar sesuai *operator precedence*.

**5.** Buatlah program yang meminta pengguna memasukkan **suhu boiler** dan **beban operasi (%)** suatu unit pembangkit, lalu gunakan **operator relasional dan logika** untuk menghitung apakah unit tersebut dalam kondisi **"perlu maintenance"** — yaitu benar (`True`) jika suhu boiler > 550°C **atau** beban operasi > 95%.

Tampilkan hasilnya (nilai `True`/`False`) dalam satu kalimat naratif menggunakan f-string, tanpa menggunakan `if/else` (materi percabangan baru akan dipelajari Minggu 4).

---

## Petunjuk Pengumpulan

- Soal esai (Bagian A) dikerjakan secara individu dalam bentuk tulisan singkat (boleh di dokumen terpisah atau di text cell Colab).
- Soal praktikum (Bagian B) dikerjakan di Google Colab, dengan komentar header (nama, NIM, tanggal, tujuan program) pada setiap program.
- Kumpulkan dalam bentuk Laporan seperti biasanya dengan penjelasan masing-masing sertakanlink Repo Github / Colab.