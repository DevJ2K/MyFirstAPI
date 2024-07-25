import requests
import logging
import pytest

logging.basicConfig(level=logging.INFO,
                    # filename="api.log",
                    # filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

def test_root_request():
	response = requests.get("http://127.0.0.1:2600/")
	logging.info(response.text)
	data = response.json()
	assert data["response"] == 200
	assert data["message"] == "This is the root page."


if __name__ == "__main__":
	test_root_request()

