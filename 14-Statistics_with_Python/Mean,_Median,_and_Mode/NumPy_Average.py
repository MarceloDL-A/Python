"""NumPy Average
While you’ve shown that you can calculate the average yourself, it becomes time-consuming as the size of your dataset increases — imagine adding all of the numbers in a dataset with 10,000 observations.

The NumPy .average() or .mean() function can do the work of adding and dividing for you. In the example below, we use np.average() to calculate the average of a dataset with ten values.

example_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36])

example_average = np.average(example_array)

print(example_average)
The code above calculates the average of example_array and saves the value to example_average. The resulting average of this array is 20."""

# Import packages
import numpy as np
import pandas as pd

# Read author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Set author ages to a NumPy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = 0
average_age = np.average(author_ages)

print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))