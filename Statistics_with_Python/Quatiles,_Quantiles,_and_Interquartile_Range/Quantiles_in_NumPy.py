"""
Quantiles in NumPy
The NumPy library has a function named quantile() that will quickly calculate the quantiles of a dataset for you.

quantile() takes two parameters. The first is the dataset that you are using. The second parameter is a single number or a list of numbers between 0 and 1. These numbers represent the places in the data where you want to split.

For example, if you only wanted the value that split the first 10% of the data apart from the remaining 90%, you could use this code:

import numpy as np

dataset = [5, 10, -20, 42, -9, 10]
ten_percent = np.quantile(dataset, 0.10)
ten_percent now holds the value -14.5. This result technically isn’t a quantile, because it isn’t splitting the dataset into groups of equal sizes — this value splits the data into one group with 10% of the data and another with 90%.

However, it would still be useful if you were curious about whether a data point was in the bottom 10% of the dataset.
"""

from song_data import songs
import numpy as np
"""
Instructions
The dataset containing information about the lengths of songs is stored in a variable named songs.

Create a variable named twenty_third_percentile that contains the value that splits the first 23% of the data from the rest of the data.
"""

# Define twenty_third_percentile here:
twenty_third_percentile = np.quantile(songs, 0.23)

#Ignore the code below here:
try:
  print("The value that splits 23% of the data is " + str(twenty_third_percentile) + "\n")
except NameError:
  print("You haven't defined twenty_third_percentile.")
