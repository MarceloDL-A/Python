"""Mode SciPy
Finding the mode of a dataset becomes increasingly time-consuming as the size of your dataset increases — imagine finding the mode of a dataset with 10,000 observations.

The SciPy stats.mode() function can do the work of finding the mode for you. In the example below, we import stats then use stats.mode() to calculate the mode of a dataset with ten values:

Example: One Mode
from scipy import stats

example_array = np.array([24, 16, 12, 10, 12, 28, 38, 12, 28, 24])

example_mode = stats.mode(example_array)
The code above calculates the mode of the values in example_array and saves it to example_mode.

The result of stats.mode() is an object with the mode value, and its count.

>>> example_mode
ModeResult(mode=array([12]), count=array([3]))
Example: Two Modes
If there are multiple modes, the stats.mode() function will always return the smallest mode in the dataset.

Let’s look at an array with two modes, 12 and 24:

from scipy import stats

example_array = np.array([24, 16, 12, 10, 12, 24, 38, 12, 28, 24])

example_mode = stats.mode(example_array)
The result of stats.mode() is an object with the smallest mode value, and its count.

>>> example_mode
ModeResult(mode=array([12]), count=array([3]))
"""

# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save author ages to author_ages
author_ages = greatest_books['Ages']
print(author_ages)

"""We have already imported the stats library for you.

On line 13, delete the current value set to mode_age.

Find the mode of the observations in the author_ages array. Save the result to mode_age.
"""

# Use numpy to calculate the mode age of the top 100 authors
#mode_age = np.array([np.array([0]),np.array([0])])
mode_age = stats.mode(author_ages)
print(mode_age)


print("The mode age and its frequency of authors from Le Monde's 100 greatest books is: " + str(mode_age[0][0]) + " and " + str(mode_age[1][0]))