"""
HISTOGRAMS
Range
Histograms are helpful for understanding how your data is distributed. While the average time a customer may arrive at the grocery store is 3 pm, the manager knows 3 pm is not the busiest time of day.

Before identifying the busiest times of the day, it’s important to understand the extremes of your data: the minimum and maximum values in your dataset. With the minimums and maximums, you can calculate the range.

The range of your data is the difference between the maximum value and the minimum value in your dataset.

range = max(data)\ -\ min(data)range=max(data) - min(data)
Exercise Class Example
In the example below, we have a NumPy array with the ages of people in an exercise class. Before looking at the data, let’s think about what minimum, maximum, and range values are reasonable for a group of people in an exercise class:

The minimum cannot be below 0, because people don’t have negative ages
The maximum is probably lower than 122 (the oldest person ever).
Now, let’s take a look at our data.

exercise_ages = np.array([22, 27, 45, 62, 34, 52, 42, 22, 34, 26])
The minimum age in exercise_ages is 22, the maximum age is 62, and the range is 40.

You can use the following Python commands to verify this result:

min_age = np.amin(exercise_ages) # Answer is 22
max_age = np.amax(exercise_ages) # Answer is 62
age_range = max_age - min_age
"""

# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction data to numpy arrays
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

"""
Find the minimum transaction time and save it to min_time.
Find the maximum transaction time and save it to max_time.
Find the range, and save it to range_time.
"""
# Find the minimum time, maximum time, and range
min_time = np.amin(times) # <-- Replace with min calc
max_time = np.amax(times) # <-- Replace with max calc
range_time = max_time -  min_time # <-- Replace max - min

# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))