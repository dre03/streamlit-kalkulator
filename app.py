import streamlit as st

st.header("Andre :blue[Apriyana] :sunglasses:")
st.title("Aplikasi Kalkulator Sederhana")

tambah = st.Page("./artimatika/tambah.py", title="Penambahan")
kurang = st.Page("./artimatika/kurang.py", title="Pengurangan",)
bagi = st.Page("./artimatika/bagi.py", title="Pembagian")
kali = st.Page("./artimatika/kali.py", title="Perkalian")

pg = st.navigation({"Menu Utama":[tambah,kurang,bagi,kali]})
print(type(pg))
pg.run()