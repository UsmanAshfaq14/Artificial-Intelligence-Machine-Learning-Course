from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass  # Abstract method; no implementation here

# Concrete subclass that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the abstract method
    def area(self):
        return self.width * self.height

# Uncommenting the following line will raise an error because Shape cannot be instantiated.
# shape = Shape()

# Instantiate a Rectangle (cannot instantiate Shape directly)
rect = Rectangle(5, 10)
print("Rectangle Area:", rect.area())

