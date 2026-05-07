import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("cnn_digit_model.h5")

# Title
st.title("Handwritten Digit Recognition")

st.write("Upload a digit image (0-9)")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["png", "jpg", "jpeg", "jfif"]
)

if uploaded_file is not None:

    # Open image in grayscale
    image = Image.open(uploaded_file).convert("L")

    # Resize image
    image = image.resize((28, 28))

    # Invert colors
    image = ImageOps.invert(image)

    # Improve contrast (black & white)
    image = image.point(lambda x: 255 if x > 100 else 0)

    # Display processed image
    st.image(image, caption="Processed Image", width=150)

    # Convert image to numpy array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Reshape for CNN
    img_array = img_array.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img_array)

    # Get predicted digit
    predicted_digit = np.argmax(prediction)

    # Confidence score
    confidence = np.max(prediction) * 100

    # Show result
    st.success(f"Predicted Digit: {predicted_digit}")

    st.write(f"Confidence: {confidence:.2f}%")