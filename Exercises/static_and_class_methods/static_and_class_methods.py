# calculator
from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums) -> int:
        return reduce(lambda x, y: x * y, nums)

    @staticmethod
    def subtract(*nums) -> int:
        return reduce(lambda x, y: x - y, nums)

    @staticmethod
    def divide(*nums) -> float:
        return reduce(lambda x, y: x / y, nums)


# shop
class Shop:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if sum(self.items.values()) >= self.capacity:
            return "Not enough capacity in the shop"

        self.items[item_name] = self.items.get(item_name, 0) + 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        product = self.items.get(item_name)

        if not product or amount > product:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# integer
class Integer:
    ROMAN_NUMBERS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if not isinstance(value, float):
            return "value is not a float"

        return cls(int(value))

    @classmethod
    def from_roman(cls, value: str):
        int_sum = 0

        for i in range(len(value)):
            if i != 0 and cls.ROMAN_NUMBERS[value[i]] > cls.ROMAN_NUMBERS[value[i - 1]]:
                int_sum += cls.ROMAN_NUMBERS[value[i]] - 2 * cls.ROMAN_NUMBERS[value[i - 1]]
            else:
                int_sum += cls.ROMAN_NUMBERS[value[i]]

        return cls(int_sum)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))
