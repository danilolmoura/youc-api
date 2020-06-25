import os

from . import Config

class ConfigDev(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['USERNAME_YOUC_API_DEV'],
        os.environ['PASSWORD_YOUC_API_DEV'],
        os.environ['HOST_YOUC_API_DEV'],
        os.environ['DATABASE_YOUC_API_DEV'],
    )