# Log Penggunaan AI - Audit Statistik pandas-dev/pandas

## Ringkasan

| Anggota | Peran | Alat | ~% Kode yang Dibantu AI | Sel Interpretasi Dibantu AI? |
|---|---|---|---|---|
| Muhammad Rasyid Setyadi Dwi Putra | Data Engineer | Gemini, ChatGPT, Claude | ~35% | Tidak |
| Neisya Nurfadilah | Estimation Analyst | — | — | — |
| Adinda Syafira Kusumadewi | Inference Analyst | ChatGPT | ~40% | Tidak |
| Rafiif Ikbaar Taufiqulhakiim | Hypothesis Analyst | — | — | — |
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

### Adinda Syafira Kusumadewi — Estimation Analyst

| No | Tugas | Alat | Prompt | Cara Output Digunakan |
|---|---|---|---|---|
| 1 | Mencari kesalahan kode error pada python | ChatGPT | "Apa yang salah dari kode ini?" | Terlihat adanya masalah sintaks seperti penempatan kurung kurawal yang kurang tepat hingga menyebabkan error |
| 2 | Rule Of Three pada CI Bernoulli | ChatGPT | "Apakah Penanganan Kasus Ekstrem Statistika (Rule of Three) perlu ditambah pada bernoulli?" | Ya, karena membuat fungsi lebih robust dan menangani kasus ekstrem dengan lebih realistis |

**Ditulis tanpa AI:** Seluruh sel markdown interpretasi; Rumusan 4 research question; Narasi ringkasan dan kontekstualisasi terhadap repositori pandas; Keputusan variabel yang diteruskan ke Anggota D.

---

### C — Inference Analyst

(Akan diisi oleh Anggota C.)

---

### D — Hypothesis Analyst

(Akan diisi oleh Anggota D.)

---

### E — Computation Analyst

(Akan diisi oleh Anggota E.)
