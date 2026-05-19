# 🌶️ Sistem Klasifikasi Cabai Rawit Indonesia

Website klasifikasi 4 jenis cabai rawit (Setan, Celeng, Putih, Merah Keriting) menggunakan **Streamlit**, **MobileNetV2**, dan **SQLite** dengan tema hitam-putih minimalis.

## 📋 Fitur Utama

- ✅ **Upload Gambar** - Drag & drop atau browse gambar cabai (JPG/PNG)
- ✅ **Prediksi AI** - Klasifikasi otomatis menggunakan model MobileNetV2
- ✅ **Confidence Score** - Menampilkan tingkat kepercayaan model
- ✅ **Visualisasi** - Bar chart probabilitas semua kelas cabai
- ✅ **Riwayat Prediksi** - Menyimpan dan mengelola riwayat prediksi
- ✅ **Database SQLite** - Penyimpanan lokal yang ringan
- ✅ **Tema Hitam-Putih** - Antarmuka modern, bersih, dan profesional

## 🏗️ Arsitektur Project

```
cabai-difa/
├── app.py                    # Halaman beranda
├── database.py               # Fungsi CRUD SQLite
├── train_model.py            # Script training model
├── requirements.txt          # Dependencies
├── model_cabai.keras         # Model terlatih (setelah training)
├── prediksi.db               # Database SQLite (auto-created)
├── dataset/                  # Folder dataset
│   ├── cabai_setan/
│   ├── cabai_celeng/
│   ├── cabai_putih/
│   └── cabai_merah_keriting/
├── pages/
│   ├── 1_klasifikasi.py      # Halaman klasifikasi
│   ├── 2_riwayat.py          # Halaman riwayat
│   └── 3_tentang.py          # Halaman tentang
└── assets/
    └── logo.png
```

## 🚀 Instalasi dan Setup

### 1. Clone Repository

```bash
cd c:\Projects\cabai-difa
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- streamlit==1.32.0
- tensorflow==2.15.0
- opencv-python==4.9.0
- numpy==1.26.4
- pandas==2.2.1
- Pillow==10.2.0
- matplotlib==3.8.3

### 3. Siapkan Dataset

Buat struktur folder dataset:

```
dataset/
├── cabai_setan/
├── cabai_celeng/
├── cabai_putih/
└── cabai_merah_keriting/
```

**Sumber Dataset:**
- Kaggle: https://www.kaggle.com/datasets/favioe/chili-images-for-classification
- Pengumpulan data real dari pasar tradisional
- Minimum 100 gambar per kelas direkomendasikan

### 4. Training Model (Opsional)

Jika Anda belum memiliki model yang terlatih:

```bash
python train_model.py
```

**Proses Training:**
- Load dataset dari folder
- Preprocessing (resize 224x224, normalisasi)
- Data augmentation (rotasi, zoom, flip)
- Training MobileNetV2 dengan fine-tuning
- Evaluasi model
- Save model ke `model_cabai.keras`

**Konfigurasi Training:**
- Epochs: 30
- Batch Size: 32
- Image Size: 224x224
- Classes: 4
- Dataset Split: 80% train, 20% validation

### 5. Jalankan Aplikasi

```bash
streamlit run app.py
```

Website akan terbuka di browser: **http://localhost:8501**

## 📖 Cara Menggunakan

### Halaman Beranda (app.py)
- Informasi tentang sistem klasifikasi
- Penjelasan 4 jenis cabai rawit
- Panduan penggunaan
- Tombol navigasi ke halaman klasifikasi

### Halaman Klasifikasi (pages/1_klasifikasi.py)
1. Upload gambar cabai (JPG/PNG)
2. Preview gambar yang diupload
3. Klik tombol **"Prediksi Sekarang"**
4. Lihat hasil klasifikasi dengan confidence score
5. Lihat detail probabilitas dalam bar chart
6. Klik **"Simpan ke Riwayat"** untuk menyimpan hasil

### Halaman Riwayat (pages/2_riwayat.py)
- Menampilkan tabel riwayat prediksi
- Detail: Nama file, hasil prediksi, confidence, tanggal
- Hapus riwayat per ID
- Hapus semua riwayat

### Halaman Tentang (pages/3_tentang.py)
- Informasi sistem dan pengembang
- Metode dan teknologi yang digunakan
- Arsitektur model MobileNetV2
- Dataset dan cara kerja sistem
- Persyaratan sistem

## 🤖 Model Machine Learning

### Arsitektur: MobileNetV2

**Struktur Model:**
```
MobileNetV2 (pre-trained ImageNet)
└── Global Average Pooling 2D
    └── Dropout (0.5)
        └── Dense (128, ReLU)
            └── Dropout (0.3)
                └── Dense (4, Softmax) - Output
