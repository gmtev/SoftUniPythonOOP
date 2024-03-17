# custom range
class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.temp = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.temp < self.end:
            self.temp += 1
            return self.temp
        raise StopIteration


# reverse iter
class reverse_iter:
    def __init__(self, itr_obj):
        self.itr_obj = itr_obj
        self.start_index = 0
        self.end_index = len(self.itr_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_index > self.start_index:
            self.end_index -= 1
            return self.itr_obj[self.end_index]
        raise StopIteration


# second solution
class reverse_iter_second_solution:
    def __init__(self, itr_obj):
        self.itr_obj = itr_obj

    def __iter__(self):
        return reversed(self.itr_obj)


# vowels
class vowels:

    def __init__(self, sequence):
        self.sequence = sequence
        self.vowels_list = ["y", "a", "e", "o", "i","u"]
        self.index = -1
        self.vowels_in_sequence = [c for c in self.sequence if c.lower() in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_in_sequence):
            return self.vowels_in_sequence[self.index]
        raise StopIteration


# second solution
class vowels_second_solution:

    def __init__(self, sequence):
        self.sequence = sequence
        self.vowels_list = ["y", "a", "e", "o", "i", "u"]
        self.index = -1
        self.vowels_in_sequence = [c for c in self.sequence if c.lower() in self.vowels_list]

    def __iter__(self):
        return iter(self.vowels_in_sequence)


# squares
def squares(n):

    current = 1
    while current <= n:
        yield current ** 2
        current += 1


# generator range
def genrange(start, end):

    while start <= end:
        yield start
        start += 1


# reverse text
def reverse_text(sequence):
    current = len(sequence) - 1
    while current >= 0:
        yield sequence[current]
        current -= 1
