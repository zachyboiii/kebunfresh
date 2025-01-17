import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
    if st.button(':house:', key='home'):
        st.switch_page('pages/6_Homepage.py')
with col2:
    if st.button('🛒', key='cart'):
        st.switch_page('pages/7_Cart.py')
with col3:
    st.button(':bust_in_silhouette:', key='profile')
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<h1>Profil Saya</h1>',unsafe_allow_html=True)

st.text_area('Nama','Siti',height= 68)
st.text_area('Nomor Telefon','+62 xxxx',height= 68)
st.text_area('Email','siti123@gmail.com',height= 68)
st.text_area('Alamat','Jl. Siwalankerto No.121-131, Siwalankerto, Kec. Wonocolo, Surabaya, Jawa Timur 60236',height= 68)
st.button('Upah Profil', key='editting')
