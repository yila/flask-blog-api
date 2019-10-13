import pytest
import requests
import json

base_url = 'http://localhost:5000'

def test_retrieve_user_info():
    # arrange
    expected_json_result = {'user': 'Miguel'}
    respone = requests.get(base_url + '/')
    assert respone.status_code == 200
    assert json.loads(respone.content.decode()) == expected_json_result
