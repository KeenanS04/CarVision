from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import os
import tensorflow as tf

bp = Blueprint('main', __name__)

# Load your TensorFlow model
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

    # Read the image file
    img = Image.open(file_path)

    # Get crop coordinates from the form data
    crop_x = int(float(request.form.get('cropX', 0)))
    crop_y = int(float(request.form.get('cropY', 0)))
    crop_width = int(float(request.form.get('cropWidth', 0)))
    crop_height = int(float(request.form.get('cropHeight', 0)))

    # Perform the crop operation
    cropped_img = img.crop((crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))

    # Process the cropped image for prediction
    # Here you can add your image preprocessing and model prediction logic
    # prediction = model.predict(preprocessed_image)

    # For demonstration, let's save the cropped image
    cropped_img.save(file_path)
    print(f'saved to {file_path}')

    # Redirect to a new page or return a result
    return 'Image processed successfully'  # You can also render a template here
