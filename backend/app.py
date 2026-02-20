import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Big Mart Sales Prediction")

st.title("🛒 Big Mart Sales Prediction")

# Load full pipeline model
model = pickle.load(open("ml_model3.pkl", "rb"))

# User Inputs
product_id = st.text_input("Product ID")
weight = st.number_input("Weight")
fat_content = st.selectbox("Fat Content", ["Low Fat", "Regular"])
product_visibility = st.number_input("Product Visibility")
product_type = st.text_input("Product Type")
mrp = st.number_input("MRP")
outlet_id = st.text_input("Outlet ID")
establishment_year = st.number_input("Establishment Year")
outlet_size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
location_type = st.selectbox("Location Type", ["Tier 1", "Tier 2", "Tier 3"])
outlet_type = st.selectbox(
    "Outlet Type",
    ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"]
)

input_df = pd.DataFrame({
    "ProductID": [product_id],
    "Weight": [weight],
    "FatContent": [fat_content],
    "ProductVisibility": [product_visibility],
    "ProductType": [product_type],
    "MRP": [mrp],
    "OutletID": [outlet_id],
    "EstablishmentYear": [establishment_year],
    "OutletSize": [outlet_size],
    "LocationType": [location_type],
    "OutletType": [outlet_type]
})

if st.button("Predict Sales"):
    prediction = model.predict(input_df)
    st.success(f"💰 Predicted Sales: ₹ {prediction[0]:.2f}")