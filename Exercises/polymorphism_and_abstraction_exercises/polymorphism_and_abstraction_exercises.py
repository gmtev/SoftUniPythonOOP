# vehicle
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    CONDITIONER = 0.9

    def drive(self, distance):
        required = (self.CONDITIONER + self.fuel_consumption) * distance
        if self.fuel_quantity >= required:
            self.fuel_quantity -= required

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER = 1.6
    TANK_PERCENTAGE = 0.95

    def drive(self, distance):
        required = (self.CONDITIONER + self.fuel_consumption) * distance
        if self.fuel_quantity >= required:
            self.fuel_quantity -= required

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.TANK_PERCENTAGE


# groups
from typing import List


class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

    def __getitem__(self, idx: int):
        return f"Person {idx}: {str(self.people[idx])}"


# account
from typing import List


class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property
    def balance(self) -> int:
        return sum(self._transactions) + self.amount

    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)

        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx: int):
        return self._transactions[idx]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):  # >
        return self.balance > other.balance

    def __ge__(self, other):  # >=
        return self.balance >= other.balance

    def __eq__(self, other):  # ==
        return self.balance == other.balance

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transactions = self._transactions + other._transactions

        return new_account
