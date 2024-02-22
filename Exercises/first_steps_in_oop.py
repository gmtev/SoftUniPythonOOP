# rhombus of stars
n = int(input())


def print_row(size, row):
    print(f"{' '*(size - row)}{'* ' * row}")


def print_rhombus(size):
    for row in range(1, size + 1):  # upper half and centre
        print_row(size, row)
    for row in range(size-1, 0, -1):  # lower half
        print_row(size, row)


print_rhombus(n)

# scope mess
x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)


# class book
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# car
class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


# music
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


