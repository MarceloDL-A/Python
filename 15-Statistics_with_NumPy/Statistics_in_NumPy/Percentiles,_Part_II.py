"""
INTRODUCTION TO STATISTICS WITH NUMPY
Percentiles, Part II
Some percentiles have specific names:

The 25th percentile is called the first quartile
The 50th percentile is called the median
The 75th percentile is called the third quartile
The minimum, first quartile, median, third quartile, and maximum of a dataset are called a five-number summary. This set of numbers is a great thing to compute when we get a new dataset.

The difference between the first and third quartile is a value called the interquartile range. For example, say we have the following array:

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
We can calculate the 25th and 75th percentiles using np.percentile:

np.percentile(d, 25)
>>> 3.5
np.percentile(d, 75)
>>> 6.5
Then to find the interquartile range, we subtract the value of the 25th percentile from the value of the 75th:

6.5 - 3.5 = 3
50% of the dataset will lie within the interquartile range. The interquartile range gives us an idea of how spread out our data is. The smaller the interquartile range value, the less variance in our dataset. The greater the value, the larger the variance.
"""
import numpy as np

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

"""
An online movie streaming company wants to know how many movies users watch in one week. At the top of the script.py, we have included sample data from 15 users in an array.

Find the 25th and 75th percentiles, and save them to the corresponding variables: first_quarter and third_quarter.
"""
first_quarter = np.percentile(movies_watched, 25)
print("first_quarter: " + str(first_quarter))
third_quarter = np.percentile(movies_watched, 75)
print("third_quarter: " + str(third_quarter))


"""
Create a variable named interquartile_range. Calculate the interquartile range and save it to this variable.
"""
interquartile_range = third_quarter - first_quarter
print("interquartile_range: " + str(interquartile_range))




