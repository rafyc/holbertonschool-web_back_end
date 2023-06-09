#!/usr/bin/env python3
'''Main app
'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.route('/')
def index():
    '''Generate template
    '''
    return render_template('1-index.html')


babel = Babel(app)


class Config:
    '''Configuration module
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
