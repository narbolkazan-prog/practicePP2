for i in range(10):
    if i == 7:
        break
    print(i)


for i in range(1,9):
    if i % 2 == 0:
        break
    print(i)


nums = [2, 6, -1, 0]
for n in nums:
    if n < 0:
        break
    print(n)


words = ["go", "run", "stop", "jump"]
for w in words:
    if w == "stop":
        break
    print(w)


letters = ['a', 'b', 'c', 'D','e']
for l in letters:
    if l.isupper():
        break
    print(l)


for i in range(1, 20):
    if i % 5 == 0:
        break
    print(i)


for i in range(-5, 8):
    if i == 0:
        break
    print(i)


text = "Hello World"
for ch in text:
    if ch == " ":
        break
    print(ch)


chars = ['a','b','x','y']
for c in chars:
    if c == 'x':
        break
    print(c)


number= int(input())
for i in range(1, 51):
    if i % number != 0:
        print(number, "is not divisible by", i)
    else:
        print(number, "is divisible by", i)
        break
 