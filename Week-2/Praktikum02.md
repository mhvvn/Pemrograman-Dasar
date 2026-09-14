# Modul Praktikum 1 — Pengenalan Python

**Program Studi:** Teknologi Rekayasa Pembangkit Energi (TRPE)
**Mata Kuliah:** Pemrograman Dasar
**Semester:** Ganjil 2026/2027 · **Media:** Google Colab / Jupyter · **Repo:** GitHub

### Capaian Pembelajaran (Tujuan Pembelajaran)

- **TP-1.1** Menjelaskan sejarah, karakteristik, serta kelebihan dan kekurangan Python.
- **TP-1.2** Membuat dan menamai variabel sesuai aturan sintaks dan konvensi PEP 8.
- **TP-1.3** Membedakan dan menggunakan tipe data primitif dan non-primitif.
- **TP-1.4** Mengimplementasikan pembuatan variabel dan pemilihan tipe data yang tepat pada kasus data teknik elektro/energi.

> **Lingkup modul ini:** kita fokus pada **membuat variabel** dan **mengenali tipe data**. Cara mengolah variabel (operator aritmatika, pembanding, logika) akan dibahas pada **pertemuan berikutnya**. Di sini kita hanya memakai tanda `=` untuk memberi nilai.

---

## 1. Sejarah Python

Python dikembangkan oleh **Guido van Rossum** di Belanda. Ia mulai menulis Python pada Desember 1989, dan rilis publik pertama (versi 0.9.0) muncul pada **Februari 1991**. Nama "Python" tidak diambil dari ular, melainkan dari acara komedi Inggris *Monty Python's Flying Circus* — itulah kenapa banyak contoh di dokumentasi lama bernuansa humor.

Filosofi desainnya menekankan **keterbacaan kode** (readability). Prinsip ini dirangkum dalam *The Zen of Python* yang bisa Anda panggil sendiri:

```python
# Jalankan sel ini untuk melihat filosofi desain Python
import this
```

**Garis waktu singkat:**

| Tahun | Versi | Catatan |
|-------|-------|---------|
| 1991  | 0.9.0 | Rilis publik pertama |
| 1994  | 1.0   | Versi stabil pertama |
| 2000  | 2.0   | Fitur list comprehension, garbage collection |
| 2008  | 3.0   | Perombakan besar, **tidak backward-compatible** dengan 2.x |
| 2020  | —     | Python 2.7 resmi *end-of-life* (berhenti didukung) |
| 3.x   | 3.13+ | Lini yang dipakai sekarang; wajib pakai Python 3 |

> **Catatan untuk mahasiswa:** Anda mungkin masih menemukan tutorial lama dengan `print "..."` (tanpa kurung). Itu sintaks Python 2 dan sudah usang. Semua materi kuliah ini memakai **Python 3**.

```python
# Program pertama Anda
print("Halo, Python! — Praktikum TRPE")
```

---

## 2. Kelebihan dan Kekurangan Python

Sebagai calon teknisi/insinyur pembangkit energi, penting memahami *kapan* Python adalah alat yang tepat.

### Kelebihan

- **Sintaks sederhana & mudah dibaca** — mendekati bahasa Inggris, cocok untuk pemula.
- **Multiplatform** — kode yang sama jalan di Windows, Linux, macOS, hingga Raspberry Pi.
- **Ekosistem library sangat luas** — untuk kebutuhan teknik: `NumPy` (numerik), `Pandas` (data), `Matplotlib` (grafik), `scikit-learn` (machine learning), `pyserial` (komunikasi sensor).
- **Komunitas besar** — mudah mencari solusi dan dokumentasi.
- **Cepat untuk prototyping** — ideal untuk analisis data sensor, IoT, dan riset.
- **Open source & gratis.**

### Kekurangan

- **Lebih lambat** dibanding C/C++ karena bersifat *interpreted* (diterjemahkan baris demi baris saat dijalankan).
- **Konsumsi memori lebih tinggi.**
- **Kurang ideal untuk kontrol real-time / embedded tingkat rendah** — untuk memprogram mikrokontroler (misal kontrol motor presisi), C/C++ masih lebih disukai.
- **Dynamic typing** memudahkan penulisan, tapi bisa menyembunyikan bug tipe data sampai program berjalan.

