class Person:
    species = "Human"
    @classmethod
    def set_species(cls, name):
        cls.species = name
Person.set_species("Alien")
print(Person.species)


class Employee:
    company = "TechCorp"
    @classmethod
    def set_company(cls, name):
        cls.company = name
Employee.set_company("MegaCorp")
print(Employee.company)


class Circle:
    pi = 3.1416
    @classmethod
    def area_from_radius(cls, r):
        return cls.pi * r * r
print(Circle.area_from_radius(5))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @classmethod
    def square(cls, side):
        return cls(side, side)
r = Rectangle.square(5)
print(r.width, r.height)


class Vehicle:
    vehicles_count = 0
    def __init__(self, name):
        self.name = name
        Vehicle.vehicles_count += 1
    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicles_count
v1 = Vehicle("Car")
v2 = Vehicle("Bike")
print(Vehicle.get_vehicle_count())


class Student:
    school_name = "ABC School"
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
Student.change_school("XYZ School")
print(Student.school_name)


class Temperature:
    @classmethod
    def f_to_c(cls, fahrenheit):
        return (fahrenheit - 32) * 5/9
print(Temperature.f_to_c(77))


class Laptop:
    default_ram = 8
    def __init__(self, ram):
        self.ram = ram
    @classmethod
    def with_default_ram(cls):
        return cls(cls.default_ram)
l = Laptop.with_default_ram()
print(l.ram)


class Book:
    library_name = "Central Library"
    @classmethod
    def change_library(cls, name):
        cls.library_name = name
Book.change_library("City Library")
print(Book.library_name)


class Cat:
    @classmethod
    def sound(cls):
        return "Meow!"
print(Cat.sound())
