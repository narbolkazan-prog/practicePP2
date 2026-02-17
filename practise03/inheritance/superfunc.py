class A:
    def show(self):
        print("A show")
class B(A):
    def show(self):
        super().show()
        print("B show")
b = B()
b.show()


class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
c = Child()
c.greet()


class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
d = Dog()
d.speak()


class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starts")
c = Car()
c.start()


class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
s = Student("Alice", "A")
print(s.name, s.grade)


class Employee:
    def __init__(self, name):
        self.name = name
class Manager(Employee):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept
m = Manager("Bob", "HR")
print(m.name, m.dept)


class Device:
    def turn_on(self):
        print("Device on")
class Phone(Device):
    def turn_on(self):
        print("Phone booting")
        super().turn_on()
ph = Phone()
ph.turn_on()


class Writer:
    def write(self):
        print("Writer writes")
class Author(Writer):
    def write(self):
        print("Author starts writing")
        super().write()
au = Author()
au.write()


class Base:
    def filter_even(self, lst):
        return [x for x in lst if x % 2 == 0]
class Derived(Base):
    def filter_even(self, lst):
        return [x+1 for x in super().filter_even(lst)]
d = Derived()
print(d.filter_even([1,2,3,4,5]))


class Base:
    def average(self, lst):
        return sum(lst)/len(lst)
class Derived(Base):
    def average(self, lst):
        return super().average(lst) + 10
d = Derived()
print(d.average([10,20,30]))
