import requests_mock
import pytest
from main import madlib
from fastapi import Response
from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_madlib():
    with requests_mock.Mocker(real_http=True) as mock_request:
        url='https://reminiscent-steady-albertosaurus.glitch.me/'
        mock_request.get(url+'adjective', text="adjective word")
        mock_request.get(url+'verb', text="verb word")
        mock_request.get(url+'noun', text="noun word")

        response = client.get("/madlib")
        assert response.status_code == 200
        assert response.text=='It was a adjective word day. I went downstairs to see if I could verb word dinner. I asked, "Does the stew need fresh noun word?"'


