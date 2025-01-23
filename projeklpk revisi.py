import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Food Freshness App", page_icon="🍎", layout="wide")

# Palet Warna
PRIMARY_COLOR = "#4CAF50"
SECONDARY_COLOR = "#F44336"
BACKGROUND_COLOR = "#E3F2FD"  # Biru muda
TEXT_COLOR = "#333333"
ACCENT_COLOR = "#FFC107"

# CSS Kustom
st.markdown(f"""
    <style>
    .main {{
        background-color: {BACKGROUND_COLOR} !important;
        color: {TEXT_COLOR};
        font-family: 'Poppins', sans-serif;
    }}
    .stApp {{
        background-color: {BACKGROUND_COLOR} !important;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }}
    .stButton>button:hover {{
        background-color: {SECONDARY_COLOR};
        transform: scale(1.05);
    }}
    .sidebar .sidebar-content {{
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }}
    h1, h2, h3 {{
        color: {PRIMARY_COLOR};
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        color: {PRIMARY_COLOR};
    }}
    .subtitle {{
        font-size: 24px;
        color: {TEXT_COLOR};
        margin-bottom: 20px;
    }}
    .image-container {{
        text-align: center;
        margin: 20px 0;
    }}
    </style>
""", unsafe_allow_html=True)


# --- Efek Animasi Balon dan Salju ---
def animation_effect():
    st.balloons()
    for _ in range(5):
        st.markdown('<div class="snowflake">❄️</div>', unsafe_allow_html=True)


# --- Navigasi Sidebar ---
menu = st.sidebar.selectbox("📂 Menu", [
    "🏠 Beranda", 
    "🧮 Penilaian Kelayakan Makanan", 
    "ℹ️ Info"
])

from datetime import datetime
import streamlit as st
import numpy as np

# --- Beranda ---
if menu == "🏠 Beranda":
    st.title("🍎 FRESH CHECK - Pendeteksi Kelayakan Konsumsi Makanan")

    # Gambar lebih menarik mencakup semua kategori makanan
    st.image("https://png.pngtree.com/png-clipart/20220125/original/pngtree-nut-food-png-image_7222167.png", width=700)

    # Deskripsi aplikasi dengan ikon dan bullet point yang lebih menarik
    st.markdown("""
    ### 🌟 Selamat Datang di **Pendeteksi Kelayakan Konsumsi Makanan**!  
    Aplikasi ini dirancang untuk membantu Anda mengonsumsi makanan yang **sehat** dan **aman** dengan fitur-fitur menarik berikut:

    - 📅 **Pengecekan Tanggal Kedaluwarsa**: Pantau masa simpan makanan agar tetap aman.  
    - 💬 **Forum Diskusi**: Berbagi pengalaman dan tips dengan pengguna lainnya.
    """)

     # Tambahkan tombol untuk langsung menuju fitur utama
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Penilaian Kelayakan Makanan"):
            st.success("Silakan buka menu 📊 Penilaian Kelayakan Makanan di sidebar!")

    # Catatan di bagian bawah
    st.markdown("---")
    st.info("💡 **Tips:** Jaga kesehatan dengan memilih makanan bergizi dan mengolahnya dengan cara yang tepat!")

