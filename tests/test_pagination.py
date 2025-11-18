
from http import HTTPStatus

import pytest
import requests

def test_get_all_users(app_url):
    response = requests.get(f"{app_url}/api/users/?page=1&size=5")
    assert response.status_code == HTTPStatus.OK
    json_response = response.json()
    print(json_response)
    assert json_response["total"] == 12

@pytest.mark.parametrize("size", [1, 3, 8, 12])
def test_value_items_with_different_size(app_url, size):
    response = requests.get(f"{app_url}/api/users/?page=1&size={size}")
    assert response.status_code == HTTPStatus.OK
    json_response = response.json()
    assert len(json_response["items"]) == size

@pytest.mark.parametrize("size, page", [(1, 12), (6, 2), (12, 1)])
def test_value_page_with_different_size(app_url, size, page):
    response = requests.get(f"{app_url}/api/users/?page=1&size={size}")
    assert response.status_code == HTTPStatus.OK
    json_response = response.json()
    assert json_response["size"] == size
    assert json_response["pages"] == page

@pytest.mark.parametrize("page, items", [(1, [1, 2, 3, 4, 5]), (2, [6, 7, 8, 9, 10]), (3, [11, 12])])
def test_value_items_with_different_page(app_url, page, items):
    response = requests.get(f"{app_url}/api/users/?page={page}&size=5")
    assert response.status_code == HTTPStatus.OK
    json_response = response.json()
    ids = [item["id"] for item in json_response['items']]
    assert ids == items
