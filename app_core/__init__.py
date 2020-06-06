import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from config import BaseConfig

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

def create_app(environment):
    app = Flask(__name__)

    env = os.getenv("ENV")

    app.config.from_object(environment)

    from app_core.api.shape.controllers import shape

    """ Cors settings will be here. We maybe use this endpoint later. """
    cors = CORS(app, resources={
        r'/api/*': {
            'origins': BaseConfig.ORIGINS
        }
    })


    app.url_map.strict_slashes = False


    app.register_blueprint(shape, url_prefix='/api/shapes')

    return app