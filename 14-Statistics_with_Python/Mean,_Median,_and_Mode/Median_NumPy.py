"""MEDIAN
Median NumPy
Finding the median of a dataset becomes increasingly time-consuming as the size of your dataset increases — imagine finding the median of an unsorted dataset with 10,000 observations.

The NumPy .median() function can do the work of sorting, then finding the median for you. In the example below, we use np.median() to calculate the median of a dataset with ten values:

example_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36, 42])

example_median = np.median(example_array)

print(example_median)
The code above prints the median of the dataset, 24. The mean of this dataset is 22. It’s worth noting these two values are close to one another, but not equal.
"""

# Import packages
import numpy as np
import pandas as pd

# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save author ages to author_ages
author_ages = greatest_books['Ages']
print(author_ages)

"""Use NumPy to find the median of the author_ages array. Save the result to median_age.

Does the median age of the authors surprise you? If so, how? Is it older, or younger than you expected?"""

# Use numpy to calculate the median age of the top 100 authors
median_age = 0
median_age = np.median(author_ages)

print("The median age of the 100 greatest authors, according to a survey by Le Monde is: " + str(median_age))