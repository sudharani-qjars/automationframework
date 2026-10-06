import json
import os
from utilities import log_util

log = log_util.CommonLogger("config_reader").get_logger()

class ConfigReader:
    def __init__(self, file_path, env):
        self.file_path = file_path
        self.env = env
        log.info(f"Initialising the config data with file {self.file_path}")

    def load_data(self):
        if not os.path.exists(self.file_path):
            log.error(f"File {self.file_path} does not exist")
            raise FileNotFoundError("File does not exist")

        try:
            with open(self.file_path, "r") as read_file:
                data = json.load(read_file)
                log.info(f"Loaded data from {self.file_path}")
                return data["config"][self.env]
        except Exception as e:
            log.error(f"Failed to load data from {self.file_path}")
            raise e

    def get_data(self, variable_name):
        log.info(f"Getting data for variable {variable_name}")
        try:
            value = self.load_data()[variable_name]
            log.info(f"The value is {value}")
        except Exception as e:
            log.error(f"Failed to get data the value for the variable {variable_name}")
            raise e
