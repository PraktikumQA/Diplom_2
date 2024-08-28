import allure
import requests

from data import ApiURLS, Responses, ExistingUser
from generator import Generator


class TestGetOrders:

    @allure.title('Получение заказов пользователя с авторизацией')
    def test_get_orders_authenticated_user(self):
        existing_user = {'email': ExistingUser.email,
                         'password': ExistingUser.password,
                         'name': ExistingUser.name
                         }
        login = requests.post(ApiURLS.LOGIN_URL, data=existing_user)
        token = login.json()["accessToken"]
        response = requests.get(ApiURLS.USER_URL, headers={'Authorization': token}, data=existing_user)
        assert (response.status_code == 200
                and response.json()['success'] is True)

    @allure.title('Получение заказов пользователя без авторизации')
    def test_get_orders_unauthenticated_user(self):
        response = requests.get(ApiURLS.ORDER_URL)
        assert (response.status_code == 401
                and response.json() == {'success': False, 'message': Responses.UNAUTHORISED_USER})
