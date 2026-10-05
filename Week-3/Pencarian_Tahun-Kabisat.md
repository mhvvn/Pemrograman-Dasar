# Menentukan Tahun Kabisat

## Studi Kasus

Sebuah tahun disebut tahun kabisat jika memenuhi salah satu dari dua kondisi berikut:

- a. Tahun tersebut habis dibagi 4, tetapi tidak habis dibagi 100.
- b. Tahun tersebut habis dibagi 400.

---

## 1. Ekspresi Logika Kompleks

```python
(tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
```

| Bagian | Arti |
|---|---|
| `tahun % 4 == 0` | habis dibagi 4 |
| `tahun % 100 != 0` | tidak habis dibagi 100 |
| `and` | kondisi (a): **dan** |
| `or` | kondisi (a) **atau** (b) |
| `tahun % 400 == 0` | kondisi (b): habis dibagi 400 |

Hasilnya bertipe `bool` (`True`/`False`).

### Uji Nilai

| Tahun | %4==0 | %100!=0 | %400==0 | Hasil |
|---|---|---|---|---|
| 2024 | True | True | False | **True** |
| 1900 | True | False | False | **False** |
| 2000 | True | False | True | **True** |
| 2026 | False | True | False | **False** |

---

## 2. Program Sederhana (Python)

Program memuat lingkup, input, output, dan operasi aritmatika.

```python
# Lingkup: semua variabel berada di lingkup global (satu file)
tahun_sekarang = 2026

# INPUT
tahun = int(input("Masukkan tahun: "))

# Ekspresi logika 
kabisat = (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

# Operasi aritmatika
selisih = tahun_sekarang - tahun        # pengurangan
dekade = tahun // 10                    # pembagian bulat
sisa = tahun % 10                       # modulus
kuadrat = sisa ** 2                     # pangkat
jumlah = dekade + kuadrat               # penjumlahan
rata2 = (tahun + tahun_sekarang) / 2    # pembagian desimal

# indeks list dari nilai bool (False=0, True=1)
keterangan = ["Bukan Tahun Kabisat", "Tahun Kabisat"][kabisat]

# OUTPUT
print("Tahun               :", tahun)
print("Status (bool)       :", kabisat)
print("Keterangan          :", keterangan)
print("Selisih dg sekarang :", selisih)
print("Tahun // 10         :", dekade)
print("Tahun % 10          :", sisa)
print("Sisa ** 2           :", kuadrat)
print("Dekade + Kuadrat    :", jumlah)
print("Rata-rata tahun     :", rata2)
```

### Contoh Output (input 2024)

```
Tahun               : 2024
Status (bool)       : True
Keterangan          : Tahun Kabisat
Selisih dg sekarang : 2
Tahun // 10         : 202
Tahun % 10          : 4
Sisa ** 2           : 16
Dekade + Kuadrat    : 218
Rata-rata tahun     : 2025.0
```

### Penjelasan

| Unsur | Penjelasan |
|---|---|
| Lingkup | Semua variabel berlingkup global karena program tidak memakai fungsi |
| Input | `input()` dibungkus `int()` agar teks menjadi bilangan bulat |
| Output | `print()` |
| Operasi aritmatika | `-`, `//`, `%`, `**`, `+`, `/` |
| Tanpa percabangan | Keputusan dibuat dengan operator logika `and`, `or`, dan teks dipilih lewat indeks list `[...][kabisat]` |
