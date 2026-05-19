# 🎯 Panduan Meningkatkan Akurasi Model

## Masalah yang Anda Alami

Gambar cabai setan terdeteksi sebagai cabai merah keriting. Ini terjadi karena:
1. Model belum dilatih dengan benar
2. Dataset mungkin tidak berkualitas atau tidak seimbang
3. Model perlu fine-tuning lebih lanjut

## ✅ Solusi Lengkap

### Langkah 1: Periksa Kualitas Dataset

```bash
python check_dataset.py
```

Script ini akan:
- ✓ Cek apakah ada gambar corrupt
- ✓ Cek ukuran gambar (minimal 100x100 piksel)
- ✓ Analisis keseimbangan dataset
- ✓ Tampilkan contoh gambar
- ✓ Simpan grafik distribusi

### Langkah 2: Pastikan Labeling Benar

**PENTING! Periksa folder dataset Anda:**

```
dataset/
├── cabai_setan/          ← HANYA gambar cabai setan
├── cabai_celeng/         ← HANYA gambar cabai celeng
├── cabai_putih/          ← HANYA gambar cabai putih
└── cabai_merah_keriting/ ← HANYA gambar cabai merah keriting
```

⚠️ **JANGAN ADA GAMBAR YANG SALAH FOLDER!**

### Langkah 3: Training Model dengan Improvements

Model sudah di-upgrade dengan fitur berikut:

**✅ Improvements:**
- **Fine-tuning**: Unfreeze 24 layer terakhir (sebelumnya semua freeze)
- **Augmentasi agresif**: 
  - Rotasi 40° (sebelumnya 30°)
  - Zoom 30% (sebelumnya 20%)
  - Brightness variation
  - Vertical flip
- **Arsitektur enhanced**:
  - Layer 256 → 128 (lebih dalam)
  - Dropout 0.6 dan 0.4 (lebih robust)
- **Learning rate scheduler**: ReduceLROnPlateau
- **Early stopping**: patience=8 (lebih stabil)
- **Validation split**: 15% (lebih banyak data training)

**Jalankan training:**

```bash
python train_model.py
```

**Proses training akan:**
1. Load semua gambar dari dataset
2. Augmentasi data (memperbanyak variasi)
3. Training MobileNetV2 dengan fine-tuning
4. Monitor accuracy dan loss
5. Simpan model terbaik otomatis
6. Visualisasi training history

### Langkah 4: Monitor Training

Perhatikan output di terminal:

```
Epoch 1/30
Training accuracy: 0.45 → 0.65 → 0.78 → ... → 0.95+
Validation accuracy: 0.50 → 0.70 → 0.82 → ... → 0.85+
```

**Target:**
- Training accuracy harus naik hingga >95%
- Validation accuracy stabil di >85%
- Jika val_acc tidak naik 8 epoch → training berhenti otomatis

### Langkah 5: Test Model Baru

Setelah training selesai:

```bash
streamlit run app.py
```

Upload gambar cabai yang sama untuk test apakah sudah akurat!

##  Target Akurasi per Kelas

| Jenis Cabai | Target Akurasi |
|-------------|---------------|
| Cabai Setan | >90% |
| Cabai Celeng | >88% |
| Cabai Putih | >90% |
| Cabai Merah Keriting | >88% |

## 🔍 Jika Masih Salah Klasifikasi

### Opsi A: Tambah Dataset

```
Minimal: 300 gambar per kelas
Ideal: 500+ gambar per kelas
```

Fokus pada:
- Berbagai sudut (atas, samping, bawah)
- Berbagai pencahayaan (terang, redup, natural)
- Berbagai background (gelap, terang, pasar)
- Close-up dan medium shot
- Cabai segar dan agak layu

### Opsi B: Improve Dataset Quality

1. **Hapus gambar ambigu**
   - Gambar yang buram/tidak jelas
   - Gambar yang bukan cabai rawit
   - Gambar duplicate

2. **Cek labeling ulang**
   - Pastikan semua gambar di folder yang benar
   - Jangan ada campuran antar kelas

3. **Balancing dataset**
   - Pastikan jumlah gambar per kelas seimbang
   - Jika satu kelas terlalu sedikit, tambahkan gambar

### Opsi C: Train Lebih Lama

Edit `train_model.py`:

```python
EPOCHS = 50  # Ubah dari 30 ke 50
```

Dan ubah patience:

```python
early_stopping = EarlyStopping(
    monitor='val_accuracy',
    patience=10,  # Ubah dari 8 ke 10
    restore_best_weights=True,
    verbose=1
)
```

### Opsi D: Gunakan Model Lebih Besar

Jika masih belum akurat, ganti MobileNetV2 dengan model yang lebih besar:

Edit `train_model.py`:

```python
# Ganti MobileNetV2 dengan ResNet50
from tensorflow.keras.applications import ResNet50

base_model = ResNet50(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
```

Atau EfficientNet:

```python
from tensorflow.keras.applications import EfficientNetB0

base_model = EfficientNetB0(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
```

##  Tips Khusus per Jenis Cabai

### Cabai Setan
- Biasanya **kecil**, **merah cerah**, **bentuk kerucut**
- Tambahkan gambar dengan:
  - Background gelap dan terang
  - Variasi warna dari hijau muda ke merah tua
  - Sudut yang berbeda-beda

### Cabai Celeng
- **Lebih besar** dari cabai setan
- **Permukaan lebih halus**
- Tambahkan gambar:
  - Close-up untuk detail tekstur
  - Variasi ukuran (kecil, sedang, besar)

### Cabai Putih
- Warna **putih kekuningan**
- ️ Hati-hati: jangan tertukar dengan cabai hijau muda
- Tambahkan gambar:
  - Dengan lighting berbeda
  - Close-up untuk warna yang jelas

### Cabai Merah Keriting
- **Bentuk keriting khas**
- **Panjang dan bergelombang**
- Pastikan:
  - Bentuk keriting terlihat jelas
  - Tidak tertukar dengan cabai merah biasa

## 📈 Checklist Meningkatkan Akurasi

- [ ] Dataset minimal 300 gambar per kelas
- [ ] Semua gambar di folder yang benar
- [ ] Tidak ada gambar corrupt/buram
- [ ] Dataset seimbang antar kelas
- [ ] Training model dengan `python train_model.py`
- [ ] Validation accuracy >85%
- [ ] Test dengan gambar baru
- [ ] Catat kesalahan klasifikasi
- [ ] Perbaiki dataset berdasarkan error
- [ ] Training ulang jika perlu

##  Lihat Tips Lengkap

```bash
python AKURASI_TIPS.py
```

Script ini akan menampilkan panduan lengkap meningkatkan akurasi!

---

**© 2026 - Project Cabai Difa**

*Dibangun dengan ❤️ untuk akurasi maksimal*
