import logging

import requests
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
CONFIG_SERVER_URL = "http://localhost:5000"
cache = {}


def update_config(service_name):
    global cache
    response = requests.get(f"{CONFIG_SERVER_URL}/getConfig/{service_name}")
    if response.status_code == 200:
        cache = response.json()
        logging.info("Config updated")
    else:
        logging.error("Config could not be updated")


@app.route("/refreshConfig", methods=["GET"])
def refresh_config():
    service_name = request.args.get("service_name")
    update_config(service_name)
    return jsonify({"message": "Config updated", "config": cache})


@app.route("/homepage", methods=["GET"])
def homepage():
    if not cache:
        update_config("example1")

    html_file = cache.get("html_file_name")
    try:
        with open(html_file, "r") as file:
            content = file.read()
        return render_template_string(content)
    except FileNotFoundError:
        return "HTML file not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
