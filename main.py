import streamlit as st
import requests

# API key and URL for real-time currency conversion
API_KEY = "3b8f5ebe58d36804ad0a4c70"  # Replace with your real API key
API_URL = "https://v6.exchangerate-api.com/v6/{}/latest/ILS".format(API_KEY)

def get_try_to_ils_rate():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return float(response.json()['conversion_rates']['TRY'])
    except Exception as e:
        st.error(f"Error fetching exchange rate: {e}")
        return 0.0

# Streamlit application
st.title("ממיר מטבעות")

# Input fields
amount = st.number_input("הזן סכום בלירה טורקית:", min_value=0.0, step=0.01, format="%g", value=None)

# Conversion logic
if st.button("המר"):
    try_to_ils_rate = get_try_to_ils_rate()
    converted_amount = amount / try_to_ils_rate
    st.write(f"{converted_amount:.2f} ש\"ח")
