class Stack:

    def __init__(self):
        self.data = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self, element) -> str:
        return self.data.pop(element)

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self) -> str:
        reversed_data = reversed(self.data)
        result = ', '.join(reversed_data)
        return f"[{result}]"
