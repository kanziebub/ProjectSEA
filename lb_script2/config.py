import os
from util.utils import read_yaml


class Config:
    def __init__(self, file_name: str):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(self.current_dir, file_name)
        self.config = read_yaml(config_path)

    def set_filepath(self, file_path: str):
        return os.path.join(self.current_dir, file_path)
