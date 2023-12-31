from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/results', methods=['POST'])
def results():
    # Placeholder for processing and model prediction
    return render_template('results.html', prediction="Your prediction here")
