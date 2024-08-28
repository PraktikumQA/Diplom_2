import allure
import requests

from data import ApiURLS, ExistingUser, Responses
from generator import Generator


class TestAuthentication:

    @allure.title('Успешная аутентификация в аккаунт')
    def test_login(self):
        payload = {'email': ExistingUser.email,
                   'password': ExistingUser.password,
                   'name': ExistingUser.name
                   }
        response = requests.post(ApiURLS.LOGIN_URL, data=payload)
        assert (response.status_code == 200
                and response.json()['success'] is True)

    @allure.title('НЕ успешная аутентификация с неверным логином и паролем')
    def test_auth_with_invalid_password_fail(self):
        payload = {'email': Generator.create_email,
                   'password': Generator.create_password,
                   'name': Generator.create_name
                   }
        response = requests.post(ApiURLS.LOGIN_URL, data=payload)
        assert (response.status_code == 401
                and response.json() == {'success': False, 'message': Responses.LOGIN_WITH_INCORRECT_DATA})
