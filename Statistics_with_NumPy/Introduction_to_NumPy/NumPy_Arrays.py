"""
INTRODUCTION TO NUMPY
NumPy Arrays
NumPy includes a powerful data structure known as an array. A NumPy array is a special type of list. It’s a data structure that organizes multiple items. Each item can be of any type (strings, numbers, or even other arrays).

Arrays are most powerful when they are used to store numbers. This is because arrays give us special ways of performing mathematical operations that are both simpler to write and more efficient computationally. We’ll get more into this later.

A NumPy array looks a lot like a Python list:

my_array = np.array([1, 2, 3, 4, 5, 6])
We can transform a regular list into a NumPy array by using np.array() and saving the value to a new variable:

my_list = [1, 2, 3, 4, 5, 6]
my_array = np.array(my_list)
"""
import numpy as np
test_1 = np.array([92, 94, 88, 91, 87])