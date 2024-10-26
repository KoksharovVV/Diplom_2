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


class TestDataLogin:
    user_does_not_exist = {
        "email": "svin123124@mail.ru",
        "password": "123123"
    }

    valid_user_with_incorrect_password = {
        "email": "svin123123@mail.ru",
        "password": "123124"
    }


class TestCreateOrderData:
    ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6e"]
    }
    invalid_ingredient_hash = {
        "ingredients": ["61c0c5a71d1fbdaaa70231324324244"]
    }
    no_ingredients = {
        "ingredients": [""]
    }
