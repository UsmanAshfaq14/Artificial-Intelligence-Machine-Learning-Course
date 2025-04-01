# Magic Methods / Dunder Functions
In Python, magic methods (also known as dunder methods) are special methods that have double underscores at the beginning and end of their names. These methods are used to define how objects of a class behave when certain operations are performed on them. For example, the `__init__` method is called when an object is created, and the `__str__` method is called when an object is converted to a string.



---

### Overall Description of Magic Methods / Dunder Functions

Magic methods are special methods in Python that begin and end with double underscores (e.g., `__init__`, `__add__`, `__str__`). They allow you to define or “override” the default behavior of objects for built-in operations. For example, by implementing `__add__`, you can customize how the `+` operator works for your custom class. These methods enable operator overloading, provide hooks for object creation and deletion, and support many other built-in behaviors in Python.

---
### 7 types of Operators in Python

- Arithmetic Operators: +, -, *, /, %, ** (exponentiation), // (floor division).
- Comparison Operators: ==, !=, <, >, <=, >=.
- Logical Operators: and, or, not.
- Bitwise Operators: &, |, ^, ~, <<, >>.
- Assignment Operators: =, +=, -=, etc.
- Identity Operators: is, is not.
- Membership Operators: in, not in.

--- 

### Binary Operators

| Operator | Magic Method              |
|----------|---------------------------|
| +        | `__add__(self, other)`    |
| -        | `__sub__(self, other)`    |
| *        | `__mul__(self, other)`    |
| /        | `__truediv__(self, other)`|
| //       | `__floordiv__(self, other)`|
| %        | `__mod__(self, other)`    |
| **       | `__pow__(self, other)`    |
| >>       | `__rshift__(self, other)` |
| <<       | `__lshift__(self, other)` |
| &        | `__and__(self, other)`    |
| \|       | `__or__(self, other)`     |
| ^        | `__xor__(self, other)`    |

---

### Comparison Operators

| Operator | Magic Method              |
|----------|---------------------------|
| <        | `__lt__(self, other)`     |
| >        | `__gt__(self, other)`     |
| <=       | `__le__(self, other)`     |
| >=       | `__ge__(self, other)`     |
| ==       | `__eq__(self, other)`     |
| !=       | `__ne__(self, other)`     |

---

### Assignment Operators

| Operator | Magic Method              |
|----------|---------------------------|
| -=       | `__isub__(self, other)`   |
| +=       | `__iadd__(self, other)`   |
| *=       | `__imul__(self, other)`   |
| /=       | `__idiv__(self, other)` or `__itruediv__(self, other)` |
| //=      | `__ifloordiv__(self, other)` |
| %=       | `__imod__(self, other)`   |
| **=      | `__ipow__(self, other)`   |
| >>=      | `__irshift__(self, other)`|
| <<=      | `__ilshift__(self, other)`|
| &=       | `__iand__(self, other)`   |
| \|=      | `__ior__(self, other)`    |
| ^=       | `__ixor__(self, other)`   |

---

### Unary Operators

| Operator | Magic Method             |
|----------|--------------------------|
| -        | `__neg__(self)`          |
| +        | `__pos__(self)`          |
| ~        | `__invert__(self)`       |

---

This structured overview helps you see how Python lets you customize the behavior of your objects when used with these operators by implementing the corresponding magic methods.

### Example:
```
# Python program which attempts to
# overload ~ operator as binary operator


class A:
    def __init__(self, a):
        self.a = a

    # Overloading ~ operator, but with two operands
    def __invert__(self):
        return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)

print(~ob1)

# Output:
# This is the ~ operator, overloaded as binary operator.
```