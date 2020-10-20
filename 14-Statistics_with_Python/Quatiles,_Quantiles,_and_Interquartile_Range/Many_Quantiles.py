"""
Many Quantiles
In the last exercise, we found a single “quantile” — we split the first 23% of the data away from the remaining 77%.

However, quantiles are usually a set of values that split the data into groups of equal size. For example, you wanted to get the 5-quantiles, or the four values that split the data into five groups of equal size, you could use this code:

import numpy as np

dataset = [5, 10, -20, 42, -9, 10]
ten_percent = np.quantile(dataset, [0.2, 0.4, 0.6, 0.8])
Note that we had to do a little math in our head to make sure that the values [0.2, 0.4, 0.6, 0.8] split the data into groups of equal size. Each group has 20% of the data.

The data is split into 5 groups where each group has 4 datapoints.
If we used the values [0.2, 0.4, 0.7, 0.8], the function would return the four values at those split points. However, those values wouldn’t split the data into five equally sized groups. One group would only have 10% of the data and another group would have 30% of the data!
"""

from song_data import songs
import numpy as np

"""
Create a variable named quartiles that contains the quartiles of the songs dataset.

The quartiles of a dataset split the data into four groups of equal size. Each group should have 25% of the data, so you’ll want to use [0.25, 0.5, 0.75] as the second parameter to the quantile() function.
"""
"""
Create a variable named deciles. deciles should store the values that split the dataset into ten groups of equal size. Each group should have 10% of the data.

The first value should be at 10% of the data. The next value should be at 20% of the data. The final value should be at 90% of the data.
"""
"""
Look at the printout of the deciles. If you had a song that was 170 seconds long, what tenth of the dataset would it fall in?

Create a variable named tenth and set it equal to the 1 if you think the 170 second song would fall in the first tenth of the data. Set it equal to 2 if you think the song would fall in the second tenth of the data. If you think the song would fall in the final tenth of the data, set tenth equal to 10.
"""

# Define quartiles, deciles, and tenth here:
quartiles = np.quantile(songs, [0.25, 0.5, 0.75])
deciles = np.quantile(songs, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
tenth = 3

#Ignore the code below here:
try:
  print("The quariles are " + str(quartiles) + "\n")
except NameError:
  print("You haven't defined quartiles.\n")
try:
  print("The deciles are " + str(deciles) + "\n")
except NameError:
  print("You haven't defined deciles.\n")
