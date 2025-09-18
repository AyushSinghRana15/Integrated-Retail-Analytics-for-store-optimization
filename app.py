import streamlit as st
import pandas as pd
import joblib

# Load your trained model (update path to your actual file)
model = joblib.load('best_sales_forecasting_model.joblib')

# Default values for the features
defaults = {
    'Temperature': 70.0,
    'Fuel_Price': 3.0,
    'Total_MarkDown': 0.0,
    'CPI': 200.0,
    'Unemployment': 7.0,
    'IsHoliday': 0,
    'Type': 'A',
    'Size': 100000,
    'Month': 1,
    'Week': 1,
    'Year': 2023
}

st.title("Sales Forecast")

# Input widgets for each feature
Temperature = st.number_input("Temperature (F)", value=defaults['Temperature'])
Fuel_Price = st.number_input("Fuel Price ($)", value=defaults['Fuel_Price'])
Total_MarkDown = st.number_input("Total MarkDown ($)", value=defaults['Total_MarkDown'])
CPI = st.number_input("CPI", value=defaults['CPI'])
Unemployment = st.number_input("Unemployment rate (%)", value=defaults['Unemployment'])
IsHoliday = st.selectbox("Is Holiday?", options=[0, 1], index=defaults['IsHoliday'])
Type = st.selectbox("Store Type", options=['A', 'B', 'C'], index=['A','B','C'].index(defaults['Type']))
Size = st.number_input("Store Size (sqft)", value=defaults['Size'])
Month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=defaults['Month'])
Week = st.number_input("Week (1-53)", min_value=1, max_value=53, value=defaults['Week'])
Year = st.number_input("Year", min_value=2000, max_value=2100, value=defaults['Year'])

if st.button("Predict Sales"):
    # Prepare input DataFrame
    input_data = pd.DataFrame([{
        'Temperature': Temperature,
        'Fuel_Price': Fuel_Price,
        'Total_MarkDown': Total_MarkDown,
        'CPI': CPI,
        'Unemployment': Unemployment,
        'IsHoliday': IsHoliday,
        'Type': Type,
        'Size': Size,
        'Month': Month,
        'Week': Week,
        'Year': Year
    }])
    input_data['Type'] = input_data['Type'].astype('category').cat.codes

    # If your model needs encoding for 'Type' do it here; for now assuming label encoding was done
    # For example:
    # input_data['Type'] = input_data['Type'].map({'A':0, 'B':1, 'C':2})

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")
