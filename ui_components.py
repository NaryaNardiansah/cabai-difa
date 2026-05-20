import streamlit as st

def render_navbar(active_page):
    """
    Renders an ultra-premium Webflow-style floating capsule navigation bar
    and wraps the app in an iPhone 17 Pro Max frame on desktop view.
    """
    # CSS to style the custom layout
    st.markdown("""
    <style>
        /* Sembunyikan sidebar bawaan Streamlit secara mutlak */
        [data-testid="sidebar-nav-container"], 
        [data-testid="stSidebar"], 
        [data-testid="collapsedControl"],
        [data-testid="stHeader"],
        footer {
            display: none !important;
        }
        
        /* Default mobile view: normal full screen */
        .main .block-container,
        [data-testid="stAppViewBlockContainer"] {
            padding-top: 130px !important;
        }
        
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
        
        .nav-links {
            display: flex;
            gap: 4px;
            background: rgba(0, 0, 0, 0.03);
            padding: 4px;
            border-radius: 100px;
            border: 1px solid rgba(0, 0, 0, 0.01);
        }
        
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
        
        .nav-item.active {
            color: #FFFFFF !important;
            background: linear-gradient(135deg, #FF4D4D 0%, #F59E0B 100%) !important;
            box-shadow: 0 4px 12px rgba(255, 77, 77, 0.2);
        }
        
        /* Mobile responsive defaults */
        .iphone-decorations {
            display: none !important;
        }
        
        /* Desktop: iPhone 17 Pro Max Frame Mockup View */
        @media (min-width: 768px) {
            .main {
                background: #0A0A0F !important;
                background-image: 
                    radial-gradient(circle at 15% 15%, rgba(255, 77, 77, 0.12) 0%, transparent 45%),
                    radial-gradient(circle at 85% 85%, rgba(245, 158, 11, 0.1) 0%, transparent 45%),
                    radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.06) 0%, transparent 50%) !important;
                height: 100vh !important;
                overflow: hidden !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }
            
            /* Reset Streamlit main container layout to center the phone */
            [data-testid="stAppViewMain"] {
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                height: 100vh !important;
                width: 100vw !important;
                background: transparent !important;
            }
            
            /* Wrap the actual Streamlit page column into iPhone screen */
            [data-testid="stAppViewBlockContainer"] {
                width: 390px !important;
                max-width: 390px !important;
                height: 800px !important;
                min-height: 800px !important;
                background-color: #FAFAFA !important;
                border-radius: 46px !important;
                border: 11px solid #8A8D93 !important; /* Titanium Bezel */
                padding: 150px 16px 30px 16px !important; /* Spacing to push content below floating navbar */
                overflow-y: auto !important;
                position: relative !important;
                box-shadow: 
                    inset 0 1px 0 0 rgba(255,255,255,0.25),
                    0 25px 60px rgba(0,0,0,0.6) !important;
                scrollbar-width: none;
                margin: auto !important;
            }
            
            [data-testid="stAppViewBlockContainer"]::-webkit-scrollbar {
                display: none;
            }
            
            /* Volume/Power buttons on the left & right of screen */
            [data-testid="stAppViewBlockContainer"]::before {
                content: '';
                position: absolute;
                left: -15px;
                top: 170px;
                width: 4px;
                height: 50px;
                background: #8A8D93;
                border-radius: 3px 0 0 3px;
                box-shadow: -1px 0 2px rgba(0,0,0,0.4);
                z-index: 99999;
            }
            
            [data-testid="stAppViewBlockContainer"]::after {
                content: '';
                position: absolute;
                right: -15px;
                top: 210px;
                width: 4px;
                height: 75px;
                background: #8A8D93;
                border-radius: 0 3px 3px 0;
                box-shadow: 1px 0 2px rgba(0,0,0,0.4);
                z-index: 99999;
            }
            
            /* Force Stack Streamlit columns and grids inside the iPhone */
            [data-testid="stAppViewBlockContainer"] [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                gap: 16px !important;
            }
            
            [data-testid="stAppViewBlockContainer"] [data-testid="column"],
            [data-testid="stAppViewBlockContainer"] [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 100% !important;
                max-width: 100% !important;
                flex-basis: 100% !important;
            }
            
            /* Force grid layout stacks */
            [data-testid="stAppViewBlockContainer"] .stats-container,
            [data-testid="stAppViewBlockContainer"] .features-grid,
            [data-testid="stAppViewBlockContainer"] .chili-grid {
                grid-template-columns: 1fr !important;
                gap: 16px !important;
            }
            
            /* Custom list and grid cards padding resets */
            [data-testid="stAppViewBlockContainer"] .premium-card,
            [data-testid="stAppViewBlockContainer"] .spotlight-card,
            [data-testid="stAppViewBlockContainer"] .stat-card,
            [data-testid="stAppViewBlockContainer"] .chili-card,
            [data-testid="stAppViewBlockContainer"] .chili-glass-card {
                padding: 20px 16px !important;
                margin-bottom: 16px !important;
                min-height: auto !important;
            }
            
            [data-testid="stAppViewBlockContainer"] .flow-container {
                flex-direction: column !important;
                gap: 24px !important;
            }
            
            [data-testid="stAppViewBlockContainer"] .flow-line {
                display: none !important;
            }
            
            /* Text sizing adaptations for small iPhone screen */
            [data-testid="stAppViewBlockContainer"] .hero-title {
                font-size: 26px !important;
                line-height: 1.25 !important;
            }
            
            [data-testid="stAppViewBlockContainer"] .hero-subtitle {
                font-size: 13px !important;
                line-height: 1.5 !important;
            }
            
            [data-testid="stAppViewBlockContainer"] .section-title {
                font-size: 20px !important;
            }
            
            [data-testid="stAppViewBlockContainer"] .page-title {
                font-size: 22px !important;
            }
            
            [data-testid="stAppViewBlockContainer"] .hero-actions {
                flex-direction: column !important;
                align-items: center !important;
                gap: 12px !important;
                margin-bottom: 30px !important;
            }
            [data-testid="stAppViewBlockContainer"] .hero-actions a {
                display: block !important;
                width: 100% !important;
            }
            [data-testid="stAppViewBlockContainer"] .hero-actions button {
                width: 100% !important;
                max-width: 100% !important;
                justify-content: center !important;
                box-sizing: border-box !important;
            }
            
            /* Custom floating navbar inside the phone screen - Mobile Layout Mode */
            .custom-navbar {
                position: fixed !important;
                top: calc(50vh - 400px + 11px + 48px + 10px) !important;
                left: 50% !important;
                transform: translateX(-50%) !important;
                width: 344px !important;
                padding: 10px 12px !important;
                border-radius: 20px !important; /* Fully rounded floating capsule */
                border: 1px solid rgba(0, 0, 0, 0.05) !important;
                box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
                flex-direction: column !important;
                gap: 8px !important;
                background: rgba(250, 250, 250, 0.95) !important;
                backdrop-filter: blur(10px) !important;
                z-index: 999999 !important;
            }
            
            .nav-logo {
                font-size: 14px !important;
                width: 100% !important;
                justify-content: center !important;
            }
            
            .nav-links {
                width: 100% !important;
                justify-content: space-between !important;
                flex-wrap: nowrap !important;
                gap: 2px !important;
                padding: 2px !important;
            }
            
            .nav-item {
                font-size: 10px !important;
                padding: 6px 8px !important;
                flex: 1 !important;
                justify-content: center !important;
                text-align: center !important;
            }
            
            /* Show iphone elements */
            .iphone-decorations {
                display: block !important;
            }
            
            /* Phone Elements Layout - Fixed to center of screen matching the frame */
            .iphone-dynamic-island {
                position: fixed !important;
                top: calc(50vh - 400px + 11px + 10px) !important;
                left: 50% !important;
                transform: translateX(-50%) !important;
                width: 110px !important;
                height: 28px !important;
                background: #000000 !important;
                border-radius: 20px !important;
                z-index: 1000000 !important;
                box-shadow: 0 0 0 1px rgba(255,255,255,0.05) !important;
            }
            
            .iphone-dynamic-island::after {
                content: '' !important;
                position: absolute !important;
                right: 12px !important;
                top: 50% !important;
                transform: translateY(-50%) !important;
                width: 8px !important;
                height: 8px !important;
                background: radial-gradient(circle, #1a1a2e 0%, #000 70%) !important;
                border-radius: 50% !important;
            }
            
            .iphone-status-bar {
                position: fixed !important;
                top: calc(50vh - 400px + 11px) !important;
                left: 50% !important;
                transform: translateX(-50%) !important;
                width: 368px !important;
                height: 48px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: space-between !important;
                padding: 0 20px !important;
                z-index: 999998 !important;
                background: rgba(250, 250, 250, 0.95) !important;
                backdrop-filter: blur(10px) !important;
                border-top-left-radius: 35px !important;
                border-top-right-radius: 35px !important;
                font-size: 12px !important;
                font-weight: 700 !important;
                color: #000000 !important;
            }
            
            .iphone-status-bar-icons {
                display: flex !important;
                align-items: center !important;
                gap: 5px !important;
            }
            
            .iphone-url-bar {
                display: none !important;
            }
            
            .iphone-url-text {
                background: rgba(0, 0, 0, 0.04) !important;
                padding: 3px 12px !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
                color: #333333 !important;
            }
            
            .iphone-home-indicator {
                position: fixed !important;
                bottom: calc(50vh - 400px + 11px + 8px) !important;
                left: 50% !important;
                transform: translateX(-50%) !important;
                width: 120px !important;
                height: 5px !important;
                background: rgba(0, 0, 0, 0.25) !important;
                border-radius: 100px !important;
                z-index: 1000000 !important;
            }
        }
        
        /* Mobile adjustments */
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
    
    # Render iPhone Decorations & Custom Navbar HTML
    st.markdown(f"""
    <!-- iPhone Decorations (only visible on desktop via CSS) -->
    <div class="iphone-decorations">
        <div class="iphone-dynamic-island"></div>
        <div class="iphone-status-bar">
            <span class="iphone-time" id="iphone-live-time">10:46 AM</span>
            <div class="iphone-status-bar-icons">
                <span style="font-size: 11px;">📶</span>
                <span style="font-size: 11px;">⦿</span>
                <span style="font-size: 11px;">100% 🔋</span>
            </div>
        </div>
        <div class="iphone-url-bar">
            <span>🔒</span>
            <span class="iphone-url-text">cabai-difa-anasera007.streamlit.app</span>
        </div>
        <div class="iphone-home-indicator"></div>
    </div>
    
    <script>
        function updateIphoneTime() {{
            const now = new Date();
            let hours = now.getHours();
            const minutes = now.getMinutes().toString().padStart(2, '0');
            const ampm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12 || 12;
            const timeStr = hours + ":" + minutes + " " + ampm;
            const el = document.getElementById('iphone-live-time');
            if (el) el.textContent = timeStr;
        }}
        updateIphoneTime();
        setInterval(updateIphoneTime, 30000);
    </script>
    
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

