from faker import Faker

faker = Faker()
fakerRU = Faker


class Generator:

    @staticmethod
    def create_email():
        email = faker.email()
        return email

    @staticmethod
    def create_password():
        password = faker.password(length=8)
        return password

    @staticmethod
    def create_name():
        name = faker.name()
        return name
