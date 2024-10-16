
# Leaf Disease Detection System


The Leaf Disease Detection System is a web-based application designed to identify plant diseases using deep learning. Users can upload images of leaves, which are processed and analyzed by a pre-trained convolutional neural network (CNN). The system classifies the leaves into various disease categories, providing instant feedback on their health status. This tool aims to assist farmers and agricultural professionals in early disease detection, ultimately promoting healthier crops and better yields.
## Run Locally

Install Python 3.10.0


  https://www.python.org/downloads/release/python-3100/

Install Node 21.6.2


  https://nodejs.org/en/blog/release/v21.6.2


Clone the project

```bash
  git clone https://github.com/chamoddissanayake/Leaf-Disease-Detection-System.git
```

Go to Frontend Folder

```bash
  Frontend > leaf-disease-detection
```

Install dependencies

```bash
  npm install
```

Start the Frontend

```bash
  npm start
```

Go to Frontend Web App

```bash
  http://localhost:3000/
```

Go to Backend Folder

```bash
  Backend >
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the Backend

```bash
  python app.py
```
## Tech Stack

**Backend Framework:** 
* Flask (Python)

**Machine Learning Libraries:**

  * TensorFlow
  * Keras

**Image Processing:**

  * TensorFlow 
  * Keras 
  * Image Preprocessing

**Frontend Technologies:**

  * React (Typescript)

**Data Manipulation:**

  * NumPy

**Image Augmentation:**

  * ImageDataGenerator (from Keras)
## Usage/Examples


POST Method

```bash
http://localhost:5006/predict
```

Request
```javascript
{
    "image_path": "./im_for_testing_purpose/a.blackrot.JPG"
}
```
Response
```javascript
{
    "status": "Apple___Black_rot"
}
```
