for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)


for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)


names = ["Amy", "David", "John", "Sophia"]
for name in names:
    if len(name) < 5:
        continue
    print(name)


nums = [0, 1, 2, 0, 3]
for n in nums:
    if n == 0:
        continue
    print(n)


temps = [-5, 0, 10, -2, 20]
for t in temps:
    if t < 0:
        continue
    print(t)


names = ["Alice", "Bob", "Anna", "Mike"]
for name in names:
    if name.startswith("B"):
        continue
    print(name)


for i in range(1, 20):
    if i % 4 != 0:
        continue
    print(i)


for i in range(1, 10):
    if i % 2 == 0 or i % 3 == 0:
        continue
    print(i)


letters = "AbCdEfG"
for l in letters:
    if l.isupper():
        continue
    print(l)

for i in range(1, 10):
    if i <= 3:
        continue
    print(i)

