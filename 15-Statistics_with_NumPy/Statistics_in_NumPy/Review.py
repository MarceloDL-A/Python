"""
Review
Let's review! In this lesson, you learned how to use NumPy to analyze single-variable datasets. Here's what we covered:

Using the np.sort method to locate outliers.
Calculating central positions of a dataset using np.mean and np.median.
Understanding the spread of our data using percentiles and the interquartile range.
Finding the standard deviation of a dataset using np.std.
In our next lesson, we'll continue our exploration of NumPy and see how we can use it to analyze different statistical distributions. Follow the checkpoints below to practice what you just learned!
"""
import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

"""
A group of citizen scientists has been collecting data on rainfall in Seattle. They've presented their data to you in the form of monthly averages, measured in inches.

Month	Avg. Precipitation
January	5.21
February	3.76
March	3.27
April	2.35
May	1.89
June	1.55
July	0.65
August	1.06
September	1.72
October	3.36
November	4.82
December	5.11
We've saved this data to the NumPy array rainfall.
"""

"""
Find the mean of the rainfall array and save it to the variable rain_mean.
"""
rain_mean = np.mean(rainfall)
print("rain_mean: " + str(rain_mean))

"""
Find the median of the rainfall array and save it to the variable rain_median.
"""
rain_median = np.median(rainfall)
print("rain_median: " + str(rain_median))

"""
Find the 25th and the 75th percentiles of the original rainfall array and save them to the arrays first_quarter and third_quarter, respectively.
"""
first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)
print("first_quarter: " + str(first_quarter))
print("third_quarter: " + str(third_quarter))

"""Calculate the interquartile range and save it to the variable, interquartile_range.
"""
interquartile_range = third_quarter - first_quarter
print("interquartile_range: " + str(interquartile_range))

"""
Determine the standard deviation of the set and save it to the variable rain_std.
"""
rain_std = np.std(rainfall)
print("rain_std: " + str(rain_std))





