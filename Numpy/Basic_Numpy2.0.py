import numpy as np

# Create a sample 2D array (matrix) for demonstration.
sample_data = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
                        
# Save the array to a file using NumPy's save function.
# This saves the file in binary format with a '.npy' extension.
np.save('sample_data.npy', sample_data)
print("Array saved to 'sample_data.npy'.")

# Load the saved array from file.
loaded_data = np.load('sample_data.npy')
print("Loaded data:")
print(loaded_data)


# -----------------------------------------------------------------------------
# Section 2: NumPy Indexing and Selection
# -----------------------------------------------------------------------------

# a) Indexing a 2D array:
# Access the element in the 2nd row and 3rd column.
# (Remember: Indexing starts at 0, so row 2 is index 1, and column 3 is index 2.)
element = loaded_data[1, 2]
print("\nElement at row 2, column 3:", element)

# b) Logical (Boolean) Selection:
# Select all elements in the array greater than 5.
# This creates a new array with only the elements that satisfy the condition.
selected_elements = loaded_data[loaded_data > 5]
print("Elements greater than 5:", selected_elements)


# -----------------------------------------------------------------------------
# Section 3: Broadcasting
# -----------------------------------------------------------------------------

# Broadcasting allows operations on arrays with different shapes.
# For example, adding a 1D array (vector) to every row of a 2D array.

# Define a 2D array (matrix).
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
                   
# Define a 1D array (vector) with three elements.
vector = np.array([10, 20, 30])

# The vector is automatically "broadcasted" so that it can be added to each row of the matrix.
broadcast_result = matrix + vector
print("\nResult of broadcasting addition:")
print(broadcast_result)


# -----------------------------------------------------------------------------
# Section 4: Type Casting
# -----------------------------------------------------------------------------

# Type casting changes the data type of an array.
# Create an array of floating-point numbers.
float_array = np.array([1.7, 2.8, 3.9])

# Convert the float array to an integer array using astype().
# This truncates the decimal part.
int_array = float_array.astype(int)
print("\nOriginal float array:", float_array)
print("Converted to integer array:", int_array)


# -----------------------------------------------------------------------------
# Section 5: Arithmetic Operations
# -----------------------------------------------------------------------------

# Define two arrays of the same shape.
array_a = np.array([10, 20, 30])
array_b = np.array([1, 2, 3])

# Element-wise addition.
addition = array_a + array_b
print("\nAddition:", addition)

# Element-wise subtraction.
subtraction = array_a - array_b
print("Subtraction:", subtraction)

# Element-wise multiplication.
multiplication = array_a * array_b
print("Multiplication:", multiplication)

# Element-wise division.
division = array_a / array_b
print("Division:", division)

# Element-wise exponentiation: each element in array_a is raised to the power 
# of the corresponding element in array_b.
exponentiation = array_a ** array_b
print("Exponentiation (a^b):", exponentiation)


# -----------------------------------------------------------------------------
# Section 6: Universal Array Functions
# -----------------------------------------------------------------------------

# Create an array to demonstrate universal functions.
u_array = np.array([1, 4, 9, 16])

# Calculate the square root of each element.
sqrt_result = np.sqrt(u_array)
print("\nSquare root of u_array:", sqrt_result)

# Apply the exponential function (e^x) on each element.
exp_result = np.exp(u_array)
print("Exponential of u_array:", exp_result)

# Calculate the sine for each element.
sin_result = np.sin(u_array)
print("Sine of u_array:", sin_result)

# Determine the maximum value using a universal function.
max_value = np.max(u_array)
print("Maximum value in u_array:", max_value)
