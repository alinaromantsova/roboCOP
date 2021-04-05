from flask import Blueprint, current_app, request, make_response
from werkzeug.datastructures import ImmutableMultiDict

from robocop_api.utils.slack_utils import check_whitelist, echo_message, send_message

reprocess_blueprint = Blueprint("reprocess", __name__)


@reprocess_blueprint.route("/", methods=["POST"])
def ping_request():
    try:
        data: ImmutableMultiDict = request.form
        data = data.to_dict()
        response_url = data['response_url']
        check_whitelist(data, 'ping')
        echo_message(data)
        send_message('Pong', response_url)
        return make_response("", 200)
    except Exception as e:
        current_app.logger.error(f"Failed: {e}")
        raise
