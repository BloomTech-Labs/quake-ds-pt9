from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Quake(db.Model):
    __tablename__ = "quakes"
    # id
    id = db.Column(db.String(30), primary_key=True)
    # geometry.coordinates.0
    longitude = db.Column(db.Float, nullable=False)
    # geometry.coordinates.1
    latitude = db.Column(db.Float, nullable=False)
    # geometry.coordinates.2
    depth = db.Column(db.Float, nullable=True)
    # properties.mag
    magnitude = db.Column(db.Float, nullable=False)
    # properties.place
    place = db.Column(db.String(200))
    # properties.time
    time = db.Column(db.BigInteger, nullable=False)
    # properties.felt
    felt = db.Column(db.Integer, nullable=True)


    def __init__(self, id, longitude, latitude, depths, magnitude, place, time):
        self.id = id
        self. longitude = longitude
        self.latitude = latitude
        self.depths = depths
        self.magnitude = magnitude
        self.place = place
        self.time = time

    def __repr__(self):
        return f'<Quake location (lat, long): {self.longitude}, {self.latitude}>'