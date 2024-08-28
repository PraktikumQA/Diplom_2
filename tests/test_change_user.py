import allure
import requests

from data import ApiURLS, Responses
from generator import Generator


class TestChangeUserData:

    @allure.title('Проверка изменения данных пользователя с авторизацией')
    def test_change_data_with_login(self):
        old_data = {'email': Generator.create_email,
                    'password': Generator.create_password,
                    'name': Generator.create_name
                    }

        new_data = {'email': Generator.create_email,
                    'password': Generator.create_password,
                    'name': Generator.create_name
                    }

        requests.post(ApiURLS.REGISTER_URL, data=old_data)
        login = requests.post(ApiURLS.LOGIN_URL, data=old_data)
        token = login.json()['accessToken']
        response = requests.patch(ApiURLS.USER_URL, headers={'Authorization': token}, data=new_data)
        assert (response.status_code == 200
                and login.json()['user']['email']['name'] != response.json()['user']['email']['name'])

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_change_data_without_login(self):
        old_data = {'email': Generator.create_email,
                    'password': Generator.create_password,
                    'name': Generator.create_name
                    }

        new_data = {'email': Generator.create_email,
                    'password': Generator.create_password,
                    'name': Generator.create_name
                    }
        requests.post(ApiURLS.REGISTER_URL, data=old_data)
        response = requests.patch(ApiURLS.USER_URL, data=new_data)
        assert (response.status_code == 401
                and response.json() == {'success': False, 'message': Responses.UNAUTHORISED_USER})
