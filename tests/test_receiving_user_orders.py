import allure
import requests
from data import TestDataUrl


class TestReceivingUserOrders:
    def test_receiving_user_orders_with_authorization(self, create_user_delete_user):
        response = requests.get(
            url=TestDataUrl.CREATE_ORDER_URL, headers={"Authorization": create_user_delete_user[2]})
        orders = response.json()['orders']
        total = response.json()['total']
        total_today = response.json()['totalToday']
        assert response.status_code == 200 and response.text == f'{{"success":true,"orders":{orders},"total":{total},"totalToday":{total_today}}}'

    def test_get_orders_for_non_authorized_user(self):
        response = requests.get(url=TestDataUrl.CREATE_ORDER_URL)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'
