import os
import yaml

def load_tab_configs(config_dir):
    tab_groups = {}
    create_dir(config_dir)
    for filename in os.listdir(config_dir):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            with open(os.path.join(config_dir, filename), "r") as file:
                tab_config = yaml.safe_load(file)
                for group_name, tabs in tab_config.items():
                    tab_groups[group_name] = tabs
    return tab_groups

def create_dir(config_dir):
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
