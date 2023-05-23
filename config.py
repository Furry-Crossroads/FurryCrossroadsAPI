import os

# Need to show that this environment is for a FCAPI
if not os.environ.get("FCAPI"):
    raise RuntimeError("FCAPI environment variable not set.")

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'my-secret-key'  # You should change this!

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
