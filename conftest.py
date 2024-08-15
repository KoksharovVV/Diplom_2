import pytest
import requests
from faker import Faker
from data import TestDataUrl


@pytest.fixture
def fake_user():
    fake = Faker()
    fake_user = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }
    return fake_user


@pytest.fixture
def create_user_delete_user(fake_user):
    response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=fake_user)
    access_token = response.json()["accessToken"]
    yield response, fake_user, access_token
    requests.delete(url=TestDataUrl.AUTH_USER_URL, headers={'Authorization': access_token})
