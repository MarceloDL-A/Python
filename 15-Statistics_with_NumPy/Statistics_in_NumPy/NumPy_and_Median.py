"""
INTRODUCTION TO STATISTICS WITH NUMPY
NumPy and Median
Another key metric that we can use in data analysis is the median. The median is the middle value of a dataset that's been ordered in terms of magnitude (from lowest to highest).

Let's look at the following array:

np.array( [1, 1, 2, 3, 4, 5, 5])
In this example, the median would be 3, because it is positioned half-way between the minimum value and the maximum value.

If the length of our dataset was an even number, the median would be the value halfway between the two central values. So in the following example, the median would be 3.5:

np.array( [1, 1, 2, 3, 4, 5, 5, 6])
But what if we had a very large dataset? It would get very tedious to count all of the values. Luckily, NumPy also has a function to calculate the median, np.median:

>>> my_array = np.array([50, 38, 291, 59, 14])
>>> np.median(my_array)
50.0
"""
import numpy as np

large_set = np.genfromtxt('household_income.csv', delimiter=',')
"""
You're doing some research on household incomes and come across the following small dataset:

10100, 35500, 105000, 85000, 25500, 40500, 65000
Calculate the median, without using Numpy, and save the value to the variable small_set_median.
"""
small_set_median = 40500

"""
As you continue your research, you come across a trove of research in the file household_income.csv, which we've already included in your program and saved as large_set.

Use NumPy to find the median of large_set and save the result to the variable large_set_median.
"""
large_set_median = np.median(large_set)

"""Print the results of small_set_median and large_set_median to the terminal.
"""
print("small_set_median: " + str(small_set_median))
print("large_set_median: " + str(large_set_median))