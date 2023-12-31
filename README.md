# CarVision

CarVision is a web application that allows users to upload images of cars and uses machine learning to predict the car model. It's built with Flask for the backend, Tailwind CSS for the front-end styling, and TensorFlow to handle the machine learning aspect.

## Features

- **Image Upload**: Users can upload images of cars for analysis.
- **Image Cropping**: Users have the option to crop the image to focus on the car.
- **Model Prediction**: The application predicts the car model using a pre-trained TensorFlow model and displays the predictions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need the following installed to run the application:
- Python 3.8 or higher
- pip (Python package installer)
- npm (Node package manager)

### Installation

Follow these steps to get your development environment set up:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/CarVision.git
2. Navigate to the project directory:
    ```bash
    cd CarVision
3. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
4. Install npm packages and build Tailwind CSS:
    ```bash
    npm install
    npm run build
5. Start the Flask application:
    ```bash
    python run.py

Now, you can visit http://localhost:5000 in your web browser to see the application.

Built With
Flask - The web framework used.
Tailwind CSS - The CSS framework used.
TensorFlow - ML library used for car model predictions.