"""Simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return round(a / b, 2)


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("10 / 4 =", divide(10, 4))
    print("10 / 3 =", divide(10, 3))
    print("5 / 0 =", divide(5, 0))
