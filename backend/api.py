from flask import Flask, request, jsonify
from flask_cors import CORS


APP = Flask(__name__)
CORS(APP)
DATA = [
    {"id": 1, "nameserver": "www.dunce.com", "address": "80",},
    {"id": 2, "nameserver": "other.dunce.com", "address": "localhost:8005",},
]



@APP.route("/", methods=["GET"])
def current_proxies():
    return jsonify(DATA)


@APP.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    if username == "d" and password == "1":
        return jsonify(True)
    return jsonify(False)


@APP.route("/set_proxies", methods=["POST"])
def set_proxies():
    try:
        global DATA
        DATA = request.json
        return jsonify(True)
    except:
        return jsonify(False)



if __name__ == "__main__":
    APP.run(debug=True, port="8081")
