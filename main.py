from robocop_api import create_app, db

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run(debug=False)
# app.py
from flask import Flask, request, make_response
from werkzeug.datastructures import ImmutableMultiDict
from robocop_api.utils.slack_utils import check_whitelist, echo_message, send_message

# app = Flask(__name__)


# @app.route('/', methods=['POST'])
# def hello_world():
#     data: ImmutableMultiDict = request.form
#     data = data.to_dict()
#     response_url = data['response_url']
#     check_whitelist(data, 'ping')
#     echo_message(data)
#     send_message('Pong', response_url)
#     return make_response("", 200)


# We only need this for local development.
# if __name__ == '__main__':
#     app.run()

"""
{'api_app_id': 'A01TEUKRM6V',
'channel_id': 'D01TF8ZTTCH',
'channel_name': 'directmessage',
'command': '/ping',
'is_enterprise_install': 'false',
'response_url': 'https://hooks.slack.com/commands/T17LJF6FR/1938367507089/QdDad38cDgdR96jZCjo2gS1j',
'team_domain': 'perlegoteam',
'team_id': 'T17LJF6FR',
'text': 'how how how',
'token': 'R1BA2EEckfpCiWuEQt28Ny7R',
'trigger_id': '1910978215319.41698516535.f30bf48d4d96e16b544aed89d8fc6ef9',
'user_id': 'U017V6TC3UK'
"""
