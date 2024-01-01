# CarVision

CarVision is a web application that enables users to upload images of cars and uses machine learning to identify the car model. The application is built with Flask, Tailwind CSS, and TensorFlow.

## Features

- **Image Upload**: Users can upload car images for analysis.
- **Image Cropping**: Provides the option to crop the image for better prediction accuracy.
- **Model Prediction**: Utilizes a TensorFlow model to predict and display the most likely car models.

## Getting Started

These instructions will guide you through setting up a copy of the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- npm (Node.js package manager)

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/KeenanS04/CarVision.git
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd CarVision
    ```

3. **Set Up a Python Virtual Environment (Optional)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Install npm Packages**
    ```bash
    npm install
    ```

6. **Build Tailwind CSS File**
    ```bash
    npx tailwindcss -i ./app/static/css/tailwind.css -o ./app/static/css/style.css --minify
    ```

7. **Start the Flask Application**
    ```bash
    flask run
    ```
    or
    ```bash
    python run.py
    ```

    Now, the application should be running on `http://localhost:5000`.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Tailwind CSS](https://tailwindcss.com/) - For styling the application.
- [TensorFlow](https://www.tensorflow.org/) - Used for making model predictions.

## Note

The machine learning model is a work in progress, and prediction accuracy is expected to improve over time.
