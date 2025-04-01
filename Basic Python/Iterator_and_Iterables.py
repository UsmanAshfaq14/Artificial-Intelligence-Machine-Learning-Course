#1. Iterable
# Define a custom iterator class called Counter.
class Counter:
    def __init__(self, start, end):
        self.current = start      # Initialize the counter with a starting value.
        self.end = end            # Set the ending value.

    def __iter__(self):
        return self               # The iterator is the object itself.

    def __next__(self):
        if self.current > self.end:
            raise StopIteration   # No more items: signal the end of iteration.
        else:
            result = self.current  # Store the current value.
            self.current += 1      # Move to the next value.
            return result          # Return the current value.

# Create an instance of Counter that counts from 1 to 5.
counter = Counter(1, 50)
for number in counter:
    print("Counter value:", number)
# Output:
# Counter value: 1
# Counter value: 2
# Counter value: 3
# Counter value: 4
# Counter value: 5

#2. Iterator
#list of numbers
my_list = [4, 7, 0, 3]
#iterator
my_iter = iter(my_list)
#iterating through the list
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


