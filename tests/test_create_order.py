import requests
from data import TestDataUrl, TestCreateOrderData


class TestCreateOrder:
    def test_create_order_with_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients,
            headers={"Authorization": create_user_delete_user[2]})
        assert response.status_code == 200

    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        assert response.status_code == 200

    def test_create_order_with_ingredients(self):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.no_ingredients, headers=None)
        assert response.status_code == 400

    def test_create_order_without_ingredients(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.no_ingredients, headers=None)
        assert response.status_code == 400

    def test_create_order_with_invalid_ingredient_hash(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.invalid_ingredient_hash, headers=None)
        assert response.status_code == 500
