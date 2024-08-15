from faker import Faker


class TestDataUrl:
    CREATE_USER_URL = "https://stellarburgers.nomoreparties.site/api/auth/register"
    AUTHORIZATION_URL = "https://stellarburgers.nomoreparties.site/api/auth/login"
    AUTH_USER_URL = "https://stellarburgers.nomoreparties.site/api/auth/user"
    CREATE_ORDER_URL = "https://stellarburgers.nomoreparties.site/api/orders"


class TestDataCreateUser:
    create_user_without_email = {
        "password": "password",
        "name": "user_name"
    }
    create_user_without_pass = {
        "email": "email",
        "name": "user_name"
    }
    create_user_without_name = {
        "email": "email",
        "password": "password",
    }
