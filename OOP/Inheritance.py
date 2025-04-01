# --- Multilevel Inheritance Example ---
class Animal:
    def eat(self):
        print("Animal is eating.")

class Mammal(Animal):
    def walk(self):
        print("Mammal is walking.")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking.")

# Hierarchical Inheritance
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class Truck(Vehicle):
    def haul(self):
        print("Truck is hauling.")
        

# --- Multiple Inheritance and MRO Example ---
class Father:
    def skills(self):
        print("Father: Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother: Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        # This method overrides both parent's skills,
        # but we can use super() to call the next method in the MRO.
        print("Child: Sports, Music")
        super().skills()  # Calls the next method in the MRO

# --- Testing the Inheritance Examples ---
print("Multilevel Inheritance Example:")
dog = Dog()
dog.eat()     # Inherited from Animal
dog.walk()    # Inherited from Mammal
dog.bark()    # Defined in Dog

print("\nHierarchical Inheritance Example:")
car = Car()
truck = Truck()
car.move()    # Inherited from Vehicle
car.drive()   # Defined in Car
truck.move()  # Inherited from Vehicle
truck.haul()  # Defined in Truck

print("\nMultiple Inheritance Example and MRO:")
child = Child()
child.skills()  # Calls Child.skills() then via super() Father.skills() based on MRO
print("Method Resolution Order for Child:", Child.__mro__)