> **Intinya untuk TRPE:** Python unggul untuk **analisis data, visualisasi, dan prototipe di sisi PC/single-board computer**; sedangkan untuk **kontrol tertanam yang butuh presisi waktu**, bahasa low-level tetap relevan.

---

## 3. Membuat Variabel dan Aturan Penamaan

**Variabel** adalah nama yang menunjuk ke sebuah nilai yang tersimpan di memori. Di Python, Anda **tidak perlu mendeklarasikan tipe** — cukup memberi nilai dengan tanda `=`.

```python
# Contoh: data sebuah panel surya
tegangan = 220          # int
arus = 5.5              # float
nama_alat = "Inverter"  # str
aktif = True            # bool

print(tegangan, arus, nama_alat, aktif)
```

### 3.1 Aturan Wajib (kalau dilanggar → error)

1. Diawali **huruf** atau **underscore** (`_`), **tidak boleh** diawali angka.
2. Hanya boleh mengandung huruf, angka, dan underscore.
3. **Case-sensitive** — `Suhu`, `suhu`, dan `SUHU` adalah tiga variabel berbeda.
4. Tidak boleh berupa **kata kunci** (keyword) Python.
5. Tidak boleh mengandung **spasi**.

```python
# Melihat daftar kata kunci yang TIDAK boleh dipakai sebagai nama variabel
import keyword
print(keyword.kwlist)
```

| Valid          | Tidak Valid     | Alasan                        |
|----------------|-----------------|-------------------------------|
| `suhu_ruang`   | `2suhu`         | Diawali angka                 |
| `teganganAC`   | `tegangan AC`   | Mengandung spasi              |
| `_daya`        | `daya-motor`    | `-` dianggap operasi kurang   |
| `arus1`        | `class`         | `class` adalah keyword        |

### 3.2 Konvensi Penamaan (PEP 8 — sangat dianjurkan)

Aturan wajib bikin kode *jalan*; konvensi bikin kode *dibaca orang lain*.

- **`snake_case`** untuk variabel dan fungsi → `daya_output`, `hitung_efisiensi`.
- **`HURUF_BESAR`** untuk konstanta → `TEGANGAN_NOMINAL = 220`.
- Gunakan nama **deskriptif**: `t` kurang jelas, `suhu_generator` jauh lebih baik.

```python
# Beberapa nilai sekaligus & tukar nilai (swap)
v1, v2, v3 = 12, 24, 48
print(v1, v2, v3)

# Menukar tanpa variabel bantu — ciri khas Python
a, b = 10, 20
a, b = b, a
print("Setelah swap:", a, b)
```

---

## 4. Tipe Data: Primitif dan Non-Primitif

> **Catatan konsep:** Di Python secara teknis *semua adalah objek*. Namun secara pedagogis, tipe data dibagi menjadi **primitif** (nilai tunggal/dasar) dan **non-primitif** (kumpulan/terstruktur). Kita pakai pembagian ini agar mudah dipahami.

### 4.1 Tipe Data Primitif

| Tipe      | Contoh          | Keterangan                              |
|-----------|-----------------|-----------------------------------------|
| `int`     | `220`           | Bilangan bulat                          |
| `float`   | `5.5`           | Bilangan desimal                        |
| `bool`    | `True` / `False`| Nilai logika                            |
| `str`     | `"Generator"`   | Teks (deret karakter)                   |
| `complex` | `complex(3, 2)` | Bilangan kompleks (berguna di analisis AC!) |

```python
# Deklarasi tipe primitif dengan konteks kelistrikan
frekuensi = 50                 # int  — Hz
faktor_daya = 0.85             # float — cos φ
tiga_fasa = True               # bool
label = "Trafo Distribusi"     # str
impedansi = complex(4, 3)      # complex — Z = R + jX (Ohm)

# Fungsi type() untuk memeriksa tipe data
print(type(frekuensi))
print(type(faktor_daya))
print(type(tiga_fasa))
print(type(label))
print(type(impedansi))
```

