"""
INTRODUCTION TO STATISTICS WITH NUMPY
Mean vs. Median
In a dataset, the median value can provide an important comparison to the mean. Unlike a mean, the median is not affected by outliers. This becomes important in skewed datasets, datasets whose values are not distributed evenly. Let's write a program that explores this idea further.
"""
"""
The company that you work for wants to know the average amount of time someone spends on the company website in minutes. We've imported this dataset into your program as time_spent.

Press 'Run' to print the data set to the terminal, and take a look at the values.
"""
import numpy as np

time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)

"""
Find the average amount of time in minutes spent on the website and save it to the variable minutes_mean.
"""
minutes_mean = np.mean(time_spent)
print("minutes_mean: " + str(minutes_mean))

"""
Now, find the median of the array and save it to the variable minutes_median.
"""
minutes_median = np.median(time_spent)
print("minutes_median: " + str(minutes_median))

"""
Take a moment to notice the difference between the two values. Which one do you think best represents the majority of the data present?

Choose the variable that represents this value, and save it to the variable best_measure.
"""
best_measure = minutes_median

