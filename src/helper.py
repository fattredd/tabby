import os
import yaml

def load_tab_configs(config_dir):
    tabs = []
    create_dir(config_dir)
    for filename in os.listdir(config_dir):
        if filename.endswith(".yaml"):
            with open(os.path.join(config_dir, filename), "r") as file:
                tab_config = yaml.safe_load(file)
                tabs.extend(tab_config.get("tabs", []))
    return tabs

def create_dir(config_dir):
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
