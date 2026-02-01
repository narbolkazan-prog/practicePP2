i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    if i % 2 == 1:
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1


i = 0
word = "apple"
while i < len(word):
    if word[i] == "a":
        i += 1
        continue
    print(word[i])
    i += 1


nums = [-2, -1, 0, 1, 2]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1


i = 0
text = "hi there"
while i < len(text):
    if text[i] == " ":
        i += 1
        continue
    print(text[i])
    i += 1


i = 1
while i <= 6:
    if i < 3:
        i += 1
        continue
    print(i)
    i += 1


i = 0
word = "PyTHon"
while i < len(word):
    if word[i].islower():
        i += 1
        continue
    print(word[i])
    i += 1


nums = [-5, 3, -1, 0, 7, -9]

i = 0
while i < len(nums):
    if nums[i] >= 0:
        i += 1
        continue
    print(nums[i])
    i += 1
