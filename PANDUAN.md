# 📘 Panduan Cepat - Sistem Klasifikasi Cabai Rawit

## 🚀 Memulai dalam 3 Langkah

### Langkah 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Atau double-click file `run.bat` (otomatis install + jalankan aplikasi)

### Langkah 2: Siapkan Dataset

1. Kumpulkan gambar cabai (minimal 100 per kelas)
2. Simpan ke folder:
   - `dataset/cabai_setan/`
   - `dataset/cabai_celeng/`
   - `dataset/cabai_putih/`
   - `dataset/cabai_merah_keriting/`

**Sumber dataset:**
- Kaggle: https://www.kaggle.com/datasets/favioe/chili-images-for-classification
- Foto sendiri dari pasar
- Internet (Google Images)

### Langkah 3: Jalankan Aplikasi

```bash
streamlit run app.py
```

Website akan terbuka di: **http://localhost:8501**

---

## 🎯 Alur Kerja Lengkap

### A. Training Model (Jika Belum Ada)

```bash
# 1. Pastikan dataset sudah siap
# 2. Jalankan training
python train_model.py

# Tunggu 1-3 jam (tergantung hardware)
# Model akan tersimpan sebagai model_cabai.keras
```

### B. Menjalankan Website

```bash
streamlit run app.py
```

### C. Menggunakan Aplikasi

1. **Buka Beranda** → Baca informasi tentang sistem
2. **Klik "Mulai Klasifikasi"** → Ke halaman klasifikasi
3. **Upload Gambar** → Pilih foto cabai (JPG/PNG)
4. **Klik "Prediksi Sekarang"** → Tunggu hasil
5. **Lihat Hasil** → Jenis cabai + confidence score
6. **Simpan ke Riwayat** → Data tersimpan di database

### D. Melihat Riwayat

1. Klik menu **"Riwayat"** di sidebar
2. Lihat semua prediksi yang sudah disimpan
3. Hapus riwayat tertentu atau semua sekaligus

---

## 📁 Struktur File Penting

```
cabai-difa/
├── app.py                 ← Halaman beranda (START HERE)
├── database.py            ← Fungsi database SQLite
├── train_model.py         ← Script training model
├── requirements.txt       ← List dependencies
├── run.bat               ← Quick start (Windows)
├── check_system.py       ← Cek kesiapan sistem
│
├── pages/
│   ├── 1_klasifikasi.py  ← Halaman klasifikasi
│   ├── 2_riwayat.py      ← Halaman riwayat
│   └── 3_tentang.py      ← Halaman tentang
│
└── dataset/              ← Folder dataset gambar
    ├── cabai_setan/
    ├── cabai_celeng/
    ├── cabai_putih/
    └── cabai_merah_keriting/
```

---

## ⚠️ Troubleshooting

### Error: "ModuleNotFoundError"
```bash
# Solusi: Install dependencies
pip install -r requirements.txt
```

### Error: "Model tidak ditemukan"
```bash
# Solusi: Train model terlebih dahulu
python train_model.py
```

### Error: "Dataset tidak ditemukan"
```
# Solusi: Pastikan folder dataset sudah ada
# dan berisi gambar cabai sesuai kelas
```

### Aplikasi Lambat
```
# Gunakan GPU untuk training
# Untuk prediksi, CPU sudah cukup cepat
```

---

## 🔍 Cek Kesiapan Sistem

```bash
python check_system.py
```

Script ini akan mengecek:
- ✓ Versi Python (minimal 3.8)
- ✓ Dependencies terinstall
- ✓ Struktur folder lengkap
- ✓ Dataset ada
- ✓ Model sudah terlatih
- ✓ Database siap

---

## 📊 Informasi Teknis

### Model
- **Arsitektur:** MobileNetV2
- **Framework:** TensorFlow + Keras
- **Pre-trained:** ImageNet
- **Classes:** 4 jenis cabai
- **Image Size:** 224x224 pixels

### Training
- **Epochs:** 30
- **Batch Size:** 32
- **Optimizer:** Adam
- **Dataset Split:** 80% train, 20% validation

### Database
- **Type:** SQLite
- **File:** prediksi.db
- **Tabel:** prediksi (id, nama_file, hasil, confidence, tanggal)

---

## 🎨 Fitur Website

### Halaman Beranda
- Informasi sistem
- Penjelasan 4 jenis cabai
- Panduan penggunaan

### Halaman Klasifikasi
- Upload gambar (drag & drop)
- Preview gambar
- Prediksi otomatis
- Confidence score
- Bar chart probabilitas
- Simpan ke riwayat

### Halaman Riwayat
- Tabel riwayat prediksi
- Detail lengkap (file, hasil, confidence, tanggal)
- Hapus per ID
- Hapus semua

### Halaman Tentang
- Informasi teknis
- Metode dan teknologi
- Arsitektur model
- Dataset
- Cara kerja sistem

---

## 💡 Tips

1. **Dataset Berkualitas** = Model Akurat
   - Minimal 100 gambar per kelas
   - Variasi sudut, pencahayaan, background
   - Gambar jelas, tidak buram

2. **Training Optimal**
   - Gunakan GPU jika ada
   - Monitor training history
   - Early stopping mencegah overfitting

3. **Prediksi Akurat**
   - Upload gambar cabai yang jelas
   - Cabai terlihat dominan
   - Pencahayaan baik
   - Resolusi minimal 224x224

---

## 📞 Butuh Bantuan?

1. Cek file README.md untuk dokumentasi lengkap
2. Jalankan `python check_system.py` untuk diagnosa
3. Lihat halaman "Tentang" di website untuk info teknis

---

**© 2026 - Project Cabai Difa**
