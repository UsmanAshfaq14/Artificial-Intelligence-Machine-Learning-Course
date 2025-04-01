# Operator Overloading
# Python Program illustrate how 
# to overload an binary + operator
# And how it actually works
"""
class A:
    def __init__(self, a):
        self.a = a

    # adding two objects 
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("Hello")
ob4 = A("World")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2)) 
print(A.__add__(ob3,ob4)) 
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

"""
# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading.

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

     # adding two objects 
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)



