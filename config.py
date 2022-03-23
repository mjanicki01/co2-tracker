"""Flask configuration."""

from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


"""Base config."""
SECRET_KEY = environ.get('SECRET_KEY')
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'

FLASK_ENV = 'development'
TESTING = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = "postgresql:///co2budget"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True





# from os import environ, path
# from dotenv import load_dotenv


# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

# class Config:
#     """Base config."""
# # SECRET_KEY = environ.get('SECRET_KEY')
# STATIC_FOLDER = 'static'
# TEMPLATES_FOLDER = 'templates'


# class ProdConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = environ.get('PROD_DATABASE_URI')
    

# class DevConfig(Config):
#     FLASK_ENV = 'development'
#     DEBUG = True
#     TESTING = True
#     # DATABASE_URI = environ.get('DEV_DATABASE_URI')
#     DEBUG_TB_INTERCEPT_REDIRECTS = False

#     # Database
#     SQLALCHEMY_DATABASE_URI = "postgresql:///co2budget"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_ECHO = True