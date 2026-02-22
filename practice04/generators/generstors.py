def one():
    yield 1
for i in one():
    print(i)



def one_to_three():
    yield 1
    yield 2
    yield 3
for i in one_to_three():
    print(i)



def say_hi():
    for _ in range(5):
        yield "Hi"
for word in say_hi():
    print(word)



def two_numbers():
    yield 10
    yield 20
for i in two_numbers():
    print(i)



def true_false():
    yield True
    yield False
for i in true_false():
    print(i)



def multiply_two():
    for i in range(5):
        yield i * 2
for i in multiply_two():
    print(i)



def empty_line():
    yield ""
for i in empty_line():
    print(i)



def number_generator():
    for i in range(5):
        yield i
for num in number_generator():
    print(num)



def number_generator():
    for i in range(5):
        yield i
for num in number_generator():
    print(num)



def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
for num in even_numbers(10):
    print(num)