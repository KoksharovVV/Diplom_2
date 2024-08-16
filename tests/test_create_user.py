import allure
import requests
import pytest
from data import TestDataUrl, TestDataCreateUser


class TestUserRegistration:
    @allure.title("Регистрация пользователя")
    def test_create_uniq_user(self, fake_user):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=fake_user)
        name = response.json()["user"]["name"]
        email = response.json()["user"]["email"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}},' \
                                                                                                                        f'"accessToken":"{access_token}","refreshToken":"{refresh_token}"}}'

    @allure.title("Повторная регистрация пользователя")
    def test_creating_user_who_is_already_registered(self, create_user_delete_user, fake_user):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=fake_user)
        assert response.status_code == 403 and response.text == f'{{"success":false,"message":"User already exists"}}'

    @allure.title("Пропуск поля при регистрации")
    @pytest.mark.parametrize("data", (
        TestDataCreateUser.create_user_without_email,
        TestDataCreateUser.create_user_without_name,
        TestDataCreateUser.create_user_without_pass
    ))
    def test_creating_user_abd_not_filling_out_one_field(self, data):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=data)
        assert response.status_code == 403 and response.text == f'{{"success":false,"message":"Email, password and name are required fields"}}'
