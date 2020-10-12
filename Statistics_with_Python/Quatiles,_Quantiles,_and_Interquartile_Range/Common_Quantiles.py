"""
Common Quantiles
One of the most common quantiles is the 2-quantile. This value splits the data into two groups of equal size. Half the data will be above this value, and half the data will be below it. This is also known as the median!

Ten points are below the median and ten points are above the median.
The 4-quantiles, or the quartiles, split the data into four groups of equal size. We found the quartiles in the previous exercise. Options

Quartiles split a dataset of 20 points into 4 groups with 5 points each
Finally, the percentiles, or the values that split the data into 100 groups, are commonly used to compare new data points to the dataset. You might hear statements like “You are above the 80th percentile in height”. This means that your height is above whatever value splits the first 80% of the data from the remaining 20%.

Instructions
We won’t make you calculate all 99 percentiles, but let’s take a look at one. Find the value that separates the first 32% of the data from the rest.

Store that value in a variable named percentile.

"""
from song_data import songs
import numpy as np

# Define percentile and answer here:
"""We won’t make you calculate all 99 percentiles, but let’s take a look at one. Find the value that separates the first 32% of the data from the rest.
Store that value in a variable named percentile."""
percentile = np.quantile(songs, 0.32)

"""
Look at the printout. If you had a song that was exactly three minutes long, is that song above or below the 32nd percentile?

Create a variable named answer and set it equal to either "above" or "below". Don’t forget to include the quotes!
"""
answer = "below"

#Ignore the code below here:
try:
  print("Your percentile is " + str(percentile) + "\n")
except NameError:
  print("You haven't defined percentile")
