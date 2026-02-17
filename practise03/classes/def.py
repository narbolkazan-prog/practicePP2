class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Bob", 25)
print(p.name, p.age)


class Person:
    def greet(self):
        print("Hello!")
p = Person()
p.greet()


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
c = Circle(5)
print(c.area())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
r = Rectangle(4, 5)
print(r.area())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
s = Student("Alice", [80, 90, 70])
print(s.average())


class Dog(Animal):
    def speak(self):
        print("Woof!")
d = Dog("Buddy")
d.speak()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(2, 3)
p2 = Point(5, 6)
print(p1.x, p1.y, p2.x, p2.y)


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        return f"{self.brand} {self.model}, {self.year}"
c = Car("Toyota", "Corolla", 2020)
print(c.info())


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
t = Temperature(25)
print(t.fahrenheit)


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
a = Counter()
b = Counter()
print(Counter.count)
