import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt

"""
In this lesson we’ll be looking at a dataset about music. We’ve plotted a histogram of song lengths (measured in seconds) of 9,975 random songs.

Look up the length of a favorite song of yours. Do you think that song falls in the first, second, third or fourth quarter of the data?

For example, we’ve picked one of our favorite songs, Chicago by Sufjan Stevens. Chicago is 364 seconds long — we’ve plotted it as a red vertical line. It looks like Chicago is in either the third or fourth quarter of the data, but it’s hard to say for sure. Let’s find the quartiles of the dataset!
"""
plt.hist(songs, bins = 200)
plt.axvline(x=364, label="Chicago", c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.legend()
plt.show()