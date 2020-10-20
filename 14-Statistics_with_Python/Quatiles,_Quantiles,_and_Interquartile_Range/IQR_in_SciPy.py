"""
INTERQUARTILE RANGE
IQR in SciPy
In the last exercise, we calculated the IQR by finding the quartiles using NumPy and finding the difference ourselves. The SciPy library has a function that can calculate the IQR all in one step.

The iqr() function takes a dataset as a parameter and returns the Interquartile Range. Notice that when we imported iqr(), we imported it from the stats submodule:

From scipy.stats import iqr

dataset = [4, 10, 38, 85, 193]
interquartile_range = iqr(dataset)
"""
from song_data import songs
from scipy.stats import iqr

"""
Let’s calculate the IQR again, but this time, use SciPy’s function.
Create a variable named interquartile_range and set it equal to the result of calling iqr() using songs as a parameter.
"""
#Create the variables interquartile_range here:
interquartile_range = iqr(songs)

# Ignore the code below here
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")