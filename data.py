class ApiURLS:
    HOME_PAGE_URL = "https://stellarburgers.nomoreparties.site"
    REGISTER_URL = f"{HOME_PAGE_URL}/api/auth/register"
    LOGIN_URL = f"{HOME_PAGE_URL}/api/auth/login"
    USER_URL = f"{HOME_PAGE_URL}/api/auth/user"
    ORDER_URL = f"{HOME_PAGE_URL}/api/orders"


class ExistingUser:
    email = "300@ya.ru"
    password = "123456"
    name = "Test1User"


class Burger:
    burger_1 = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    burger_2 = []
    burger_3 = ["65en6dnrd6567nwe4b4567gd"]


class Responses:
    EXISTING_USER = 'User already exists'
    REGISTRATION_EMPTY_FIELD = 'Email, password and name are required fields'
    LOGIN_WITH_INCORRECT_DATA = 'email or password are incorrect'
    CHANGE_USER_WITHOUT_LOGIN = 'You should be authorised'
    NO_INGREDIENTS = 'Ingredient ids must be provided'
    INVALID_INGREDIENT = 'Internal Server Error'
    UNAUTHORISED_USER = 'You should be authorised'
