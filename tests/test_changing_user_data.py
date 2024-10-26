import allure
import requests
from data import TestDataUrl


class TestChangingUserData:
    @allure.title("Изменение данных пользователя с авторизоацией")
    def test_changing_user_data_with_authorization(self, create_user_delete_user, update):
        access_token = create_user_delete_user[2]
        response = requests.patch(url=TestDataUrl.AUTH_USER_URL, json=update, headers={"Authorization": access_token})
        email = response.json()['user']['email']
        name = response.json()['user']['name']
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self, create_user_delete_user, update):
        response = requests.patch(url=TestDataUrl.AUTH_USER_URL, json=update, headers=None)
        assert response.status_code == 401 and response.text == f'{{"success":false,"message":"You should be authorised"}}'
