import flask
from flask import Flask, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)