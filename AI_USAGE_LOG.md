# Log Penggunaan AI - Audit Statistik pandas-dev/pandas

## Ringkasan

| Anggota | Peran | Alat | ~% Kode yang Dibantu AI | Sel Interpretasi Dibantu AI? |
|---|---|---|---|---|
| Muhammad Rasyid Setyadi Dwi Putra | Data Engineer | Gemini, ChatGPT, Claude | ~35% | Tidak |
| Neisya Nurfadilah | Estimation Analyst | ChatGPT | ~30% | Tidak | 
| Adinda Syafira Kusumadewi | Inference Analyst | ChatGPT | ~40% | Tidak |
| Rafiif Ikbaar Taufiqulhakiim | Hypothesis Analyst | Gemini | ~25% | Tidak |
| Muhammad Risqi Maulana | Computation Analyst | — | — | — |

---

## Detail Per-Anggota

### Muhammad Rasyid Setyadi Dwi Putra — Data Engineer

| No | Tugas | Alat | Prompt | Cara Output Digunakan |
|---|---|---|---|---|
| 1 | Debug error kolom `merged` bernilai NaN | Gemini | "Kenapa kolom merged NaN semua padahal datanya dari GitHub API?" | Dari situ ketahuan `merged_at` ada di dalam objek `pull_request` bukan di level atas, kodenya tetap ditulis sendiri |
| 2 | Merapikan kalimat di sel markdown | ChatGPT | "Rapihin kalimat ini, isinya jangan diubah" | Beberapa susunan kalimat diperbaiki, kecuali interpretasi statistik |
| 3 | Perbaikan skrip pengumpul data | Claude | "Skrip ini error pas dijalankan, tolong bantu cek kenapa" | Claude menunjukkan bagian yang bermasalah di `collect_data.py` |

**Ditulis tanpa AI:**
- Keputusan variabel mana yang diteruskan ke tiap anggota dan alasan statistiknya
- Narasi ringkasan EDA dan kaitannya dengan lapisan analisis berikutnya
- Fungsi `clean_issues()` secara keseluruhan, termasuk penanganan isu terbuka dan derivasi kolom `has_bug` dan `has_enhancement`
- Interpretasi distribusi right-skewed dan implikasinya terhadap uji Z

---

### B — Estimation Analyst

(Akan diisi oleh Anggota B.)

---

### Adinda Syafira Kusumadewi — Inference Analyst

| No | Tugas | Alat | Prompt | Cara Output Digunakan |
|---|---|---|---|---|
| 1 | Mencari kesalahan kode error pada python | ChatGPT | "Apa yang salah dari kode ini?" | Terlihat adanya masalah sintaks seperti penempatan kurung kurawal yang kurang tepat hingga menyebabkan error |
| 2 | Rule Of Three pada CI Bernoulli | ChatGPT | "Apakah Penanganan Kasus Ekstrem Statistika (Rule of Three) perlu ditambah pada bernoulli?" | Ya, karena membuat fungsi lebih robust dan menangani kasus ekstrem dengan lebih realistis |

**Ditulis tanpa AI:** Seluruh sel markdown interpretasi; Rumusan 4 research question; Narasi ringkasan dan kontekstualisasi terhadap repositori pandas; Keputusan variabel yang diteruskan ke Anggota D.

---

### Rafiif Ikbaar Taufiqulhakiim — Hypothesis Analyst

| No | Tugas | Alat | Prompt | Cara Output Digunakan |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Pembuatan struktur fungsi dasar `z_test_two_sample` | Gemini | "Bagaimana formula Python untuk manual Two-Sample Z-Test berdasarkan buku statistik?" | Output template fungsi digunakan sebagai basis logika komputasi matematika di cell 2, namun disesuaikan kembali alur kondisinya. |
| 2 | Otomatisasi penanganan *path* direktori | Gemini | "Solusi jika sys.path.append tidak bisa mendeteksi root project karena double folder ekstraksi zip" | Digunakan sebagai alternatif solusi dinamis menggunakan modul `os` bawaan Python agar pencarian file data bersifat *robust*. |

**Ditulis tanpa AI:** * Seluruh pengerjaan penyusunan narasi interpretasi akademik hasil uji hipotesis (analisis nilai $P$-value $= 0.3918$ terhadap tingkat signifikansi $\alpha = 0.05$).
* Keputusan akhir statistik untuk Gagal Menolak $H_0$ serta analisis kritis mengenai ketimpangan jumlah sampel ($n_{\text{bug}}=52$ vs $n_{\text{enhancement}}=6$).
* Penyelarasan, pembersihan *missing value* (`.dropna()`), dan pemetaan manual variabel target berdasarkan kolom riil dataset hasil preprocessing kelompok (`'labels'` dan `'days_to_close'`).

---

### E — Computation Analyst

(Akan diisi oleh Anggota E.)
