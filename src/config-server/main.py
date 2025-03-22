import json

from flask import Flask, jsonify

app = Flask(__name__)


def load_config(service_name):
    with open(f"config.{service_name}.json", "r") as file:
        return json.load(file)


@app.route("/getConfig/<service_name>", methods=["GET"])
def get_config(service_name):
    config = load_config(service_name)
    return jsonify(config), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
