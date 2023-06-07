#!/usr/bin/env python3
'''Main app
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''Generate template
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
