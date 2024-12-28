import configparser
import os


class Config:
    def __init__(self):
        pass

    @staticmethod
    def get_config(section, key):
        file_root = os.path.dirname(__file__)
        config_file = os.path.join(file_root, "config.conf")
        config = configparser.ConfigParser()
        config.read(config_file)
        return config.get(section, key)
