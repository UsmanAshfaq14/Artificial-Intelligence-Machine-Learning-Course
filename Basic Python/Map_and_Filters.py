#1. Lambda
#In Python, an anonymous function means that a function is without a name.
# As we already know that def keyword is used to define the normal functions
# the lambda keyword is used to create anonymous functions.
#Create a Lambda function that takes two arguments and returns their sum.
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output:  8

#2. Map
#The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
#It takes two arguments: a function and a sequence.
#The function is applied to each item of the sequence (list, tuple etc.) in order.
#The map() function returns a map object, which is an iterator.
# define a list
numbers = [1, 2, 3, 4, 5]
# use map to double each item in the list
doubled_numbers = map(lambda x: x * 2, numbers)
#3. Filter
#The filter() function filters a given sequence with the help of a function that tests each element in the sequence to be true or not.
#The filter() function returns a filter object, which is an iterator.
# use filter to get only even numbers from the list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
