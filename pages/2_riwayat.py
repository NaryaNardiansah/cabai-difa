import streamlit as st
import pandas as pd
from database import ambil_riwayat, hapus_riwayat, hapus_semua_riwayat, get_total_riwayat
from ui_components import render_navbar

# Konfigurasi halaman
st.set_page_config(
    page_title="Riwayat Prediksi",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render Custom Premium Top Navigation Bar
render_navbar("riwayat")

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
background: radial-gradient(circle, rgba(245, 158, 11, 0.06) 0%, rgba(255, 255, 255, 0) 70%);
top: -150px;
left: -150px;
border-radius: 50%;
filter: blur(90px);
}

.blob-2 {
position: absolute;
width: 600px;
height: 600px;
background: radial-gradient(circle, rgba(16, 185, 129, 0.06) 0%, rgba(255, 255, 255, 0) 70%);
bottom: -150px;
right: -150px;
border-radius: 50%;
filter: blur(90px);
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

/* Statistics Section */
.stats-container {
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 24px;
max-width: 1000px;
margin: 20px auto 40px auto;
z-index: 1;
position: relative;
}

.stat-card {
background: rgba(255, 255, 255, 0.85);
backdrop-filter: blur(12px);
border: 1px solid rgba(229, 231, 235, 0.8);
border-top: 4px solid #FF4D4D;
border-radius: 20px;
padding: 24px;
text-align: center;
box-shadow: 0 8px 30px rgba(0,0,0,0.02);
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.stat-card.variant {
border-top-color: #F59E0B;
}

.stat-card.model {
border-top-color: #10B981;
}

.stat-card:hover {
transform: translateY(-4px);
box-shadow: 0 15px 35px rgba(0,0,0,0.05);
}

.stat-number-box {
display: flex;
align-items: center;
justify-content: center;
gap: 8px;
margin-bottom: 8px;
}

.stat-icon {
font-size: 28px;
}

.stat-number {
font-size: 38px;
font-weight: 900;
color: #111111;
line-height: 1.2;
}

.stat-label {
font-size: 13px;
color: #6B7280;
font-weight: 700;
letter-spacing: 1px;
margin-top: 4px;
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

.premium-card h3 {
font-size: 19px;
font-weight: 800;
margin-bottom: 15px;
display: flex;
align-items: center;
gap: 8px;
}

/* Custom Warning/Info Boxes */
.warning-box {
background: rgba(239, 68, 68, 0.04) !important;
border: 1px dashed rgba(239, 68, 68, 0.3) !important;
border-radius: 12px !important;
padding: 16px !important;
color: #B91C1C !important;
font-size: 13.5px !important;
line-height: 1.5 !important;
margin-bottom: 20px !important;
}

.empty-state {
background: rgba(255, 255, 255, 0.8);
border: 1px dashed rgba(229, 231, 235, 0.8);
border-radius: 20px;
padding: 50px 30px;
text-align: center;
box-shadow: 0 8px 30px rgba(0,0,0,0.02);
max-width: 600px;
margin: 40px auto;
position: relative;
z-index: 1;
}

.empty-icon {
font-size: 48px;
margin-bottom: 20px;
}

/* Button Custom Styles */
.stButton > button {
background: #111111 !important;
color: #FFFFFF !important;
border: none !important;
border-radius: 12px !important;
padding: 14px 28px !important;
font-size: 15px !important;
font-weight: 700 !important;
box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
width: 100% !important;
}

.stButton > button:hover {
transform: translateY(-2px) !important;
background: #222222 !important;
box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
}

/* Red Delete Buttons */
.delete-btn button {
background: linear-gradient(135deg, #FF4D4D 0%, #DC2626 100%) !important;
box-shadow: 0 6px 16px rgba(255, 77, 77, 0.15) !important;
}

.delete-btn button:hover {
background: linear-gradient(135deg, #FF6666 0%, #B91C1C 100%) !important;
box-shadow: 0 10px 24px rgba(255, 77, 77, 0.25) !important;
}

/* Responsive Global Adjustments */
@media (max-width: 768px) {
    .page-title { font-size: 36px; line-height: 1.2; }
    .page-subtitle { font-size: 15px; }
    .page-header { padding-top: 60px; padding-bottom: 20px; }
    .stats-container { grid-template-columns: 1fr; gap: 16px; }
    .stat-number { font-size: 32px; }
    .stat-card { padding: 20px; }
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

# 2. PAGE HEADER (Pushed down beautifully by layout margin)
st.markdown("""
<div class="page-header gsap-fade-in">
<div class="hero-badge" style="margin-bottom: 16px;">📊 SQLite Database</div>
<h1 class="page-title">Riwayat <span>Prediksi</span></h1>
<p class="page-subtitle">Kelola dan tinjau seluruh rekaman analisis cabai rawit yang tersimpan di sistem lokal SQLite Anda.</p>
</div>
""", unsafe_allow_html=True)

# Statistik
total_riwayat = get_total_riwayat()

# 3. STATISTIK CARDS (GSAP Stagger & High-Contrast Styles)
st.markdown(f"""
<div class="stats-container gsap-stats">
<div class="stat-card">
<div class="stat-number-box">
<span class="stat-icon">📈</span>
<span class="stat-number">{total_riwayat}</span>
</div>
<div class="stat-label">TOTAL PREDIKSI</div>
</div>
<div class="stat-card variant">
<div class="stat-number-box">
<span class="stat-icon">🌶️</span>
<span class="stat-number">4</span>
</div>
<div class="stat-label">VARIETAS CABAI</div>
</div>
<div class="stat-card model">
<div class="stat-number-box">
<span class="stat-icon">🧠</span>
<span class="stat-number" style="font-size: 22px;">Gemini AI</span>
</div>
<div class="stat-label">MODEL DETEKSI</div>
</div>
</div>
""", unsafe_allow_html=True)

# Ambil riwayat dari database
riwayat = ambil_riwayat()

if len(riwayat) == 0:
    st.markdown("""
<div class="empty-state gsap-fade-in">
<div class="empty-icon">📭</div>
<h3 style="font-size: 22px; font-weight: 800; margin-bottom: 10px;">Belum Ada Riwayat Tersimpan</h3>
<p style="color: #6B7280; font-size: 14.5px; line-height: 1.6; margin-bottom: 25px;">Anda belum melakukan analisis apa pun atau riwayat telah dikosongkan. Silakan menuju halaman Klasifikasi untuk mulai mendeteksi jenis cabai rawit Anda.</p>
</div>
""", unsafe_allow_html=True)
    
    col_l, col_c, col_r = st.columns([1, 1, 1])
    with col_c:
        if st.button("🌶️ Mulai Klasifikasi"):
            st.switch_page("pages/1_klasifikasi.py")
else:
    # Konversi ke DataFrame
    df = pd.DataFrame(riwayat, columns=['ID', 'Nama File', 'Hasil Prediksi', 'Confidence Score (%)', 'Tanggal'])
    
    # Format tanggal
    df['Tanggal'] = pd.to_datetime(df['Tanggal']).dt.strftime('%d-%m-%Y %H:%M')
    
    # Format confidence score
    df['Confidence Score (%)'] = df['Confidence Score (%)'].round(2)
    
    # Display table in a premium card
    st.markdown(f"""
<div class="premium-card gsap-card">
<h3>📊 Database Riwayat ({len(df)} Rekaman)</h3>
</div>
""", unsafe_allow_html=True)
    
    # Render dataframe table
    st.dataframe(
        df,
        hide_index=True,
        column_config={
            "ID": st.column_config.NumberColumn(
                "ID",
                help="ID transaksi riwayat unik",
                format="%d"
            ),
            "Nama File": st.column_config.TextColumn(
                "Nama File",
                help="Nama berkas gambar yang dideteksi"
            ),
            "Hasil Prediksi": st.column_config.TextColumn(
                "Hasil Prediksi",
                help="Kategori cabai rawit yang dideteksi"
            ),
            "Confidence Score (%)": st.column_config.NumberColumn(
                "Confidence (%)",
                help="Persentase keyakinan deteksi Gemini AI",
                format="%.2f"
            ),
            "Tanggal": st.column_config.TextColumn(
                "Tanggal",
                help="Waktu pencatatan deteksi"
            )
        }
    )
    
    st.markdown("")
    
    # Tombol hapus (Kelola Riwayat) dalam dua kartu premium terpisah
    col_hapus1, col_hapus2 = st.columns(2)
    
    with col_hapus1:
        st.markdown("""
<div class="premium-card gsap-card" style="height: 100%;">
<h3>🗑️ Hapus Rekaman Tertentu</h3>
<p style="color: #6B7280; font-size: 13.5px; line-height: 1.5; margin-bottom: 20px;">Pilih ID unik dari riwayat tabel di atas untuk menghapus satu baris rekaman prediksi tersebut secara permanen.</p>
</div>
""", unsafe_allow_html=True)
        
        id_list = df['ID'].tolist()
        id_to_delete = st.selectbox("Pilih ID yang ingin dihapus:", id_list, key="delete_id_select")
        
        st.markdown('<div class="delete-btn">', unsafe_allow_html=True)
        if st.button("🗑️ Hapus Rekaman Ini"):
            hapus_riwayat(id_to_delete)
            st.success(f"✅ Riwayat dengan ID {id_to_delete} berhasil dihapus!")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_hapus2:
        st.markdown("""
<div class="premium-card gsap-card" style="height: 100%;">
<h3>⚠️ Kosongkan Semua Database</h3>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("""
<div class="warning-box">
<strong>Peringatan Penting:</strong> Tindakan ini akan menghapus seluruh isi tabel riwayat klasifikasi secara permanen dari SQLite database lokal Anda. Tindakan ini tidak dapat dibatalkan!
</div>
""", unsafe_allow_html=True)
        
        st.markdown('<div class="delete-btn">', unsafe_allow_html=True)
        if st.button("🚨 Bersihkan Semua Riwayat"):
            hapus_semua_riwayat()
            st.success("✅ Seluruh riwayat database lokal berhasil dibersihkan!")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888888; padding: 20px 0; font-size: 13.5px;" class="gsap-fade-in">
<p><strong>Database lokal:</strong> SQLite 3 | <strong>Framework:</strong> Streamlit + Pandas Dataframe</p>
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

        // Animasi stagger-up untuk kartu statistik
        gsap.from(".gsap-stats .stat-card", {
            duration: 1,
            opacity: 0,
            y: 30,
            stagger: 0.15,
            ease: "power3.out",
            delay: 0.2
        });

        // Animasi stagger-up untuk kartu kelola riwayat dan tabel
        gsap.from(".gsap-card", {
            duration: 1,
            opacity: 0,
            y: 30,
            stagger: 0.15,
            ease: "power3.out",
            delay: 0.4
        });
    } catch(e) {
        console.log("GSAP Error:", e);
    }
});
</script>
""", unsafe_allow_html=True)
