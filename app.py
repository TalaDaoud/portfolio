import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Function to preprocess a single image
def preprocess_image(image, target_size):
    try:
        # Resize the image preserving aspect ratio
        image.thumbnail(target_size, Image.LANCZOS)
        # Create a blank canvas with target size
        canvas = Image.new("RGB", target_size, (0, 0, 0))
        # Center the image on the canvas
        paste_x = (target_size[0] - image.size[0]) // 2
        paste_y = (target_size[1] - image.size[1]) // 2
        canvas.paste(image, (paste_x, paste_y))
        # Convert to numpy array, normalize, and add batch dimension
        return np.expand_dims(np.array(canvas) / 255.0, axis=0)
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Load the trained model
#model_path = "/home/motaseam/Desktop/ai_human_face_classifier/model/cnn_model_binary.h5"
model_path = "C:/Users/HUAWEI/Desktop/Graduation project/Face-detection/model/cnn_model_binary.keras"
model = load_model(model_path)

# Streamlit UI
st.title("🖼️ Image Classification: Real or Fake")
st.markdown(
    """
    This application uses a trained CNN model to classify images as **Real** or **Fake**.
    Simply upload an image, and the model will predict its class along with a confidence score.
    """
)

# Sidebar for instructions
st.sidebar.title("Instructions")
st.sidebar.write(
    """
    1. Click **Browse files** to upload an image.
    2. Supported formats: JPG, JPEG, PNG.
    3. Once uploaded, the app will display the image and its classification result.
    """
)

# File uploader
st.sidebar.header("Upload Image")
uploaded_file = st.sidebar.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the image
    with Image.open(uploaded_file) as img:
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("🔄 Processing the image...")

        # Preprocess the image
        image_size = (178, 218)
        preprocessed_image = preprocess_image(img, image_size)

        if preprocessed_image is not None:
            # Make a prediction
            prediction = model.predict(preprocessed_image)
            label = "Fake" if prediction[0][0] > 0.5 else "Real"
            confidence = float(prediction[0][0])

            # Display the result with better visuals
            st.success(f"**Prediction:** {label}")
else:
    st.warning("Please upload an image to proceed.")
