"""
HISTOGRAMS
Finding your Best Bin Size
The figure below displays the graph that you created in the last exercise:

Histogram
This histogram is helpful for our store manager. The last six hours of the day are the busiest — from 6 pm until midnight. Does this mean the manager should staff their grocery store with the most employees between 6 pm and midnight?

To the manager, this doesn’t make much sense. The manager knows the store is busy when many people get off work, but the rush certainly doesn’t continue later than 9 pm.

The issue with this histogram is that we have too few bins. When plotting a histogram, it’s essential to select bins that fully capture the trends in the underlying data. Often, this will require some guessing and checking. There isn’t much of a science to selecting bin size.

How many bins do you think makes sense for this example? I would try 24 because there are 24 hours in a day.
"""
# Import packages
import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

"""
Change the number of bins in your code from 4 to 24.

What do you notice about the data?

Given this new graph, when would you recommend staffing the grocery store?

Check the hint to see what we thought.
"""
# Use plt.hist() below
plt.hist(times, range=(0, 24), bins=24,  edgecolor="black")
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")

plt.show()

"""
It looks like the busiest times of day are in the morning, from 5am to 10am, and in the evening from 5pm to 10pm.

This histogram has two distinct peaks, neither of which are close to our average of 3pm. As you can see, averages don’t tell the full story. By visualizing the shape of our data, we can make better-informed decisions.
"""