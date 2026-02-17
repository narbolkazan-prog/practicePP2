def greet():
    print("Hello, world!")
greet()


def add(a, b):
    return a + b
print(add(5, 3))


def multiply(a, b):
    return a * b
print(multiply(6, 7))


def divide(a, b):
    return a / b
print(divide(20, 4))


def is_even(num):
    return num % 2 == 0
print(is_even(8))


def square(num):
    return num ** 2
print(square(9))


def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(10, 20))


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))


def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4]))


def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))