
import streamlit as st
import pandas as pd
import numpy as np
import joblib


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
