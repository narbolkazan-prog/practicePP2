import os
if os.path.exists("receipt.txt"):
    print("have a file")
else:
    print("dont have a file")



with open("receipt.txt", "r", encoding="utf-8") as f:
    print(f.readline())



with open("receipt.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines[-1])



with open("receipt.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text.upper().count("TOTAL"))



with open("receipt.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(len(text))



with open("receipt.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.upper())



with open("receipt.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
longest = max(lines, key=len)
print(longest)



with open("receipt.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text.lower())



with open("receipt.txt", "r", encoding="utf-8") as f:
    for i in range(5):
        print(f.readline().strip())



with open("receipt.txt", "r", encoding="utf-8") as f:
    text = f.read()
print("len of space:", text.count(" "))