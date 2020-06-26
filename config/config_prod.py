import os

from . import Config

class ConfigProd(Config):
    DEBUG = False
    FLASK_ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['PROD_USERNAME_YOUC_API'],
        os.environ['PROD_PASSWORD_YOUC_API'],
        os.environ['PROD_HOST_YOUC_API'],
        os.environ['PROD_DATABASE_YOUC_API'],
    )