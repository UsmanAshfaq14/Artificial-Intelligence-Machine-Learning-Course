#Method Resolution Order

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(C,B):
    def __init__(self):
        print("D")
        super().__init__()
d = D()
#D B C A
#B C A
#C A
#A
print("Method Resolution Order")
print(D.__mro__)