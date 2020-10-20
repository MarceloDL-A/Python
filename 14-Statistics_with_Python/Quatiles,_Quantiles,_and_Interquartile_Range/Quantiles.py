"""
QUANTILES
Quantiles
Quantiles are points that split a dataset into groups of equal size. For example, let’s say you just took a test and wanted to know whether you’re in the top 10% of the class. One way to determine this would be to split the data into ten groups with an equal number of datapoints in each group and see which group you fall into.

Thirty students grades split into ten groups of three.
There are nine values that split the dataset into ten groups of equal size — each group has 3 different test scores in it.

Those nine values that split the data are quantiles! Specifically, they are the 10-quantiles, or deciles.

You can find any number of quantiles. For example, if you split the dataset into 100 groups of equal size, the 99 values that split the data are the 100-quantiles, or percentiles.

The quartiles are some of the most commonly used quantiles. The quartiles split the data into four groups of equal size.

In this lesson, we’ll show you how to calculate quantiles using NumPy and discuss some of the most commonly used quantiles.

Instructions
We’ve imported a dataset of song lengths (measured in seconds). We’ve drawn a few histograms showing different quantiles.

What do you think a histogram that shows the 100-quantiles would look like?
"""
import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt
import numpy as np

q1 = np.quantile(songs, 0.25)
q2 = np.quantile(songs, 0.5)
q3 = np.quantile(songs, 0.75)

plt.subplot(3,1,1)
plt.hist(songs, bins = 200)
plt.axvline(x=q1, c = 'r')
plt.axvline(x=q2, c = 'r')
plt.axvline(x=q3, c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.title("4-Quantiles")

plt.subplot(3,1,2)
plt.hist(songs, bins = 200)
plt.axvline(x=np.quantile(songs, 0.2), c = 'r')
plt.axvline(x=np.quantile(songs, 0.4), c = 'r')
plt.axvline(x=np.quantile(songs, 0.6), c = 'r')
plt.axvline(x=np.quantile(songs, 0.8), c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.title("5-Quantiles")

plt.subplot(3,1,3)
plt.hist(songs, bins = 200)
for i in range(1, 10):
  plt.axvline(x=np.quantile(songs, i/10), c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.title("10-Quantiles")

plt.tight_layout()
plt.show()