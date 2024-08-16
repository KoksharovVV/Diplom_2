import allure
import requests
from data import TestDataUrl, TestDataLogin


class TestLoginUser:
    @allure.title("Авторизация существующего в системе пользователя")
    def test_login_user(self, create_user_delete_user, fake_user):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, data=fake_user)
        name = response.json()["user"]["name"]
        email = response.json()["user"]["email"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"accessToken":"{access_token}","refreshToken":"{refresh_token}",' \
                                                                f'"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Авторизация с неверным логином")
    def test_login_with_incorrect_login(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.user_does_not_exist)
        assert response.status_code == 401 and response.text == f'{{"success":false,"message":"email or password are incorrect"}}'

    @allure.title("Авторизация с неверным паролем")
    def test_login_with_correct_login_and_incorrect_password(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.valid_user_with_incorrect_password)
        assert response.status_code == 401 and response.text == f'{{"success":false,"message":"email or password are incorrect"}}'
