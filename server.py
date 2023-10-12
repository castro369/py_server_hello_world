#!/bin/python

from flask import Flask

app = Flask(__name__)

# Create route for / index
@app.route("/")
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run()