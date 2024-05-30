"""Flask configuration."""

from os import environ, path
import os
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

uri = os.environ.get('DATABASE_URL')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

if not uri:
    raise ValueError("DATABASE_URL environment variable is not set or is empty")

"""Base config."""
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'

FLASK_ENV = 'development'
TESTING = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG = False

# Database
SQLALCHEMY_DATABASE_URI = uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True