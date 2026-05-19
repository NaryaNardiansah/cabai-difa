import streamlit as st

def render_navbar(active_page):
    """
    Renders an ultra-premium Webflow-style floating capsule navigation bar
    and hides the default Streamlit sidebar and elements.
    """
    # CSS to hide Streamlit default sidebar and header, and style the custom navbar
    st.markdown("""
    <style>
        /* Sembunyikan sidebar bawaan Streamlit secara mutlak */
        [data-testid="sidebar-nav-container"], 
        [data-testid="stSidebar"], 
        [data-testid="collapsedControl"] {
            display: none !important;
        }
        
        /* Tambahkan margin atas agar konten tidak terpotong oleh fixed navbar */
        .main .block-container,
        [data-testid="stAppViewBlockContainer"] {
            padding-top: 130px !important;
        }
        
        /* Custom Premium Webflow Floating Capsule Navbar */
        .custom-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(229, 231, 235, 0.7);
            padding: 10px 24px;
            position: fixed;
            top: 16px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 48px);
            max-width: 1100px;
            border-radius: 100px;
            z-index: 999999;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03), 0 1px 3px rgba(0, 0, 0, 0.01);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        /* Logo Styles */
        .nav-logo {
            font-family: 'Outfit', sans-serif !important;
            font-size: 19px;
            font-weight: 900;
            color: #111111;
            display: flex;
            align-items: center;
            gap: 8px;
            letter-spacing: -0.5px;
        }
        
        .nav-logo-text span {
            background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Nav Links Capsule Container */
        .nav-links {
            display: flex;
            gap: 4px;
            background: rgba(0, 0, 0, 0.03);
            padding: 4px;
            border-radius: 100px;
            border: 1px solid rgba(0, 0, 0, 0.01);
        }
        
        /* Individual Nav Items */
        .nav-item {
            text-decoration: none !important;
            color: #555555 !important;
            font-size: 13.5px;
            font-weight: 700;
            padding: 8px 18px;
            border-radius: 100px;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .nav-item:hover {
            color: #000000 !important;
            background-color: rgba(0, 0, 0, 0.04);
            transform: translateY(-1px);
        }
        
        /* Active Nav Item - Sleek Branded Gradient Pill */
        .nav-item.active {
            color: #FFFFFF !important;
            background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%) !important;
            box-shadow: 0 4px 12px rgba(255, 77, 77, 0.2);
        }
        
        /* Responsive Mobile & Tablet Styles */
        @media (max-width: 768px) {
            .custom-navbar {
                flex-direction: column;
                gap: 12px;
                border-radius: 24px;
                padding: 14px 16px;
                width: calc(100% - 32px);
            }
            .nav-links {
                width: 100%;
                justify-content: space-between;
                flex-wrap: wrap;
                gap: 4px;
            }
            .nav-item {
                font-size: 12.5px;
                padding: 6px 10px;
                flex: 1;
                justify-content: center;
                text-align: center;
            }
            .main .block-container,
            [data-testid="stAppViewBlockContainer"] {
                padding-top: 180px !important;
            }
        }
        
        @media (max-width: 480px) {
            .nav-item {
                font-size: 11px;
                padding: 6px 8px;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Active class mapping
    active_home = "active" if active_page == "home" else ""
    active_klasifikasi = "active" if active_page == "klasifikasi" else ""
    active_riwayat = "active" if active_page == "riwayat" else ""
    active_tentang = "active" if active_page == "tentang" else ""
    
    # Render Navbar HTML (Flat against left margin)
    st.markdown(f"""
    <div class="custom-navbar">
        <div class="nav-logo">
            <span>🌶️</span>
            <div class="nav-logo-text">Cabai <span>Difa</span></div>
        </div>
        <div class="nav-links">
            <a href="/" target="_self" class="nav-item {active_home}">🏠 Beranda</a>
            <a href="/klasifikasi" target="_self" class="nav-item {active_klasifikasi}">📸 Klasifikasi</a>
            <a href="/riwayat" target="_self" class="nav-item {active_riwayat}">📊 Riwayat</a>
            <a href="/tentang" target="_self" class="nav-item {active_tentang}">ℹ️ Tentang</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
