# Classroom Assignment: Analyzing Hourly Temperature Data with NumPy

## Overview

In this assignment, you will simulate and analyze hourly temperature data collected from a weather sensor. The goal is to get hands-on experience with the fundamental features of NumPy, including array creation, querying attributes, performing arithmetic and indexing operations, reshaping arrays, and combining data.

Use the following tasks to guide you through the assignment. Complete each task step by step, and add your own comments to explain what each section of your code is doing.

## Tasks

### Task 1: Creating Arrays

1. **From Python Lists**  
   - Create a one-dimensional NumPy array named `temp_day1` representing the hourly temperature readings for a single day (use at least 8 values).  
   - Example: `temp_day1 = np.array([temp1, temp2, ..., temp8])`

2. **Using Built-in Methods**  
   - Use `np.arange` to create an array named `hours` that represents the hours of the day (e.g., from 0 to 23 if you want to simulate a full day).
   - Use `np.linspace` to generate an array that might represent the gradual temperature increase from early morning to noon (you could create 5 sample points between a starting temperature and a peak temperature).

3. **Random Data Generation**  
   - Simulate random noise to mimic sensor fluctuations. Use `np.random.rand` to generate a small array of noise values, and add this noise to a baseline temperature to create a more realistic temperature array for a day.

### Task 2: Exploring Array Attributes and Methods

1. **Check Attributes**  
   - Print the array’s shape, data type (`dtype`), size, and number of dimensions (`ndim`) for your `temp_day1` array.
   - Use methods like `temp_day1.shape` and `temp_day1.dtype` and explain what each attribute represents.

2. **Reshape Operation**  
   - Reshape your `temp_day1` array to a 2D array (for example, a single row with multiple columns or a column vector).  
   - Explain in comments why reshaping might be useful (e.g., aligning data for mathematical operations).

### Task 3: Basic Array Operations

1. **Finding Extremes**  
   - Use NumPy functions to find the maximum and minimum temperatures of the day.
   - Determine the indices (using `argmax` and `argmin`) at which these extremes occur.

2. **Arithmetic Operations**  
   - Create two arrays: one for day 1 (`temp_day1`) and another for day 2 (`temp_day2`), with simulated temperature readings for a second day.
   - Perform element-wise addition, subtraction, multiplication, or division between these arrays (for example, calculate the difference between the two days).
   - Use a brief comment to explain what each arithmetic operation shows in the context of temperature differences.

### Task 4: Manipulating Arrays

1. **Copying, Appending, and Inserting**  
   - Make a copy of the `temp_day1` array using `np.copy()`.
   - Append a new temperature reading (simulating an extra sensor reading) to the copied array.
   - Insert a temperature value at a specific index (simulate manual correction for a suspected erroneous value).

2. **Sorting and Deleting**  
   - Sort the array containing your updated day’s temperatures.
   - Delete the outlier temperature value (using `np.delete()`) if you suspect one reading is too low or too high compared to the rest.

3. **Concatenation and Splitting**  
   - Concatenate `temp_day1` and `temp_day2` to create a new array representing data from two days.
   - Use `np.split()` to divide the concatenated array back into separate day arrays.
   - Explain when concatenation and splitting might be useful in real-time data analysis (for example, combining data from multiple sensors and later analyzing each sensor’s readings separately).

### Task 5: Real-Time Data Analysis

1. **Daily Summary**  
   - For each day's data (you may simulate a week’s data by concatenating 7 arrays representing different days), compute:
     - The overall daily average temperature.
     - The highest temperature and the time (index) it occurred.
     - The lowest temperature and the time (index) it occurred.

2. **Broadcasting Example (Optional)**  
   - Use broadcasting to add a fixed calibration offset (e.g., add 0.5 degrees Celsius) to all temperature readings across a day.
   - Explain the benefit of broadcasting in this scenario.

## Deliverables

- A well-commented Python script or Jupyter Notebook that completes all tasks.
- The final submission should include comments that explain:
  - What each section of the code does.
  - How the operations (reshaping, sorting, concatenation, etc.) help in analyzing temperature data.
  - The overall insights you can gather from your computed daily summaries.

## Evaluation Criteria

- **Correctness:** Code should run without errors and produce the expected results.
- **Clarity:** Code should be well-organized and commented, explaining how each operation is used.
- **Real-World Relevance:** The assignment should demonstrate your understanding of how NumPy operations apply to a real-time data analysis problem.
- **Creativity:** Additional insights, improvements, or visualizations (if any) that help in further understanding the data will be appreciated.

---

### Tips for Students

- Review the functions you used during class (such as `np.array`, `np.arange`, `np.linspace`, `np.random.rand`, `reshape`, `max`, `min`, etc.) before starting this assignment.
- Think about how you would handle data from a real sensor and the need to clean, analyze, and interpret that data.
- Work in small steps and test your code frequently to ensure everything works as expected.

Good luck, and have fun exploring data with NumPy!
