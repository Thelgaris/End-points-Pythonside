from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
   
    def serialize(self):
        return {
            "user_name": self.user_name,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    gender = db.Column(db.String(120))
    age = db.Column(db.Integer)
    datebirth = db.Column(db.String(120))

    def serialize(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "DoB": self.datebirth,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    terrain = db.Column(db.String(120))
    population = db.Column(db.Integer)
    gravity = db.Column(db.String(120))

    def serialize(self):
        return {
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
            "gravity": self.gravity,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    model = db.Column(db.String(120))
    crew = db.Column(db.Integer)
  

    def serialize(self):
        return {
            "name": self.name,
            "model": self.model,
            "crew": self.crew,
         
            # do not serialize the password, its a security breach
        }

class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)     
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship(Characters)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet = db.relationship(Planets)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship(Vehicles)

   