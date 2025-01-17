import streamlit as st
import pandas as pd
import time

# ------------------ Header ------------------

home, cart, prof = st.columns(3)
with home:
    if st.button(':house:', key='home'):
        st.switch_page('pages/6_Homepage.py')
with cart:
    st.button('🛒', key='cart')

with prof:
    if st.button(':bust_in_silhouette:', key='profile'):
        st.switch_page('pages/4_Profile.py')
st.markdown("<hr>", unsafe_allow_html=True)

st.title("Keranjang Belanja🛒💨")

product_data = {
    "Nama Farm": ["FARM A", "FARM A", "FARM C", "FARM D"],
    "Nama Produk": ["Bayam", "Wortel", "Tomat", "Kentang"],
    "Harga (Rp)": [5000, 7000, 8000, 10000],
    "Ready": ["Sekarang", "Sekarang", "Dalam 2 bulan", "Dalam 1 bulan"],
    "Gambar": [
        "https://akcdn.detik.net.id/visual/2018/07/11/cc01493c-6a04-4bea-b33d-3be0086c9f09_169.jpeg?w=650",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3zWb4BCP-FZVsUZFWPvjfXktU6PEYutg1UA&s",
        "https://res.cloudinary.com/dk0z4ums3/image/upload/v1629681328/attached_image/9-manfaat-tomat-buah-yang-disangka-sayur.jpg",
        "https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/30033712/Tak-Hanya-Meningkatkan-Fungsi-Otak-Ini-11-Manfaat-kentang-untuk-Kesehatan.jpg.webp",
    ],
}



product_df = pd.DataFrame(product_data)

# Initialize session state for quantities and selected products
if "quantities" not in st.session_state:
    st.session_state["quantities"] = [0] * len(product_df)
    st.session_state["selected"] = [False] * len(product_df)  # To track selected products

# ------------------ Products Cards ------------------

st.header("Jangan Lupa Beli :smile:")

# Group products by farm
grouped = product_df.groupby("Nama Farm")

total_all_farms = 0  # To store total of all farms

for farm, group in grouped:
    st.markdown(f"""
        <h3 style="color: white; font-weight:bold;">{farm}</h3>
    """, unsafe_allow_html=True)

    # Initialize farm total
    total_farm = 0

    with st.container():
        for index, row in group.iterrows():
            ready_color = 'green' if row['Ready'] == 'Sekarang' else 'white'
            st.markdown(f"""
            <div style="border: 2px solid white; padding: 15px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 15px; display: grid; grid-template-columns: 1fr 2fr; gap: 20px;">
                <div style="text-align: center;">
                    <img src="{row['Gambar']}" alt="{row['Nama Produk']}" style="width: 100%; border-radius: 8px;">
                </div>
                <div style="color: white;">
                    <h4>{row['Nama Produk']}</h4>
                    <p><strong>💰 Harga:</strong> Rp {row['Harga (Rp)']:,}/gram</p>
                    <p><strong>🕒 Ready:</strong> <span style="color: {ready_color};">{row['Ready']}</span></p>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Checkbox for selecting product
            selected = st.checkbox(f"Pilih {row['Nama Produk']}", key=f"checkbox_{index}")
            st.session_state["selected"][index] = selected  

            # Show quantity input only if the product is selected
            if selected:
                st.session_state["quantities"][index] = st.number_input(
                    f"Jumlah untuk {row['Nama Produk']}",
                    min_value=0,
                    max_value=1000,
                    value=st.session_state["quantities"][index],
                    step=1,
                    key=f"quantity_input_{index}"
                )

                # Calculate total for this product and add to the farm's total
                quantity = st.session_state["quantities"][index]
                price = row["Harga (Rp)"] * quantity
                total_farm += price

        # Show farm total if there are selected products
        if total_farm > 0:
            st.write(f"Total untuk {farm}: Rp {total_farm:,}")

    # Update the total for all farms
    total_all_farms += total_farm

    st.markdown("</div>", unsafe_allow_html=True)  

def checkout():
    with st.spinner("Memproses pesanan anda..."):
        time.sleep(2)  # Simulate order processing time

    # Order success message with custom CSS to center it
    st.markdown("""
    <style>
        .success-message {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 128, 0, 0.8);
            color: white;
            padding: 20px 40px;
            border-radius: 10px;
            font-size: 24px;
            z-index: 9999;
        }
        .back-btn {
            position: fixed;
            top: 60%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
            z-index: 9999;
        }
    </style>
    """, unsafe_allow_html=True)

    # Show the success message
    st.markdown('<div class="success-message">Order Sukses! ✅</div>', unsafe_allow_html=True)
    
    # Show the back to home button
    if st.button('Kembali ke Halaman Utama', key='backhome'):
        st.switch_page('pages/6_Homepage.py')

if st.button("Checkout 🛒"):
    if total_all_farms > 0:
        checkout()
    else:
        st.warning("Pilih minimal 1 produk untuk di-check out.")

# ------------------ Checkout Button ------------------

# st.markdown(
#     """
#     <style>
#     .stButton > button {
#         position: fixed;
#         bottom: 20px;
#         right: 20px;
#         background-color: #4CAF50;
#         color: white;
#         border: none;
#         padding: 15px 32px;
#         text-align: center;
#         font-size: 16px;
#         cursor: pointer;
#         border-radius: 10px;
#     }

#     .modal {
#         display: none;
#         position: fixed;
#         z-index: 1000;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background-color: rgba(0,0,0,0.4);
#         padding-top: 60px;
#         text-align: center;
#         animation: fadeIn 0.5s ease;
#     }

#     .modal-content {
#         background-color: #fefefe;
#         margin: 10% auto;
#         padding: 40px;
#         border: 1px solid #888;
#         width: 40%;
#         border-radius: 8px;
#         text-align: center;
#         box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
#     }

#     .modal-content h2 {
#         color: #4CAF50;
#     }

#     .close {
#         color: #aaa;
#         font-size: 28px;
#         font-weight: bold;
#         float: right;
#         cursor: pointer;
#     }

#     .close:hover,
#     .close:focus {
#         color: black;
#         text-decoration: none;
#     }

#     @keyframes fadeIn {
#         from { opacity: 0; }
#         to { opacity: 1; }
#     }

#     .modal .spinner {
#         animation: spin 2s linear infinite;
#     }

#     @keyframes spin {
#         from { transform: rotate(0deg); }
#         to { transform: rotate(360deg); }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Show modal popup after checkout
# if st.button("Checkout 🛒"):
#     if total_all_farms > 0:
#         with st.empty():
#             modal = st.empty()  
#             modal.markdown("""
#             <div class="modal" style="display:block;">
#                 <div class="modal-content">
#                     <span class="close" onclick="document.getElementById('modal').style.display='none'">&times;</span>
#                     <h2>Processing Your Order...</h2>
#                     <p>We're waiting for your payment...</p>
#                     <div class="spinner">
#                         <img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif" width="50" height="50" />
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#             time.sleep(2)

#             # Once loading is complete, show success modal
#             modal.markdown("""
#             <div class="modal" style="display:block;">
#                 <div class="modal-content">
#                     <span class="close" onclick="document.getElementById('modal').style.display='none'">&times;</span>
#                     <h2 style="color: #4CAF50;">Order Success! ✅</h2>
#                     <p style="color: black;">Your order has been processed successfully.</p>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
        


#     else:
#         st.warning("Please select at least one product to checkout.")