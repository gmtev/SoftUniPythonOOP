from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        price_of_equipment = sum(el.price for el in self.equipment)
        avg_protection = sum([eq.protection for eq in self.equipment]) / len(self.equipment) if self.equipment else 0
        result = f"Name: {self.name}\nCountry: {self.country}\nAdvantage: {self.advantage} points\n" \
                 f"Budget: {self.budget:.2f}EUR\nWins: {self.wins}\n" \
                 f"Total Equipment Price: {price_of_equipment:.2f}\n" \
                 f"Average Protection: {int(avg_protection)}"

        return result
