import os
import time
from flask import Flask, request,send_from_directory, jsonify
import numpy as np
from keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import cnn_train
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Folder to store uploaded images
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<path:filename>', methods=['GET'])
def serve_image(filename):
    # Use send_from_directory to serve the image file
    return send_from_directory(UPLOAD_FOLDER, filename)

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the model
def load_model():
    if not os.path.exists("model/model1.json") or not os.path.exists("model/leaf_model1.weights.h5"):
        print("Model not found. Training model...")
        cnn_train.train_model()
    print("Loading model from disk...")
    json_file = open('model/model1.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model/leaf_model1.weights.h5")
    print("Model loaded successfully.")
    return loaded_model

model = load_model()

# Labels for classification
labels = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___Healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Healthy", "Corn_(maize)___Northern_Leaf_Blight", "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)", "Grape___Healthy", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Potato___Early_blight", "Potato___Healthy", "Potato___Late_blight", "Tomato___Bacterial_spot",
    "Tomato___Early_blight", "Tomato___Healthy", "Tomato___Late_blight", "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites Two-spotted_spider_mite", 
    "Tomato___Target_Spot", "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus"
]

# Helper function to get file extension
def get_file_extension(filename):
    return os.path.splitext(filename)[1]

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Get the file extension from the original file
    file_extension = get_file_extension(file.filename)
    
    # Refactor the file name to the current epoch time with original extension
    epoch_time = int(time.time())
    filename = f"{epoch_time}{file_extension}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return jsonify({"image_path": file_path}), 200


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image_path = data.get('image_path')

    if not image_path or not os.path.exists(image_path):
        return jsonify({"error": "Invalid image path"}), 400

    # Load and preprocess the image
    test_image = image.load_img(image_path, target_size=(128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    # Predict
    result = model.predict(test_image)
    label2 = labels[result.argmax()]

    return jsonify({"status": label2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
