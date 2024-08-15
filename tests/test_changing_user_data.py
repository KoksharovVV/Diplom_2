import requests
from data import TestDataUrl


class TestChangingUserData:
    def test_changing_user_data_with_authorization(self, create_user_delete_user, update):
        access_token = create_user_delete_user[2]
        response = requests.patch(url=TestDataUrl.AUTH_USER_URL, json=update, headers={"Authorization": access_token})
        assert response.status_code == 200

    def test_changing_user_data_without_authorization(self, create_user_delete_user, update):
        response = requests.patch(url=TestDataUrl.AUTH_USER_URL, json=update, headers=None)
        assert response.status_code == 401
