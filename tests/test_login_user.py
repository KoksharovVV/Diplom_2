import requests
from data import TestDataUrl, TestDataLogin


class TestLoginUser:
    def test_login_user(self, create_user_delete_user, fake_user):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, data=fake_user)
        assert response.status_code == 200

    def test_login_with_incorrect_login(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.user_does_not_exist)
        assert response.status_code == 401

    def test_login_with_correct_login_and_incorrect_password(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.valid_user_with_incorrect_password)
        assert response.status_code == 401
