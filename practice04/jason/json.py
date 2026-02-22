import json
data = {"name": "Ali", "age": 20}
json_data = json.dumps(data)
print(json_data)



import json
numbers = [1, 2, 3, 4]
print(json.dumps(numbers))



import json
data = {"active": True}
print(json.dumps(data))



import json
data = {"a": 1}
text = json.dumps(data)
print(text)



import json
text = '{"name": "Ali", "age": 20}'
data = json.loads(text)
print(data["name"])



import json
text = '{"name": "Ali", "age": 20}'
data = json.loads(text)
print(data["age"])



import json
text = '{"name": "Ali", "age": 20}'
data = json.loads(text)
data["age"] = 25
print(json.dumps(data))



import json
people = [
    {"name": "Ali"},
    {"name": "Aruzhan"}
]
with open("people.json", "w") as f:
    json.dump(people, f, indent=4)



import json
people = [
    {"name": "Ali", "age": 25},
    {"name": "Aruzhan", "age": 19}
]
people.sort(key=lambda x: x["age"])
print(json.dumps(people, indent=4))



import json
text = '{"numbers":[1,2,3,4]}'
data = json.loads(text)
print(len(data["numbers"]))