> **Catatan:** `str` secara teknis adalah *sequence* objek yang immutable, tetapi biasa diajarkan sebagai tipe dasar karena mewakili satu nilai teks.

### 4.2 Tipe Data Non-Primitif (Koleksi)

| Tipe    | Sintaks        | Terurut? | Bisa Diubah?    | Duplikat?  |
|---------|----------------|----------|-----------------|------------|
| `list`  | `[ ]`          | Ya       | Ya (mutable)    | Boleh      |
| `tuple` | `( )`          | Ya       | Tidak (immutable)| Boleh     |
| `set`   | `{ }`          | Tidak    | Ya              | **Tidak**  |
| `dict`  | `{key: value}` | Ya*      | Ya              | Key unik   |

\* `dict` mempertahankan urutan penyisipan sejak Python 3.7.

```python
# LIST — data pembacaan suhu generator (bisa diubah, ada indeks)
suhu_harian = [68.5, 70.1, 71.3, 69.8, 72.0]
print("Suhu jam ke-3:", suhu_harian[2])   # indeks mulai dari 0
suhu_harian.append(73.2)                   # menambah data
print("Setelah ditambah:", suhu_harian)

# TUPLE — spesifikasi tetap yang tidak boleh berubah
rating_trafo = (220, 380, 50)   # (V primer, V sekunder, frekuensi)
print("Tegangan primer:", rating_trafo[0])

# SET — daftar jenis pembangkit unik (duplikat otomatis dibuang)
jenis_pembangkit = {"PLTU", "PLTA", "PLTS", "PLTU"}
print("Jenis unik:", jenis_pembangkit)

# DICT — spesifikasi satu unit pembangkit (akses lewat key)
generator = {
    "nama": "Unit-1",
    "kapasitas_MW": 100,
    "tegangan_kV": 11,
    "status": "operasi"
}
print("Kapasitas:", generator["kapasitas_MW"], "MW")
generator["status"] = "pemeliharaan"   # mengubah nilai
print(generator)
```

---

## 5. Fungsi dan Method yang Digunakan dalam Praktikum

Sebelum mengerjakan latihan, kenali dulu "alat" yang akan Anda pakai. Semuanya adalah **fungsi bawaan (built-in)** Python — blok kode siap pakai yang tinggal dipanggil dengan namanya, diikuti tanda kurung `( )`. Apa yang ditulis di dalam kurung disebut **argumen** (masukan untuk fungsi tersebut).

```python
nama_fungsi(argumen)
#    ↑          ↑
#  nama      masukan
```

### Fungsi vs Method — perbedaan penulisan

- **Fungsi** dipanggil berdiri sendiri: `print(nilai)`, `type(nilai)`.
- **Method** adalah fungsi yang "menempel" pada suatu objek dan dipanggil dengan **titik**: `daftar.append(nilai)`. Method hanya bisa dipakai oleh tipe data tertentu (misal `.append()` khusus untuk `list`).

### Ringkasan

| Nama        | Jenis            | Kegunaan                                        | Contoh              |
|-------------|------------------|-------------------------------------------------|---------------------|
| `print()`   | Fungsi           | Menampilkan nilai ke layar                      | `print("Halo")`     |
| `type()`    | Fungsi           | Memberitahu **tipe data** sebuah nilai          | `type(220)` → `int` |
| `len()`     | Fungsi           | Menghitung **jumlah elemen** dalam koleksi/teks | `len([1,2,3])` → `3`|
| `complex()` | Fungsi           | **Membuat** bilangan kompleks dari real & imajiner | `complex(4, 3)`  |
| `.append()` | Method (`list`)  | Menambah **satu** elemen di akhir list          | `data.append(5)`    |
| `import`    | Pernyataan       | Memanggil modul/library tambahan                | `import keyword`    |

### Penjelasan singkat

