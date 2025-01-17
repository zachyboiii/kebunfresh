import streamlit as st

st.set_page_config(page_title="KebunFresh", page_icon="🌿", layout="wide")
pages = {
    "Login": [
        st.Page('pages/1_Hero.py'),
        st.Page('pages/2_Login.py'),
        st.Page('pages/3_SignUp.py')
    ],
    "App Nav Bar": [
        st.Page('pages/4_Profile.py'),
        st.Page('pages/6_Homepage.py'),
        st.Page('pages/7_Cart.py')
    ],
    "Other pages":[
        st.Page('pages/5_FarmPage.py')
    ]
}
pg = st.navigation(pages)
pg.run()