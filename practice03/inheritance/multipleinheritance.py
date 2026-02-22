class A:
    def a(self):
        print("A method")
class B:
    def b(self):
        print("B method")
class C(A, B):
    pass
c = C()
c.a()
c.b()



class Parent1:
    def greet1(self):
        print("Hello from Parent1")
class Parent2:
    def greet2(self):
        print("Hello from Parent2")
class Child(Parent1, Parent2):
    pass
ch = Child()
ch.greet1()
ch.greet2()



class X:
    def func_x(self):
        print("X function")
class Y:
    def func_y(self):
        print("Y function")
class Z(X, Y):
    def func_z(self):
        print("Z function")
z = Z()
z.func_x()
z.func_y()
z.func_z()



class Animal:
    def eat(self):
        print("Animal eats")
class Mammal:
    def breathe(self):
        print("Mammal breathes")
class Dog(Animal, Mammal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.eat()
d.breathe()
d.sound()



class Teacher:
    def teach(self):
        print("Teaching")
class Artist:
    def paint(self):
        print("Painting")
class CreativePerson(Teacher, Artist):
    pass
cp = CreativePerson()
cp.teach()
cp.paint()



class Vehicle:
    def wheels(self):
        print("Vehicle has wheels")
class Engine:
    def start(self):
        print("Engine starts")
class Car(Vehicle, Engine):
    pass
c = Car()
c.wheels()
c.start()



class Father:
    def skills(self):
        print("Father skills")
class Mother:
    def skills(self):
        print("Mother skills")
class Child(Father, Mother):
    pass
ch = Child()
ch.skills()



class Phone:
    def call(self):
        print("Calling")
class Camera:
    def snap(self):
        print("Snapping photo")
class SmartPhone(Phone, Camera):
    pass
sp = SmartPhone()
sp.call()
sp.snap()



class Writer:
    def write(self):
        print("Writing book")
class Blogger:
    def blog(self):
        print("Writing blog")
class Author(Writer, Blogger):
    pass
a = Author()
a.write()
a.blog()



class Engine:
    def start(self):
        print("Engine starts")
class Wheels:
    def roll(self):
        print("Wheels roll")
class Bike(Engine, Wheels):
    def drive(self):
        print("Bike drives")
b = Bike()
b.start()
b.roll()
b.drive()