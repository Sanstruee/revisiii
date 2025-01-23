import streamlit as st
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(page_title="Food Freshness App", page_icon="🍎", layout="wide")

# Beranda
st.title("🍎 FRESH CHECK - Pendeteksi Kelayakan Konsumsi Makanan")

# Gambar lebih menarik mencakup semua kategori makanan
st.image("https://png.pngtree.com/png-clipart/20220125/original/pngtree-nut-food-png-image_7222167.png", width=700)

# Deskripsi aplikasi
st.markdown("""
### 🌟 Selamat Datang di **Pendeteksi Kelayakan Konsumsi Makanan**!  
Aplikasi ini dirancang untuk membantu Anda mengonsumsi makanan yang **sehat** dan **aman** dengan fitur-fitur menarik berikut:

- 📅 **Pengecekan Tanggal Kedaluwarsa**: Pantau masa simpan makanan agar tetap aman.  
- 🔍 **Penilaian Kelayakan Makanan**: Evaluasi apakah makanan masih layak dikonsumsi.
""")

st.markdown("---")

# Penilaian Kelayakan Makanan
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

if st.button("🔎 Cek Kelayakan"):
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

# Informasi Pembuat Aplikasi
st.markdown("---")
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

st.markdown("---")
st.caption("🥗 *Dirancang untuk mendukung gaya hidup sehat dan aman setiap hari.*")
