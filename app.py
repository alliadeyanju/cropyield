
import streamlit as st
import pandas as pd
import numpy as np
import joblib

import joblib

# Define the Streamlit app code string
# We use standard quotes for the inner markdown to avoid syntax errors with nested triple quotes
app_code = """
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the saved pipeline (which includes preprocessing)
try:
    model = joblib.load('random_forest_model.pkl')
except FileNotFoundError:
    st.error("Model file 'random_forest_model.pkl' not found. Please ensure it is in the same directory as app.py.")

st.set_page_config(page_title='Crop Yield Predictor', page_icon='🌾')
st.title('🌾 Global Crop Yield Prediction')

st.markdown('This application uses a Machine Learning model (Random Forest) to predict agricultural yield based on historical environmental and geographic data.')

# Sidebar for inputs
st.sidebar.header('Input Parameters')

def user_input_features():
    area = st.sidebar.text_input('Country/Area', 'India')
    item = st.sidebar.selectbox('Crop Item', ['Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans', 'Wheat', 'Cassava', 'Sweet potatoes', 'Plantains', 'Yams'])
    year = st.sidebar.slider('Year', 1990, 2030, 2024)
    rainfall = st.sidebar.number_input('Average Rainfall (mm/year)', 0.0, 10000.0, 1100.0)
    pesticides = st.sidebar.number_input('Pesticides (tonnes)', 0.0, 1000000.0, 75000.0)
    temp = st.sidebar.number_input('Average Temperature (°C)', -10.0, 50.0, 24.5)
    
    data = {
        'Area': area,
        'Item': item,
        'Year': year,
        'average_rain_fall_mm_per_year': rainfall,
        'pesticides_tonnes': pesticides,
        'avg_temp': temp
    }
    return pd.DataFrame([data])

input_df = user_input_features()

st.subheader('User Input parameters')
st.write(input_df)

if st.button('Predict Yield'):
    prediction = model.predict(input_df)[0]
    st.subheader('Prediction')
    st.success(f'Estimated Crop Yield: {prediction:,.2f} hg/ha')

st.info("Note: The model was trained on historical FAO and World Bank data.")
"""

# Write the string to app.py
with open('app.py', 'w') as f:
    f.write(app_code.strip())

print("app.py has been successfully generated for Streamlit deployment.")
# Load the best pipeline (includes preprocessor and model)
model = joblib.load('random_forest_model.pkl')

st.set_page_config(page_title='Crop Yield Predictor', page_icon='🌾')
st.title('🌾 Global Crop Yield Prediction')

st.markdown('This app predicts agricultural yield based on environmental factors.')

# Create input fields based on dataset features
col1, col2 = st.columns(2)

with col1:
    area = st.text_input('Country/Area', 'India')
    item = st.text_input('Crop Item', 'Maize')
    year = st.number_input('Year', 1990, 2030, 2024)

with col2:
    rainfall = st.number_input('Average Rainfall (mm/year)', 0.0, 10000.0, 1000.0)
    pesticides = st.number_input('Pesticides (tonnes)', 0.0, 1000000.0, 100.0)
    temp = st.number_input('Average Temperature (°C)', -10.0, 50.0, 25.0)

if st.button('Predict Yield'):
    # Create a dataframe for the model
    input_data = pd.DataFrame([[
        area, item, year, rainfall, pesticides, temp
    ]], columns=['Area', 'Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'])

    prediction = model.predict(input_data)[0]
    st.success(f'Estimated Yield: {prediction:,.2f} hg/ha')
