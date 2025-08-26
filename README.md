Bengaluru House Price Predictor

An ML model that generally calculates the house price in Bengaluru depending on location, square feet, number of bathrooms, and BHK. 


How it works:

1.Data Preprocessing-
Remove outliers in price per square foot from the dataset for cleaning
Standardize numerical features (total_sqft, bath, bhk)
One-hot encode the location column for model input

2.Model Training-
Perform Ridge Regression on house price prediction
Combine preprocessing + model into a single Pipeline from scikit-learn
Train and save model in compressed .pkl format for Deployment

3.Prediction Workflow-
User selects location and enters property details in the Streamlit app
Input is transformed by the same preprocessing pipeline that was fit during training
Model outputs predicted price in Lakhs


Key Highlights:

-Dropdown for location — no typos in input

-Complete content-based prediction (no external APIs)

-Model + Preprocessing packaged together for easy deployment

-Lightweight and fast — runs in realtime on Streamlit Cloud



Technologies Used

Python 3.x

scikit-learn – for preprocessing & Ridge Regression

pandas – for data cleaning & transformation

numpy – for numerical operations

Streamlit – for interactive web app UI
