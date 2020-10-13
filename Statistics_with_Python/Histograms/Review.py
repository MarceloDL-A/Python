"""
HISTOGRAMS
Review
In this lesson, you learned what a histogram is, how to calculate it using NumPy, and how to plot one with Matplotlib.

The example that we used throughout this lesson, finding the busiest times of day at a grocery store, shows how histograms can be used to derive meaning, and inform decisions with our data.

Looking at the hourly customer count histogram was more helpful to inform staffing decisions than knowing the average time that a customer arrives at the grocery store.

Although average is an important, and quick way to summarize your data, histograms tell you much more of the story.
"""
# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

"""
Now, the store manager wants a histogram of transaction costs. Try plotting a histogram for the cost variable.

Some things to think about:

What is a reasonable minimum for transaction data? Maybe 0 dollars.
What is a reasonable maximum for the transaction data? Using np.amax(cost), we get 161.4. So, you could make the maximum 165.
How many bins should you use to adequately represent the data? Do some guess and check work to figure this out.
Finally, think about how this data could be useful to the store manager.
"""
# Use plt.hist() below
max_cost = np.amax(cost)
print(max_cost)
plt.hist(cost, range = (0, max_cost), bins = 50)
plt.title("Transaction costs")
plt.xlabel("Cost")
plt.ylabel("Transactions")
plt.show()


