import os
from flask import Flask
import app.Routes as RouteMan
import logging

logging.basicConfig(level=logging.INFO)


def create_app(config=None):
    print("Creating App instance....")
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile('/app/config.py', silent=False)
    else:
        app.config.from_mapping(config)

    return app


def routes_setup(app_instance):
    route = RouteMan.Routes()
    route.set_route(app_instance)


def get_new_app_instance(config=None):
    app_instance = create_app(config)
    routes_setup(app_instance)
    return app_instance
