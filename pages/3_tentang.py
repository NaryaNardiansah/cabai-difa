import streamlit as st
from ui_components import render_navbar

# Konfigurasi halaman
st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render Custom Premium Top Navigation Bar
render_navbar("tentang")

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
width: 600px;
height: 600px;
background: radial-gradient(circle, rgba(255, 77, 77, 0.05) 0%, rgba(255, 255, 255, 0) 70%);
top: -150px;
left: -150px;
border-radius: 50%;
filter: blur(90px);
}

.blob-2 {
position: absolute;
width: 600px;
height: 600px;
background: radial-gradient(circle, rgba(16, 185, 129, 0.05) 0%, rgba(255, 255, 255, 0) 70%);
bottom: -150px;
right: -150px;
border-radius: 50%;
filter: blur(90px);
}

.blob-3 {
position: absolute;
width: 400px;
height: 400px;
background: radial-gradient(circle, rgba(245, 158, 11, 0.04) 0%, rgba(255, 255, 255, 0) 70%);
top: 40%;
left: 50%;
transform: translate(-50%, -50%);
border-radius: 50%;
filter: blur(80px);
}

/* Page Header */
.page-header {
text-align: center;
padding: 40px 20px 20px 20px;
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
background: rgba(255, 255, 255, 0.8) !important;
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

/* Info Box / Badge Styles */
.info-box {
background: linear-gradient(135deg, rgba(255, 77, 77, 0.02) 0%, rgba(245, 158, 11, 0.02) 100%);
border-left: 5px solid #FF4D4D;
padding: 20px;
border-radius: 16px;
margin-bottom: 24px;
box-shadow: 0 4px 15px rgba(0,0,0,0.01);
}

.info-box p {
margin: 6px 0;
font-size: 14.5px;
color: #4B5563;
}

.secure-badge {
background: rgba(16, 185, 129, 0.1);
border: 1px solid rgba(16, 185, 129, 0.2);
color: #059669;
padding: 6px 16px;
border-radius: 100px;
font-size: 12.5px;
font-weight: 700;
display: inline-block;
margin-bottom: 16px;
letter-spacing: 0.5px;
}

.tech-item {
background: rgba(255, 255, 255, 0.7);
border: 1px solid rgba(229, 231, 235, 0.8);
border-radius: 12px;
padding: 18px;
margin: 14px 0;
font-size: 14px;
line-height: 1.6;
color: #4B5563;
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
font-size: 14.5px;
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

.info-list.features li::before {
content: '✦';
background: rgba(255, 77, 77, 0.1);
color: #FF4D4D;
}

/* Soft Colored Glassmorphism Cards for Chili Catalog */
.chili-glass-card {
background: rgba(255, 255, 255, 0.6);
backdrop-filter: blur(8px);
border: 1px solid rgba(229, 231, 235, 0.6);
border-radius: 20px;
padding: 30px;
text-align: center;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
box-shadow: 0 8px 30px rgba(0,0,0,0.01);
min-height: 270px;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
}

.chili-glass-card:hover {
transform: translateY(-5px);
box-shadow: 0 15px 35px rgba(0,0,0,0.05);
}

.chili-glass-card.setan {
background: rgba(255, 77, 77, 0.03);
border-color: rgba(255, 77, 77, 0.15);
}
.chili-glass-card.setan:hover {
border-color: rgba(255, 77, 77, 0.4);
box-shadow: 0 15px 35px rgba(255, 77, 77, 0.05);
}

.chili-glass-card.gendot {
background: rgba(16, 185, 129, 0.03);
border-color: rgba(16, 185, 129, 0.15);
}
.chili-glass-card.gendot:hover {
border-color: rgba(16, 185, 129, 0.4);
box-shadow: 0 15px 35px rgba(16, 185, 129, 0.05);
}

.chili-glass-card.putih {
background: rgba(245, 158, 11, 0.03);
border-color: rgba(245, 158, 11, 0.15);
}
.chili-glass-card.putih:hover {
border-color: rgba(245, 158, 11, 0.4);
box-shadow: 0 15px 35px rgba(245, 158, 11, 0.05);
}

.chili-glass-card.keriting {
background: rgba(220, 38, 38, 0.03);
border-color: rgba(220, 38, 38, 0.15);
}
.chili-glass-card.keriting:hover {
border-color: rgba(220, 38, 38, 0.4);
box-shadow: 0 15px 35px rgba(220, 38, 38, 0.05);
}

.chili-glass-card h3 {
font-size: 18px;
font-weight: 800;
margin: 15px 0 10px 0;
color: #111111;
}

.chili-glass-card p {
font-size: 13.5px;
color: #6B7280;
line-height: 1.6;
margin: 0;
}

.chili-emoji {
font-size: 44px;
line-height: 1;
transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
display: inline-block;
}

.chili-glass-card:hover .chili-emoji {
transform: scale(1.15) rotate(5deg);
}

/* Responsive Global Adjustments */
@media (max-width: 768px) {
    .page-title { font-size: 36px; line-height: 1.2; }
    .page-subtitle { font-size: 15px; }
    .page-header { padding-top: 60px; padding-bottom: 20px; }
    .chili-glass-card { min-height: auto; padding: 20px; }
}
</style>
""", unsafe_allow_html=True)

# 1. FIXED AMBIENT BACKGROUND BLOBS
st.markdown("""
<div class="ambient-container">
<div class="blob-1"></div>
<div class="blob-2"></div>
<div class="blob-3"></div>
</div>
""", unsafe_allow_html=True)

# 2. PAGE HEADER
st.markdown("""
<div class="page-header gsap-fade-in">
<div class="hero-badge" style="margin-bottom: 16px;">ℹ️ App Information</div>
<h1 class="page-title">Tentang <span>Aplikasi</span></h1>
<p class="page-subtitle">Pelajari lebih dalam mengenai teknologi cloud AI, spesifikasi, dan arsitektur pengamanan yang melandasi sistem klasifikasi cabai rawit ini.</p>
</div>
""", unsafe_allow_html=True)

# Layout Kolom Deskripsi Utama
col1, col2 = st.columns([1.1, 0.9])

with col1:
    st.markdown("""
<div class="info-box gsap-card">
<p><strong>Versi Aplikasi:</strong> 1.1.0 (Gemini AI Premium Edition)</p>
<p><strong>Kategori Sistem:</strong> Smart Agriculture & Computer Vision Platform</p>
<p><strong>Pengembang Resmi:</strong> Project Cabai Difa</p>
</div>

<div class="premium-card gsap-card">
<h3>📖 Deskripsi Aplikasi</h3>
<p style="color: #4B5563; font-size: 14.5px; line-height: 1.7; margin-bottom: 16px;">
<strong>Sistem Klasifikasi Cabai Rawit Indonesia</strong> adalah platform kecerdasan buatan mutakhir yang dirancang khusus untuk mendeteksi, mengenali, dan mengklasifikasikan jenis cabai rawit Indonesia secara instan.
</p>
<p style="color: #4B5563; font-size: 14.5px; line-height: 1.7; margin: 0;">
Dengan mengintegrasikan teknologi cloud <strong>Google Gemini AI Multimodal</strong>, sistem ini mampu mengenali bentuk, warna, dan detail visual cabai dengan tingkat akurasi yang luar biasa tinggi, serta memberikan analisis karakteristik khusus cabai secara cerdas.
</p>
</div>

<div class="premium-card gsap-card">
<h3>🎯 Misi & Tujuan Pengembangan</h3>
<ul class="info-list">
<li><strong>Digitalisasi Sektor Pertanian:</strong> Membantu petani lokal dan pelaku usaha pangan mengidentifikasi jenis cabai secara instan tanpa kerumitan manual.</li>
<li><strong>Edukasi Karakteristik Visual:</strong> Memberikan wawasan mendalam mengenai struktur khusus dan keunikan masing-masing varietas cabai rawit.</li>
<li><strong>Akurasi Tinggi & Instan:</strong> Menghemat waktu analisis dengan menyajikan hasil letupan data real-time berbasis tangkapan kamera langsung.</li>
</ul>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="premium-card gsap-card" style="height: 100%;">
<h3>🛠️ Rangkaian Fitur Utama</h3>
<ul class="info-list features">
<li><strong>📸 Kamera Instan Aktif:</strong> Ambil foto langsung melalui kamera gadget Anda untuk proses identifikasi super cepat.</li>
<li><strong>📤 Pengunggah Fleksibel:</strong> Mendukung pengunggahan berkas gambar dengan format JPG, JPEG, dan PNG.</li>
<li><strong>🧠 Google Gemini Engine:</strong> Klasifikasi tingkat tinggi yang ditenagai oleh kecerdasan buatan cloud generasi teranyar.</li>
<li><strong>🛡️ Sistem Penyaring Objek:</strong> Proteksi otomatis untuk mendeteksi dan menolak gambar non-cabai (wajah, barang, pemandangan).</li>
<li><strong>💾 Sinkronisasi SQLite Lokal:</strong> Pengarsipan otomatis yang aman untuk menyimpan data riwayat prediksi ke dalam perangkat Anda.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Metode dan Teknologi
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;" class="gsap-fade-in">
<h2 style="font-size: 28px; font-weight: 800; margin-bottom: 10px;">🔧 Arsitektur Sistem & Privasi Kredensial</h2>
<p style="color: #6B7280; font-size: 15px;">Bagaimana kecerdasan buatan bekerja di balik layar dan melindungi API Key Anda.</p>
</div>
""", unsafe_allow_html=True)

col_metode1, col_metode2 = st.columns(2)

with col_metode1:
    st.markdown("""
<div class="premium-card gsap-card" style="min-height: 440px;">
<h3>🧠 Metode Analisis Gemini Multimodal</h3>
<p style="color: #4B5563; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">
Aplikasi ini memanfaatkan model kecerdasan buatan berbasis cloud <strong>Gemini AI</strong>. Berbeda dengan model klasifikasi tradisional (CNN biasa), Gemini AI memproses kombinasi data visual (gambar) dan teks instruksi (prompt kustom) secara bersamaan.
</p>
<strong style="color: #111111; font-size: 14.5px;">Alur Inferensi Data:</strong>
<ol style="padding-left: 20px; margin: 10px 0 0 0; color: #4B5563; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Kompresi & Transmisi:</strong> Gambar dikompresi dengan aman untuk efisiensi jaringan dan dikirim ke API Google AI Studio.</li>
<li style="margin-bottom: 8px;"><strong>Deteksi Fitur:</strong> AI membedakan tekstur luar, warna kelopak, kelenturan tangkai, dan kebundelan buah cabai.</li>
<li style="margin-bottom: 8px;"><strong>Penyaringan Objek (Shield):</strong> Secara pintar menyaring dan menolak objek jika terdeteksi bukan merupakan buah cabai.</li>
<li style="margin-bottom: 8px;"><strong>Enkode Output JSON:</strong> Mengembalikan hasil berupa data JSON terstruktur berisi nama kelas, persen akurasi, dan penjelasan karakteristik.</li>
</ol>
</div>
""", unsafe_allow_html=True)

with col_metode2:
    st.markdown("""
<div class="premium-card gsap-card" style="min-height: 440px;">
<div class="secure-badge">🔒 SECURED & PROTECTED</div>
<h3>Kebijakan Perlindungan Kredensial</h3>
<p style="color: #4B5563; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">
Sistem ini mematuhi standar pengembangan perangkat lunak modern untuk menjamin data rahasia Anda aman dan tidak bocor ke publik.
</p>

<div class="tech-item">
<strong>🔑 Kunci API Tersimpan Aman (Hidden API Key)</strong><br>
Seluruh token otentikasi Google Gemini API Key disimpan secara eksklusif pada file latar belakang <code>.env</code> di server backend lokal. Kode sistem tidak pernah menampilkan, membocorkan, atau menyelipkan kunci API ini ke dalam antarmuka halaman web.
</div>

<div class="tech-item">
<strong>💾 SQLite Database Sandbox</strong><br>
Data riwayat disimpan seutuhnya di dalam perangkat Anda sendiri menggunakan database sandbox SQLite 3. Tidak ada pihak luar yang dapat mengakses data riwayat prediksi ini.
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Varietas Cabai yang Didukung (Gaya Glassmorphism Berwarna Premium)
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;" class="gsap-fade-in">
<h2 style="font-size: 28px; font-weight: 800; margin-bottom: 10px;">🌶️ Klasifikasi Cabai yang Didukung</h2>
<p style="color: #6B7280; font-size: 15px;">Empat varietas cabai khas Indonesia yang dilatih untuk dikenali secara cerdas.</p>
</div>
""", unsafe_allow_html=True)

col_cabai1, col_cabai2, col_cabai3, col_cabai4 = st.columns(4)

with col_cabai1:
    st.markdown("""
<div class="chili-glass-card setan gsap-chili">
<div class="chili-emoji">😈</div>
<h3>Cabai Setan/Rawit</h3>
<p>Cabai merah/oranye kecil dengan tingkat pedas ekstrem, permukaan buah yang sedikit berkerut, dan berlekuk tajam.</p>
</div>
""", unsafe_allow_html=True)

with col_cabai2:
    st.markdown("""
<div class="chili-glass-card gendot gsap-chili">
<div class="chili-emoji">🫑</div>
<h3>Cabai Gendot</h3>
<p>Cabai bulat bengkak seperti lampion kecil, berkulit tebal mengkilap, dan umumnya berwarna hijau segar di pasar lokal.</p>
</div>
""", unsafe_allow_html=True)

with col_cabai3:
    st.markdown("""
<div class="chili-glass-card putih gsap-chili">
<div class="chili-emoji">🌶️</div>
<h3>Cabai Putih</h3>
<p>Cabai lalapan yang berwarna kuning pucat keputihan saat muda, bertubuh mulus ramping, dan berubah merah ketika matang.</p>
</div>
""", unsafe_allow_html=True)

with col_cabai4:
    st.markdown("""
<div class="chili-glass-card keriting gsap-chili">
<div class="chili-emoji">🌀</div>
<h3>Cabai Merah Keriting</h3>
<p>Cabai ramping memanjang dengan permukaan meliuk-liuk keriting berkerut tegas, sering digunakan untuk bumbu sambal.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888888; padding: 20px 0; font-size: 13.5px;" class="gsap-fade-in">
<p style="margin: 5px 0; font-weight: 700; color: #111111;">Sistem Klasifikasi Cabai Rawit Indonesia</p>
<p style="margin: 5px 0;">© 2026 - Project Cabai Difa. Hak Cipta Dilindungi.</p>
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

        // Animasi stagger-up untuk kartu deskripsi & fitur
        gsap.from(".gsap-card", {
            duration: 1,
            opacity: 0,
            y: 30,
            stagger: 0.15,
            ease: "power3.out",
            delay: 0.2
        });

        // Animasi stagger-scale untuk kartu cabai
        gsap.from(".gsap-chili", {
            duration: 0.8,
            scale: 0.9,
            opacity: 0,
            stagger: 0.1,
            ease: "back.out(1.5)",
            delay: 0.5
        });
    } catch(e) {
        console.log("GSAP Error:", e);
    }
});
</script>
""", unsafe_allow_html=True)
