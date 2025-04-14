#!/usr/bin/env python3

# 3rd party imports go here:
# python3 -m pip install flask
import flask

app = flask.Flask(__name__)


@app.route('/') # if an HTTP GET arrives at '/' run this code
def welcome():
    return "Welcome to our vulnerable app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)


