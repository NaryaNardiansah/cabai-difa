import sqlite3
from datetime import datetime
import os

# Path database
DB_PATH = os.path.join(os.path.dirname(__file__), 'prediksi.db')

def get_connection():
    """Membuat koneksi ke database SQLite"""
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    """Inisialisasi database dan tabel prediksi"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Buat tabel prediksi jika belum ada
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prediksi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_file TEXT NOT NULL,
                hasil_prediksi TEXT NOT NULL,
                confidence_score REAL NOT NULL,
                tanggal_prediksi DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    except Exception as e:
        pass

def simpan_prediksi(nama_file, hasil_prediksi, confidence_score):
    """
    Menyimpan hasil prediksi ke database
    
    Parameters:
    - nama_file: Nama file gambar yang diprediksi
    - hasil_prediksi: Jenis cabai hasil prediksi
    - confidence_score: Tingkat kepercayaan model (0-100)
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO prediksi (nama_file, hasil_prediksi, confidence_score, tanggal_prediksi)
            VALUES (?, ?, ?, ?)
        ''', (nama_file, hasil_prediksi, confidence_score, datetime.now()))
        
        conn.commit()
        conn.close()
    except Exception as e:
        pass

def ambil_riwayat():
    """
    Mengambil semua riwayat prediksi dari database
    
    Returns:
    - List of tuples berisi riwayat prediksi
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, nama_file, hasil_prediksi, confidence_score, tanggal_prediksi
        FROM prediksi
        ORDER BY tanggal_prediksi DESC
    ''')
    
    riwayat = cursor.fetchall()
    conn.close()
    
    return riwayat

def hapus_riwayat(id):
    """
    Menghapus satu riwayat prediksi berdasarkan ID
    
    Parameters:
    - id: ID riwayat yang akan dihapus
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM prediksi WHERE id = ?
        ''', (id,))
        
        conn.commit()
        conn.close()
    except Exception as e:
        pass

def hapus_semua_riwayat():
    """Menghapus semua riwayat prediksi"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM prediksi')
        
        conn.commit()
        conn.close()
    except Exception as e:
        pass

def get_total_riwayat():
    """Menghitung total riwayat prediksi"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM prediksi')
    total = cursor.fetchone()[0]
    
    conn.close()
    return total

# Inisialisasi database saat module diimport (safe version)
try:
    init_db()
except Exception:
    pass
