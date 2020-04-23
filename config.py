"""
Configuration for Flask app
"""
import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['API_SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    POTION_DEFAULT_PER_PAGE = 20
    POTION_MAX_PER_PAGE = 5000
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

class ConfigDev(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['USERNAME_YOUC_API_DEV'],
        os.environ['PASSWORD_YOUC_API_DEV'],
        os.environ['HOST_YOUC_API_DEV'],
        os.environ['DATABASE_YOUC_API_DEV'],
    )

class ConfigTest(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['USERNAME_YOUC_API_TEST'],
        os.environ['PASSWORD_YOUC_API_TEST'],
        os.environ['HOST_YOUC_API_TEST'],
        os.environ['DATABASE_YOUC_API_TEST'],
    )

class ConfiProd(Config):
    DEBUG = False


class ConfigStaging(Config):
    DEVELOPMENT = True
    DEBUG = True


config_by_name = dict(
    dev=ConfigDev,
    test=ConfigTest,
    prod=ConfiProd,
    stagging=ConfigStaging
)