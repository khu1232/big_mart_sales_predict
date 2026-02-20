import streamlit as st
import pickle 
import numpy as np 
import pandas as pd

st.set_page_config(page_title="BIG MART SALES PRICE PREDICATION")

st.title("BIG MART SALES PRICE PREDICATION")
st.write("This is a web application that predicts the sales price of a product based on its features. The model used for prediction is a Random Forest Regressor, which has been trained on a dataset of sales data from Big Mart.")

model = pickle.load(open('ml_model.pkl','rb'))

item_weight = st.number_input("Enter the weight of the item(in gms):")
item_visibility = st.number_input("Enter the visibility of the item:")
item_mrp = st.number_input("Enter the MRP of the item:")

item_fat_content = st.selectbox("FAT CONTENT",['Low Fat','Regular'])


item_outlet_size = st.selectbox("OUTLET SIZE",['Small','Medium','High'])

item_outlet_location_type = st.selectbox("OUTLET LOCATION TYPE",['Tier 1','Tier 2','Tier 3'])

item_outlet_type = st.selectbox("OUTLET TYPE",['Grocery Store','Supermarket Type1','Supermarket Type2','Supermarket Type3'])

fat_map = {"Low Fat": 0, "Regular": 1}
size_map = {"Small": 0, "Medium": 1, "High": 2}
location_map = {"Tier 1": 0, "Tier 2": 1, "Tier 3": 2}
type_map = {
    "Grocery Store": 0,
    "Supermarket Type1": 1,
    "Supermarket Type2": 2,
    "Supermarket Type3": 3
}


input_array = ([[
item_weight,
item_visibility,
item_mrp,
fat_map[item_fat_content],
size_map[item_outlet_size],
location_map[item_outlet_location_type],
type_map[item_outlet_type]

]])

if st.button("Predict Sales Price"):
     prediction = model.predict(input_array)
     st.success(f"The predicted sales price is: {prediction[0]}")