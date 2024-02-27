# Vet
class Vet:
    animals = []
    space = 5

    def __init__(self, name: str,):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"

        return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"


# Time
class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours, new_minutes, new_seconds) -> None:
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        # hours_to_return = self.hours
        # if self.hours < 10:
        #     hours_to_return = f"0{self.hours}"
        # minutes_to_return = self.minutes
        # if self.minutes < 10:
        #     minutes_to_return = f"0{self.minutes}"
        # seconds_to_return = self.seconds
        # if self.seconds < 10:
        #     seconds_to_return = f"0{self.seconds}"
        # return f"{hours_to_return}:{minutes_to_return}:{seconds_to_return}"

    def next_second(self) -> str:
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0

        return self.get_time()


# Account
class Account:
    def __init__(self, _id: int, name: str, balance: int = 0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# Pizza delivery
class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
            self.price += quantity * price_per_quantity

            # if ingredient in self.ingredients.keys():
            #     self.ingredients[ingredient] += quantity
            # else:
            #     self.ingredients[ingredient] = quantity
          # self.price += quantity * price_per_quantity

        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if not self.ingredients.get(ingredient):
          # if ingredient not in self.ingredients.keys():
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            elif quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        ingredients_str = ", ".join(f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items())
        return f"You've ordered pizza {self.name} prepared with {ingredients_str} and the price will be" \
               f" {self.price}lv."



