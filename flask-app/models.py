from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Quake(db.Model):
    # id
	id = db.Column(db.String(30), primary_key=True)
    # geometry.coordinates.0
	longitude = db.Column(db.Float, nullable=False)
    # geometry.coordinates.1
    latitude = db.Column(db.Float, nullable=False)
    # properties.mag
    magnitude = db.Column(db.Float, nullable=False)
    # properties.place
    place = db.Column(db.String(50))
    # properties.time
	time = db.Column(db.BigInteger, nullable=False)

	def __repr__(self):
		return f'<Quake location (lat, long): {self.longitude}, {self.latitude}>'
