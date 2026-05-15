import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("sales_model.pkl", "rb"))

product_map = {
    "Printer": 0,
    "Mouse": 1,
    "Tablet": 2,
    "Camera": 3,
    "Headphones": 4,
    "Smartwatch": 5,
    "Monitor": 6,
    "Smartphone": 7,
    "Keyboard": 8,
    "Laptop": 9
}

category_map = {
    "Office": 0,
    "Accessories": 1,
    "Electronics": 2
}

region_map = {
    "North": 0,
    "East": 1,
    "South": 2,
    "West": 3
}

st.set_page_config(
    page_title="Ecommerce Sales Predictor",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Ecommerce Sales Predictor")
st.write("Predict ecommerce sales using machine learning")

product = st.selectbox("Select Product", list(product_map.keys()))
category = st.selectbox("Select Category", list(category_map.keys()))
region = st.selectbox("Select Region", list(region_map.keys()))

quantity = st.number_input("Quantity", min_value=1, step=1)
year = st.number_input("Year", min_value=2020, max_value=2035, step=1)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
day = st.number_input("Day", min_value=1, max_value=31, step=1)

if st.button("Predict Sales 🚀"):
    features = np.array([[
        product_map[product],
        category_map[category],
        region_map[region],
        quantity,
        year,
        month,
        day
    ]])

    prediction = model.predict(features)

    st.success(f"🎉 Predicted Sales: ₹ {prediction[0]:.2f}")
    st.balloons()