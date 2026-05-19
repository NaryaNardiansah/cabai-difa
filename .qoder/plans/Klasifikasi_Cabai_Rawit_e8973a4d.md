# Klasifikasi Cabai Rawit Indonesia

## Overview
Website klasifikasi 4 jenis cabai rawit (Setan, Celeng, Putih, Merah Keriting) menggunakan Streamlit + MobileNetV2 + SQLite dengan tema hitam-putih.

---

## Struktur Proyek

```
c:\Projects\cabai-difa\
├── app.py                    # Main Streamlit app
├── model_cabai.keras         # Model terlatih (akan dibuat)
├── database.py               # Database SQLite functions
├── prediksi.db               # Database file (auto-created)
├── requirements.txt          # Dependencies
├── train_model.py            # Script training model
├── dataset/                  # Dataset folder
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

---

## Tahap 1: Setup Project

### File: `requirements.txt`
```
streamlit==1.32.0
tensorflow==2.15.0
opencv-python==4.9.0
numpy==1.26.4
pandas==2.2.1
Pillow==10.2.0
matplotlib==3.8.3
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Tahap 2: Database SQLite

### File: `database.py`
Fungsi utama:
- `init_db()`: Inisialisasi database dan tabel `prediksi`
- `simpan_prediksi(nama_file, hasil_prediksi, confidence_score)`: Simpan hasil prediksi
- `ambil_riwayat()`: Ambil semua riwayat dari database
- `hapus_riwayat(id)`: Hapus satu riwayat berdasarkan ID
- `hapus_semua_riwayat()`: Hapus semua riwayat

Struktur tabel `prediksi`:
```sql
CREATE TABLE IF NOT EXISTS prediksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_file TEXT NOT NULL,
    hasil_prediksi TEXT NOT NULL,
    confidence_score REAL NOT NULL,
    tanggal_prediksi DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

---

## Tahap 3: Dataset Preparation

### Dataset dari Kaggle
Karena dataset spesifik cabai rawit Indonesia mungkin tidak tersedia di Kaggle, Anda perlu:

1. **Cari dataset cabai di Kaggle**: Kunjungi https://www.kaggle.com/datasets/favioe/chili-images-for-classification
2. **Download dan ekstrak** ke folder `dataset/`
3. **Organisir folder** sesuai kelas:
   - `dataset/cabai_setan/`
   - `dataset/cabai_celeng/`
   - `dataset/cabai_putih/`
   - `dataset/cabai_merah_keriting/`

4. **Jika dataset tidak tersedia**, Anda bisa:
   - Mengumpulkan gambar sendiri dari pasar/internet
   - Menggunakan augmentasi untuk memperbanyak dataset
   - Minimum 100 gambar per kelas untuk training yang baik

### Pembagian dataset:
- Training: 70%
- Validation: 15%
- Testing: 15%

---

## Tahap 4: Training Model

### File: `train_model.py`
Langkah training:

1. **Load dataset** dengan `tf.keras.utils.image_dataset_from_directory`
2. **Preprocessing**:
   - Resize ke 224x224
   - Normalisasi pixel (0-1)
3. **Augmentasi**:
   - Random rotation
   - Random zoom
   - Random flip
   - Random translation
4. **Load MobileNetV2** dengan weights ImageNet
5. **Fine-tuning**:
   - Freeze base model
   - Tambahkan layer Dense untuk 4 kelas
   - Compile dengan Adam optimizer
6. **Training**:
   - Epochs: 20-30
   - Batch size: 32
   - Callbacks: Early Stopping, ModelCheckpoint
7. **Evaluasi** dengan test set
8. **Save model** ke `model_cabai.keras`

Arsitektur model:
```python
base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dropout(0.5),
    Dense(4, activation='softmax')  # 4 kelas cabai
])
```

---

## Tahap 5: Website Streamlit

### File: `app.py` (Halaman Beranda)
Tampilan:
- Judul: "Sistem Klasifikasi Cabai Rawit Indonesia"
- Deskripsi singkat
- Penjelasan 4 jenis cabai dengan gambar
- Tombol "Mulai Klasifikasi" → redirect ke halaman klasifikasi

Tema hitam-putih dengan custom CSS:
```python
st.markdown("""
<style>
    .main { background-color: white; color: black; }
    .stButton > button { 
        background-color: black; 
        color: white; 
        border: none;
    }
    .stButton > button:hover { 
        background-color: #333333; 
    }
</style>
""", unsafe_allow_html=True)
```

### File: `pages/1_klasifikasi.py` (Halaman Klasifikasi)
Fitur:
1. Upload gambar cabai (drag & drop atau browse)
2. Preview gambar yang diupload
3. Tombol "Prediksi Sekarang"
4. Proses preprocessing gambar (resize 224x224, normalisasi)
5. Load model `model_cabai.keras`
6. Prediksi dan tampilkan:
   - Jenis cabai dengan probabilitas tertinggi
   - Confidence score dalam persen
   - Bar chart probabilitas semua kelas
7. Tombol "Simpan ke Riwayat" → simpan ke database

Alur prediksi:
```python
def prediksi_gambar(image, model):
    # Resize ke 224x224
    img = image.resize((224, 224))
    # Convert ke array
    img_array = np.array(img)
    # Normalisasi
    img_array = img_array / 255.0
    # Expand dimensions
    img_array = np.expand_dims(img_array, axis=0)
    # Prediksi
    predictions = model.predict(img_array)
    # Get class dengan probabilitas tertinggi
    class_idx = np.argmax(predictions[0])
    confidence = predictions[0][class_idx] * 100
    return class_idx, confidence
