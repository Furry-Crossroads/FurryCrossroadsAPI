from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config.Config')
api = Api(app)
db = SQLAlchemy(app)

__all__ = ['app', 'api', 'db']

# register resource routes
from .resources.test_resource import TestResource
api.add_resource(TestResource, '/test')

# import views (after initializing app to avoid circular imports)
from app import views