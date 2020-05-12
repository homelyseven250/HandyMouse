import mouse_module as mouse
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/send-data')
def hello_world():
    return request.args["test"]

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)