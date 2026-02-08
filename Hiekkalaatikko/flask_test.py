from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

app.run(use_reloader=True, host='127.0.0.1', port=3000)