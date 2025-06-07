import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
# model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\best_model.pkl")
model = joblib.load(r"D:\Stress_Detection_Prediction-main\models\best_model.pkl")

# Title for the app
st.title("PSS Score Prediction")

# Description
st.write("""
This app predicts the Perceived Stress Scale (PSS) score based on input features. 
Adjust the sliders or input values below and click 'Predict' to see the result.
""")

# Define the input features
features = [
    'Openness', 'Conscientiousness', 'Extraversion',
    'Agreeableness', 'Neuroticism', 'sleep_time', 'wake_time',
    'sleep_duration', 'skin_conductance', 'mobility_radius'
]

# Create input fields for each feature
input_data = {}
input_data['Openness'] = st.slider("Openness", 1.0, 5.0, 3.0)
input_data['Conscientiousness'] = st.slider("Conscientiousness", 1.0, 5.0, 3.0)
input_data['Extraversion'] = st.slider("Extraversion", 1.0, 5.0, 3.0)
input_data['Agreeableness'] = st.slider("Agreeableness", 1.0, 5.0, 3.0)
input_data['Neuroticism'] = st.slider("Neuroticism", 1.0, 5.0, 3.0)
input_data['sleep_time'] = st.slider("Sleep Time (hours)", 6.0, 9.0, 7.0)
input_data['wake_time'] = st.slider("Wake Time (hours)", 5.0, 8.0, 6.5)
input_data['sleep_duration'] = st.slider("Sleep Duration (hours)", 6.0, 9.0, 7.5)
input_data['skin_conductance'] = st.slider("Skin Conductance", 0.5, 5.0, 1.5)
input_data['mobility_radius'] = st.slider("Mobility Radius", 0.1, 2.0, 1.0)

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.write(f"### Predicted PSS Score: {prediction[0]:.2f}")

    app.run(debug=True)