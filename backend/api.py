"""NRPS- nginx reverse proxy setter
Author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
The backend api
"""
from os import system, path
from secrets import token_hex
from flask import Flask, request, jsonify
from flask_cors import CORS


# enter things here
USERNAME = ""
PASSWORD = ""
# enter things here

APP = Flask(__name__)
CORS(APP)
PATH_TO_CONF = "../sites-enabled/main.conf"
SECRET_FILE = "./secrets.txt"


def config_parser(config):
    """Parses the given string of the config into a list of dictionary of proxies
    """

    # local variables
    proxies = []
    proxy = {
        "id": 0,
        "nameserver": "",
        "address": "",
    }
    count = 1

    # removing uncecessary seperators
    config = config.replace("\n", "").replace("\t", "")

    # separating using `;`
    config_lines = config.split(";")

    # looping through lines
    for config_line in config_lines:
        config_line = config_line.strip()

        # scraping for nameserver
        if config_line.find("server_name") != -1:
            proxy["nameserver"] = config_line.split(" ", 1)[1]

        # scraping the address
        if config_line.find("proxy_pass") != -1:
            proxy["type"] = "proxy"
            proxy["address"] = config_line.split()[-1]
            # putting in the address and appending to proxies
            proxy["id"] = count
            count += 1
            proxies.append(proxy.copy())

        if config_line.find("root") != -1:
            proxy["type"] = "static"
            proxy["address"] = config_line.split()[-1]
            # putting in the address and appending to proxies
            proxy["id"] = count
            count += 1
            proxies.append(proxy.copy())
    return proxies


@APP.route("/", methods=["GET"])
def current_proxies():
    """Route for understanding the current config
    """
    with open(PATH_TO_CONF, "r") as config_file:
        data = config_parser(config_file.read())
    return jsonify(data)


def save(secret_key):
    """saving the security key in a file to read later
    """
    with open(SECRET_FILE, "a+") if path.isfile(SECRET_FILE) else open(
        SECRET_FILE, "w+"
    ) as secrets_file:
        inside = secrets_file.read()
        secrets_file.write(inside + "\n" + secret_key)


@APP.route("/login", methods=["POST"])
def login():
    """For logging in
    """
    username = request.json["username"]
    password = request.json["password"]
    if (username, password) == (USERNAME, PASSWORD):
        secret_key = "".join(token_hex(16) for i in range(8))
        save(secret_key)
        return jsonify(secret_key)
    return jsonify(False)


def config_writer(proxies):
    """Converting proxies into a config string
    """
    config = ""
    for proxy in proxies:
        config += "server {\n\tlisten 80"
        if proxy["id"] == 1:
            config += " default_server"
        if proxy["type"] == "proxy":
            config += (
                ";\n\tserver_name "
                + proxy["nameserver"]
                + ";\n\tlocation / {\n\t\tproxy_set_header X-Real-IP $remote_addr;\n\t\tproxy_pass "
                + proxy["address"]
                + ";\n\t}\n}\n"
            )
        elif proxy["type"] == "static":
            config += (
                ";\n\tserver_name "
                + proxy["nameserver"]
                + ";\n\tlocation / {\n\t\troot "
                + proxy["address"]
                + ";\n\t}\n}\n"
            )
    return config


def check_key(secret_key):
    """Check if the secret key is the one generated here
    """
    with open(SECRET_FILE, "r") as secrets_file:
        all_keys = secrets_file.read()
        all_keys = all_keys.split("\n")
        if secret_key in all_keys:
            return True
    return False


@APP.route("/set_proxies", methods=["POST"])
def set_proxies():
    """Route for setting up configs
    """
    config = config_writer(request.json["proxies"])
    if check_key(request.json["securityKey"]):
        with open(PATH_TO_CONF, "r") as config_file:
            config = config_file.readline() + "\n" + config
        with open(PATH_TO_CONF, "w") as config_file:
            config_file.write(config)
        restart_nginx()
        return jsonify(True)
    return jsonify(False)


@APP.route("/restart_server", methods=["POST"])
def restart_nginx():
    """Route for restarting nginx
    """
    if check_key(request.json["securityKey"]):
        try:
            system("systemctl restart nginx")
            return jsonify(True)
        except:
            pass
    return jsonify(False)


@APP.route("/clean_secrets", methods=["POST"])
def clean_secrets():
    """cleaning all the secrets, i.e. deleting the SECRETS_FILE
    """
    if check_key(request.json["securityKey"]):
        try:
            system("rm -rf " + SECRET_FILE)
            return jsonify(True)
        except:
            pass
    return jsonify(False)


if __name__ == "__main__":
    ROUTE = "127.0.0.1"
    APP.run(debug=True, host=ROUTE, port="8081")
