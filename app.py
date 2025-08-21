import streamlit as st
import pandas as pd
import pickle

import streamlit as st
import pandas as pd
import pickle

# Load model
with open("RidgeModel.pkl", "rb") as f:
    pipe = pickle.load(f)

# Try to get known locations from the model
def get_locations_from_pipeline(pipeline):
    try:
        # 'preprocess' step is a ColumnTransformer
        ohe = pipeline.named_steps['preprocess'].named_transformers_['cat']
        return list(ohe.categories_[0])
    except Exception as e:
        st.warning(f"Could not extract locations from model: {e}")
        return []

import json
with open("locations.json", "r") as f:
    locations_list = json.load(f)


st.title("🏠 Bengaluru House Price Predictor")

# Dropdown for location
if locations_list:
    location = st.selectbox("Location", sorted(locations_list))
else:
    location = st.text_input("Location")  # fallback if list can't be loaded

sqft = st.number_input("Total Sqft", min_value=200.0, max_value=20000.0, value=1000.0, step=10.0)
bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)
bhk = st.number_input("BHK", min_value=1, max_value=10, value=2, step=1)

# Prediction
if st.button("Predict Price"):
    input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                            columns=['location', 'total_sqft', 'bath', 'bhk'])
    price = pipe.predict(input_df)[0]
    st.success(f"Estimated Price: ₹ {price:,.2f} Lakhs")

