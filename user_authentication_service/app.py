#!/usr/bin/env python3
'''
'''

from flask import Flask, jsonify
from flask import request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def hello_world():
    '''Main
    '''
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify(email=email, message='user created')
    except ValueError:
        return jsonify(message='email already registered'), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(401)

    check = AUTH.valid_login(email=email, password=password)
    if not check:
        abort(401)

    session_id = AUTH.create_session(email=email)
    res = jsonify(email=email, message='logged in')
    res.set_cookie('session_id', res)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
