# Class in Python
# Define a class
class Person:
    # Class variable: shared by all instances
    species = "Homo sapiens"

    # Constructor: initializes new instances
    def __init__(self, name, age):
        # Instance variables: unique for each object
        self.name = name
        self.age = age
        print(f"{self.name} has been created.")

    # Instance method: operates on instance variables
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Class method: operates on class variable
    @classmethod
    def show_species(cls):
        print(f"All persons are of the species: {cls.species}")

    # Destructor: called when an object is deleted
    def __del__(self):
        print(f"{self.name} is being deleted.")

# Create two Person instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Call instance methods
person1.say_hello()
person2.say_hello()

# Access class method to show the shared class variable
Person.show_species()

# Delete one instance (triggering destructor)
del person1
