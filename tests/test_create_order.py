import allure
import requests
from data import ApiURLS, Responses, ExistingUser, Burger


class TestCreateOrder:
    @allure.title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    def test_create_order_with_ingredients_authorized_user(self):
        existing_user = {'email': ExistingUser.email,
                         'password': ExistingUser.password,
                         'name': ExistingUser.name
                         }
        login = requests.post(ApiURLS.LOGIN_URL, data=existing_user)
        token = login.json()["accessToken"]
        response = requests.post(ApiURLS.ORDER_URL, headers={'Authorization': token}, data=Burger.burger_1)
        assert (response.status_code == 200
                and response.json()["success"] is True)

    @allure.title('Проверка создания заказа с ингредиентами не авторизованным пользователем')
    def test_create_order_with_ingredients_unauthorized_user(self):
        payload = {'ingredients': [Burger.burger_1]}
        response = requests.post(ApiURLS.ORDER_URL, data=payload)
        assert (response.status_code == 200
                and response.json()['success'] is True)

    @allure.title('Проверка создания заказа без ингредиентов не авторизованным пользователем')
    def test_create_order_no_ingredients_unauthorized_user(self):
        payload = {'ingredients': [Burger.burger_2]}
        response = requests.post(ApiURLS.ORDER_URL, data=payload)
        assert (response.status_code == 400
                and response.json() == {'success': False, 'message': Responses.NO_INGREDIENTS})

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов авторизованным пользователем')
    def test_create_order_wrong_hash_authorized_user(self):
        existing_user = {'email': ExistingUser.email,
                         'password': ExistingUser.password,
                         'name': ExistingUser.name
                         }
        payload = {'ingredients': [Burger.burger_3]}
        login = requests.post(ApiURLS.LOGIN_URL, data=existing_user)
        token = login.json()["accessToken"]
        response = requests.get(ApiURLS.ORDER_URL, headers={'Authorization': token}, data=payload)
        assert (response.status_code == 500
                and response.json() == {'success': False, 'message': Responses.INVALID_INGREDIENT})
