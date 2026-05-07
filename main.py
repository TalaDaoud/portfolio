from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
#model_path = "/home/motaseam/Desktop/ai_human_face_classifier/model/cnn_model_binary.h5"
model_path = r"C:\Users\HUAWEI\Desktop\Graduation project\Face-detection\model\cnn_model_binary.keras"
model = load_model(model_path)
print("Model loaded successfully.")

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
        print(f"Error processing image: {e}")
        return None

# Define the target image size
image_size = (178, 218)

# Route to predict an image
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    try:
        # Open the image
        with Image.open(file) as img:
            # Preprocess the image
            preprocessed_image = preprocess_image(img, image_size)
            if preprocessed_image is None:
                return jsonify({'error': 'Error processing the image'}), 500

            # Make a prediction
            prediction = model.predict(preprocessed_image)
            label = 'Fake' if prediction[0][0] > 0.5 else 'Real'

            # Return the result
            return jsonify({'prediction': label, 'confidence': float(prediction[0][0])})
    except Exception as e:
        print(f"Error handling image: {e}")
        return jsonify({'error': 'An error occurred while processing the image'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
