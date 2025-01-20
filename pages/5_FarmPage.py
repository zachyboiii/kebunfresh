import streamlit as st
from classes import a

# ------------------ Header ------------------

home, cart, prof = st.columns(3)
with home:
    if st.button(':house:', key='home'):
        st.switch_page('pages/6_Homepage.py')
with cart:
    if st.button('🛒', key='cart'):
        st.switch_page('pages/7_Cart.py')
with prof:
    if st.button(':bust_in_silhouette:', key='profile'):
        st.switch_page('pages/4_Profile.py')
st.markdown("<hr>", unsafe_allow_html=True)
st.title("Profil Farm A 🥦")

# ------------------ Store Profile Information ------------------

# Store information
store_name = "Farm A"
store_description = "Kami menyediakan berbagai macam sayuran segar dan sehat langsung dari petani lokal."
contact_info = "email@tokosayur.com"
store_address = "Jalan Gunung Anyar No. 123, Surabaya, Indonesia"

# ------------------ Display Store Profile ------------------

st.header(f"📋 {store_name}")
st.write(f"**Deskripsi Toko:** {store_description}")
st.write(f"**Kontak:** {contact_info}")
st.markdown('**Nomor Telefon:** [+62 811-3110-511](https://wa.me/628113110511)')
st.write(f"**Alamat:** {store_address}")


# ------------------ Display Products as Cards ------------------

st.header("📦 Katalog Produk")

# Create a row for each product and display it as a card
for veg in a.prod_dict.values():
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(veg.img, width=150)
        with cols[1]:
            st.subheader(veg.name)
            st.write(f"**💰 Harga:** Rp {veg.price:,}/gram")
            if veg.readytime == 'Sekarang':
                st.write(f'**🕒 Ready:** :green[{veg.readytime}]')
            else:
                st.write(f'**🕒 Ready:** {veg.readytime}')
            if st.button("🛒", key = veg.name):
                st.success('_Ditambah ke Keranjang._')
    st.markdown("---")

