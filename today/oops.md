# Python and Its OOP Concepts

## Overview of OOP

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications. Objects can contain data (attributes) and code (methods). OOP aims to increase code reusability, scalability, and maintainability.

### key Concepts of OOP in Python

### Classes and Objects

`Class`: A blueprint for creating objects. It defines attributes and methods.
`Object`: An instance of a class. It contains real values instead of variables.

```python

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy says Woof!
```

    Attributes:
    
    Instance Attributes: Specific to an instance.
    Class Attributes: Shared across instances.
    Private Attributes: Intended for internal use.
    
    Methods:
    
    Instance Methods: Operate on instances.
    Class Methods: Operate on the class itself.
    Static Methods: Independent of class/instance context.

### Encapsulation

The bundling of data and methods that operate on that data within one unit (class). It restricts direct access to some of an object's components.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Output: 100
```

### Inheritance

The mechanism by which one class can inherit attributes and methods from another class. It promotes code reusability.

```python

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

my_animal = Dog()
print(my_animal.speak())  # Output: Dog barks
```

### Polymorphism

The ability to use a common interface for different underlying forms (data types). In Python, this is often achieved through method overriding.

```python
class Cat(Animal):
    def speak(self):
        return "Cat meows"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Output: Dog barks
animal_sound(Cat())  # Output: Cat meows
```

### Abstraction

The concept of hiding the complex reality while exposing only the necessary parts. In Python, this can be implemented using abstract classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
```

```python

class Britania: # company
 product = "honey" # class attribute

 def __init__(self):
  self.resource = "bee" # instance attribute

 def __str__(self):
  # This method will get called.
  # only in below scenarios
  # obj = Britania()
  # print(obj)
  # >>> str(obj)
  return "Britania object"

 def fn1(self): # instance method
  # 🏷️ In instance method
  #   mostly we will access all 
  #   instance attributes
  #  and perform logics
  return self.resource
 
 def __repr__(self): 
  # This method will get called.
  # only in below scenarios
  # obj = Britania()
  # >>> obj
  # output is `Britania object in interpreter`
  return "Britania object in interpreter"

 @classmethod 
 def fn2(cls):
  # 🏷️ IN class method, we will only
  #     access Class attributes
  #     and perform logics
  return cls.product 
 
 @staticmethod
 def fn3():
  # 🏷️ IN static method, we won't access
  #     Either class attributes nor
  #     instance attributes.
  #     But we have to perform some logic
  return "I am Britania"

obj = Britania()
print(obj.fn1())
# Britania.fn1() # ERROR
# Above ☝️ is accessing instance method.
# we can only access it using 
# instance/object
print(obj.fn2()) 
print(Britania.fn2())
# Above ☝️ is accessing class method.
# we can access it using both instance and 
# Class name.
print(obj.fn3())
print(Britania.fn3())
# Above ☝️ is accessing static method.
# we can access it using both instance & Class name.
```
