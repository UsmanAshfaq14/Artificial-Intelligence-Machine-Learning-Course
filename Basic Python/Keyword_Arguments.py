def greet(name, message="The number you have dailed is powered off"):
    print(f"{message}, {name}!")

# Using keyword arguments
greet(name="Alice", message="Hi")
greet(message="Good morning", name="Bob")
greet(name="Charlie")  # Uses the default message
