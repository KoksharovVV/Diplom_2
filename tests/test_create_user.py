import allure
import requests
import pytest
from data import TestDataUrl, TestDataCreateUser


class TestUserRegistration:
    @allure.title("Регистрация пользователя")
    def test_create_uniq_user(self, fake_user):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=fake_user)
        assert response.status_code == 200

    @allure.title("Повторная регистрация пользователя")
    def test_creating_user_who_is_already_registered(self, create_user_delete_user, fake_user):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=fake_user)
        assert response.status_code == 403

    @allure.title("Пропуск поля при регистрации")
    @pytest.mark.parametrize("data", (
        TestDataCreateUser.create_user_without_email,
        TestDataCreateUser.create_user_without_name,
        TestDataCreateUser.create_user_without_pass
    ))
    def test_creating_user_abd_not_filling_out_one_field(self, data):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=data)
        assert response.status_code == 403
