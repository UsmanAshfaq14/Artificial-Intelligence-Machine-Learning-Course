"""#1. Multiple Nested Classes
# create outer class
class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print('In outer class')
        print('Name:', self.name)

    # create a 1st Inner class
    class Dentist:
        def __init__(self):
            self.name = 'Dr. Savita'
            self.degree = 'BDS'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    # create a 2nd Inner class
    class Cardiologist:
        def __init__(self):
            self.name = 'Dr. Amit'
            self.degree = 'DM'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors()
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()"""

#2 Multilevel Nested Class
# create an outer class
class Base:

    def __init__(self):
        # create an inner class object
        self.inner = self.Inner()

    def show(self):
        print('This is an outer class')

    # create a 1st inner class

    class Inner:
        def __init__(self):
            # create an inner class of inner class object
            self.innerclassofinner = self.Innerclassofinner()

        def show(self):
            print('This is the inner class')

        # create an inner class of inner

        class Innerclassofinner:
            def show(self):
                print('This is an inner class of inner class')


# create an outer class object
# i.e.Base class object
outer = Base()
outer.show()
print()

# create an inner class object
Inner = outer.inner
Inner.show()
print()

# create an inner class of inner class object
Inner_Inner = outer.inner.innerclassofinner
Inner_Inner.show()
