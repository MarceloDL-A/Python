"""
HISTOGRAMS
Summarizing Your Data
The purpose of a histogram is to summarize data that you can use to inform a decision or explain a distribution.

While a histogram is one of the most useful tools for communicating trends, people often use the average of a dataset to make broad claims about its underlying trends.

While the average value of data may be useful to interpret where the data is centered, it can also be misleading.

Average grocery store time
Throughout this lesson, you will analyze grocery store data to understand how a histogram may be a better tool for communicating trends in your data. You will use this data to determine the best times for a manager to staff their store.

Let’s start by looking at our data and calculating the average time that a person will enter the grocery store.
"""

# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")
transactions = transactions.drop(["Unnamed: 0"], axis = 1)

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

"""
The main.py file imports a data frame. Before you start making a histogram, it’s important to understand the shape of your data.

Use the following code to print your data:

print(transactions)
Run your code.

Scroll to the top of the output panel to see the column names, and values in the columns.

Can you identify some maximums and minimums in each column?
"""
# Print transactions below
print(transactions)

"""
Use the following code to find the average time that a person arrives at the grocery store:

print(np.average(times))
The Transaction Time column contains numbers between 0 and <24. The number 0 is 12:00am. You can think of <24 as just before midnight the next day, or 11:59pm.

You should find that the average time is 14.9, which is close to 3pm. We calculated this by subtracting 12 from 14.9, which is close to 3pm.

This doesn’t make much sense to the manager, because they know their busiest times of the day are after 6pm, as many customers stop by on their way home from work.
"""
# Print the average times below
print("The avg time is: " + str(np.average(times)))




