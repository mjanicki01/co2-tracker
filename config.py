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
SQLALCHEMY_DATABASE_URI = "postgresql://hgifrxexffyssu:b9dd8d70cd8274992d6a03f1e7e8d65cc291526f4ebad3fecf794e4dac8972ce@ec2-34-197-84-74.compute-1.amazonaws.com:5432/d1regc6ohtn56m"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
