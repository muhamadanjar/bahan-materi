from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_marshmallow import Marshmallow
from flask_cors import CORS 

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)
    return app
