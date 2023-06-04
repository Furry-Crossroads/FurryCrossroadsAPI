from app import db
from flask_restful import Resource

from . import basic_auth, token_auth, generate_and_store_token



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
