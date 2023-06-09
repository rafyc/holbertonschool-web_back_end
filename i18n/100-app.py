#!/usr/bin/env python3
'''Main app
'''
import datetime
import locale
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''Configuration module
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''
    '''
    try:
        locale = request.args.get('locale')
        if locale in Config.LANGUAGES:
            return locale
        locale = g.user.get('locale')
        if locale in Config.LANGUAGES:
            return locale
    except Exception:
        pass
    return request.accept_languages.best_match('LANGUAGES')


def get_user():
    '''
    '''
    try:
        user_nb = int(request.args.get('login_as'))
        if user_nb in users.keys() and user_nb is not None:
            return users[user_nb]
    except Exception:
        return None


@app.before_request
def before_request():
    '''
    '''
    user = get_user()
    if user:
        g.user = user


@babel.timezoneselector
def get_timezone() -> str:
    '''
    '''
    try:
        url_timezone = request.args.get('timezone')
        if pytz.timezone(url_timezone):
            return url_timezone

        user_timezone = g.user.get('timezone')
        if pytz.timezone(user_timezone):
            return user_timezone

    except Exception:
        BABEL_DEFAULT_TIMEZONE

    return request.accept_languages.best_match(default_timezone)

@app.route('/')
def index():
    '''Generate template
    '''
    try:
        username = g.user['name']
        print(username)
        timezone = get_timezone()
        date = datetime.datetime.now(pytz.timezone(timezone))

        if get_locale() == 'en':
            locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
            format_str = '%b %d, %Y, %I:%M:%S %p'
            current_time = date.strftime(format_str)

        if get_locale() == 'fr':
            locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
            format_str = '%d %b %Y à %H:%M:%S'

    except Exception:
        username = None
        current_time = None

    print(username)
    return render_template('index.html', username=username, current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8001")
