from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .config import get_config_object


def make_app(Config=get_config_object()):
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

app = make_app()
api = Api(app)
db = SQLAlchemy(app)

# import after initializing to avoid circular imports
from . import models
from . import resources
from . import views
__all__ = ['app', 'api', 'db', 'resources', 'views', 'models']
api.add_resource(resources.TokenGen, '/token')
with app.app_context():
    db.create_all()



print("App initialization complete.")