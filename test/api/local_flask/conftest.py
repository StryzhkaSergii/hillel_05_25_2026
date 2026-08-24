import time
import sqlite3
import pytest
import requests
import os

from constants import BASE_PROJECT_PATH
from core.api.local_flask_controller.local_controller import LocalFlaskController


# session
# package
# module
# class
# function

@pytest.fixture(scope="session", autouse=True)
def timing_of_all_tests():
    start_time = time.time()
    yield
    print(f"Time of all tests is {time.time()-start_time}")

@pytest.fixture(scope="session")
def flask_controller():
    return LocalFlaskController()

@pytest.fixture(scope="package")
def sql_lite_cursor():
    conn = sqlite3.connect(os.path.join(BASE_PROJECT_PATH, 'local_server', 'test_db.db'))
    cursor = conn.cursor()
    yield cursor
    conn.close()

# @pytest.fixture(scope="session")
# def base_url():
#     print("setUp base_url fixture")
#     yield "http://127.0.0.1:8080"
#     print("tearDown base_url fixture")

# @pytest.fixture(scope="session")
# def auth_headers(base_url):
#     token = requests.post(url=f"{base_url}/auth/", json={"name":"test", "password": "test"}).text
#     return {"token":token}