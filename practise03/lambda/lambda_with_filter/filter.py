print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))


print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6])))


print(list(filter(lambda x: x < 5, [1, 3, 5, 7])))


print(list(filter(lambda x: len(x) > 3, ["cat", "python", "java"])))


print(list(filter(lambda x: x.endswith("n"), ["python", "java", "c++"])))


print(list(filter(lambda x: x.isdigit(), ["123", "abc", "456"])))


print(list(filter(lambda x: x.isupper(), ["HELLO", "python", "WORLD"])))


print(list(filter(lambda x: x % 4 == 0, [4, 8, 10, 12, 15])))


print(list(filter(lambda x: len(x) == 5, ["apple", "banana", "grape", "melon"])))


print(list(filter(lambda x: x != x[::-1], ["level", "hello", "radar", "world"])))
