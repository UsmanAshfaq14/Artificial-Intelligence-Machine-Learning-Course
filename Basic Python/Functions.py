#1. Functions 
# Define a simple function that greets a person.
def greet(name):
    """Return a greeting message for the given name."""
    return "Hello, " + name + "!"

# Call the function with the argument "Alice" and print the result.
print(greet("Alice"))
#-----------------------------------------------------------
#2. Functions and variable scope
# Global variable defined outside any function.
x = "global value"

def my_function():
    # Local variable inside the function, shadowing the global variable.
    x = "local value"
    print("Inside function, x =", x)

# Call the function and print the global variable afterward.
my_function()                 
print("Outside function, x =", x)
#-----------------------------------------------------------
#3. Inner/Nested functions
# Define an outer function that creates and returns an inner function.
def outer_function(message):
    # Inner function that uses the message from the outer scope.
    def inner_function():
        return "Inner says: " + message
    # Return the inner function itself.
    return inner_function

# Get the inner function by calling the outer function.
greet_func = outer_function("Hello, World!")
# Now call the inner function.
print(greet_func())
#-----------------------------------------------------------

