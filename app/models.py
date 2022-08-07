from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

user_pokemon = db.Table('user_pokemon', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    team = db.relationship("Pokemon",
        secondary=user_pokemon,
        backref='trainers',
        lazy='dynamic'
        )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self):
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    pokemon_type = db.Column(db.String)
    ability = db.Column(db.String)
    img_url = db.Column(db.String)
    hp = db.Column(db.String)
    attack = db.Column(db.String)
    defense = db.Column(db.String)

    def __init__(self, name, pokemon_type, ability, img_url, hp, attack, defense):
        self.name = name
        self. pokemon_type = pokemon_type
        self.ability = ability
        self.img_url = img_url
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def save(self):
        db.session.add(self)
        db.session.commit()