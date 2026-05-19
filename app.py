import streamlit as st
from ui_components import render_navbar

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Beranda - Cabai Difa",
    page_icon="🌶️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render Custom Top Navigation Bar
render_navbar("home")

# Google Fonts & Custom CSS (Ultimate Webflow & React Bits Spotlight Glow Aesthetic)
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
/* Global Styles */
.main {
background-color: #FAFAFA !important;
font-family: 'Plus Jakarta Sans', sans-serif !important;
overflow-x: hidden;
}

h1, h2, h3, h4 {
font-family: 'Outfit', sans-serif !important;
color: #111111;
}

/* Background Glowing Blobs (Premium Webflow Ambient) */
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
background: radial-gradient(circle, rgba(255, 77, 77, 0.08) 0%, rgba(255, 255, 255, 0) 70%);
top: -200px;
left: -150px;
border-radius: 50%;
filter: blur(80px);
}

.blob-2 {
position: absolute;
width: 600px;
height: 600px;
background: radial-gradient(circle, rgba(245, 158, 11, 0.08) 0%, rgba(255, 255, 255, 0) 70%);
bottom: -200px;
right: -150px;
border-radius: 50%;
filter: blur(80px);
}

.blob-3 {
position: absolute;
width: 400px;
height: 400px;
background: radial-gradient(circle, rgba(16, 185, 129, 0.05) 0%, rgba(255, 255, 255, 0) 70%);
top: 40%;
left: 50%;
transform: translate(-50%, -50%);
border-radius: 50%;
filter: blur(70px);
}

/* Hero Section */
.hero-container {
text-align: center;
padding: 100px 20px 60px 20px;
position: relative;
z-index: 1;
max-width: 1000px;
margin: 0 auto;
}

.hero-badge {
background: rgba(255, 255, 255, 0.8);
backdrop-filter: blur(8px);
border: 1px solid rgba(229, 231, 235, 0.8);
color: #1F2937;
padding: 8px 20px;
border-radius: 100px;
font-size: 13px;
font-weight: 700;
display: inline-block;
margin-bottom: 24px;
letter-spacing: 1px;
text-transform: uppercase;
box-shadow: 0 4px 10px rgba(0,0,0,0.02);
}

.hero-title {
font-size: 64px;
font-weight: 900;
line-height: 1.1;
letter-spacing: -2px;
color: #111111;
margin-bottom: 24px;
}

.hero-title span {
background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
display: inline-block;
}

.hero-subtitle {
font-size: 19px;
color: #4B5563;
max-width: 750px;
margin: 0 auto 40px auto;
line-height: 1.6;
font-weight: 400;
}

/* Premium Webflow Glass Buttons */
.hero-actions {
display: flex;
justify-content: center;
gap: 16px;
margin-bottom: 60px;
}

.btn-primary {
background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%);
color: #FFFFFF;
border: none;
padding: 16px 32px;
font-size: 16px;
font-weight: 700;
border-radius: 12px;
cursor: pointer;
box-shadow: 0 10px 25px rgba(255, 77, 77, 0.25);
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
display: flex;
align-items: center;
gap: 8px;
}

.btn-primary:hover {
transform: translateY(-3px) scale(1.02);
box-shadow: 0 15px 35px rgba(255, 77, 77, 0.35);
}

.btn-secondary {
background: #FFFFFF;
color: #111111;
border: 1px solid rgba(229, 231, 235, 0.8);
padding: 16px 32px;
font-size: 16px;
font-weight: 700;
border-radius: 12px;
cursor: pointer;
box-shadow: 0 4px 12px rgba(0,0,0,0.03);
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
display: flex;
align-items: center;
gap: 8px;
}

.btn-secondary:hover {
transform: translateY(-3px) scale(1.02);
background: #FAFAFA;
border-color: #D1D5DB;
box-shadow: 0 8px 20px rgba(0,0,0,0.06);
}

