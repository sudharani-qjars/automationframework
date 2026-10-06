import json
import os
from utilities import log_util

log = log_util.CommonLogger("data_reader").get_logger()

class TestDataReader:
    def __init__(self, file_path, env):
        self.file_path = file_path
        self.env = env
        log.info(f"Initialising the test data with file {self.file_path}")

    def load_data(self):
        if not os.path.exists(self.file_path):
            log.error(f"File {self.file_path} does not exist")
            raise FileNotFoundError("File does not exist")

        try:
            with open(self.file_path, "r") as read_file:
                data = json.load(read_file)
                log.info(f"Loaded data from {self.file_path}")
                return data[self.env]
        except Exception as e:
            log.error(f"Failed to load data from {self.file_path}")
            raise e

    def get_data(self,page_name, variable_name):
        log.info(f"Getting data from page {page_name} with variable {variable_name}")
        try:
            value = self.load_data()[page_name][variable_name]
            log.info(f"The value is {value}")
            return value
        except Exception as e:
            log.error(f"Failed to get data from page {page_name} with variable {variable_name}")
            raise e

# file_path = os.path.join(os.path.dirname(os.getcwd()),"testdata")
# file_name = "data.json"
# reader = TestDataReader(os.path.join(file_path, file_name),"stg")
# print(reader.get_data(page_name="signup", variable_name="name"))
