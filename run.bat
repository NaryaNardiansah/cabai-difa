@echo off
echo ========================================
echo   Sistem Klasifikasi Cabai Rawit
echo ========================================
echo.
echo   Memeriksa dependencies...
echo.

pip install -r requirements.txt

echo.
echo   Dependencies berhasil diinstall!
echo.
echo ========================================
echo   Menjalankan aplikasi Streamlit...
echo ========================================
echo.
echo   Aplikasi akan terbuka di browser
echo   URL: http://localhost:8501
echo.
echo   Tekan Ctrl+C untuk menghentikan
echo.

streamlit run app.py

pause
