# Import packages
from flask import render_template, Blueprint

# Create Blueprint and views
base = Blueprint('base', __name__)

@base.route('/')
@base.route('/home')
def home():
    return render_template('home.html')

@base.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@base.route('/background')
def background():
    return render_template('background.html')