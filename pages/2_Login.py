import streamlit as st


st.markdown('<h1>Halaman Masuk</h1>',unsafe_allow_html=True)
st.text_input('Nama   :red[*]')
st.text_input('Kata Sandi  :red[*]')
if st.button('Masuk', key = 'loginn'):
        st.switch_page('pages/6_Homepage.py')
st.markdown('<p style="text-align: left;">Belum punya akun?</p>',unsafe_allow_html=True)
if st.button('Daftar', key='signup'):
        st.switch_page('pages/3_SignUp.py')