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
DEBUG = False

# Database
# SQLALCHEMY_DATABASE_URI = "postgresql://oalakyzygocekd:094c598c123f898c5f4f4c312d1bcff1d61faaf956fd115b79a449f6e82dad35@ec2-54-160-109-68.compute-1.amazonaws.com:5432/d42efu0qie1guq"
SQLALCHEMY_DATABASE_URI = "postgresql-fitted-72536"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
