import socket
from http import HTTPStatus

import requests


def test_status(app_url):
    response = requests.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK
    assert response.json()['users'] == True

def test_local_service_host():
    with socket.create_connection(("localhost", 8002), timeout=5) as sock:
        ip, port = sock.getpeername()
        assert ip == "127.0.0.1"
        assert port == 8002
