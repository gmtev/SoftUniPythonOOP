# Shop
class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# Hero
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


# Employee
class Employee:
    def __init__(self, _id: int, first_name: str, last_name: str, salary: float):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return self.first_name + ' ' + self.last_name

    def get_annual_salary(self) -> float:
        return self.salary * 12

    def raise_salary(self, amount: float) -> float:
        self.salary += amount
        return self.salary


# Cup
class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> None:
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

    def status(self) -> int:
        return self.size - self.quantity


# Flower
class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f'{self.name} is {"" if self.is_happy else "not "}happy'
        # if self.is_happy:
        #     return f"{self.name} is happy"
        # return f"{self.name} is not happy"


# Steam user
from typing import List


class SteamUser:
    def __init__(self, username: str, games: List[str]):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game_name: str, hours: int) -> str:
        if game_name not in self.games:
            return f'{game_name} is not in library'
        self.played_hours += hours

        return f"{self.username} is playing {game_name}"

    def buy_game(self, game_name: str) -> str:
        if game_name in self.games:
            return f"{game_name} is already in your library"
        self.games.append(game_name)

        return f"{self.username} bought {game_name}"

    def status(self) -> str:
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


# Programmer
class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"

        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.skills >= skills_needed:
            if self.language != new_language:
                previous_language = self.language
                self.language = new_language
                return f"{self.name} switched from {previous_language} to {new_language}"

            return f"{self.name} already knows {self.language}"

        return f"{self.name} needs {skills_needed - self.skills} more skills"

