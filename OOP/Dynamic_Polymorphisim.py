# Base class
class Animal:
    def speak(self):
        # Dynamic polymorphism: Subclasses should override this method.
        # raise NotImplementedError("Subclasses must implement speak()")
        print("Animal Sound")

# Subclass Dog overrides the speak() method.
class Dog(Animal):
    def speak(self):
        print("Bark")

# Subclass Cat overrides the speak() method.
class Cat(Animal):
    def speak(self):
        print("Meow")

# A function that expects an object of type Animal (or its subclass).
def animal_sound(animal):
    # Dynamic polymorphism: the correct speak() is called based on the object's actual type.
    animal.speak()
A1 = Animal()
# Create a list of animals (different subclasses).
animals = [Dog(), Cat()]
animal_sound(A1)

# Iterate through the list and call animal_sound() on each.
for animal in animals:
    animal_sound(animal)
