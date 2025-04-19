# Import the NumPy library
import numpy as np

# ----------------------------------------------------------------------
# 1. Creating NumPy Arrays
# ----------------------------------------------------------------------

# a) Creating an array from a Python list.
# The np.array() function converts the given list into a NumPy array.
python_list = [1, 2, 3, 4, 5]
array_from_list = np.array(python_list)
print("Array from list:", array_from_list)

# b) Creating an array using a built-in method: np.arange.
# np.arange(start, stop, step) creates an array with values starting from 'start'
# up to (but not including) 'stop' with the specified 'step'.
array_arange = np.arange(0, 10, 2)  # Creates [0, 2, 4, 6, 8]
print("Array using np.arange:", array_arange)

# c) Creating an array using a built-in method: np.linspace.
# np.linspace(start, stop, num) creates an array of 'num' equally spaced values between 'start' and 'stop'.
array_linspace = np.linspace(0,5, 5)  # Creates 5 numbers between 0 and 1
print("Array using np.linspace:", array_linspace)

# d) Creating an array with random values using np.random.
# np.random.rand(rows, columns) creates a 2D array with the given shape with random numbers between 0 and 1.
random_array = np.random.rand(3, 3)
print("Random Array (3x3):\n", random_array)

# ----------------------------------------------------------------------
# 2. Array Attributes and Methods
# ----------------------------------------------------------------------

# Using array_from_list for demonstration, and also using random_array for numeric methods.

# a) Reshape: Changing the dimensions of an array without changing its data.
# Here, we reshape a 1D array into a 2D array (1 row and 5 columns).
reshaped_array = np.reshape(array_from_list, (1, 5))
print("\nReshaped Array (1x5):", reshaped_array)

# b) Finding maximum and minimum values in an array.
# Using the random_array to show these operations.
max_value = random_array.max()
min_value = random_array.min()
print("Maximum of random_array:", max_value)
print("Minimum of random_array:", min_value)

# c) argmax and argmin: Finding the indices of the maximum and minimum values.
# These return the index in the flattened version of the array.
argmax_index = random_array.argmax()
argmin_index = random_array.argmin()
print("Index of max value (flattened):", argmax_index)
print("Index of min value (flattened):", argmin_index)

# d) Other useful attributes:
# - shape: The dimensions of the array.
# - dtype: The data type of the array elements.
# - size: The total number of elements in the array.
# - ndim: The number of dimensions of the array.
print("Shape of random_array:", random_array.shape)
print("Data type (dtype) of random_array:", random_array.dtype)
print("Total number of elements (size) in random_array:", random_array.size)
print("Number of dimensions (ndim) of random_array:", random_array.ndim)

# ----------------------------------------------------------------------
# 3. Operations on Arrays
# ----------------------------------------------------------------------

# a) Copying an array.
# Using np.copy to create an independent copy of array_from_list.
copy_array = np.copy(array_from_list)
print("\nCopied array:", copy_array)

# b) Append and Insert operations:
# - np.append() adds an element to the end of an array.
# - np.insert() adds an element at a specific index.
appended_array = np.append(array_from_list, 6)
print("Array after appending 6:", appended_array)

# Insert 99 at index position 2 in the original array.
inserted_array = np.insert(array_from_list, 2, 99)
print("Array after inserting 99 at index 2:", inserted_array)

# c) Sorting an array.
# np.sort() returns a sorted copy of the array.
sorted_array = np.sort(appended_array)
print("Sorted array:", sorted_array)

# d) Removing/Deleting an element from an array.
# np.delete() removes the element at the specified index.
# Here, we delete the element at index 2 from inserted_array.
deleted_array = np.delete(inserted_array, 2)
print("Array after deleting element at index 2:", deleted_array)

# e) Combining/Concatenating arrays.
# We combine two arrays using np.concatenate(), which joins arrays along an existing axis.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
concatenated_array = np.concatenate((array1, array2))
print("Concatenated array:", concatenated_array)

# f) Splitting an array.
# np.split() splits an array into multiple sub-arrays.
# Here, we split the concatenated array into 2 equal parts.
split_arrays = np.split(concatenated_array, 3)
print("Arrays after splitting concatenated array into 2 parts:", split_arrays)
