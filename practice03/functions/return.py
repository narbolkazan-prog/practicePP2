def get_five():
    return 5
print(get_five())


def subtract(a, b):
    return a - b
print(subtract(10, 3))


def multiply(a, b):
    return a * b
print(multiply(3, 7))


def is_positive(n):
    return n > 0
print(is_positive(-2))


def square(n):
    return n * n
print(square(9))


def min_of_two(a, b):
    if a < b:
        return a
    return b
print(min_of_two(5, 9))


def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total
print(sum_list([1, 2, 3, 4]))


def reverse_text(text):
    return text[::-1]
print(reverse_text("Python"))


def to_upper(text):
    return text.upper()
print(to_upper("python"))


def even_numbers(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]
print(even_numbers(10))