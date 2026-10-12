# Praktikum & Latihan — Pertemuan 4 RPE311
## Control Flow Bagian I: Percabangan (`if`, `elif`, `else`)

**CLO:** CLO-1 (Terkait SO-PI: A–(A.3))

**Sub-topik (sesuai RPS):** Branching (if/elif/else) — menggabungkan operator aritmatika, relasional, dan logika di dalam kondisi percabangan.

---

## Materi: Percabangan pada Python

Percabangan (*branching*) adalah mekanisme yang memungkinkan program memilih blok kode yang dijalankan berdasarkan kondisi tertentu. Tanpa percabangan, program hanya berjalan lurus dari atas ke bawah dan tidak bisa merespons perbedaan input atau situasi.

### Bentuk-Bentuk Percabangan

**1. `if` tunggal** — digunakan ketika hanya ada satu kondisi yang perlu diperiksa. Jika kondisi `False`, tidak ada yang dijalankan.

```python
suhu = 600
if suhu > 550:
    print("Suhu melebihi batas aman")
# Jika suhu <= 550, tidak ada output sama sekali
```

**2. `if / else`** — digunakan ketika ada tepat dua kemungkinan: kondisi terpenuhi atau tidak.

```python
beban = 320
kapasitas = 300
if beban > kapasitas:
    print("OVERLOAD")
else:
    print("Aman")
```

**3. `if / elif / else`** — digunakan ketika ada tiga kemungkinan atau lebih. `elif` adalah kependekan dari *else if*.

```python
efisiensi = 38
if efisiensi >= 40:
    kategori = "Sangat Baik"
elif efisiensi >= 35:
    kategori = "Baik"
else:
    kategori = "Perlu Evaluasi"
```

**4. `if` bersarang (*nested if*)** — kondisi `if` di dalam blok `if` lain. Digunakan saat satu kondisi perlu diperiksa lebih lanjut setelah kondisi luar terpenuhi.

```python
daya = 250
frekuensi = 49
if daya > 200:
    if frekuensi < 50:
        print("Daya tinggi, frekuensi rendah — waspada")
    else:
        print("Daya tinggi, frekuensi normal")
```

> **Catatan:** `if` bersarang bisa diganti dengan operator `and`/`or` untuk kode yang lebih ringkas. Pilih mana yang lebih mudah dibaca.

### Operator yang Sering Dikombinasikan dalam Kondisi

Kondisi pada `if`/`elif` tidak hanya berupa satu perbandingan sederhana. Dalam praktik, kondisi sering menggabungkan beberapa jenis operator sekaligus:

| Jenis Operator | Contoh | Hasil |
|---|---|---|
| **Aritmatika** | `energi_output / energi_input * 100` | Menghitung nilai dulu sebelum dibandingkan |
| **Relasional** | `efisiensi >= 40`, `suhu > 550` | Menghasilkan `True` atau `False` |
| **Logika** | `suhu > 550 and tekanan > 13` | Menggabungkan dua kondisi relasional |

Contoh kondisi yang menggabungkan ketiganya:

```python
energi_input = 1000
energi_output = 420

# Operator aritmatika di dalam kondisi relasional:
if (energi_output / energi_input) * 100 >= 40:
    print("Efisiensi sangat baik")

# Operator relasional digabung dengan logika:
suhu = 560
tekanan = 14
if suhu > 550 and tekanan > 13:
    print("EMERGENCY")
```

### Urutan Evaluasi Kondisi

Python mengevaluasi kondisi dari **kiri ke atas ke bawah**:

1. Operator aritmatika dihitung lebih dulu (`*`, `/`, `+`, `-`).
2. Operator relasional dievaluasi berikutnya (`>`, `>=`, `<`, `<=`, `==`, `!=`).
3. Operator logika dievaluasi terakhir: `not` → `and` → `or`.

Gunakan **tanda kurung `()`** untuk memperjelas urutan atau memaksa urutan yang berbeda dari default.

### `elif` sebagai Penyaring Otomatis

Salah satu keuntungan `elif` yang sering tidak disadari pemula: **jika program sudah sampai ke `elif`, semua kondisi di atasnya sudah pasti `False`**. Ini berarti kita tidak perlu menuliskan kondisi gabungan yang panjang.

