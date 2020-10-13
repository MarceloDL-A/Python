"""
INTERQUARTILE RANGE
Range Review
One of the most common statistics to describe a dataset is the range. The range of a dataset is the difference between the maximum and minimum values. While this descriptive statistic is a good start, it is important to consider the impact outliers have on the results:

A dataset with some outliers.
In this image, most of the data is between 0 and 15. However, there is one large negative outlier (-20) and one large positive outlier (40). This makes the range of the dataset 60 (The difference between 40 and -20). That’s not very representative of the spread of the majority of the data!

The interquartile range (IQR) is a descriptive statistic that tries to solve this problem. The IQR ignores the tails of the dataset, so you know the range around-which your data is centered.

In this lesson, we’ll teach you how to calculate the interquartile range and interpret it.
"""
import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt
"""
We’ve imported a dataset of song lengths (measured in seconds) and plotted a histogram.

It looks like there are some outliers — this might be a good opportunity to use the IQR.

Before we do that, let’s calculate the range. We’ve found the maximum and minimum values of the dataset and stored them in variables named maximum and minimum.

Create a variable named song_range and set it equal to the difference between the maximum and the minimum.
"""
maximum = max(songs)
minimum = min(songs)
#Create the variable song_range here:
song_range  = maximum - minimum

# Ignore the code below here
plt.hist(songs, bins = 200)
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.show()

try:
  print("The range of the dataset is " + str(song_range) + " seconds")
except NameError:
  print("You haven't defined the variable song_range yet")