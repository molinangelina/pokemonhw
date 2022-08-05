from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# create our models based off ERD
# class Poke(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     poke_name = db.Column(db.String(50), nullable=False, unique=True)
#     def __init__(self, poke_name):
#         self.poke_name = poke_name