from slack_sdk import WebhookClient

from robocop_api.config import USER_WHITELIST


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