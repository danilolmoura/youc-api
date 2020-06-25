import os

from . import Config

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
