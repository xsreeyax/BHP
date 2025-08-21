import streamlit as st
import pandas as pd
import pickle

# Load model
with open("RidgeModel.pkl", "rb") as f:
    pipe = pickle.load(f)

st.title("🏠 Bengaluru House Price Predictor")

# Inputs
location = st.text_input("Location")
sqft = st.number_input("Total Sqft", min_value=200.0, max_value=20000.0, value=1000.0, step=10.0)
bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)
bhk = st.number_input("BHK", min_value=1, max_value=10, value=2, step=1)

# Prediction
if st.button("Predict Price"):
    input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                             columns=['location', 'total_sqft', 'bath', 'bhk'])
    price = pipe.predict(input_df)[0]
    st.success(f"Estimated Price: ₹ {price:,.2f} Lakhs")
