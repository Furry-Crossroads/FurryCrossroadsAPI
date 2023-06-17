from flask import g, jsonify, request
from flask_restful import Resource
from . import basic_auth, token_auth
from app.models import Member

class MemberMethods(Resource):
    # The decorators make sure that a valid token or password is provided
    @token_auth.login_required(optional=True)
    @basic_auth.login_required(optional=True)
    def get(self):
        user = g.current_user
        if user.role in ['admin', 'mod']:  # If user is admin or mod
            # Query a member by username or registration
            username = request.args.get('username')
            registration = request.args.get('registration')

            if username is not None:
                member = Member.query.filter_by(username=username).first()
                return jsonify(member.as_dict())
            elif registration is not None:
                member = Member.query.filter_by(registration=registration).first()
                return jsonify(member.as_dict())
            else:
                # Return all members if no argument is given
                members = Member.query.all()
                return jsonify([member.as_dict() for member in members])
        else:  # If user is a regular member
            # Return only this user's data
            return jsonify(user.as_dict())

    @token_auth.login_required(optional=True)
    @basic_auth.login_required(optional=True)
    def post(self):
        # Logic for creating new member
        pass

    @token_auth.login_required(optional=True)
    @basic_auth.login_required(optional=True)
    def put(self):
        # Logic for updating member's info
        pass

    @token_auth.login_required
    def delete(self):
        # Logic for deleting member
        pass
