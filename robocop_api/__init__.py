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

    app.register_blueprint(book_blueprint, url_prefix="/book")
    app.register_blueprint(books_blueprint, url_prefix="/books")
    app.register_blueprint(book_file_blueprint, url_prefix="/book-file")
    app.register_blueprint(book_files_blueprint, url_prefix="/book-files")
    app.register_blueprint(distributor_blueprint, url_prefix="/distributor")
    app.register_blueprint(distributors_blueprint, url_prefix="/distributors")