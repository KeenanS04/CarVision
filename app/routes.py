from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from .utils import image_processing
import numpy as np
import tensorflow as tf
import csv

def load_car_classes(csv_path):
    classes = {}
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            car_model = row
            classes[i] = car_model
            i += 1
    return classes

# Load car classes
csv_path = os.path.join(os.getcwd(), 'data', 'names.csv')
car_classes = load_car_classes(csv_path)

bp = Blueprint('main', __name__)

# Load TensorFlow model
def load_model():
    model_path = 'app/models/01'
    return tf.keras.models.load_model(model_path)

model = load_model()

@bp.route('/', methods=['GET'])
def index():
    # Render the home page with the image upload form
    return render_template('index.html')

@bp.route('/results', methods=['POST'])
def results():
    # Check if an image file is part of the POST request
    print(request.form)
    if 'image' not in request.files:
        print('file not found')
        return redirect(url_for('main.index'))

    file = request.files.get('image')
    
    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        print('file not selected')
        return redirect(url_for('main.index'))

    # Secure the filename and save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join('uploads', filename)
    file.save(file_path)

    # Process the image
    preprocessed_image = image_processing.preprocess_image(file_path)

    # Make a prediction
    predictions = model.predict(preprocessed_image)

    # Convert prediction to a class
    top_indices = np.argsort(predictions[0])[-3:][::-1]  # Sort and get top 3 indices
    top_predictions = [(car_classes[i], predictions[0][i]) for i in top_indices]

    # Delete image after it's been processed:
    os.remove(file_path)
    
    # Pass the prediction to the results template
    return render_template('results.html', top_predictions=top_predictions)
