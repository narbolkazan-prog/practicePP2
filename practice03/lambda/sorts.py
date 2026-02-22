print(sorted([5, 2, 9, 1, 7]))


print(sorted([5, 2, 9, 1, 7], reverse=True))


print(sorted([5, 2, 9, 1, 7], key=lambda x: -x))


print(sorted(["banana", "apple", "cherry"]))


print(sorted(["banana", "apple", "cherry"], key=lambda x: len(x)))


print(sorted([1.2, 3.4, 0.5, 2.1], key=lambda x: int(x)))


print(sorted([(1, 5), (2, 0), (3, 1)], key=lambda x: -(x[0] + x[1])))


print(sorted([10, -5, 20, 0], key=lambda x: abs(x)))


print(sorted(["apple", "banana", "cherry"], key=lambda x: x.count("a")))


print(sorted([1.2, 3.4, 0.5, 2.1], key=lambda x: round(x)))
