import os
from helper import *
from flask import Flask, render_template

app = Flask(__name__)

# These tabs will be used if the config file is not found
default_tabs = [
    {"name": "Google", "url": "http://syncthing_machine_ip:8384"},
    {"name": "Local", "url": "http://127.0.0.1:80"}
]

TAB_CONFIG_DIR = os.environ.get("TAB_CONFIG_DIR", "config")

tabs = load_tab_configs(TAB_CONFIG_DIR) or default_tabs


@app.route("/")
def index():
    return render_template("index.html", tabs=tabs)


if __name__ == "__main__":
    app.run(debug=True)
