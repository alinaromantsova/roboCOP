# app.py
from flask import Flask, request, make_response
from slack_sdk.webhook import WebhookClient

from werkzeug.datastructures import ImmutableMultiDict

from robocop_api.config import USER_WHITELIST

app = Flask(__name__)


def check_whitelist(data, action):
    if data['user_name'] not in USER_WHITELIST[action]:
        msg = f"Unfortunately, user <@{data['user_id']}> isn't allowed to perform command `{data['command']}`." \
              f" Requesting help of human <@U01NB8JD6PP>"
        send_message(msg, data['response_url'])


def echo_message(data):
    command_confirmation = f"User <@{data['user_id']}> called command `{data['command']}` " \
                           f"with arguments: `{data['text']}`"
    send_message(command_confirmation, data['response_url'])


def send_message(msg, response_url):
    webhook = WebhookClient(response_url)
    # Send a reply in the channel
    webhook.send(text=msg, response_type='in_channel')


@app.route('/', methods=['POST'])
def hello_world():
    data: ImmutableMultiDict = request.form
    data = data.to_dict()
    response_url = data['response_url']
    check_whitelist(data, 'ping')
    echo_message(data)
    send_message('Pong', response_url)
    return make_response("", 200)


# We only need this for local development.
if __name__ == '__main__':
    app.run()

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
