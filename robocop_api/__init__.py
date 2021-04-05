import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from robocop_api.config import Config

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
db = SQLAlchemy()


# App Factory
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.logger = logger
    app.url_map.strict_slashes = False

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)
    return app


def register_blueprints(app):
    from robocop_api.reprocess.views import reprocess_blueprint
    app.register_blueprint(reprocess_blueprint, url_prefix="/ping")
