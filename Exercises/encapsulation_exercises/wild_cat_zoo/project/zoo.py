from typing import List
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.caretaker import Caretaker
from project.vet import Vet
from project.keeper import Keeper


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Cheetah or Lion or Tiger] = []
        self.workers: List[Vet or Keeper or Caretaker] = []

    def add_animal(self, animal: Lion or Tiger or Cheetah, price: int) -> str:
        if self.__animal_capacity > 0:
            if self.__budget >= price:
                self.__budget -= price
                self.animals.append(animal)
                self.__animal_capacity -= 1
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Vet or Keeper or Caretaker) -> str:
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        to_pay = 0
        for worker in self.workers:
            to_pay += worker.salary
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        to_pay = 0
        for animal in self.animals:
            to_pay += animal.money_for_care
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = '\n'.join(lion.__repr__() for lion in self.animals if isinstance(lion, Lion))
        cheetahs = '\n'.join(ch.__repr__() for ch in self.animals if isinstance(ch, Cheetah))
        tigers = '\n'.join(ti.__repr__() for ti in self.animals if isinstance(ti, Tiger))
        return f"You have {len(self.animals)} animals\n" \
               f"----- {sum(isinstance(x, Lion) for x in self.animals)} Lions:\n" \
               f"{lions}\n" \
               f"----- {sum(isinstance(x, Tiger) for x in self.animals)} Tigers:\n" \
               f"{tigers}\n" \
               f"----- {sum(isinstance(x, Cheetah) for x in self.animals)} Cheetahs:\n" \
               f"{cheetahs}"

    def workers_status(self) -> str:
        keepers = '\n'.join(keeper.__repr__() for keeper in self.workers if isinstance(keeper, Keeper))
        caretakers = '\n'.join(caretaker.__repr__() for caretaker in self.workers if isinstance(caretaker, Caretaker))
        vets = '\n'.join(vet.__repr__() for vet in self.workers if isinstance(vet, Vet))
        return f"You have {len(self.workers)} workers\n" \
               f"----- {sum(isinstance(x, Keeper) for x in self.workers)} Keepers:\n" \
               f"{keepers}\n" \
               f"----- {sum(isinstance(x, Caretaker) for x in self.workers)} Caretakers:\n" \
               f"{caretakers}\n" \
               f"----- {sum(isinstance(x, Vet) for x in self.workers)} Vets:\n" \
               f"{vets}"

