from flask import Flask
from flask_restful import Api
from .resources.test_resource import TestResource

app = Flask(__name__)
api = Api(app)

# register resource routes
api.add_resource(TestResource, '/test')

# import views (after initializing app to avoid circular imports)
from app import views