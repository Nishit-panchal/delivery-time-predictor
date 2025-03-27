import streamlit as st
import datetime

def predict_delivery_time(product_category, customer_location, shipping_method):
    base_time = 2  # Base delivery time in days
    
    if shipping_method == "Express":
        base_time -= 1
    elif shipping_method == "Standard":
        base_time += 2
    
    if customer_location == "Remote":
        base_time += 3
    
    return datetime.date.today() + datetime.timedelta(days=base_time)

st.title("Delivery Time Prediction App")

product_category = st.selectbox("Select Product Category:", ["Electronics", "Clothing", "Groceries", "Other"])
customer_location = st.selectbox("Select Customer Location:", ["Urban", "Suburban", "Remote"])
shipping_method = st.selectbox("Select Shipping Method:", ["Express", "Standard", "Economy"])

if st.button("Predict Delivery Time"):
    predicted_date = predict_delivery_time(product_category, customer_location, shipping_method)
    st.success(f"Expected Delivery Date: {predicted_date}")


