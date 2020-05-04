from decouple import config
from flask import Flask, render_template, request
from flask_migrate import Migrate
import folium
from .models import db, Quake
import requests


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
    db.init_app(app)
    #migrate = Migrate(app, db)

    @app.route('/grabquakes', methods=['POST', 'GET'])
    def grab_quakes():

        def usgs_parser():
            usgs_data = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson')

            for entry in usgs_data.json()['features']:
                # checks if entry already exists
                if db.session.query(Quake.id).filter_by(id=entry['id']).scalar() is not None:
                    updated_entry = Quake.query.filter_by(id=entry['id']).first()
                    updated_entry.longitude = entry['geometry']['coordinates'][0]
                    updated_entry.latitude = entry['geometry']['coordinates'][1]
                    updated_entry.magnitude = entry['properties']['mag']
                    updated_entry.place = entry['properties']['place']
                    updated_entry.time = entry['properties']['time']
                    updated_entry.felt = entry['properties']['felt']
                    db.session.commit()

                else:
                    try:
                        quake_entry = Quake(id=entry['id'],
                        longitude=entry['geometry']['coordinates'][0],
                        latitude=entry['geometry']['coordinates'][1],
                        magnitude=entry['properties']['mag'],
                        place=entry['properties']['place'],
                        time=entry['properties']['time'])
                        db.session.add(quake_entry)

                    except IntegrityError:
                        print(f"Oh no something failed on {entry['id']}!")

        usgs_parser()
        db.session.commit()

        return render_template('grabquakes.html', title='Home', quakes=Quake.query.all())


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

    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        return render_template('base.html', title='Reset database!')

    return app
