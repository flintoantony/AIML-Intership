import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("gender_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# Title
st.title("Gender Classification App")

st.write("Enter the details below:")

# Inputs
long_hair = st.number_input("Long Hair (0 or 1)", min_value=0, max_value=1)

forehead_width_cm = st.number_input("Forehead Width (cm)")

forehead_height_cm = st.number_input("Forehead Height (cm)")

nose_wide = st.number_input("Nose Wide (0 or 1)", min_value=0, max_value=1)

nose_long = st.number_input("Nose Long (0 or 1)", min_value=0, max_value=1)

lips_thin = st.number_input("Lips Thin (0 or 1)", min_value=0, max_value=1)

distance_nose_to_lip_long = st.number_input(
    "Distance Nose To Lip Long (0 or 1)",
    min_value=0,
    max_value=1
)

# Predict button
if st.button("Predict"):

    input_data = pd.DataFrame([[
        long_hair,
        forehead_width_cm,
        forehead_height_cm,
        nose_wide,
        nose_long,
        lips_thin,
        distance_nose_to_lip_long
    ]], columns=[
        "long_hair",
        "forehead_width_cm",
        "forehead_height_cm",
        "nose_wide",
        "nose_long",
        "lips_thin",
        "distance_nose_to_lip_long"
    ])

    prediction = model.predict(input_data)

    result = encoder.inverse_transform(prediction)

    st.success(f"Predicted Gender: {result[0]}")