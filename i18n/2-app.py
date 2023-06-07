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


class Config:
    '''Configuration module
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

def get_locale()
    return request.accept_languages.best_match(LANGUAGES)

babel = Babel(app, locale_selector=get_locale,)
app.config.from_object(Config)
