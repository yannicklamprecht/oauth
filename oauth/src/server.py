from flask import Flask, redirect

from oauth.src.static import CLIENT_ID
from oauth.src.utils import append_params_to_uri

app = Flask(__name__)


@app.route("/callback")
def index():
    return "Hello World!"


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