# --- Penilaian Kelayakan Makanan ---
if menu == "🧮 Penilaian Kelayakan Makanan":
    st.title("🔍 Penilaian Kelayakan Makanan")

    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", [
        "Sayuran 🥦", "Buah-buahan 🍎", "Daging 🍖", 
        "Susu & Produk Olahan 🥛", "Roti & Kue 🍞", 
        "Makanan Kaleng 🥫", "Minuman 🥤"
    ])

    tanggal_input = st.date_input("📅 Tanggal Pembelian")

    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
        "Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"
    ])
    perubahan_fisik = st.multiselect("⚠️ Perubahan Fisik", [
        "Perubahan warna 🎨", "Bau tidak sedap 🤢", 
        "Tekstur berlendir 🦠", "Jamur 🍄"
    ])

    
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fungsi untuk mengirim email notifikasi
def kirim_notifikasi_email(email_pengguna, jenis_makanan, hari_tanggal):
    try:
        # Setup email
        pengirim_email = "your_email@example.com"  # Ganti dengan email pengirim
        password_email = "your_password"  # Ganti dengan password pengirim
        penerima_email = email_pengguna
        
        # Buat pesan email
        msg = MIMEMultipart()
        msg['From'] = pengirim_email
        msg['To'] = penerima_email
        msg['Subject'] = f"Peringatan Kedaluwarsa {jenis_makanan}"
        
        body = f"""
        Hallo,

        Kami ingin mengingatkan Anda bahwa {jenis_makanan} Anda hampir kedaluwarsa pada {hari_tanggal}.
        Harap pastikan untuk segera mengonsumsinya atau memeriksanya kembali.

        Terima kasih,
        Pendeteksi Kelayakan Makanan
        """
        msg.attach(MIMEText(body, 'plain'))
        
        # Kirim email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(pengirim_email, password_email)
            server.sendmail(pengirim_email, penerima_email, msg.as_string())
        
        st.success("Notifikasi email berhasil dikirim!")
    except Exception as e:
        st.error(f"Error mengirim email: {e}")

# Integrasi fitur notifikasi di dalam alur penilaian kelayakan makanan
if menu == "🧮 Penilaian Kelayakan Makanan":
    email_pengguna = st.text_input("📧 Masukkan Email Anda untuk Notifikasi", "")
    
    if st.button("🔎 Cek Kelayakan"):
        animation_effect()
        hari_ini = datetime.now().date()
        lama_simpan = (hari_ini - tanggal_input).days

        if tanggal_input > hari_ini:
            st.error("❗ Tanggal yang Anda masukkan tidak valid. Silakan masukkan tanggal yang logis.")
        else:
            if perubahan_fisik:
                st.error("❌ Makanan tidak layak dikonsumsi!")
                st.write("⚠️ *Perubahan fisik pada makanan menandakan kerusakan.*")
            else:
                batas_penyimpanan = {
                    "Daging 🍖": {"Freezer (-18°C) 🧊": 180, "Kulkas (0–4°C) ❄️": 3, "Suhu Ruang 🌡️": 1},
                    "Sayuran 🥦": {"Freezer (-18°C) 🧊": 12, "Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 2},
                    "Buah-buahan 🍎": {"Freezer (-18°C) 🧊": 30, "Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 3},
                    "Susu & Produk Olahan 🥛": {"Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 1},
                    "Roti & Kue 🍞": {"Kulkas (0–4°C) ❄️": 5, "Suhu Ruang 🌡️": 2},
                    "Makanan Kaleng 🥫": {"Suhu Ruang 🌡️": 365},
                    "Minuman 🥤": {"Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 3}
                }

                batas_hari = batas_penyimpanan.get(jenis_makanan, {}).get(kondisi_penyimpanan, 0)

                if lama_simpan > batas_hari:
                    st.error("❌ Makanan sudah tidak layak dikonsumsi.")
                elif (batas_hari - lama_simpan) <= 2:
                    st.warning(f"⚠️ Makanan hampir kedaluwarsa dalam {batas_hari - lama_simpan} hari!")
                    st.success("✅ Makanan masih layak dikonsumsi.")
                else:
                    st.success("✅ Makanan masih layak dikonsumsi.")
                    st.info(f"🗓️ Lama penyimpanan: {lama_simpan} hari dari batas {batas_hari} hari.")
                    
# --- Info ---
elif menu == "ℹ️ Info":
    st.title("ℹ️ Informasi Pembuat Aplikasi")
    st.markdown("""
    **Aplikasi ini dikembangkan oleh:**

    - 👩‍💻 **Azzahra Sadrina Nadzifa (2350080)**
    - 👩‍💻 **Dhyza Aulia Shabirah (2350084)**
    - 👩‍💻 **Diyah Theda Mufarrihah (2350085)** 
    - 👩‍💻 **Haija Nafiah (2350094)**
    - 👨‍💻 **Irsan Abdurrahman (2350100)**

    Dibuat dengan ❤️ oleh Kelompok 10

    D-IV Nanoteknologi Pangan
    
    Politeknik AKA Bogor
    """)


# --- Footer ---
st.markdown("---")
st.caption("🥗 *Dirancang untuk mendukung gaya hidup sehat dan aman setiap hari.*")