```python
# TIDAK PERLU menulis ini:
elif efisiensi >= 35 and efisiensi < 40:

# CUKUP tulis ini — kondisi < 40 sudah terjamin oleh if di atasnya:
elif efisiensi >= 35:
```

---

## Pengingat Singkat: Struktur Percabangan

```python
if kondisi_1:
    # dijalankan jika kondisi_1 True
elif kondisi_2:
    # dijalankan jika kondisi_1 False dan kondisi_2 True
else:
    # dijalankan jika semua kondisi di atas False
```

Tiga hal yang sering terlewat oleh pemula:
1. **Titik dua `:`** wajib ada di akhir baris `if`, `elif`, dan `else`.
2. **Indentasi** (menjorok ke dalam, 4 spasi) menentukan baris mana yang menjadi isi percabangan.
3. Python memeriksa kondisi **dari atas ke bawah** dan **berhenti** pada cabang pertama yang bernilai `True` — sisanya dilewati.

---

# SOAL LATIHAN

> Setiap soal mengharuskan kamu menggabungkan **lebih dari satu jenis operator** (aritmatika, relasional, dan/atau logika) di dalam kondisi `if`/`elif`. Perhatikan `TODO` dan bagian `...` yang harus dilengkapi.

---

## Soal 1 — Kalkulator Faktorial (1 sampai 5)

### Latar Belakang
Faktorial suatu bilangan bulat positif `n` (ditulis `n!`) adalah hasil perkalian semua bilangan bulat dari 1 hingga `n`. Faktorial sering muncul dalam perhitungan kombinatorika, probabilitas, dan analisis statistik yang relevan di bidang teknik.

```
1! = 1
2! = 2 × 1 = 2
3! = 3 × 2 × 1 = 6
4! = 4 × 3 × 2 × 1 = 24
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Soal
Buatlah program yang:
1. Meminta pengguna memasukkan **sebuah bilangan bulat antara 1 sampai 5**.
2. Menghitung **faktorial** dari bilangan tersebut menggunakan `if / elif / else` — **bukan** dengan fungsi bawaan Python.
3. Menampilkan hasil faktorial.
4. Jika input **di luar rentang 1–5**, tampilkan pesan bahwa input tidak valid.

> **Petunjuk operator:** kondisi validasi input menggunakan **operator relasional** (`<` dan `>`) digabung dengan **operator logika** (`or`), sedangkan perhitungan faktorial di dalam setiap cabang menggunakan **operator aritmatika** (`*`).

### Contoh Uji

| Input | Output |
|---|---|
| 1 | 1! = 1 |
| 3 | 3! = 6 |
| 5 | 5! = 120 |
| 0 | Input tidak valid. Masukkan bilangan antara 1 sampai 5. |
| 6 | Input tidak valid. Masukkan bilangan antara 1 sampai 5. |

### Kode untuk Dilengkapi

```python
# Soal 1 — Kalkulator faktorial 1 sampai 5
n = int(input("Masukkan bilangan bulat (1–5): "))

# TODO: Validasi input — jika n kurang dari 1 ATAU lebih dari 5, tampilkan pesan tidak valid
# Gunakan operator logika 'or' untuk menggabungkan dua kondisi relasional
if ... or ...:   #kondisi1
    print("Input tidak valid. Masukkan bilangan antara 1 sampai 5.")

# TODO: Lengkapi setiap cabang elif dengan perhitungan faktorial menggunakan operator *
# Cabang untuk n == 1

elif ...:  #kondisi1
elif n..:  #kondisi2
elif n...: #kondisi3
elif n == 4: # #kondisi4
else: #kondisi terakhir

