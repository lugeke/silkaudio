# brings the application instance into the top-level of the application package
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    print(app.instance_path)
    app.config.from_pyfile('flask.cfg')
    config[config_name].init_app(app)

    db.init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app