"""This module has configurations for flask app."""
import os

CONFIGURATIONS = {
    "Development": "app.config.Development",
    "testing": "app.config.Testing",
    "Production": "app.config.Production",
    "default": "app.config.Development"
}

basedir = os.path.abspath(os.path.dirname(__file__))

class Base(object):
    """Base class for default set of configs."""

    DEBUG = False
    TESTING = False

    # Change it based on your admin user
    ADMIN_USER = 'admin'
    ADMIN_PASSWORD = 'admin'

    MONGO_CONNECT = False

class Development(Base):
    """Default set of configurations for development mode."""

    DEBUG = True
    TESTING = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'c4df-792842bc-4de1-792842bc-c4df-4de1'
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017
    MONGODB_DB = "cms"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""


class Production(Base):
    """Default set of configurations for prod mode."""

    DEBUG = False
    TESTING = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = '9177-d5207bd9faa6-792842bc-c4df-4de1'
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017
    MONGODB_DB = "cms"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""
