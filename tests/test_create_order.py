import allure
import requests
from data import TestDataUrl, TestCreateOrderData


class TestCreateOrder:
    @allure.title("Cоздание заказа с авторизацией")
    def test_create_order_with_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients,
            headers={"Authorization": create_user_delete_user[2]})
        assert response.status_code == 200

    @allure.title("Cоздание заказа без авторизации")
    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        name = response.json()['name']
        order_number = response.json()["order"]["number"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"name":"{name}","order":{{"number":{order_number}}}}}'

    @allure.title("Cоздание заказа без ингредиентов с авторизацией")
    def test_create_order_with_ingredients(self):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.no_ingredients, headers=None)
        assert response.status_code == 400 and response.text == f'{{"success":false,"message":"Ingredient ids must be provided"}}'

    @allure.title("Cоздание заказа без ингредиентов без авторизации")
    def test_create_order_without_ingredients(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.no_ingredients, headers=None)
        assert response.status_code == 400 and response.text == f'{{"success":false,"message":"Ingredient ids must be provided"}}'

    @allure.title("Cоздание заказа невалидным хешем ингридиента")
    def test_create_order_with_invalid_ingredient_hash(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.invalid_ingredient_hash, headers=None)
        assert response.status_code == 500
