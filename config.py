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
