#!/usr/bin/env python3
'''Seeting up simple Flask app'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''class to setup configurations for the app'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False, methods=['GET'])
def welcome():
    '''function to render 4-index.html'''
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    '''function to get locale based on defined languages'''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    '''run the app if the file is run as main'''
    app.run(debug=True)
