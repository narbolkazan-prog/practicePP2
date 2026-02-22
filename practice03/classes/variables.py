class Person:
    species = "Human"
p1 = Person()
p2 = Person()
Person.species = "Alien"
print(p1.species, p2.species)


class Employee:
    company = "TechCorp"
e1 = Employee()
e2 = Employee()
e1.company = "MegaCorp"
print(e1.company, e2.company, Employee.company)


class Circle:
    pi = 3.1416
c1 = Circle()
c2 = Circle()
c1.pi = 3.14
print(c1.pi, c2.pi, Circle.pi)


class Dog:
    species = "Canine"
d1 = Dog()
d2 = Dog()
d1.species = "Wolf"
print(d1.species, d2.species, Dog.species)


class Student:
    school_name = "ABC School"
s1 = Student()
s2 = Student()
Student.school_name = "XYZ School"
print(s1.school_name, s2.school_name)


class Laptop:
    default_ram = 8
l1 = Laptop()
l2 = Laptop()
l1.default_ram = 16
print(l1.default_ram, l2.default_ram, Laptop.default_ram)


class Vehicle:
    default_color = "White"
v1 = Vehicle()
v2 = Vehicle()
v1.default_color = "Red"
print(v1.default_color, v2.default_color, Vehicle.default_color)


class BankAccount:
    interest_rate = 0.05
b1 = BankAccount()
b2 = BankAccount()
b1.interest_rate = 0.06
print(b1.interest_rate, b2.interest_rate, BankAccount.interest_rate)


class Book:
    library = "Central Library"
    def __init__(self, title):
        self.title = title
    def __repr__(self):
        return f"{self.title} in {Book.library}"
b1 = Book("1984")
print(b1)


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def display_count(cls):
        return f"Total: {cls.count}"
c1 = Counter()
c2 = Counter()
print(Counter.display_count())
