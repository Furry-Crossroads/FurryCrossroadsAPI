from app import app, db

from app.models import ApiToken, Member, Logs

from flask import request, abort, g

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from hashlib import sha256
from datetime import datetime, timedelta
import secrets

# Create two authentication objects
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('Bearer')

# Verify username and password
@basic_auth.verify_password
def verify_password(username, password):
    member = Member.query.filter_by(username=username).first()
    if member and member.check_password(password):
        return member

# Verify token
@token_auth.verify_token
def verify_token(token):
    api_token = ApiToken.query.filter_by(token=token, active=True).first()
    if api_token and api_token.expiration > datetime.utcnow():
        return api_token

@app.before_request
def start_timer():
    g.start = datetime.now()
    if not request.headers.get('User-Agent'):
        abort(400, "User-Agent header is required.")

@app.after_request
def log_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response

    now = datetime.now()
    duration = now - g.start
    log_params = {
        "authorization":    str(request.authorization),
        "ip_address":       request.remote_addr,
        "endpoint":         request.url,
        "method":           request.method,
        "duration":         duration.seconds,
        "timestamp":        now,
        "status":           response.status_code,
        "host":             request.host,
        "params":           request.view_args,
        "useragent":        request.user_agent.string,
    }

    # Log the details
    log = Logs(
        authorization   = sha256(log_params.get("authorization", "").encode()).hexdigest(),
        ip_address      = log_params["ip_address"],
        endpoint        = log_params["endpoint"],
        method          = log_params["method"],
        duration        = log_params["duration"],
        timestamp       = log_params["timestamp"],
        status          = log_params["status"],
        host            = log_params["host"],
        params          = str(log_params["params"]),
        useragent       = log_params["useragent"],

        # Add more information as required
    )

    db.session.add(log)
    db.session.commit()

    return response