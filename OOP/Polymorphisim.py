#Polymorphism
# Polymorphism is a Greek word, which means "many-shapes". In programming, polymorphism means that a name can have many forms.
# In Python, polymorphism is achieved through method overriding.
# Method overriding occurs when a derived class has a definition for one of the methods of the base class.
# This is often used in the context of inheritance.
# Python does not support method overloading in the traditional sense.
# Method overloading occurs when a class has multiple methods with the same name but different parameters.
# This is often used in the context of operator overloading.
# Method overriding is a form of polymorphism.
# Base class
class Animal:
    def make_sound(self):
        # This method is expected to be overridden in derived classes.
        # raise NotImplementedError("Subclasses must implement this method.")
        print("Animal sound")

# Derived class Dog overriding make_sound()
class Dog(Animal):
    def make_sound(self):
        print("Bark")

# Derived class Cat overriding make_sound()
class Cat(Animal):
    def make_sound(self):
        print("Meow")

# A function that demonstrates polymorphism:
def animal_sound(animal):
    # This function expects an object that has a make_sound() method.
    animal.make_sound()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the animal_sound function on different types of animals
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
