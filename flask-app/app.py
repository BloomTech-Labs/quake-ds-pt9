from decouple import config
from flask import Flask, render_template,
from .models import DB


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')

    @app.route('/')
    def root():
        return render_template('base.html', title='Epicentral')

    @app.route('/map', methods=['POST', 'GET'])
    def map():

        return render_template('map.html', title='Map data got!')

    return app
