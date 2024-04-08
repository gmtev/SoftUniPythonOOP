# number increment

def number_increment(numbers):

    def increase():
        increased = [x+1 for x in numbers]
        return increased

    return increase()


print(number_increment([1, 2, 3]))


# vowel filter

def vowel_filter(function):
    def wrapper():
        result = function()
        return [el for el in result if el in "aeiouy"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


# even numbers




# multiply

def multiply(num):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * num
        return wrapper
    return decorator


@multiply
def add_ten(number):
    return number + 10