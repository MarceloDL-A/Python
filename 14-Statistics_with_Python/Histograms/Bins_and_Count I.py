"""
Bins and Count I
In the previous exercise, you found that the earliest transaction time is close to 0, and the latest transaction is close to 24, making your range nearly 24 hours.

Now, we have the information we need to start building our histogram. The two key features of a histogram are bins and counts.

Bins
A bin is a sub-range of values that falls within the range of a dataset. In the grocery store example, a valid bin may be from 0 hours to 6 hours. This bin includes all times from just after midnight (0) until 6 am (6).

Additionally, all bins in a histogram must be the same width.

If the range of values in our dataset is from 0 to 24, and the first bin in our grocery store example is from 0 to 6, can you figure out the minimums and maximums of the other bins?

The grocery store bins are:

0 to 6 hours
6 to 12 hours
12 to 18 hours
18 to 24 hours
"""

# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

"""
In script.py, there is an array called days_old_bread that contains values for the age of different loaves of bread in the grocery store.
Find the minimum value of the array and save it to min_days_old.
Find the maximum value of the array and save it to max_days_old.
"""
# Set the minimum and maximums of the array below
min_days_old = np.amin(days_old_bread)
max_days_old = np.amax(days_old_bread)
print("min_days_old: " + str(min_days_old))
print("max_days_old: " + str(max_days_old))

# Set the number of bins to 3
bins = 3

# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")

"""
Set the variable bins equal to 3.

When you run the code, it will output the number of bins for this histogram, and the width of these bins. In the next exercise, we’ll figure out which values fall into each bin.

At the bottom of script.py, we calculate the bin width by subtracting min_days_old from max_days_old, adding one, then dividing by three. We must add one because there are nine possible answers from zero to eight.
"""


