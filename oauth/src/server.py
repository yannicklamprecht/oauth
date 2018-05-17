import json
import urllib.parse

import requests
from flask import Flask, redirect, request, Response

from oauth.src.static import CLIENT_ID, CLIENT_SECRET
from oauth.src.utils import append_params_to_uri
import urllib

app = Flask(__name__)


@app.route("/oauthcallback")
def oauthcallback():
    return "callback"


@app.route("/callback")
def callback():
    authorization_key: str = request.args['code']
    data = urllib.parse.urlencode({
        'code': authorization_key,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': "https://qcnawwa4ej.execute-api.eu-central-1.amazonaws.com/dev/oauthcallback",
        'grant_type': "authorization_code",
    })

    token_result: Response = requests.post(
        "https://accounts.google.com/o/oauth2/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    # return token_result.json()


@app.route("/authenticate")
def authenticate():
    uri = append_params_to_uri("https://accounts.google.com/o/oauth2/auth", {
        'redirect_uri': 'https://qcnawwa4ej.execute-api.eu-central-1.amazonaws.com/dev/callback',
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': 'https://mail.google.com/',
        'approval_prompt': 'force',
        'access_type': 'offline',
    })

    return redirect(uri)


if __name__ == '__main__':
    app.run()
