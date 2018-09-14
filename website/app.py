from flask import Flask
from .routes import homex
from .routes import authx


def create_app(config=None):
    app = Flask(__name__)
    # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    app.register_blueprint(homex,url_prefix='')
    app.register_blueprint(authx, url_prefix='/auth')
    return app