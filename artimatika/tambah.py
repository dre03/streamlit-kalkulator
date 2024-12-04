import streamlit as st

st.write('Hitung Penjumlahan')

with st.form('penjumalahn'):
    angka1 = st.number_input(f'Angka ke satu:', format="%f")
    angka2 = st.number_input(f'Angka ke dua:', format="%f")
    submit = st.form_submit_button('Hasil')
    # Tombol untuk menghitung
    if submit:
        is_angka1_int = angka1 % 1 == 0
        is_angka2_int = angka2 % 1 == 0
        if is_angka1_int and is_angka2_int:
            hitung = int(angka1) + int(angka2)
            st.success(f"Hasil perhitungan dari {int(angka1)} + {int(angka2)} = {int(hitung)}")
        elif is_angka1_int == False and is_angka2_int == False:
            hitung = angka1 + angka2
            st.success(f"Hasil perhitungan dari {angka1} + {angka2} = {hitung}")
        elif is_angka1_int == True and is_angka2_int == False:
            hitung = int(angka1) + angka2
            st.success(f"Hasil perhitungan dari {int(angka1)} + {angka2} = {hitung}")
        elif is_angka1_int == False and is_angka2_int == True:
            hitung = angka1 + int(angka2)
            st.success(f"Hasil perhitungan dari {angka1} + {int(angka2)} = {hitung}")
        