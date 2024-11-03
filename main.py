import streamlit as st
import requests

# API key and URL for real-time currency conversion
API_KEY = "3b8f5ebe58d36804ad0a4c70"  # Replace with your real API key
API_URL = "https://v6.exchangerate-api.com/v6/{}/latest/ILS".format(API_KEY)
ILS = 1

def get_TRY_value():
    API_KEY = "3b8f5ebe58d36804ad0a4c70"  # Replace with your real API key
    API_URL = "https://v6.exchangerate-api.com/v6/{}/latest/ILS".format(API_KEY)
    result = requests.get(url="https://v6.exchangerate-api.com/v6/{}/latest/ILS".format(API_KEY))
    TRY = float(result.json()['conversion_rates']['TRY'])
    return TRY


# אפליקציית Streamlit
st.title("ממיר מטבעות")

# שדות קלט
amount = st.number_input("הזן סכום:", min_value=0.0, step=0.01)
currency = st.selectbox("המר מ/אל:", ["שקל חדש ללירה טורקית", "לירה טורקית לשקל חדש"])

# לוגיקת המרה
if st.button("בצע המרה"):
    if currency == "שקל חדש ללירה טורקית":
        converted_amount = amount * get_TRY_value()
        st.write(f"{converted_amount:.2f} לירה טורקית")
    else:
        converted_amount = amount / get_TRY_value()
        st.write(f"{converted_amount:.2f} ש\"ח")
