"""
BOXPLOTS
Boxplots in Matplotlib
We’ve spent this lesson building a boxplot by hand. Let’s now look at how Python’s Matplotlib library does it!

The matplotlib.pyplot module has a function named boxplot(). boxplot() takes a dataset as a parameter. This dataset could be something like a list of numbers, or a Pandas DataFrame.

import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5]
plt.boxplot(data)
plt.show()
One of the strengths of Matplotlib is the ease of plotting two boxplots side by side. If you pass boxplot() a list of datasets, Matplotlib will make a boxplot for each, allowing you to compare their spread and central tendencies,

import matplotlib.pyplot as plt

dataset_one = [1, 2, 3, 4, 5]
dataset_two = [3, 4, 5, 6, 7]
plt.boxplot([dataset_one, dataset_two])
plt.show()
"""
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from music_data import two_thousand, two_thousand_one, two_thousand_two

"""
We’ve imported the dataset of song lengths, but this time, we’ve split the data into three groups — songs that were released in the year 2000 (two_thousand), songs that were released in the year 2001 (two_thousand_one), and songs that were released in the year 2002 (two_thousand_two).

Plot all three datasets as three separate boxplots in the order described above.

Make sure to call plt.show() after calling the plt.boxplot() function.
"""
labels = ["2000 Songs", "2001 Songs", "2002 Songs"]
plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], labels = labels)
plt.show()

"""Let’s add labels to our graph so we know which box plot is which.

Add the parameter labels = ["2000 Songs", "2001 Songs", "2002 Songs"] to your call to the plt.boxplot() function.
"""












