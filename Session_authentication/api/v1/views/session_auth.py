#!/usr/bin/env python3
""" Module of Sessions views
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from typing import List
from models.user import User
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    '''
    '''
    email = request.form.get(email)
    if email == '':
        return jsonify({ "error": "email missing" }), 400
    pswd = request.form.get(password)
    if pswd == '':
        return jsonify({ "error": "password missing" }), 400

    users = User.search(email)
    if users is None
        return jsonify({ "error": "no user found for this email" }), 404
    for user in users:
        check: bool = user.is_valid_password(password)
        if not check:
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user = users[0]
    user_id = user.id
    session_id = auth.create_session(user_id)

    cookie_name = getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response
