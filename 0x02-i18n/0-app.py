#!/usr/bin/env python3

'''Seeting up simple Flask app'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def welcome():
    '''function to render 0-index.html'''
    return render_template('0-index.html')


if __name__ == '__main__':
    '''run the app if the file is run as main'''
    app.run(debug=True)
