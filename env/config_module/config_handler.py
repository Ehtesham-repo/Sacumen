import yaml
import configparser
import json
import os

class ConfigHandler:
    def __init__(self):
        self.data = {}

    def read_yaml(self, file_path):
        with open(file_path, 'r') as file:
            self.data = yaml.safe_load(file)
        return self._convert_to_flat_dict(self.data)

    def read_ini(self, file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        self.data = {f"{section}_{key}": value for section in config.sections() for key, value in config.items(section)}
        return self.data

    def read_conf(self, file_path):
        return self.read_ini(file_path)

    def _convert_to_flat_dict(self, data, parent_key='', sep='_'):
        items = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._convert_to_flat_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def write_to_env(self, data, file_path):
        with open(file_path, 'w') as file:
            for key, value in data.items():
                file.write(f"{key}={value}\n")

    def write_to_json(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def set_env_variables(self, data):
        for key, value in data.items():
            os.environ[key] = str(value)
