# Import packages
from flask import render_template, Blueprint

# Create Blueprint and views
base = Blueprint('base', __name__)

@base.route('/')
@base.route('/home')
def home():
    return render_template('index.html')

@base.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@base.route('/education')
def education():
    return render_template('education.html')

@base.route('/work')
def work():
    return render_template('work.html')