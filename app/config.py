import os

# Need to show that this environment is for a FCAPI
if not os.environ.get("FCAPI"):
    raise RuntimeError("FCAPI environment variable not set.")


def get_config_object(**kwargs) -> object:
    """Returns a Config object with the given kwargs set as attributes.
    """

    class _Config(object):
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

    # Set class attributes from kwargs
    for key, value in kwargs.items():
        setattr(_Config, key, value)

    # Enforce that all SQLAlchemy settings are set.
    if not all((
        _Config.SQLALCHEMY_USERNAME, 
        _Config.SQLALCHEMY_PASSWORD, 
        _Config.SQLALCHEMY_HOST, 
        _Config.SQLALCHEMY_DATABASE_NAME)
    ):
        raise RuntimeError("One or more of the SQLAlchemy environment variables are not set.")
    _Config.SQLALCHEMY_DATABASE_URI = f"{_Config.SQLALCHEMY_DATABASE_TYPE}://{_Config.SQLALCHEMY_USERNAME}:{_Config.SQLALCHEMY_PASSWORD}@{_Config.SQLALCHEMY_HOST}/{_Config.SQLALCHEMY_DATABASE_NAME}"
    _Config.SQLALCHEMY_TRACK_MODIFICATIONS = True

    return _Config



