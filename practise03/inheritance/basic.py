class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass
dog = Dog()
dog.speak()


class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    def study(self):
        print("Studying")
s = Student()
s.greet()
s.study()


class Vehicle:
    def start(self):
        print("Vehicle starting")
class Bike(Vehicle):
    def start(self):
        print("Bike starting")
b = Bike()
b.start()


class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
sq = Square(5)
print(sq.area())


class Worker:
    def work(self):
        print("Working")
class Programmer(Worker):
    def code(self):
        print("Coding")
p = Programmer()
p.work()
p.code()


class Parent:
    def func1(self):
        print("Parent func1")
class Child(Parent):
    def func2(self):
        print("Child func2")
c = Child()
c.func1()
c.func2()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
acc = SavingsAccount(100)
acc.deposit(50)
print(acc.balance)


class Bank:
    def info(self):
        print("Bank Info")
class Customer(Bank):
    def details(self):
        print("Customer details")
cust = Customer()
cust.info()
cust.details()


class Fruit:
    def taste(self):
        print("Fruits taste good")
class Apple(Fruit):
    def taste(self):
        print("Apple is sweet")
a = Apple()
a.taste()


class Phone:
    def call(self):
        print("Calling...")
class SmartPhone(Phone):
    def browse(self):
        print("Browsing internet")
sp = SmartPhone()
sp.call()
sp.browse()