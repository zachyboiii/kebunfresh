import streamlit as st

st.markdown('<h1>Pendaftaran</h1>',unsafe_allow_html=True)
st.text_input('Nama   :red[*]')
st.text_input('Nomor Telefon  :red[*]')
st.text_input('Alamat   :red[*]')
st.text_input('Email')
st.text_input('Kata Sandi   :red[*]')
st.text_input('Konfirmari Kata Sandi  :red[*]')
if st.button('Daftar', key='signup'):
        st.switch_page('pages/2_Login.py')