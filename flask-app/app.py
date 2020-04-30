from decouple import config
from flask import Flask, render_template, request
import folium


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    # DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Epicentral')

    @app.route('/map', methods=['POST', 'GET'])
    def map():
        usgs_month_data = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson'
        m = folium.Map(
            location=[-59.1759, -11.6016],
            tiles='Stamen Terrain',
            zoom_start=2  # Limited levels of zoom for free Mapbox tiles.
            )

        folium.GeoJson(
            usgs_month_data,
            name='geojson'
            ).add_to(m)
        m.save('templates/map.html')
        return render_template('map.html', title='Map data got!')

    return app
