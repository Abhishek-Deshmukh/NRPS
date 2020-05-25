from flask import Flask, request, jsonify
from flask_cors import CORS
from parser_writer import *


APP = Flask(__name__)
CORS(APP)
PATH_TO_CONF = "./main.config"


@APP.route("/", methods=["GET"])
def current_proxies():
    with open(PATH_TO_CONF, "r") as config_file:
        data = config_parser(config_file.read())
    return jsonify(data)


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
        config = config_writer(request.json)
        with open(PATH_TO_CONF, "w") as config_file:
            config_file.write(config)
        return jsonify(True)
    except:
        return jsonify(False)


if __name__ == "__main__":
    APP.run(debug=True, port="8081")
