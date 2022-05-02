from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters_list = db.Column(db.String(120), unique=True, nullable=False)

class One_character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(120), unique=True, nullable=False)
    character_props = db.Column(db.String(120), unique=True, nullable=False)
    

class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }