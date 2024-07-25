import requests
import logging
import pytest

logging.basicConfig(level=logging.INFO,
                    # filename="api.log",
                    # filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def root_response():
	try:
		return requests.get("http://127.0.0.1:2600/")
	except:
		return None

def test_root_request(root_response):
	if root_response == None:
		return
	logging.info(root_response.text)
	data = root_response.json()
	assert data["response"] == 200
	assert data["message"] == "This is the root page."


if __name__ == "__main__":
	test_root_request(requests.get("http://127.0.0.1:2600/"))

