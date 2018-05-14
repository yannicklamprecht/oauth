import urllib.parse

import requests
from flask import Flask, redirect, request

from oauth.src.static import CLIENT_ID, CLIENT_SECRET
from oauth.src.utils import append_params_to_uri
import urllib

app = Flask(__name__)


@app.route("/oauthcallback")
def oauthcallback():
    return "callback"


@app.route("/callback")
def callback():
    authorization_key: str = "code"  # request.args['code']
    data = urllib.parse.quote({
        'Code': authorization_key,
        'Client_id': CLIENT_ID,
        'Client_secret': CLIENT_SECRET,
        'Redirect_uri': "https://o8tluz7hga.execute-api.eu-central-1.amazonaws.com/dev/oauthcallback",
        'Grant_type': "authorization_code",
    })

    request.headers["Content-Type"] = "application/x-www-form-urlencoded"
    requests.post(
        "https://accounts.google.com/o/oauth2/token",
        data=data
    )


@app.route("/authenticate")
def authenticate():
    uri = append_params_to_uri("https://accounts.google.com/o/oauth2/auth", {
        'redirect_uri': 'https://o8tluz7hga.execute-api.eu-central-1.amazonaws.com/dev/callback',
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': 'https://mail.google.com/',
        'approval_prompt': 'force',
        'access_type': 'offline',
    })

    return redirect(uri)


if __name__ == '__main__':
    app.run()
