# Person
class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


# Mammal
class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type: str, sound: str):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return Mammal.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"


# Profile
class Profile:
    def __init__(self, username: str, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_case_in_value = len([c for c in value if c.isupper()]) > 0
        is_digit_in_value = len([c for c in value if c.isdigit()]) > 0

        if not is_digit_in_value or not is_length_valid or not is_upper_case_in_value:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# Email Validator
