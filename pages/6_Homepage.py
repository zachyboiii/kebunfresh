import streamlit as st
import pandas as pd

# Set page configuration


home, cart, prof = st.columns(3)
with home:
    st.button(':house:', key='home')
with cart:
    if st.button('🛒', key='cart'):
        st.switch_page('pages/7_Cart.py')
with prof:
    if st.button(':bust_in_silhouette:', key='profile'):
        st.switch_page('pages/4_Profile.py')
st.markdown("<hr>", unsafe_allow_html=True)

# Display location
st.subheader("📍**Lokasi Anda**")
location = st.text_input("Masukkan lokasi anda:", value="Petra Christian University")

if location:
    st.write(f"Lokasi saat ini: **{location}**")
else:
    st.write("Lokasi belum ditambahkan. Tambahkan lokasi.")

# Search bar and sorting dropdown
st.subheader("🔎 Search for Products")
col_search, col_sort = st.columns([3, 1])
with col_search:
    search_query = st.text_input("Masukkan nama produk, kategori, atau nama toko dalam pencarian:")
with col_sort:
    sort_option = st.selectbox(
        "Urutkan Berdasarkan:",
        options=["Jarak", "Harga", "Rating"],
        index=0,  # Default is "Distance"
    )

# Example market data (10 entries)
market_data = {
    "Nama Market": [
        'Farm A', 'Farm B', 'Farm C', 'Farm D', 'Farm E', 'Farm F', 'Farm G', 'Farm H', 'Farm I', 'Farm J'
    ],
    "Jarak (km)": [1.5, 2.0, 1.0, 2.5, 1.2, 3.0, 2.3, 1.8, 2.7, 1.4],
    "Nama Produk": ["Bayam", "Wortel", "Tomat", "Kentang", "Bayam", "Tomat", "Kentang", "Wortel", "Bayam", "Tomat"],
    "Harga (Rp)": [5000, 7000, 8000, 10000, 4500, 8500, 9000, 7500, 4800, 8200],
    "Ready": ["Sekarang", "Sekarang", "Dalam 2 bulan", "Dalam 1 bulan", "Sekarang", "Dalam 1 bulan", "Dalam 2 minggu", "Sekarang", "Sekarang", "Dalam 1 bulan"],
    "Gambar": [
        "https://akcdn.detik.net.id/visual/2018/07/11/cc01493c-6a04-4bea-b33d-3be0086c9f09_169.jpeg?w=650",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3zWb4BCP-FZVsUZFWPvjfXktU6PEYutg1UA&s",
        "https://res.cloudinary.com/dk0z4ums3/image/upload/v1629681328/attached_image/9-manfaat-tomat-buah-yang-disangka-sayur.jpg",
        "https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/30033712/Tak-Hanya-Meningkatkan-Fungsi-Otak-Ini-11-Manfaat-kentang-untuk-Kesehatan.jpg.webp",
        "https://akcdn.detik.net.id/visual/2018/07/11/cc01493c-6a04-4bea-b33d-3be0086c9f09_169.jpeg?w=650",
        "https://res.cloudinary.com/dk0z4ums3/image/upload/v1629681328/attached_image/9-manfaat-tomat-buah-yang-disangka-sayur.jpg",
        "https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/30033712/Tak-Hanya-Meningkatkan-Fungsi-Otak-Ini-11-Manfaat-kentang-untuk-Kesehatan.jpg.webp",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3zWb4BCP-FZVsUZFWPvjfXktU6PEYutg1UA&s",
        "https://akcdn.detik.net.id/visual/2018/07/11/cc01493c-6a04-4bea-b33d-3be0086c9f09_169.jpeg?w=650",
        "https://res.cloudinary.com/dk0z4ums3/image/upload/v1629681328/attached_image/9-manfaat-tomat-buah-yang-disangka-sayur.jpg",
    ],
    "Rating": [4.5, 4.0, 4.8, 4.2, 4.6, 4.1, 4.3, 4.0, 4.7, 4.4],
    "Kategori": ["Sayuran Hijau", "Umbi-umbian", "Buah", "Umbi-umbian", "Sayuran Hijau", "Buah", "Umbi-umbian", "Umbi-umbian", "Sayuran Hijau", "Buah"],
}

market_df = pd.DataFrame(market_data)

# Filter products based on search query
if search_query:
    filtered_df = market_df[
        market_df["Nama Produk"].str.contains(search_query, case=False, na=False) |
        market_df["Kategori"].str.contains(search_query, case=False, na=False) |
        market_df["Nama Market"].str.contains(search_query, case=False, na=False)
    ]
else:
    filtered_df = market_df.copy()  # Copy to avoid modifying the original DataFrame

# Apply sorting to the filtered DataFrame
if sort_option == "Distance":
    filtered_df = filtered_df.sort_values("Jarak (km)")
elif sort_option == "Price":
    filtered_df = filtered_df.sort_values("Harga (Rp)")
elif sort_option == "Rating":
    filtered_df = filtered_df.sort_values("Rating", ascending=False)

# Display product cards with buttons
for _, row in filtered_df.iterrows():
    with st.container():
        col1, col2 = st.columns([1, 3])

        # Add an image for the product
        with col1:
            st.image(row["Gambar"], width=150, caption=row["Nama Produk"])

        # Add product details
        with col2:
            st.subheader(f"{row['Nama Market']} ⭐ {row['Rating']}")
            st.write(f"📍 Lokasi: {row['Jarak (km)']} km")
            st.write(f"📦 Produk: {row['Nama Produk']} ({row['Kategori']})")
            st.write(f"💰 Harga: Rp {row['Harga (Rp)']:,}/gram")
            if row['Ready'] == 'Sekarang':
                st.write(f"🕒 Ready: :green[{row['Ready']}]")
            else:
                st.write(f"🕒 Ready: {row['Ready']}")

            # Add buttons
            button_col1, button_col2 = st.columns(2)
            with button_col1:
                if st.button("Tambahkan ke Daftar Keinginan", key=f"wishlist_{row['Nama Market']}"):
                    st.success(f"Produk Berhasil Ditambahkan ke Keranjang!")
            with button_col2:
                if st.button("Detail Kebun", key=f"farmdetails_{row['Nama Market']}"):
                    #st.info(f"Details for {row['Nama Market']} coming soon!")
                    st.switch_page("pages/5_FarmPage.py")  
