import streamlit as st
import numpy as np
from PIL import Image
import os
from database import simpan_prediksi
from ui_components import render_navbar

# Konfigurasi halaman
st.set_page_config(
    page_title="Klasifikasi Cabai",
    page_icon="🌶️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render Custom Premium Top Navigation Bar
render_navbar("klasifikasi")

# Google Fonts & Custom CSS (Webflow & React Bits Spotlight Glow Aesthetic)
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
/* Global Styles */
.main {
background-color: #FAFAFA !important;
font-family: 'Plus Jakarta Sans', sans-serif !important;
}

h1, h2, h3, h4 {
font-family: 'Outfit', sans-serif !important;
color: #111111;
}

/* Background Glowing Blobs (Webflow Ambient) */
.ambient-container {
position: fixed;
top: 0;
left: 0;
right: 0;
bottom: 0;
z-index: 0;
pointer-events: none;
}

.blob-1 {
position: absolute;
width: 500px;
height: 500px;
background: radial-gradient(circle, rgba(255, 77, 77, 0.06) 0%, rgba(255, 255, 255, 0) 70%);
top: -100px;
left: -100px;
border-radius: 50%;
filter: blur(80px);
}

.blob-2 {
position: absolute;
width: 500px;
height: 500px;
background: radial-gradient(circle, rgba(245, 158, 11, 0.06) 0%, rgba(255, 255, 255, 0) 70%);
bottom: -100px;
right: -100px;
border-radius: 50%;
filter: blur(80px);
}

/* Page Header */
.page-header {
text-align: center;
padding: 50px 20px 30px 20px;
position: relative;
z-index: 1;
}

.page-title {
font-size: 48px;
font-weight: 900;
letter-spacing: -1.5px;
margin-bottom: 12px;
}

.page-title span {
background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}

.page-subtitle {
font-size: 16px;
color: #6B7280;
max-width: 600px;
margin: 0 auto;
line-height: 1.6;
}

/* Premium Webflow Cards */
.premium-card {
background: rgba(255, 255, 255, 0.8);
backdrop-filter: blur(12px);
border: 1px solid rgba(229, 231, 235, 0.8);
border-radius: 20px;
padding: 30px;
box-shadow: 0 8px 30px rgba(0,0,0,0.02);
margin-bottom: 24px;
position: relative;
z-index: 1;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.premium-card:hover {
transform: translateY(-2px);
box-shadow: 0 15px 35px rgba(0,0,0,0.04);
border-color: rgba(255, 77, 77, 0.2);
}

.premium-card h3 {
font-size: 20px;
font-weight: 800;
margin-bottom: 20px;
display: flex;
align-items: center;
gap: 8px;
}

/* Custom list styling */
.info-list {
list-style: none;
padding: 0;
margin: 0;
}

.info-list li {
position: relative;
padding-left: 28px;
margin-bottom: 16px;
font-size: 14px;
color: #4B5563;
line-height: 1.6;
}

.info-list li::before {
content: '✓';
position: absolute;
left: 0;
top: 2px;
width: 18px;
height: 18px;
background: rgba(16, 185, 129, 0.1);
color: #10B981;
border-radius: 50%;
display: flex;
align-items: center;
justify-content: center;
font-size: 10px;
font-weight: bold;
}

.info-list.format li::before {
content: '✦';
background: rgba(245, 158, 11, 0.1);
color: #F59E0B;
}

/* Streamlit Widget Custom Styling */
.stTabs [data-baseweb="tab-list"] {
gap: 8px;
border-bottom: 2px solid rgba(229, 231, 235, 0.5);
padding-bottom: 8px;
}

.stTabs [data-baseweb="tab"] {
background-color: transparent !important;
border: 1px solid rgba(229, 231, 235, 0.8) !important;
border-radius: 8px !important;
padding: 8px 16px !important;
font-weight: 700 !important;
color: #4B5563 !important;
transition: all 0.2s ease !important;
}

.stTabs [aria-selected="true"] {
background: #000000 !important;
color: #FFFFFF !important;
border-color: #000000 !important;
}

/* Premium Gradient Button */
.stButton > button {
background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%) !important;
color: #FFFFFF !important;
border: none !important;
border-radius: 12px !important;
padding: 14px 28px !important;
font-size: 16px !important;
font-weight: 700 !important;
box-shadow: 0 8px 20px rgba(255, 77, 77, 0.2) !important;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
width: 100% !important;
}

.stButton > button:hover {
transform: translateY(-2px) !important;
box-shadow: 0 12px 30px rgba(255, 77, 77, 0.3) !important;
}

/* Premium Result Cards */
.result-box-premium {
background: rgba(255, 255, 255, 0.9);
border: 1.5px solid rgba(255, 77, 77, 0.2);
border-radius: 20px;
padding: 30px;
box-shadow: 0 15px 40px rgba(255, 77, 77, 0.08);
margin: 20px 0;
text-align: center;
position: relative;
overflow: hidden;
}

.result-box-premium::before {
content: '';
position: absolute;
top: 0;
left: 0;
right: 0;
height: 6px;
background: linear-gradient(90deg, #FF4D4D 0%, #F59E0B 100%);
}

.result-title {
font-size: 26px;
font-weight: 900;
color: #111111;
margin-bottom: 10px;
display: flex;
align-items: center;
justify-content: center;
gap: 10px;
}

.confidence-badge {
background: rgba(16, 185, 129, 0.1);
color: #10B981;
padding: 6px 16px;
border-radius: 100px;
font-size: 14px;
font-weight: 700;
display: inline-block;
margin-top: 5px;
border: 1px solid rgba(16, 185, 129, 0.2);
}

.explanation-box {
background: rgba(245, 158, 11, 0.05);
border: 1px dashed rgba(245, 158, 11, 0.3);
padding: 20px;
border-radius: 16px;
color: #B45309;
margin: 20px 0;
font-size: 14.5px;
line-height: 1.6;
text-align: left;
display: flex;
gap: 12px;
align-items: flex-start;
}

.explanation-icon {
font-size: 22px;
line-height: 1;
}

/* Responsive Global Adjustments */
@media (max-width: 768px) {
    .page-title { font-size: 36px; line-height: 1.2; }
    .page-subtitle { font-size: 15px; }
    .page-header { padding-top: 60px; padding-bottom: 20px; }
    .result-title { font-size: 22px; flex-direction: column; text-align: center; }
    .explanation-box { flex-direction: column; align-items: center; text-align: center; }
}
</style>
""", unsafe_allow_html=True)

# 1. FIXED AMBIENT BACKGROUND BLOBS
st.markdown("""
<div class="ambient-container">
<div class="blob-1"></div>
<div class="blob-2"></div>
</div>
""", unsafe_allow_html=True)

# 2. PAGE HEADER
st.markdown("""
<div class="page-header gsap-fade-in">
<div class="hero-badge" style="margin-bottom: 16px;">📸 Computer Vision Platform</div>
<h1 class="page-title">Klasifikasi <span>Cabai Rawit</span></h1>
<p class="page-subtitle">Unggah foto cabai Anda atau ambil tangkapan gambar langsung menggunakan kamera untuk diidentifikasi secara real-time oleh model Google Gemini AI.</p>
</div>
""", unsafe_allow_html=True)

# Mapping kelas cabai
KELAS_CABAI = {
    0: 'Cabai Setan/Rawit',
    1: 'Cabai Gendot',
    2: 'Cabai Putih',
    3: 'Cabai Merah Keriting'
}

def prediksi_gambar_gemini(image, api_key):
    """Melakukan prediksi menggunakan Google Gemini (dengan fallback model terbaru)"""
    try:
        import google.generativeai as genai
        import json
        import re
        
        # Konfigurasi API
        genai.configure(api_key=api_key)
        
        # Prompt instruksi klasifikasi yang sangat presisi sesuai jenis cabai Indonesia asli
        prompt = """
        Anda adalah pakar agronomi dan klasifikasi tanaman khas Indonesia. Tugas Anda adalah:
        1. Pertama, periksa apakah gambar yang diunggah benar-benar menampilkan objek buah cabai. Jika gambar tersebut JELAS BUKAN cabai (misalnya menampilkan wajah/tubuh manusia, ruangan, teks/banner, hewan, barang elektronik, pemandangan, atau benda non-cabai lainnya), Anda WAJIB mengklasifikasikannya ke dalam kelas khusus: 'Bukan Cabai'.
        2. Jika gambar tersebut menampilkan buah cabai, klasifikasikan ke dalam salah satu dari 4 kategori standar pasar Indonesia berikut:
        
        - 'Cabai Gendot' (atau Cabe Gendot / Cabe Habanero Lokal):
           - Karakteristik: Cabai yang berbentuk **sangat gemuk, bulat bengkak/gendut, menyerupai lampion kecil, lonceng, atau berbentuk oblate/lenticular (sangat mirip habanero atau paprika mini)**.
           - Warna: Dominan berwarna **hijau muda atau hijau tua mengkilap/licin (paling khas dan populer di Bandung/Jawa Barat)**, namun bisa juga berwarna kuning, oranye, atau merah terang saat matang sempurna.
           - Kulit: Tebal, sangat mulus, licin, dan mengkilap (glossy).
           - PENTING: Foto tumpukan cabai berwarna hijau bulat gemuk/bengkak seperti lampion kecil adalah 'Cabai Gendot' (100% akurat).
           
        - 'Cabai Setan/Rawit' (atau Cabai Rawit Setan / Cabai Domba): 
           - Karakteristik: Cabai rawit merah/hijau kecil yang sangat pedas.
           - Bentuk: Bulat memanjang (tapered/cylindrical), kecil hingga sedang, **tidak berbentuk lampion bulat bengkak**. Kulitnya bisa mulus atau sedikit berkerut.
           - Warna: Berwarna merah cerah, oranye, atau campuran hijau-kekuningan dan merah (seperti cabai rawit merah pasar).
           
        - 'Cabai Putih' (atau Cabai Rawit Putih / Cabe Lalap):
           - Karakteristik: Cabai rawit kecil berbentuk bulat memanjang yang berwarna putih susu, kuning pucat, atau hijau sangat muda ketika muda, dan berubah menjadi oranye/merah ketika matang. Kulitnya mulus dan ukurannya kecil.
           
        - 'Cabai Merah Keriting':
           - Karakteristik: Cabai merah yang berukuran panjang, kurus, meliuk-liuk, dan permukaannya sangat keriting, bergelombang, atau berkerut khas. Biasanya digunakan untuk bumbu balado atau sambal keriting.
         
        Format respon harus berupa JSON valid dengan struktur berikut (tanpa markdown tambahan, berikan raw JSON saja):
        {
          "class": "Cabai Setan/Rawit" | "Cabai Gendot" | "Cabai Putih" | "Cabai Merah Keriting" | "Bukan Cabai",
          "confidence": float (angka persen probabilitas antara 0.0 sampai 100.0),
          "explanation": "Penjelasan singkat dalam Bahasa Indonesia mengenai ciri-ciri visual pada gambar yang mendasari klasifikasi ini."
        }
        """
        
        # Daftar model yang dicoba (dari yang terbaru hingga yang lama)
        model_names = ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-flash-latest', 'gemini-pro-latest', 'gemini-2.5-flash-lite']
        response = None
        last_exception = None
        
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content([prompt, image])
                break
            except Exception as e:
                last_exception = e
                continue
                
        if response is None:
            raise Exception(f"Semua model Gemini gagal diakses. Error terakhir: {str(last_exception)}")
            
        # Ekstrak JSON
        text = response.text.strip()
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group(0))
        else:
            data = json.loads(text)
            
        predicted_class = data.get("class", "Cabai Setan/Rawit")
        confidence = float(data.get("confidence", 95.0))
        explanation = data.get("explanation", "")
        
        # Cek jika dideteksi bukan cabai
        if predicted_class == "Bukan Cabai":
            raise ValueError("Gambar yang Anda unggah dideteksi bukan merupakan buah cabai. Silakan unggah foto cabai yang valid!")
            
        class_map = {
            'Cabai Setan/Rawit': 0,
            'Cabai Setan': 0,
            'Cabai Gendot': 1,
            'Cabai Putih': 2,
            'Cabai Merah Keriting': 3
        }
        class_idx = class_map.get(predicted_class, 0)
        
        # Generate pseudo-probabilities untuk visualisasi chart
        probabilities = [0.0] * 4
        probabilities[class_idx] = confidence / 100.0
        remaining = (100.0 - confidence) / 3.0 / 100.0
        for i in range(4):
            if i != class_idx:
                probabilities[i] = remaining
                
        return class_idx, confidence, probabilities, explanation
    except Exception as e:
        raise e

def get_gemini_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r") as f:
                for line in f:
                    if line.strip().startswith("GEMINI_API_KEY="):
                        val = line.split("=", 1)[1].strip()
                        val = val.strip('"').strip("'")
                        if val:
                            return val
        except Exception:
            pass
    return "AIzaSyC1ReB17Wl3gFOVsikK--BUqGdktaUVSkQ"

api_key = get_gemini_api_key()

# Layout Kolom Klasifikasi
col1, col2 = st.columns([1.1, 0.9])

with col1:
    st.markdown("""
<div class="premium-card gsap-card" id="input-card">
<h3>📸 Input Gambar Cabai</h3>
</div>
""", unsafe_allow_html=True)
    
    # Tabs input file/kamera diletakkan langsung di Streamlit untuk fungsionalitas murni
    tab_upload, tab_kamera = st.tabs(["📤 Upload File", "📸 Kamera Langsung"])
    
    source_file = None
    file_name = ""
    
    with tab_upload:
        uploaded_file = st.file_uploader(
            "Pilih gambar cabai (JPG/PNG)",
            type=['jpg', 'jpeg', 'png'],
            help="Format yang didukung: JPG, JPEG, PNG",
            key="file_uploader"
        )
        if uploaded_file is not None:
            source_file = uploaded_file
            file_name = uploaded_file.name
            
    with tab_kamera:
        camera_file = st.camera_input("Ambil foto cabai langsung dari kamera Anda")
        if camera_file is not None:
            source_file = camera_file
            file_name = "tangkapan_kamera.png"
            
    if source_file is not None:
        if uploaded_file is not None:
            st.markdown("""
<div class="premium-card gsap-card" style="margin-top: 24px;">
<h3>👁️ Preview Gambar</h3>
</div>
""", unsafe_allow_html=True)
            image = Image.open(source_file)
            st.image(image, caption=file_name, use_column_width=True)
        else:
            image = Image.open(source_file)
            
        st.markdown("")
        
        # Tombol prediksi
        if st.button("🔍 Jalankan Deteksi AI"):
            with st.spinner("Menganalisis karakteristik visual dengan Gemini AI..."):
                try:
                    class_idx, confidence, probabilities, explanation = prediksi_gambar_gemini(image, api_key)
                    hasil_prediksi = KELAS_CABAI[class_idx]
                    
                    # Tampilkan hasil dengan Box Premium yang Sangat Glamor
                    st.markdown(f"""
<div class="result-box-premium gsap-result">
<div class="result-title">🌶️ {hasil_prediksi}</div>
<div class="confidence-badge">Confidence Score: {confidence:.2f}%</div>
</div>
""", unsafe_allow_html=True)
                    
                    if explanation:
                        st.markdown(f"""
<div class="explanation-box gsap-result">
<div class="explanation-icon">💡</div>
<div>
<strong>Analisis Karakteristik Visual:</strong><br>
{explanation}
</div>
</div>
""", unsafe_allow_html=True)
                        
                    # Tampilkan chart probabilitas
                    st.markdown("""
<div class="premium-card gsap-result" style="margin-top: 20px;">
<h3>📊 Detail Probabilitas Distribusi</h3>
</div>
""", unsafe_allow_html=True)
                    
                    prob_data = {
                        'Jenis Cabai': [KELAS_CABAI[i] for i in range(4)],
                        'Probabilitas (%)': [probabilities[i] * 100 for i in range(4)]
                    }
                    
                    import pandas as pd
                    df_prob = pd.DataFrame(prob_data)
                    
                    st.bar_chart(
                        df_prob.set_index('Jenis Cabai')
                    )
                    
                    # Simpan ke session state untuk disimpan ke database
                    st.session_state['prediksi_hasil'] = {
                        'nama_file': file_name,
                        'hasil_prediksi': hasil_prediksi,
                        'confidence_score': confidence
                    }
                    
                    st.markdown("""
<div style="background-color: #E6F4EA; border-left: 5px solid #10B981; padding: 15px; border-radius: 12px; color: #065F46; margin: 15px 0; font-size: 15px; font-weight: 600;" class="gsap-result">
✅ Deteksi berhasil diselesaikan!
</div>
""", unsafe_allow_html=True)
                except Exception as e:
                    err_msg = str(e)
                    if "bukan merupakan buah cabai" in err_msg:
                        st.markdown(f"""
<div style="background-color: #FFFBEB; border-left: 5px solid #F59E0B; padding: 15px; border-radius: 12px; color: #92400E; margin: 15px 0; font-size: 15px; line-height: 1.6;" class="gsap-result">
<strong>⚠️ Deteksi Objek Gagal (Shield Guard):</strong><br>
{err_msg}
</div>
""", unsafe_allow_html=True)
                    elif "API key is invalid" in err_msg or "API_KEY_INVALID" in err_msg or "403" in err_msg or "400" in err_msg or "not found" in err_msg:
                        st.markdown("""
<div style="background-color: #FEF2F2; border-left: 5px solid #EF4444; padding: 25px; border-radius: 16px; color: #991B1B; margin: 15px 0; font-size: 14.5px; line-height: 1.6;" class="gsap-result">
<strong>⚠️ Kredensial API Key Tidak Valid</strong><br><br>
Sistem keamanan otomatis Google telah menonaktifkan API Key Anda karena mendeteksinya bocor ke publik.<br><br>
<strong>Langkah Solusi Cepat:</strong>
<ol style="margin-top: 10px; padding-left: 20px;">
<li>Dapatkan API Key baru secara gratis di <a href="https://aistudio.google.com/" target="_blank" style="color: #991B1B; text-decoration: underline; font-weight: 700;">Google AI Studio</a>.</li>
<li>Buka berkas <code>.env</code> di dalam direktori utama proyek (<code>c:\\Projects\\cabai-difa\\.env</code>).</li>
<li>Ganti baris API Key Anda dengan kunci baru tersebut:
<pre style="background-color: #FEE2E2; padding: 10px; border-radius: 6px; font-family: monospace; margin-top: 6px; border: 1px solid #FCA5A5;">GEMINI_API_KEY=KUNCI_API_BARU_ANDA</pre>
</li>
<li>Simpan file <code>.env</code> dan klik tombol deteksi kembali.</li>
</ol>
</div>
""", unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
<div style="background-color: #FEF2F2; border-left: 5px solid #EF4444; padding: 15px; border-radius: 12px; color: #991B1B; margin: 15px 0; font-size: 15px;" class="gsap-result">
<strong>❌ Terjadi gangguan saat memproses gambar:</strong> {err_msg}
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="premium-card gsap-card" id="info-card">
<h3>📋 Petunjuk Penggunaan</h3>
<ul class="info-list">
<li>Pilih tab input yang Anda inginkan (unggah berkas atau menggunakan kamera aktif).</li>
<li>Pastikan foto buah cabai yang akan dideteksi berada dalam pencahayaan yang cukup baik dan fokus.</li>
<li>Klik tombol <strong>"Jalankan Deteksi AI"</strong> untuk mengirim piksel gambar ke engine.</li>
<li>Hasil klasifikasi visual beserta penjelasan karakteristik visual akan muncul di sebelah kiri.</li>
<li>Klik tombol <strong>"Simpan ke Riwayat"</strong> untuk mengarsipkan hasil prediksi ke SQLite database lokal.</li>
</ul>
</div>

<div class="premium-card gsap-card" id="format-card">
<h3>📐 Spesifikasi Input Gambar</h3>
<ul class="info-list format">
<li><strong>Format Ekstensi:</strong> JPG, JPEG, atau PNG didukung penuh oleh sistem.</li>
<li><strong>Batas Ukuran:</strong> Maksimal 10 MB per berkas gambar untuk stabilitas jaringan.</li>
<li><strong>Rekomendasi Resolusi:</strong> Minimal 224x224 piksel untuk kejelasan tangkapan objek.</li>
<li><strong>Saran Sudut Foto:</strong> Ambil foto dari arah depan atau samping buah cabai secara dekat.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Tombol simpan ke riwayat
if 'prediksi_hasil' in st.session_state:
    st.markdown("---")
    col_left, col_center, col_right = st.columns([1, 1, 1])
    
    with col_center:
        if st.button("💾 Simpan ke Riwayat"):
            hasil = st.session_state['prediksi_hasil']
            simpan_prediksi(
                hasil['nama_file'],
                hasil['hasil_prediksi'],
                hasil['confidence_score']
            )
            st.success(f"✅ Hasil prediksi berhasil disimpan ke database!")
            del st.session_state['prediksi_hasil']

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888888; padding: 20px 0; font-size: 13.5px;" class="gsap-fade-in">
<p><strong>Model AI:</strong> Google Gemini AI | <strong>Infrastruktur:</strong> Google Cloud Platform Platform</p>
</div>
""", unsafe_allow_html=True)

# INJEKSI GSAP ANIMATIONS
st.markdown("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

<script>
window.addEventListener('load', function() {
    try {
        // Animasi fade-in untuk header halaman
        gsap.from(".gsap-fade-in", {
            duration: 1,
            opacity: 0,
            y: -20,
            ease: "power2.out"
        });

        // Animasi stagger-up untuk kartu input dan informasi
        gsap.from(".gsap-card", {
            duration: 1,
            opacity: 0,
            y: 30,
            stagger: 0.15,
            ease: "power3.out",
            delay: 0.2
        });
        
        // Animasi bounce-in untuk hasil deteksi jika ada di DOM
        gsap.from(".gsap-result", {
            duration: 0.8,
            scale: 0.95,
            opacity: 0,
            stagger: 0.15,
            ease: "back.out(1.5)"
        });
    } catch(e) {
        console.log("GSAP Error:", e);
    }
});
</script>
""", unsafe_allow_html=True)
