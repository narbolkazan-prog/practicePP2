class Person:
    def __init__(self, name):
        self.name = name
p = Person("Alice")
print(p.name)


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
e = Employee("John")
print(e.salary)


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
e = Employee("John")
print(e.salary)


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        self.fahrenheit = (celsius * 9/5) + 32
t = Temperature(25)
print(t.fahrenheit)


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
d = Dog("Buddy", "Labrador")
print(d.name, d.breed)


class Cat:
    def __init__(self, name, color="Black"):
        self.name = name
        self.color = color
c = Cat("Whiskers")
print(c.color)


class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
s = Smartphone("Samsung", "S21", 128)
print(s.model, s.storage)


class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
l = Laptop("Dell", 8, 500)
print(l.ram, l.price)
 

 class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
b = Book("1984", "George Orwell")
print(b.title, b.author)
