from decouple import config
from flask import Flask, render_template, request
from functions import latlong_finder


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    # DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Epicentral')

    @app.route('/map', methods=['POST', 'GET'])
    def map():

        return render_template('map.html', title='Map data got!')

    return app