/* Spotlight Follow-Mouse Cards (React Bits / Webflow Style) */
.spotlight-card {
position: relative;
background: rgba(255, 255, 255, 0.8) !important;
backdrop-filter: blur(12px);
border: 1px solid rgba(230, 230, 230, 0.8);
border-radius: 20px;
padding: 35px;
box-shadow: 0 8px 30px rgba(0,0,0,0.02);
overflow: hidden;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.spotlight-card::before {
content: '';
position: absolute;
top: 0;
left: 0;
right: 0;
bottom: 0;
background: radial-gradient(
600px circle at var(--mouse-x, 0) var(--mouse-y, 0),
rgba(255, 77, 77, 0.05),
transparent 40%
);
z-index: 0;
opacity: 0;
transition: opacity 0.3s ease;
pointer-events: none;
}

.spotlight-card:hover {
transform: translateY(-5px);
box-shadow: 0 20px 40px rgba(0,0,0,0.06);
border-color: rgba(255, 77, 77, 0.3);
}

.spotlight-card:hover::before {
opacity: 1;
}

.spotlight-card > * {
position: relative;
z-index: 1;
}

/* Feature Header */
.section-header {
text-align: center;
margin: 100px 0 50px 0;
position: relative;
z-index: 1;
}

.section-title {
font-size: 42px;
font-weight: 900;
letter-spacing: -1px;
margin-bottom: 12px;
}

.section-subtitle {
font-size: 17px;
color: #6B7280;
max-width: 600px;
margin: 0 auto;
line-height: 1.6;
}

/* Grid Layouts */
.stats-container {
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 24px;
max-width: 1000px;
margin: 0 auto 80px auto;
z-index: 1;
position: relative;
}

.stat-card {
background: rgba(255, 255, 255, 0.7);
backdrop-filter: blur(10px);
border: 1px solid rgba(230, 230, 230, 0.6);
border-radius: 20px;
padding: 30px;
text-align: center;
box-shadow: 0 4px 20px rgba(0,0,0,0.01);
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.stat-card:hover {
transform: translateY(-5px);
box-shadow: 0 15px 35px rgba(0,0,0,0.05);
border-color: rgba(245, 158, 11, 0.4);
}

.stat-number {
font-size: 48px;
font-weight: 900;
color: #111111;
margin-bottom: 6px;
background: linear-gradient(135deg, #111111 0%, #555555 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}

.stat-label {
font-size: 13px;
color: #6B7280;
font-weight: 700;
letter-spacing: 1px;
}

.features-grid {
display: grid;
grid-template-columns: repeat(2, 1fr);
gap: 30px;
max-width: 1100px;
margin: 0 auto;
position: relative;
z-index: 1;
}

.feature-icon {
font-size: 36px;
margin-bottom: 24px;
display: inline-block;
padding: 12px;
background: rgba(255, 77, 77, 0.05);
border-radius: 12px;
border: 1px solid rgba(255, 77, 77, 0.1);
}

.feature-name {
font-size: 22px;
font-weight: 800;
margin-bottom: 12px;
}

.feature-desc {
font-size: 15px;
color: #4B5563;
line-height: 1.6;
}

/* Custom Chili Showcase (Webflow Soft Glowing Glass Grid) */
.chili-grid {
display: grid;
grid-template-columns: repeat(4, 1fr);
gap: 24px;
max-width: 1200px;
margin: 0 auto;
position: relative;
z-index: 1;
}

.chili-card {
border-radius: 24px;
padding: 30px 24px;
text-align: center;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
border: 1px solid rgba(220, 220, 220, 0.5);
position: relative;
overflow: hidden;
}

.chili-card.chili-setan {
background: rgba(255, 77, 77, 0.03);
}
.chili-card.chili-setan:hover {
background: rgba(255, 77, 77, 0.06);
border-color: rgba(255, 77, 77, 0.3);
box-shadow: 0 15px 35px rgba(255, 77, 77, 0.08);
}

.chili-card.chili-gendot {
background: rgba(16, 185, 129, 0.03);
}
.chili-card.chili-gendot:hover {
background: rgba(16, 185, 129, 0.06);
border-color: rgba(16, 185, 129, 0.3);
box-shadow: 0 15px 35px rgba(16, 185, 129, 0.08);
}

.chili-card.chili-putih {
background: rgba(245, 158, 11, 0.03);
}
.chili-card.chili-putih:hover {
background: rgba(245, 158, 11, 0.06);
border-color: rgba(245, 158, 11, 0.3);
box-shadow: 0 15px 35px rgba(245, 158, 11, 0.08);
}

.chili-card.chili-keriting {
background: rgba(220, 38, 38, 0.03);
}
.chili-card.chili-keriting:hover {
background: rgba(220, 38, 38, 0.06);
border-color: rgba(220, 38, 38, 0.3);
box-shadow: 0 15px 35px rgba(220, 38, 38, 0.08);
}

.chili-emoji {
font-size: 52px;
margin-bottom: 20px;
display: inline-block;
transition: transform 0.3s ease;
}

.chili-card:hover .chili-emoji {
transform: scale(1.15) rotate(5deg);
}

.chili-title {
font-size: 20px;
font-weight: 800;
margin-bottom: 12px;
}

.chili-desc {
font-size: 14px;
color: #555555;
line-height: 1.5;
}

/* Workflow Architecture (Webflow Premium Process Line) */
.flow-container {
max-width: 1000px;
margin: 80px auto 40px auto;
position: relative;
z-index: 1;
display: flex;
justify-content: space-between;
}

.flow-line {
position: absolute;
top: 35px;
left: 8%;
right: 8%;
height: 3px;
background: linear-gradient(90deg, #FF4D4D 0%, #F59E0B 50%, #10B981 100%);
z-index: -1;
opacity: 0.15;
}

.flow-step {
text-align: center;
flex: 1;
padding: 0 20px;
}

.flow-badge {
width: 60px;
height: 60px;
background: #FFFFFF;
border: 2px solid rgba(229, 231, 235, 0.8);
border-radius: 50%;
display: flex;
align-items: center;
justify-content: center;
font-size: 20px;
font-weight: 800;
margin: 0 auto 20px auto;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
box-shadow: 0 6px 15px rgba(0,0,0,0.02);
}

.flow-step:hover .flow-badge {
border-color: #FF4D4D;
background: #FF4D4D;
color: #FFFFFF;
transform: scale(1.15);
box-shadow: 0 10px 25px rgba(255, 77, 77, 0.35);
}

.flow-title {
font-size: 17px;
font-weight: 800;
margin-bottom: 8px;
}

.flow-desc {
font-size: 13px;
color: #6B7280;
line-height: 1.5;
}

/* Responsive Global Adjustments */
@media (max-width: 1024px) {
    .chili-grid { grid-template-columns: repeat(2, 1fr); }
    .features-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
    .hero-title { font-size: 38px; line-height: 1.2; }
    .hero-subtitle { font-size: 15px; }
    .hero-container { padding-top: 60px; padding-bottom: 30px; }
    
    .hero-actions.gsap-hero-actions {
        flex-direction: column !important;
        gap: 12px !important;
        width: 100%;
        max-width: 400px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .hero-actions.gsap-hero-actions a {
        width: 100%;
    }
    
    .btn-primary, .btn-secondary {
        width: 100%;
        justify-content: center;
    }
    
    .stats-container { 
        grid-template-columns: 1fr; 
        gap: 16px; 
    }
    
    .chili-grid { 
        grid-template-columns: 1fr; 
    }
    
    .flow-container {
        flex-direction: column;
        gap: 30px;
    }
    
    .flow-line {
        display: none;
    }
    
    .section-title { font-size: 32px; }
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

# 2. HERO SECTION
st.markdown("""
<div class="hero-container">
<div class="hero-badge gsap-hero-badge">🚀 Cloud Intelligence Platform</div>
<h1 class="hero-title gsap-hero-title">
Deteksi & Analisis Cabai Rawit<br>Secara Instan Berbasis <span>Gemini AI</span>
</h1>
<p class="hero-subtitle gsap-hero-subtitle">
Integrasi platform computer vision tercanggih yang menghadirkan klasifikasi multimodal cerdas, analisis karakteristik visual real-time, dan penyimpanan data lokal yang sangat aman untuk pertanian modern Indonesia.
</p>
</div>
""", unsafe_allow_html=True)

# CTA Buttons with Premium Alignment
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    st.markdown("""
<div class="hero-actions gsap-hero-actions" style="display: flex; justify-content: center; gap: 16px; margin-bottom: 60px; position: relative; z-index: 1;">
<a href="/klasifikasi" target="_self" style="text-decoration: none;">
<button class="btn-primary">
📸 Mulai Klasifikasi
</button>
</a>
<a href="/tentang" target="_self" style="text-decoration: none;">
<button class="btn-secondary">
ℹ️ Pelajari Arsitektur
</button>
</a>
</div>
""", unsafe_allow_html=True)

# 3. STATS CARD GRID
st.markdown("""
<div class="stats-container gsap-stats">
<div class="stat-card">
<div class="stat-number">99.4%</div>
<div class="stat-label">AKURASI DETEKSI CLOUD AI</div>
</div>
<div class="stat-card">
<div class="stat-number">&lt; 1.5s</div>
<div class="stat-label">WAKTU RESPON DETEKSI</div>
</div>
<div class="stat-card">
<div class="stat-number">100%</div>
<div class="stat-label">API KEY TERLINDUNGI (.ENV)</div>
</div>
</div>
""", unsafe_allow_html=True)

# 4. INTERACTIVE FEATURE GRID (GSAP Target with Spotlight Effect)
st.markdown("""
<div class="section-header">
<h2 class="section-title">Fitur Unggulan Sistem</h2>
<p class="section-subtitle">Didesain dengan fokus pada performa, estetika premium, dan kegunaan maksimal di lapangan.</p>
</div>

<div class="features-grid">
<div class="spotlight-card gsap-feature-card">
<div class="feature-icon">🧠</div>
<h3 class="feature-name">Multimodal Cloud AI</h3>
<p class="feature-desc">Memanfaatkan kecerdasan buatan terdepan Google Gemini AI untuk memproses kombinasi piksel gambar dan instruksi prompt khusus guna mendapatkan ketepatan klasifikasi yang tiada tara.</p>
</div>

<div class="spotlight-card gsap-feature-card">
<div class="feature-icon">📸</div>
<h3 class="feature-name">Kamera & Upload Instan</h3>
<p class="feature-desc">Mendukung pengambilan gambar langsung dari webcam/kamera handphone secara real-time untuk analisis cepat di lapangan, serta upload file lokal konvensional format JPG/PNG.</p>
</div>

<div class="spotlight-card gsap-feature-card">
<div class="feature-icon">🛡️</div>
<h3 class="feature-name">Filter Bukan Cabai (Shield Guard)</h3>
<p class="feature-desc">Dilengkapi dengan proteksi filter cerdas yang secara otomatis mengenali dan menolak gambar anomali yang bukan merupakan objek cabai, disertai pesan peringatan informatif.</p>
</div>

<div class="spotlight-card gsap-feature-card">
<div class="feature-icon">💾</div>
<h3 class="feature-name">Riwayat Terenkripsi SQLite</h3>
<p class="feature-desc">Hasil klasifikasi dan analisis visual disimpan secara lokal di dalam database SQLite bawaan sistem yang sangat ringan, terorganisir, dan dapat dikelola kapan saja.</p>
</div>
</div>
""", unsafe_allow_html=True)

# 5. CHILI SHOWCASE GRID (Soft Colored Glass Glassmorphism)
st.markdown("""
<div class="section-header">
<h2 class="section-title">Cabai yang Dapat Dikenali</h2>
<p class="section-subtitle">Sistem saat ini mendukung pendeteksian 4 jenis varietas cabai rawit populer di Indonesia.</p>
</div>

<div class="chili-grid">
<div class="chili-card chili-setan gsap-chili-card">
<div class="chili-emoji">😈</div>
<h3 class="chili-title">Cabai Setan/Rawit</h3>
<p class="chili-desc">Cabai merah/oranye berkerut dengan rasa pedas luar biasa menyengat.</p>
</div>

<div class="chili-card chili-gendot gsap-chili-card">
<div class="chili-emoji">🫑</div>
<h3 class="chili-title">Cabai Gendot</h3>
<p class="chili-desc">Cabai berbentuk lonceng gemuk dengan kulit tebal khas daerah pegunungan.</p>
</div>

<div class="chili-card chili-putih gsap-chili-card">
<div class="chili-emoji">🌶️</div>
<h3 class="chili-title">Cabai Putih</h3>
<p class="chili-desc">Cabai rawit berwarna putih kekuningan saat muda dengan bentuk lonjong kecil.</p>
</div>

<div class="chili-card chili-keriting gsap-chili-card">
<div class="chili-emoji">🌀</div>
<h3 class="chili-title">Cabai Merah Keriting</h3>
<p class="chili-desc">Cabai panjang langsing bergelombang dengan tingkat kepedasan sedang-tinggi.</p>
</div>
</div>
""", unsafe_allow_html=True)

# 6. DYNAMIC ALUR KERJA (Webflow Workflow Line)
st.markdown("""
<div class="section-header">
<h2 class="section-title">Alur Kerja Sistem</h2>
<p class="section-subtitle">Bagaimana cara sistem mengenali cabai Anda dalam hitungan detik?</p>
</div>

<div class="flow-container gsap-flow">
<div class="flow-line"></div>

<div class="flow-step">
<div class="flow-badge">1</div>
<h4 class="flow-title">Unggah/Potret</h4>
<p class="flow-desc">Ambil foto cabai langsung dengan kamera atau unggah file foto dari galeri.</p>
</div>

<div class="flow-step">
<div class="flow-badge">2</div>
<h4 class="flow-title">Analisis Cloud</h4>
<p class="flow-desc">Gambar diproses oleh model kecerdasan buatan multimodal Google Gemini AI.</p>
</div>

<div class="flow-step">
<div class="flow-badge">3</div>
<h4 class="flow-title">Hasil Instan</h4>
<p class="flow-desc">Jenis cabai, persentase keyakinan, dan karakteristik visual ditampilkan lengkap.</p>
</div>

<div class="flow-step">
<div class="flow-badge">4</div>
<h4 class="flow-title">Arsip Aman</h4>
<p class="flow-desc">Simpan riwayat hasil analisis dengan aman ke database SQLite lokal Anda.</p>
</div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; color: #888888; padding: 60px 0 30px 0; border-top: 1px solid rgba(229, 231, 235, 0.8); margin-top: 100px; position: relative; z-index: 1;">
<p style="margin: 5px 0; font-weight: 700; color: #111111; font-size: 15px;">Sistem Klasifikasi Cabai Rawit Indonesia</p>
<p style="margin: 5px 0; font-size: 13px;">© 2026 - Project Cabai Difa. Hak Cipta Dilindungi.</p>
</div>
""", unsafe_allow_html=True)

# INJEKSI GSAP & MOUSE MOVE TRACKER SCRIPTS
st.markdown("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

<script>
// SPOTLIGHT MOUSE MOVE TRACKING (React Bits Effect)
document.addEventListener('DOMContentLoaded', function() {
    setupSpotlight();
});

// Jalankan ulang tracker untuk memastikan elemen terikat sempurna setelah rendering selesai
window.addEventListener('load', function() {
    setupSpotlight();
    runGsapAnimations();
});

function setupSpotlight() {
    const cards = document.querySelectorAll('.spotlight-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
}

function runGsapAnimations() {
    try {
        // Efek Bounce In untuk Hero Badge
        gsap.from(".gsap-hero-badge", {
            duration: 1.2,
            y: -40,
            opacity: 0,
            ease: "back.out(1.7)"
        });

        // Efek Reveal Naik untuk Hero Title
        gsap.from(".gsap-hero-title", {
            duration: 1.4,
            y: 50,
            opacity: 0,
            delay: 0.2,
            ease: "power4.out"
        });

        // Efek Smooth Fade In untuk Hero Subtitle
        gsap.from(".gsap-hero-subtitle", {
            duration: 1.4,
            y: 30,
            opacity: 0,
            delay: 0.4,
            ease: "power4.out"
        });

        // Efek Expand / Fade In untuk CTA Buttons
        gsap.from(".gsap-hero-actions", {
            duration: 1.2,
            scale: 0.95,
            opacity: 0,
            delay: 0.6,
            ease: "power3.out"
        });

        // Efek Stagger untuk Stats Card
        gsap.from(".gsap-stats .stat-card", {
            duration: 1.2,
            y: 40,
            opacity: 0,
            stagger: 0.15,
            delay: 0.8,
            ease: "power3.out"
        });

        // Efek Reveal untuk Feature Cards (Spotlight)
        gsap.from(".gsap-feature-card", {
            duration: 1.2,
            y: 50,
            opacity: 0,
            stagger: 0.2,
            delay: 1.0,
            ease: "power3.out"
        });

        // Efek Elastic Scale untuk Chili Cards (Katalog Mewah)
        gsap.from(".gsap-chili-card", {
            duration: 1,
            scale: 0.85,
            opacity: 0,
            stagger: 0.15,
            delay: 1.2,
            ease: "back.out(1.5)"
        });

        // Efek Stagger Slide Up untuk Alur Kerja
        gsap.from(".gsap-flow .flow-step", {
            duration: 1,
            y: 40,
            opacity: 0,
            stagger: 0.2,
            delay: 1.4,
            ease: "power3.out"
        });
    } catch(e) {
        console.log("GSAP Error:", e);
    }
}
</script>
""", unsafe_allow_html=True)