- **`print()`** — menampilkan satu atau beberapa nilai ke layar. Bisa diberi beberapa argumen yang dipisah koma; Python otomatis memberi spasi di antaranya.
- **`type()`** — mengembalikan tipe data dari nilai/variabel. Sangat berguna untuk memastikan sebuah data benar-benar `int`, `str`, `list`, dan seterusnya.
- **`len()`** — menghitung banyaknya elemen. Bekerja pada koleksi (`list`, `tuple`, `set`, `dict`) maupun teks (`str`).
- **`complex()`** — fungsi pembuat (*constructor*) untuk tipe `complex`. Tipe `int`, `float`, `str`, dan `bool` juga punya fungsi pembuat senama (`int()`, `float()`, `str()`, `bool()`); penggunaannya untuk **konversi antar-tipe** akan dibahas pada pertemuan berikutnya.
- **`.append()`** — method milik `list` untuk menambahkan satu elemen di posisi paling akhir. Karena ini method, penulisannya `nama_list.append(...)`, bukan `append(nama_list, ...)`.
- **`import`** — bukan fungsi, melainkan **pernyataan** untuk memuat modul agar fitur tambahannya bisa dipakai (misal `import keyword` untuk melihat daftar kata kunci, atau `import this` untuk *The Zen of Python*).

> **Perhatikan:** tanda `=` (penugasan) dan `[ ]` (indeks/pembuatan list) **bukan** fungsi — keduanya adalah bagian dari sintaks dasar bahasa, bukan sesuatu yang "dipanggil".

### Sel demo — coba jalankan dan amati hasilnya

```python
# print() dengan beberapa argumen sekaligus
print("Tegangan:", 220, "Volt")

# type() untuk mengecek tipe
print(type(220))        # <class 'int'>
print(type("PLTU"))     # <class 'str'>

# len() menghitung jumlah elemen dan panjang teks
komponen = ["resistor", "kapasitor", "dioda"]
print(len(komponen))    # 3
print(len("Trafo"))     # 5

# complex() membuat bilangan kompleks
print(complex(4, 3))    # (4+3j)

# .append() method milik list
komponen.append("transistor")
print(komponen)         # bertambah 'transistor' di akhir
```

---

## 6. Latihan Mahasiswa (Implementasi Materi)

Kerjakan pada sel kosong di bawah tiap soal. Semua konteks bersifat teknik elektro/energi. Ingat: modul ini baru sampai *variabel & tipe data* — cukup gunakan `=`, indeks `[ ]`, dan fungsi/method yang sudah dijelaskan. **Belum ada perhitungan.**

### Latihan 1 — Membuat variabel *(mudah)*

Sebuah panel surya memiliki tegangan **18 volt**, arus **6 ampere**, dan jenis sel **"Monocrystalline"**. Buat tiga variabel dengan nama yang sesuai konvensi PEP 8, lalu cetak ketiganya.

```python
# Jawaban Latihan 1

```

### Latihan 2 — Tipe primitif & type() *(mudah)*

Buat satu variabel untuk **masing-masing** tipe: `int`, `float`, `bool`, `str` (data komponen elektronika bebas). Cetak **nilai** dan **tipe** tiap variabel dengan `type()`.

```python
# Jawaban Latihan 2

```

### Latihan 3 — Memilih tipe yang tepat *(sedang)*

Tentukan tipe data yang **paling sesuai** untuk tiap data berikut, buat variabelnya, lalu buktikan dengan `type()`:

- Nama unit: `PLTS Nunukan`
- Jumlah panel: `240`
- Tegangan keluaran: `48.5`
- Sedang beroperasi: `benar`

```python
# Jawaban Latihan 3

```

### Latihan 4 — List *(sedang)*

Berikut daftar pembacaan tegangan (V) sebuah panel:

```python
tegangan_harian = [217.5, 219.0, 220.3, 218.7, 221.1, 216.9]
```

Tugas: (a) cetak pembacaan **pertama** dan **terakhir** memakai indeks, (b) tambahkan satu pembacaan baru `222.0` dengan `append()`, (c) cetak **jumlah total** data dengan `len()`.

```python
# Jawaban Latihan 4

```

### Latihan 5 — Dictionary *(sedang)*

B
