import os
from flask import Flask, send_file, render_template
from app.config import CONFIGURATIONS
import app as app_root
import time
APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app_root.__file__))


def page_not_found(e):
  return render_template('Notfound.html'), 404

def create_app(config=None):
    """Configure the app w.r.t extentions"""
    app = Flask(__name__)
    if config is None:
        config = CONFIGURATIONS["Production"]
    else:
        config = CONFIGURATIONS[config]
    app.config.from_object(config)
    register_errorhandlers(app)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_errorhandlers(app):
    def render_error(e):
        return str(e.code), e.code
    for e in [401, 404, 500]:
        app.errorhandler(e)(page_not_found)


def register_extensions(app):
    from app import extentions
    from flask_mongoengine import MongoEngine
    extentions.db = MongoEngine(app)
    extentions.cors.init_app(app)



def register_blueprints(app):
    from app.views.usermgmt import user
    from app.views.usrconsole import userconsole
    app.register_blueprint(user)
    app.register_blueprint(userconsole)
    pass
