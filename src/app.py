import os
from helper import *
from flask import Flask, render_template

app = Flask(__name__)

# These tabs will be used if the config file is not found
default_tabs = {
    "syncthing": [
            {"name": "Local", "url": "http://127.0.0.1:8384"},
            {"name": "Remote", "url": "http://192.168.0.2:8384"}
    ],
    "meshtastic": [
        {"name": "Wlr", "url": "http://192.168.0.3:80"}
    ]
}

TAB_CONFIG_DIR = os.environ.get("TAB_CONFIG_DIR", "config")

tab_groups = load_tab_configs(TAB_CONFIG_DIR) or default_tabs


@app.route("/")
def index():
    return render_template("index.html", tab_groups=tab_groups)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
