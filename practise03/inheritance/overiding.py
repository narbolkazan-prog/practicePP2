class Animal:
    def sound(self):
        print("Some sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()


class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts")
c = Car()
c.start()


class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    def greet(self):
        print("Hi, I am a student")
s = Student()
s.greet()


class Shape:
    def area(self):
        print("Unknown area")
class Square(Shape):
    def area(self):
        print("Area = side * side")
sq = Square()
sq.area()


class Phone:
    def call(self):
        print("Calling...")
class SmartPhone(Phone):
    def call(self):
        print("Smartphone calling...")
sp = SmartPhone()
sp.call()


class Employee:
    def work(self):
        print("Employee working")
class Manager(Employee):
    def work(self):
        print("Manager managing")
m = Manager()
m.work()


class Parent:
    def message(self):
        print("Parent message")
class Child(Parent):
    def message(self):
        print("Child message")
ch = Child()
ch.message()


class Device:
    def power(self):
        print("Device powered on")
class Laptop(Device):
    def power(self):
        print("Laptop powered on")
l = Laptop()
l.power()


class Fruit:
    def taste(self):
        print("Some taste")
class Apple(Fruit):
    def taste(self):
        print("Apple is sweet")
a = Apple()
a.taste()