```

**Kelas Cabai:**
- 0: Cabai Setan
- 1: Cabai Celeng
- 2: Cabai Putih
- 3: Cabai Merah Keriting

**Teknik yang Digunakan:**
- Transfer Learning dari ImageNet
- Data Augmentation (rotasi, zoom, flip, shift)
- Early Stopping untuk mencegah overfitting
- Model Checkpoint untuk menyimpan model terbaik

## 💾 Database

**Database:** SQLite (prediksi.db)

**Struktur Tabel:**
```sql
CREATE TABLE prediksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_file TEXT NOT NULL,
    hasil_prediksi TEXT NOT NULL,
    confidence_score REAL NOT NULL,
    tanggal_prediksi DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

**Fungsi Database (database.py):**
- `init_db()` - Inisialisasi database
- `simpan_prediksi()` - Simpan hasil prediksi
- `ambil_riwayat()` - Ambil semua riwayat
- `hapus_riwayat(id)` - Hapus riwayat tertentu
- `hapus_semua_riwayat()` - Hapus semua riwayat
- `get_total_riwayat()` - Hitung total riwayat

## 🎨 Tema dan UI

**Tema:** Hitam-Putih Minimalis

**Warna:**
- Background: Putih (#FFFFFF)
- Header/Teks: Hitam (#000000)
- Tombol: Hitam dengan teks putih
- Hover: Abu-abu gelap (#333333)
- Border: Abu-abu muda (#E0E0E0)

**Karakteristik:**
- Minimalis dan bersih
- Fokus pada gambar dan hasil prediksi
- Mudah digunakan oleh pengguna awam
- Responsif untuk berbagai ukuran layar

## 📊 Evaluasi Model

**Metrik Evaluasi:**
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Training History:**
- Visualisasi accuracy dan loss per epoch
- Plot otomatis disimpan sebagai `training_history.png`

## 🔧 Troubleshooting

### Error: Model tidak ditemukan
```
Solusi: Jalankan training model terlebih dahulu
python train_model.py
```

### Error: Dataset tidak ditemukan
```
Solusi: Pastikan folder dataset dan subfolder sudah ada
dan berisi gambar cabai sesuai kelas
```

### Error: Module not found
```
Solusi: Install dependencies
pip install -r requirements.txt
```

## 📝 Persyaratan Sistem

**Minimum:**
- Prosesor: Intel Core i3/i5 atau setara
- RAM: 8 GB
- Storage: 10 GB kosong
- Python: 3.8+

**Direkomendasikan:**
- GPU (untuk training model)
- RAM: 16 GB
- Storage: 20 GB

## 📚 Referensi

- Sandler, M., et al. (2018). "MobileNetV2: Inverted Residuals and Linear Bottlenecks"
- TensorFlow Documentation: https://www.tensorflow.org
- Streamlit Documentation: https://docs.streamlit.io
- Kaggle Datasets: https://www.kaggle.com/datasets

## 👥 Tim Pengembang

**Project Cabai Difa** - 2026

Tech Stack:
- Frontend: Streamlit
- Backend: Python + TensorFlow
- Database: SQLite
- Model: MobileNetV2

## 📄 Lisensi

Project ini dibuat untuk tujuan pembelajaran dan edukasi.

## 🤝 Kontribusi

Silakan membuat issue atau pull request jika ingin berkontribusi pada project ini.

## 📞 Kontak

Untuk pertanyaan atau informasi lebih lanjut, silakan membuka issue di repository ini.

---

**© 2026 - Project Cabai Difa**

*Dibangun dengan ❤️ menggunakan Streamlit, TensorFlow, dan MobileNetV2*