```

---

## Soal 2 — Klasifikasi Kualitas Daya Berdasarkan Faktor Daya dan Efisiensi Distribusi

### Latar Belakang
**Faktor daya** (*power factor*, PF) menunjukkan seberapa efektif daya listrik yang disuplai benar-benar digunakan untuk kerja nyata. Nilai PF berkisar 0 hingga 1; semakin mendekati 1, semakin baik. **Efisiensi distribusi** menunjukkan persentase daya yang berhasil sampai ke beban (sisanya hilang sebagai rugi-rugi kabel dan transformator).

### Soal
Buatlah program yang:
1. Meminta **faktor daya** (nilai antara 0.0 hingga 1.0) dan **efisiensi distribusi (%)**.
2. Menghitung **skor kualitas daya** dengan rumus: `skor = faktor_daya * efisiensi`.
3. Mengklasifikasikan kualitas daya berdasarkan tabel berikut:

| Kondisi | Klasifikasi |
|---|---|
| `skor >= 85` **dan** `faktor_daya >= 0.90` | **PRIMA** — sistem dalam kondisi optimal |
| `skor >= 70` **dan** `faktor_daya >= 0.80` | **BAIK** — sistem memadai, pantau rutin |
| `skor >= 50` **atau** `faktor_daya >= 0.75` | **CUKUP** — ada ruang perbaikan |
| selain itu | **BURUK** — perlu perbaikan segera |

> **Catatan urutan:** periksa kondisi paling spesifik (ketat) terlebih dahulu. PRIMA lebih ketat dari BAIK, BAIK lebih ketat dari CUKUP.

### Contoh Uji

| Faktor Daya | Efisiensi (%) | Skor | Klasifikasi |
|---|---|---|---|
| 0.95 | 92 | 87.40 | PRIMA |
| 0.85 | 88 | 74.80 | BAIK |
| 0.78 | 80 | 62.40 | CUKUP |
| 0.60 | 70 | 42.00 | BURUK |
| 0.76 | 45 | 34.20 | CUKUP *(faktor daya >= 0.75 cukup untuk masuk CUKUP)* |

### Kode untuk Dilengkapi

```python
# Soal 2 — Klasifikasi kualitas daya
faktor_daya = float(input("Masukkan faktor daya (0.0 – 1.0): "))
efisiensi   = float(input("Masukkan efisiensi distribusi (%): "))

# TODO: Hitung skor kualitas daya menggunakan operator aritmatika (*)
skor = ...

print(f"Skor kualitas daya: {skor:.2f}")

# TODO: Lengkapi kondisi setiap cabang menggunakan operator relasional dan logika
# Ingat: periksa kondisi paling KETAT/SPESIFIK terlebih dahulu

if ... and ...: # skor >= 85 DAN faktor_daya >= 0.90
    klasifikasi = "PRIMA — sistem dalam kondisi optimal"

elif ... and ...: # skor >= 70 DAN faktor_daya >= 0.80
    klasifikasi = "BAIK — sistem memadai, pantau rutin"

elif ... or ...:  # skor >= 50 ATAU faktor_daya >= 0.75
    klasifikasi = "CUKUP — ada ruang perbaikan"

else:
    klasifikasi = "BURUK — perlu perbaikan segera"

print(f"Faktor daya {faktor_daya}, efisiensi {efisiensi}% → Klasifikasi: {klasifikasi}")
```

---

## Soal 3 — Rekomendasi Mode Operasi PLTS Berdasarkan Iradiasi dan Kapasitas Baterai

### Latar Belakang
Pada sistem **Pembangkit Listrik Tenaga Surya (PLTS)**, keputusan operasional bergantung pada dua parameter utama: **iradiasi matahari** (intensitas cahaya dalam W/m²) yang menentukan seberapa besar daya bisa dibangkitkan panel surya, dan **kapasitas baterai tersisa** (State of Charge, SoC dalam %) yang menentukan apakah kelebihan energi bisa disimpan atau tidak.

### Soal
Buatlah program yang:
1. Meminta **iradiasi matahari (W/m²)** dan **SoC baterai (%)**.
2. Menghitung **estimasi daya panel** dengan rumus: `daya_panel = iradiasi * 0.18 * 10` *(asumsi: luas panel 10 m², efisiensi 18%)*.
3. Menentukan **mode operasi** berdasarkan tabel berikut:

| Kondisi | Mode Operasi |
|---|---|
| `iradiasi > 600` **dan** `SoC < 80` | **CHARGING** — iradiasi tinggi, baterai belum penuh, prioritaskan pengisian |
| `iradiasi > 600` **dan** `SoC >= 80` | **GRID-EXPORT** — baterai sudah penuh, ekspor kelebihan daya ke jaringan |
| `iradiasi > 200` **dan** `SoC >= 20` | **NORMAL** — iradiasi dan baterai cukup, operasi mandiri |
| `iradiasi <= 200` **dan** `SoC >= 50` | **BATTERY-ONLY** — iradiasi rendah, andalkan baterai |
| selain itu | **EMERGENCY** — iradiasi rendah dan baterai hampir habis, kurangi beban |

### Contoh Uji

| Iradiasi (W/m²) | SoC (%) | Daya Panel (W) | Mode |
|---|---|---|---|
| 750 | 60 | 1350.0 | CHARGING |
| 800 | 85 | 1440.0 | GRID-EXPORT |
| 400 | 55 | 720.0 | NORMAL |
| 150 | 65 | 270.0 | BATTERY-ONLY |
| 100 | 15 | 180.0 | EMERGENCY |

### Kode untuk Dilengkapi

```python
# Soal 3 — Rekomendasi mode operasi PLTS
iradiasi = float(input("Masukkan iradiasi matahari (W/m²): "))
soc      = float(input("Masukkan SoC baterai (%): "))

