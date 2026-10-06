import requests
from utilities import log_util

log = log_util.CommonLogger("http_client").get_logger()

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        log.info(f"Initialising the api client with {self.base_url}")

    def get(self, endpoint, headers=None):
        log.info(f"Get method with {self.base_url}{endpoint} with headers {headers}")
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=headers
        )

    def post(self, endpoint, data=None, json=None, headers=None):
        log.info(f"Post method with {self.base_url}{endpoint} with headers {headers} with data {data} with json {json}")
        return requests.post(
            f"{self.base_url}{endpoint}",
            data=data,
            json=json,
            headers=headers
        )

    def put(self, endpoint, json=None, headers=None):
        log.info(f"Put method with {self.base_url}{endpoint} with headers {headers} with json {json}")
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        log.info(f"Delete method with {self.base_url}{endpoint} with headers {headers}")
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )