#!/usr/bin/env python3
'''Seeting up simple Flask app'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, get_timezone
import pytz


class Config:
    '''class to setup configurations for the app'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False, methods=['GET'])
def welcome():
    '''function to render 7-index.html'''
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    '''function to get locale based on defined languages'''
    # if locale is defined in URL
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # if locale is in user
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    '''Gets the user session'''
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)


@app.before_request
def before_request():
    '''sets user for a given request'''
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    '''sets timezone for the user'''
    # if timezone is in URL
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # validate
            pytz.timezone(timezone)
            return timezone
        except pytz.UknownTimeZoneError:
            pass

    # if timezone in user
    if g.user and g.user.get('timezone'):
        try:
            # validate
            pytz.timezone(timezone)
            return timezone
        except pytz.UknownTimeZoneError:
            pass

    # return default all have failed
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    '''run the app if the file is run as main'''
    app.run(debug=True)
