import streamlist as st

# Mengatur judul tab browser
st.set_page_config(page_title="Aplikasi Pertamamu", page_icon="+")

# Menampilkan judul dan teks di web
st.title("Aplikasi Steamlit Pertamaku!")
st.write("Halo duni! Jika kamu bisa melihat halaman ini, berarti kamu sudah **BERHASIL** Meng-upload dan mendeploy aplikasi Streamlit dari GitHub.")

st.divider() # Garis Pembatas

# Input sederhana
nama = st.text_input("Siapa namamu")

# Tombol interaktif
if st.button("Klik Saya!"):
    if nama:
        st.success(f"Halo, {nama}! Selamat belajar streamlit. Kamu hebat!")
        st.blloons() # Mmemunculkan animasi balon
    else:
        st.warning("Isi namamu dulu di kotak atas ya!")
