from random import randint

class Credentials_generator:
    @staticmethod
    def email_generator():
        email = 'vladislavzenevsky2' + str(randint(100, 999)) + '@yandex.ru'
        return email

    @staticmethod
    def password_generator():
        password = str(randint(100000, 999999))
        return password
