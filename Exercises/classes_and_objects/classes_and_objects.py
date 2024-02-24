# Vehicle
class Vehicle:
    def __init__(self, mileage: int, max_speed: int = 150,):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


# Point
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x) -> None:
        self.x = new_x

    def set_y(self, new_y) -> None:
        self.y = new_y

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"


# Circle
class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        return Circle.pi * self.radius ** 2

    def get_circumference(self) -> float:
        return 2 * Circle.pi * self.radius


# Glass
class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if Glass.capacity >= self.content + ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f"{Glass.capacity - self.content} ml left"


# Smartphone
class Smartphone:

    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        if not self.is_on:
            return f'Turn on your phone to install {app}'

        if self.memory >= app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
