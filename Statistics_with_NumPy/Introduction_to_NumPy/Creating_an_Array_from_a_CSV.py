"""
INTRODUCTION TO NUMPY
Creating an Array from a CSV
Typically, you won’t be entering data directly into an array. Instead, you’ll be importing the data from somewhere else.

We’re able to transform CSV (comma-separated values) files into arrays using the np.genfromtxt() function:

Consider the following CSV, sample.csv,

34,9,12,11,7
We can import this into a NumPy array using the following code:

csv_array = np.genfromtxt('sample.csv', delimiter=',')
Note that in this case, our file sample.csv has values separated by commas, so we use delimiter=',', but sometimes you’ll find files with other delimiters, the most common being tabs or colons.

Once imported, this CSV will create the array

>>> csv_array
array([34, 9, 12, 11, 7])
"""
import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.genfromtxt("test_2.csv", delimiter = ",")