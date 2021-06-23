from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from app.measurements import measurement

app.register_blueprint(measurement)
