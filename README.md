# Audit Statistik `pandas-dev/pandas`

** Statistika dan Probabilitas **
Repositori: [pandas-dev/pandas](https://github.com/pandas-dev/pandas)

---

## Deskripsi Proyek

Repositori `pandas-dev/pandas` dipilih sebagai objek audit karena memenuhi semua persyaratan yang ditetapkan, di mana mengandung lebih dari 1.000 isu tertutup, lebih dari 500 PR yang digabungkan, data event bertimestamp, dan berstatus proyek perangkat lunak aktif. Audit ini menerapkan konsep statistik dari Minggu 11–14 untuk menjawab pertanyaan-pertanyaan konkret tentang kesehatan dan perilaku proyek, mulai dari pengumpulan dan pembersihan data hingga estimasi parameter, pengujian hipotesis, dan simulasi komputasional.

---

## Pertanyaan Penelitian

Proyek ini berpusat pada tiga pertanyaan, masing-masing untuk satu lapisan analisis.

**P1 — Estimasi (Minggu 11):** Berapa probabilitas sebuah PR digabungkan (merged), dan seberapa besar ketidakpastiannya bila dimodelkan dengan distribusi Beta?
**P2 — Inferensi & Pengujian (Minggu 12–13):** Apakah rata-rata waktu penyelesaian isu berbeda secara signifikan antara isu berlabel `bug` dan `enhancement`?
**P3 — Simulasi (Minggu 14):** Berapa probabilitas sebuah isu membutuhkan lebih dari 30 hari untuk ditutup, bila diestimasi lewat simulasi Monte Carlo?

---

## Temuan Utama

Akan diisi setelah seluruh analisis selesai.

---

## Cara Menjalankan

Pastikan Python 3.10+ sudah terpasang, lalu jalankan:

```bash
git clone https://github.com/<username>/stat-audit-pandas-sti-2025.git
cd stat-audit-pandas-sti-2025
pip install -r requirements.txt
```

Untuk mengumpulkan ulang data mentah dari API:

```bash
python src/collect_data.py
```

Notebook dijalankan berurutan dari `01_eda.ipynb` hingga `05_simulation.ipynb`. Semua fungsi inti sudah ada di `src/` dan diimpor langsung dari sana. Jika tidak ingin mengumpulkan ulang data, `data/clean/dataset.csv` sudah tersedia dan bisa langsung dipakai.

---

## Tabel Tim

| Anggota | Peran | Tanggung Jawab |
|---|---|---|
| Muhammad Rasyid Setyadi Dwi Putra | Data Engineer | Pengumpulan data, pembersihan, EDA, pemilihan variabel |
| B | Estimation Analyst | Derivasi MLE, posterior Beta, visualisasi likelihood |
| C | Inference Analyst | Selang kepercayaan, selang kredibel |
| D | Hypothesis Analyst | Pengujian hipotesis, interpretasi p-value |
| E | Computation Analyst | Simulasi Monte Carlo, Bloom Filter, MCMC |

---

## Sumber Data

- GitHub REST API: `https://api.github.com/repos/pandas-dev/pandas/issues`
- Dokumentasi API: `https://docs.github.com/en/rest/issues/issues`
- Rentang data: isu dan PR yang dibuat antara 1 Januari 2020 hingga 31 Desember 2024
- Keterbatasan: data yang dikumpulkan merupakan sampel, bukan seluruh populasi, karena GitHub API membatasi jumlah permintaan per jam

---

## Referensi

Tsun, A. (2020). *Probability and Statistics for Engineers and Scientists*. Penerbit Universitas. (Seluruh formula diimplementasikan sesuai buku ini.)