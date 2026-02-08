def add(a, b):
    return a + b
print(add(2, 3))


def greet(name):
    print("Hello", name)
greet("Ali")


def info(name, age):
    print(name, age)
info("Sara", 20)


def info_kw(name, age):
    print(name, age)
info_kw(age=25, name="Tom")


def multiply(a, b=2):
    return a * b
print(multiply(5))
print(multiply(5, 3))


def divide(a, b=1):
    return a / b
print(divide(10))
print(divide(10, 2))


def sum_three(a, b, c):
    return a + b + c
print(sum_three(1, 2, 3))


def average(a, b, c):
    return (a + b + c) / 3
print(average(3, 6, 9))


def max_args(*args):
    print(max(args))
max_args(3, 8, 1)


def check_length(word):
    print(len(word))
check_length("Python")
