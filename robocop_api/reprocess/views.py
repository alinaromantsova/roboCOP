from flask import Blueprint, current_app

reprocess_blueprint = Blueprint("reprocess", __name__)


@reprocess_blueprint.route("/", methods=["POST"])
def create_book_file():
    """
    Takes: filename, filesize, s3_location
    """
    try:
        pass
    except Exception as e:
        current_app.logger.error(f"Failed: {e}")
        raise
