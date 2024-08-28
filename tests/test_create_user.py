import allure
import requests

from data import ApiURLS, ExistingUser, Responses
from generator import Generator


class TestCreateAccount:

    @allure.title('Создание аккаунта с корректными данными')
    def test_create_user(self):
        payload = {'email': Generator.create_email,
                   'password': Generator.create_password,
                   'name': Generator.create_name
                   }
        response = requests.post(ApiURLS.REGISTER_URL, data=payload)
        assert (response.status_code == 200
                and response.json()['success'] is True)

    @allure.title('Cоздание аккаунта с данными существующего пользователя')
    def test_create_user_existing(self):
        payload = {'email': ExistingUser.email,
                   'password': ExistingUser.password,
                   'name': ExistingUser.name
                   }
        response = requests.post(ApiURLS.REGISTER_URL, data=payload)
        assert (response.status_code == 403
                and response.json() == {'success': False, 'message': Responses.EXISTING_USER})

    @allure.title('Cоздание аккаунта с незаполненным обязательным полем')
    def test_create_user_with_one_empty_field(self):
        payload = {'email': "",
                   'password': Generator.create_password(),
                   'name': Generator.create_name()
                   }
        response = requests.post(ApiURLS.REGISTER_URL, data=payload)
        assert (response.status_code == 403
                and response.json() == {'success': False, 'message': Responses.REGISTRATION_EMPTY_FIELD})
