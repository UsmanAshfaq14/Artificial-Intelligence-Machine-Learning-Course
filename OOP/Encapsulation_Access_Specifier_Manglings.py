# program to illustrate public access modifier in a class

#1. Public Access Specifier
class Geek:

    # constructor
    def __init__(self, name, age):

        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):

        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("R2J", 20)

# finding all the fields and methods which are present inside obj
print("List of fields and methods inside obj:", dir(obj))

# accessing public data member
print("Name:", obj.geekName)

# calling public member function of the class
obj.displayAge()

#Output:
"""List of fields and methods inside obj: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'displayAge', 'geekAge', 'geekName']
Name: R2J
Age:  20"""

#2. Private Access Specifier
# program to illustrate private access modifier in a class

class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):

        # accessing private data members
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    # public member function
    def accessPrivateFunction(self):

        # accessing private member function
        self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")

print(dir(obj))
print("")

# Throws error
# obj.__name
# obj.__roll
# obj.__branch
# obj.__displayDetails()

# To access private members of a class
print(obj._Geek__name)
print(obj._Geek__roll)
print(obj._Geek__branch)
obj._Geek__displayDetails()

print("")

# calling public member function of the class
obj.accessPrivateFunction()

#Output:
"""'_Geek__branch', '_Geek__displayDetails', '_Geek__name', '_Geek__roll', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'accessPrivateFunction']

R2J
1706256
Information Technology
Name: R2J
Roll: 1706256
Branch: Information Technology

Name: R2J
Roll: 1706256
Branch: Information Technology"""

#3. Protected Access Specifier
# program to illustrate private access modifier in a class

#Protected Acess Specifier in Python:
class Geek:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):

        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek1(Geek):

    # constructor
    def __init__(self, name, roll, branch):
        Geek.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):

        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek1("R2J", 1706256, "Information Technology")
# calling public member functions of the class
obj.displayDetails()
#Output:
"""Name:  R2J
Roll:  1706256
Branch:  Information Technology"""

"""Difference Between Private and Protected in Python:

Private Members:

Syntax: Defined with a double underscore prefix (e.g., __var).

Name Mangling: Python renames these members internally (e.g., __var in class MyClass becomes _MyClass__var), making direct access from outside the class harder.

Intent: Indicates that the member is meant for internal use only, not to be accessed or overridden by subclasses or external code.

Protected Members:

Syntax: Defined with a single underscore prefix (e.g., _var).

Convention Only: They are not enforced by Python—this is simply a convention signaling that these members are for internal use within the class and its subclasses.

Intent: Suggests caution when accessing these members from outside the class; they can be accessed, but you should treat them as non-public. Subclasses are encouraged to use them, but external code should avoid it."""


