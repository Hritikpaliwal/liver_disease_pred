# frontend.py

import streamlit as st
import requests

# Define input fields
st.title('Liver Disease Prediction')

age = st.number_input('Age of the patient', min_value=0, max_value=150, value=25)
gender = st.selectbox('Gender of the patient', ['Male', 'Female'])
total_bilirubin = st.number_input('Total Bilirubin', min_value=0.2, max_value=10.0, value=0.5)
direct_bilirubin = st.number_input('Direct Bilirubin', min_value=0.0, max_value=1.0, value=0.1)
alkaline_phosphatase = st.number_input('Alkaline Phosphatase', min_value=0.2, max_value=10.0, value=0.5)
alanine_aminotransferase = st.number_input('Alanine Aminotransferase', min_value=7, max_value=1000, value=20)
aspartate_aminotransferase = st.number_input('Aspartate Aminotransferase', min_value=7, max_value=1000, value=25)
total_proteins = st.number_input('Total Proteins', min_value=6.0, max_value=10.0, value=7.0)
albumin = st.number_input('Albumin', min_value=3.0, max_value=6.0, value=4.0)
albumin_and_globulin_ratio = st.number_input('Albumin and Globulin Ratio', min_value=0.5, max_value=2.0, value=1.0)

# Convert gender to string
gender_str = 'Male' if gender == 'Male' else 'Female'

# Create payload
payload = {
    "Age_of_the_patient": age,
    "Gender_of_the_patient": gender_str,
    "Total_Bilirubin": total_bilirubin,
    "Direct_Bilirubin": direct_bilirubin,
    "Alkaline_Phosphatase": alkaline_phosphatase,
    "Alanine_Aminotransferase": alanine_aminotransferase,
    "Aspartate_Aminotransferase": aspartate_aminotransferase,
    "Total_Proteins": total_proteins,
    "Albumin": albumin,
    "Albumin_and_Globulin_Ratio": albumin_and_globulin_ratio
}

# Make prediction request
if st.button('Predict'):
    response = requests.post("http://localhost:8000/predict", json=payload)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        if prediction == 1:
            st.write('Prediction: Patient has liver disease')
        else:
            st.write('Prediction: Patient does not have liver disease')
    else:
        st.write('Error:', response.text)
