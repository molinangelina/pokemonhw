from flask import Flask
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)




app.config.from_object(Config)

# initialize database to work with our app
from .models import db

db.init_app(app)
migrate = Migrate(app, db)


from . import routes
from . import models