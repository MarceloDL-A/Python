"""
Histograms
While counting the number of values in a bin is straightforward, it is also time-consuming. How long do you think it would take you to count the number of values in each bin for:

an exercise class of 50 people?
a grocery store with 300 loaves of bread?
Most of the data you will analyze with histograms includes far more than ten values.

For these situations, we can use the numpy.histogram() function. In the example below, we use this function to find the counts for a twenty-person exercise class.

exercise_ages = np.array([22, 27, 45, 62, 34, 52, 42, 22, 34, 26, 24, 65, 34, 25, 45, 23, 45, 33, 52, 55])

np.histogram(exercise_ages, range = (20, 70), bins = 5)
Below, we explain each of the function’s inputs:

exercise_ages is the input array
range = (20, 70) — is the range of values we expect in our array. Range includes everything from 20, up until but not including 70.
bins = 5 is the number of bins. Python will automatically calculate equally-sized bins based on the range and number of bins.
Below, you can see the output of the numpy.histogram() function:

(array([7, 4, 4, 3, 2]), array([20., 30., 40., 50., 60., 70.]))
The first array, array([7, 4, 4, 3, 2]), is the counts for each bin. The second array, array([20., 30., 40., 50., 60., 70.]), includes the minimum and maximum values for each bin:

Bin 1: 20 to <30
Bin 2: 30 to <40
Bin 3: 40 to <50
Bin 4: 50 to <60
Bin 5: 60 to <70
"""
# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

"""
Use the np.histogram() function to determine the busiest six hours of the day. Save the result to times_hist on line 12.

Use the following range and number of bins.

Range: 0 to 24
Bins: 4
Can you determine which six-hour period is the busiest?

Check the hint if you need help, or want to see the correct answer.
"""
# Use numpy.histogram() below
times_hist = np.histogram(times, range = (0, 24), bins = 4)

print(times_hist)

"""
Hint:
Use the np.histogram() function with times, a range 0 to 24, and 4 bins.
You should see that the store is the busiest between the hours of 18 and 24. This is between 6pm and midnight.
"""
