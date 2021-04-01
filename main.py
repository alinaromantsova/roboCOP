# app.py
import base64
import urllib

from flask import Flask, request
import boto3
import json
import logging
import os

from base64 import b64decode

from urllib.parse import urlparse

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    print("start")
    print(request.get_json())
    print("end")
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)
    # logger.
    # params = urlparse(event['body'])
    # user = params['user_name'][0]
    # command = params['command'][0]
    # channel = params['channel_name'][0]
    # if 'text' in params:
    #     command_text = params['text'][0]
    # else:
    #     command_text = ''
    #
    err = None
    res = ""
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


# We only need this for local development.
if __name__ == '__main__':
    app.run()
