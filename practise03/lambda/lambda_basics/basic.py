add = lambda a, b: a + b
print(add(3, 4))


reverse = lambda s: s[::-1]
print(reverse("hello"))


to_upper = lambda s: s.upper()
print(to_upper("python"))


sum_list = lambda lst: lst[0] + lst[1]
print(sum_list([5, 10]))


nums = [5, 12, 7, 20]
print(list(filter(lambda x: x > 10, nums)))


first = lambda lst: lst[0]
print(first([10, 20, 30]))


div_by_5 = lambda x: x % 5 == 0
print(div_by_5(25))


square = lambda x: x * x
print(square(5))


reverse = lambda s: s[::-1]
print(reverse("hello"))


length = lambda s: len(s)
print(length("python"))

