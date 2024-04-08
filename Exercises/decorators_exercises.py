# logged
def logged(func):
    def wrapper(*args, **kwargs):
        return f"you called {func.__name__}{args}\n" \
               f"it returned {func(*args, **kwargs)}"

    return wrapper


@logged
def sum_numbers(a, b):
    return a + b


# even parameters
def even_parameters(func):

    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 == 0:
                    continue

            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def sum_numbers(a, b):
    return a + b


# bold, italic, underlined
def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"

    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"

    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"

    return wrapper


@make_underline
@make_italic
@make_bold
def greet(name):
    return f"Hello, {name}!"


# type check
def type_check(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def sum_numbers(a, b):
    return a + b


# cache
def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
            wrapper.log[num] = func(num)
        return wrapper.log[num]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)


# html tags
def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def say_hi():
    return "Hello"


# store results
def store_results(func):  # that's our decorator
    _FILE_NAME = "files/log.txt"

    def wrapper(*args, **kwargs):
        with open(_FILE_NAME, "a") as log_file:
            log_file.write(
                f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n"
            )

    return wrapper


class store_result:
    _FILE_NAME = "files/log.txt"

    def __init__(self, func):  # that's our decorator
        self.func = func

    def __call__(self, *args, **kwargs):  # the same as wrapper
        with open(self._FILE_NAME, "a") as log_file:
            log_file.write(
                f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n"
            )


# with param not defined by task
class store_result_in_file_name():
    _DIR = "files"

    def __init__(self, file_name: str):  # here goes the param
        self.file_name = file_name

    def __call__(self, func):  # this is out decorator
        def wrapper(*args, **kwargs):
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(
                    f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n"
                )

        return wrapper


@store_result_in_file_name("result.txt")
def sum_numbers(a: int, b: int):
    return a + b