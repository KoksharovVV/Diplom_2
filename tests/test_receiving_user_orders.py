import allure
import requests
from data import TestDataUrl


class TestReceivingUserOrders:
    def test_receiving_user_orders_with_authorization(self, create_user_delete_user):
        response = requests.get(
            url=TestDataUrl.CREATE_ORDER_URL, headers={"Authorization": create_user_delete_user[2]})
        assert response.status_code == 200


    def test_get_orders_for_non_authorized_user(self):
        response = requests.get(url=TestDataUrl.CREATE_ORDER_URL)
        assert response.status_code == 401