# TODO: Hitung estimasi daya panel menggunakan operator aritmatika
# Rumus: iradiasi * efisiensi_panel * luas_panel  (efisiensi = 0.18, luas = 10 m²)
daya_panel = ...

print(f"Estimasi daya panel: {daya_panel:.1f} W")

# TODO: Lengkapi seluruh kondisi percabangan di bawah ini
# Gunakan operator relasional (>, >=, <=) dan logika (and) sesuai tabel

if ... and ...: # iradiasi > 600 DAN SoC < 80
    mode = "CHARGING — prioritaskan pengisian baterai"

elif ... and ...: # iradiasi > 600 DAN SoC >= 80
    mode = "GRID-EXPORT — ekspor kelebihan daya ke jaringan"

elif ... and ...: # iradiasi > 200 DAN SoC >= 20
    mode = "NORMAL — operasi mandiri"

elif ... and ...: # iradiasi <= 200 DAN SoC >= 50
    mode = "BATTERY-ONLY — andalkan baterai"

else:
    mode = "EMERGENCY — kurangi beban segera"

print(f"Iradiasi {iradiasi} W/m², SoC {soc}% → Mode: {mode}")
```

---

## Pembuatan Laporan!
1. Buatlah laporan dalam bentuk video penjelasan dari ke 3 soal di atas, yg mencakup variabel yg di gunakan dan tipe datanya, operator yg di gunakan untuk membuat sebuah kondisi, serta breakdown cara kerja programnya bagaimana program bisa berjalan baik kondisi True ataupun False.
2. Video di harus menampilkan wajah saat menjelasakan program, buka voice over.
3. cukup input link video pada pengumpulan di learning. tempat video di upload bebas yg penting dapat di akses.


## Kesalahan Umum Dalam Menerapkan Percabangan

| Kesalahan | Contoh | Akibat | Perbaikan |
|---|---|---|---|
| Lupa titik dua | `if suhu > 550` | `SyntaxError` | `if suhu > 550:` |
| Indentasi tidak konsisten | isi `if` tidak menjorok | `IndentationError` | Gunakan 4 spasi yang sama pada semua isi blok |
| Memakai `=` bukan `==` | `if suhu = 550:` | `SyntaxError` | `=` untuk mengisi variabel, `==` untuk membandingkan |
| Urutan `elif` terbalik | cek ambang rendah dulu | Cabang tinggi tak pernah tercapai | Periksa dari yang paling ketat/tertinggi |
| Salah memilih `>` / `>=` | batas "75 atau lebih" ditulis `> 75` | Nilai batas masuk kategori salah | Ikuti bunyi soal dengan teliti |
| Input tidak dikonversi | `suhu = input(...)` lalu `suhu > 550` | `TypeError` (teks dibandingkan dengan angka) | `float(input(...))` |
| Salah urutan `and` / `or` | `or` diperiksa sebelum `and` | Kondisi spesifik tidak pernah tercapai | Periksa kondisi paling ketat (`and`) lebih dulu |
| Lupa tanda kurung | `a + b * c > 100` bukan `(a + b) * c > 100` | Hasil perhitungan salah karena *precedence* | Gunakan `()` untuk memperjelas urutan operasi |

---
