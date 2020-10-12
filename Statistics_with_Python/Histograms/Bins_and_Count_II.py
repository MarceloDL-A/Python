"""
HISTOGRAMS
Bins and Count II
A count is the number of values that fall within a bin’s range. For example, if 100 customers arrive at your grocery store between midnight (0) and 6 am (6), your count for that bin is equal to 100.

Exercise Class Example
In the example below, we have an array with ten values in it, each representing the age of a person in an exercise class. We want to calculate the number of students who are in their 20s, 30s, 40s, 50s, and 60s.

exercise_ages = np.array([20, 27, 45, 69, 34, 52, 42, 22, 34, 26])
Question: What is our range?

Answer: Between 20 and 69.
Question: How many bins do we need?

Answer: The bins are 20s, 30s, 40s, 50s, and 60s, so we need five bins, each covering ten years.
The table below shows the number of people in each binned age group:

20-29	30-39	40-49	50-59	60-69
4	2	2	1	1
"""
# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

"""
The store manager checks the age of all loaves on the shelves every three days, with the freshest loaves displayed on the most obvious shelf, and the oldest loaves being thrown out.

Because of this pattern, the store manager wants to know the number of loaves in each of three different bins.

Count the number of loaves that have values of 0, 1, or 2, and save it to days_old_012.
Count the number of loaves that have values of 3, 4, or 5, and save it to days_old_345.
Count the number of loaves that have values of 6, 7, or 8, and save it to days_old_678.
"""
# Count the values in each bin 
days_old_012 = 4
days_old_345 = 2
days_old_678 = 4

# Printing the values
print("Between 0 and 2 days: " + str(days_old_012))
print("Between 3 and 5 days: " + str(days_old_345))
print("Between 6 and 8 days: " + str(days_old_678))