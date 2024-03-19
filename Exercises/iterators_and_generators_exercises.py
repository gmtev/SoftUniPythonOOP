# take skip

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iters = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iters == self.count - 1:
            raise StopIteration
        self.iters += 1

        return self.iters * self.step


# dictionary iterator
class dictionary_iter:

    def __init__(self, dic):
        self.items = list(dic.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items) -1:
            raise StopIteration

        self.idx += 1
        return self.items[self.idx]


# second solution
class dic_iter:

    def __init__(self, dic):
        self.items = dic.items()

    def __iter__(self):
        return iter(self.items)


# countdown iterator
class countdown_iterator:

    def __init__(self, count):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        self.count -= 1

        return self.count


# sequence repeat
class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration

        self.idx += 1
        return self.sequence[self.idx % len(self.sequence)]


# take halves
def solution():

    def integers():
        num: int = 1

        while True:
            yield num
            num += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


# fibonacci generator
def fibonacci():
    n1, n2 = 0, 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2


# reader
def read_next(*args):
    for seq in args:
        yield from seq
        # for el in seq:
        #     yield el


# prime numbers
from math import sqrt


def get_primes(numbers: list):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                break
        else:
            yield number


# possible permutations
from itertools import permutations


def possible_permutations(elements: list):
    for el in permutations(elements):
        yield list(el)  # has to be list for "judge", otherwise it is a tuple
