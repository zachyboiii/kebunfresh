import streamlit as st


st.markdown('<h1>Hello!</h1>',unsafe_allow_html=True)
st.markdown('<h3>Apakah anda seorang...?</h3>',unsafe_allow_html=True)
buyer, seller = st.columns(2)

with buyer:
    if st.button('🛒\nPembeli', key='buyer'):
        st.switch_page('pages/2_Login.py')

with seller:
    if st.button('🧑‍🌾\nPenjual', key='seller'):
        st.warning("Halaman penjual tidak tersedia saat ini.")
