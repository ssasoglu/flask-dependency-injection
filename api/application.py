"""Application module."""
from flask import Flask
from api.application_config import ApplicationConfig
from api.containers import Container
from api.routes.default import index

def create_app() -> Flask:
    container = Container()

    app = Flask(__name__)
    container.init_resources()
    app.container = container

    app.add_url_rule("/", "index", index)

    return app