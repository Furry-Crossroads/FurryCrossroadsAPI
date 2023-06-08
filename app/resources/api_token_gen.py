from app import db
from app.models import ApiToken
from flask_restful import Resource

from . import basic_auth, token_auth


import secrets
from datetime import datetime, timedelta

def generate_and_store_token(member_registration, expiration_days=30):
    # Generate a secure random token
    text_token = secrets.token_hex(32)

    # Determine the expiration date
    expires_at = datetime.utcnow() + timedelta(days=expiration_days)

    # Create a new ApiToken object
    token_model = ApiToken(
        token=text_token, 
        member_registration=member_registration, 
        expiration=expires_at,
        generated_at=datetime.utcnow(),
    )

    # Add the new token to the session and commit it
    db.session.add(token_model)
    db.session.commit()

    # Return the new token
    return text_token

class TokenGen(Resource):

    # POST - Generate a new token using a username and password combo from a member
    @basic_auth.login_required
    def post(self):
        member = basic_auth.current_user()
        token = generate_and_store_token(member.registration)

        return {'token': token}, 201

    # DELETE - Make an API token inactive manually
    @token_auth.login_required
    def delete(self):
        api_token = token_auth.current_user()
        api_token.active = False
        db.session.commit()
        return '', 204
