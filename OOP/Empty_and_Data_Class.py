#1. Empty Class:
"""class Empty:
    pass

# Create an instance of the empty class.
empty_instance = Empty()
print("Empty instance created:", empty_instance)
# The empty_instance is an instance of the Empty class."""


#2. Data classes:
#Data classes are a convenient way to define classes that primarily store data. They are introduced in Python 3.7 and provide a way to automatically generate special methods like __init__, __repr__, and __eq__ based on the class attributes. Here's an example of a data class:
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# Create an instance of the data class.
person = Person(name="Alice", age=30)
print("Person:", person)
