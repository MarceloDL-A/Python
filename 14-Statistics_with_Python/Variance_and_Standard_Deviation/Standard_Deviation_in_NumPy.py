"""
STANDARD DEVIATION
Standard Deviation in NumPy
There is a NumPy function dedicated to finding the standard deviation of a dataset — we can cut out the step of first finding the variance. The NumPy function std() takes a dataset as a parameter and returns the standard deviation of that dataset:

import numpy as np

dataset = [4, 8, 15, 16, 23, 42]
standard_deviation = np.std()
Instructions
1.
We’ve removed the code that calculated the variance of each dataset. By using np.std() we don’t need to take that middle step anymore.

Call np.std() using nba_data as a parameter, and store the result in nba_standard_deviation.

Make a similar function call using okcupid_data and store the result in okcupid_standard_deviation.
"""
import numpy as np
from data import nba_data, okcupid_data

#Change these variables to be the standard deviation of each dataset. Use NumPy's function!
nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))