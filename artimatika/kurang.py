import streamlit as st

st.write("Hitung Pengurangan")
with st.form('pengurangan'):
    angka1 = st.number_input(f'Angka ke satu:', format="%f")
    angka2 = st.number_input(f'Angka ke dua:', format="%f")
    submit = st.form_submit_button('Hasil')
    # kondisi Tombol untuk menghitung
    if submit:
        hitung = angka1 - angka2
        st.success(f"Hasil perhitungan dari {int(angka1)} - {int(angka2)} = {int(hitung)}")