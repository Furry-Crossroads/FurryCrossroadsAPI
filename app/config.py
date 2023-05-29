import os

# Need to show that this environment is for a FCAPI
if not os.environ.get("FCAPI"):
    raise RuntimeError("FCAPI environment variable not set.")

class Config(object):
    DEBUG = True
    TESTING = False

    # Security settings
    SECRET_KEY = os.environ.get("FCAPI_SECRET_KEY")

    # SQLAlchemy settings
    SQLALCHEMY_USERNAME = os.environ.get("FCAPI_SQLALCHEMY_USERNAME")
    SQLALCHEMY_PASSWORD = os.environ.get("FCAPI_SQLALCHEMY_PASSWORD")
    SQLALCHEMY_HOST = os.environ.get("FCAPI_SQLALCHEMY_HOST")
    SQLALCHEMY_DATABASE_NAME = os.environ.get("FCAPI_SQLALCHEMY_DATABASE_NAME")
    SQLALCHEMY_DATABASE_TYPE = os.environ.get("FCAPI_SQLALCHEMY_DATABASE_TYPE")
    # Enforce that all SQLAlchemy settings are set.
    if not all((
        SQLALCHEMY_USERNAME, 
        SQLALCHEMY_PASSWORD, 
        SQLALCHEMY_HOST, 
        SQLALCHEMY_DATABASE_NAME)
    ):
        raise RuntimeError("One or more of the SQLAlchemy environment variables are not set.")
    SQLALCHEMY_DATABASE_URI = f"{SQLALCHEMY_DATABASE_TYPE}://{SQLALCHEMY_USERNAME}:{SQLALCHEMY_PASSWORD}@{SQLALCHEMY_HOST}/{SQLALCHEMY_DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