```

Mapping kelas:
```python
kelas_cabai = {
    0: 'Cabai Setan',
    1: 'Cabai Celeng',
    2: 'Cabai Putih',
    3: 'Cabai Merah Keriting'
}
```

### File: `pages/2_riwayat.py` (Halaman Riwayat)
Fitur:
1. Tampilkan tabel riwayat prediksi dari database
2. Kolom: No, Nama File, Hasil Prediksi, Confidence, Tanggal
3. Tombol "Hapus" untuk setiap baris
4. Tombol "Hapus Semua Riwayat"
5. Pagination jika data banyak

Tampilan tabel dengan pandas:
```python
df = pd.DataFrame(riwayat, columns=['ID', 'Nama File', 'Hasil', 'Confidence', 'Tanggal'])
st.dataframe(df, use_container_width=True)
```

### File: `pages/3_tentang.py` (Halaman Tentang)
Informasi:
- Nama sistem
- Metode: Transfer Learning dengan MobileNetV2
- Arsitektur model (diagram sederhana)
- Dataset yang digunakan
- Framework: TensorFlow, Keras, Streamlit
- Tujuan aplikasi
- Tim pengembang

---

## Tahap 6: Testing & Validasi

### Testing Model:
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- Test dengan gambar yang belum pernah dilihat model

### Testing Website:
- Upload gambar JPG/PNG → berhasil
- Prediksi → hasil muncul dengan confidence score
- Simpan riwayat → data masuk database
- Lihat riwayat → data tampil di tabel
- Hapus riwayat → data terhapus dari database

---

## Tahap 7: Menjalankan Aplikasi

### Cara menjalankan:
```bash
streamlit run app.py
```

Website akan terbuka di browser pada `http://localhost:8501`

---

## Catatan Penting

1. **Dataset**: Jika dataset dari Kaggle tidak sesuai, Anda perlu mengumpulkan gambar sendiri atau menggunakan dataset publik lainnya
2. **Training**: Training model membutuhkan waktu (1-3 jam tergantung hardware). GPU direkomendasikan tetapi tidak wajib
3. **Model**: Model yang sudah dilatih harus disimpan sebagai `model_cabai.keras` agar website bisa menggunakannya
4. **Database**: Database `prediksi.db` akan otomatis dibuat saat pertama kali menjalankan aplikasi
5. **Tema**: Tema hitam-putih diterapkan menggunakan custom CSS di Streamlit

---

## Next Steps

1. Setup project structure dan install dependencies
2. Buat `database.py` dengan semua fungsi CRUD
3. Kumpulkan dan organisir dataset cabai
4. Training model dengan `train_model.py`
5. Buat halaman Streamlit (beranda, klasifikasi, riwayat, tentang)
6. Testing menyeluruh
7. Deployment (opsional)
