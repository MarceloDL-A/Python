"""
HISTOGRAMS
Plotting a Histogram
At this point, you’ve learned how to find the numerical inputs to a histogram. Thus far the size of our datasets and bins have produced results that we can interpret. This becomes increasingly difficult as the number of bins in a histogram increases.

Because of this, histograms are typically viewed graphically, with bin ranges on the x-axis and counts on the y-axis. The figure below shows the graphical representation of the histogram for our exercise class example from last exercise. Notice, there are five equally-spaced bars, with each displaying a count for an age range. Compare the graph to the table, just below it.

Histogram
20-29	30-39	40-49	50-59	60-69
7	4	4	3	2
Histograms are an easy way to visualize trends in your data. When I look at the above graph, I think, “More people in the exercise class are in their twenties than any other decade. Additionally, the histogram is skewed, indicating the class is made of more younger people than older people.”

We created the plot above using the matplotlib.pyplot package. We imported the package using the following code:

from matplotlib import pyplot as plt
We plotted the histogram with the following code. Notice, the range and bins arguments are the same as we used in the last exercise:

plt.hist(exercise_ages, range = (20, 70), bins = 5, edgecolor='black')

plt.title("Decade Frequency")
plt.xlabel("Ages")
plt.ylabel("Count")

plt.show()
In the code above, we used the plt.hist() function to create the plot, then added a title, x-label, and y-label before showing the graph with plt.show().
"""
# Import packages
import codecademylib
import numpy as np
import pandas as pd

"""
At the top of script.py, we’ve imported codecademylib, which is a package that Codecademy uses to plot your histogram in the panel to the right. Don’t worry about this library. Any Python development environment that you may use will take care of this for you.

From matplotlib, import pyplot as plt.
"""
# import pyplot as plt
import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

"""
Use the plt.hist() function to create a plot for each six-hour period in a day. Use the following range and number of bins.
Range: 0 to 24
Bins: 4
"""
# Use plt.hist() below
plt.hist(times, range = (0, 24), bins = 4, edgecolor='black')

"""
Use plt.show() to show the figure.
Feel free to add a title, x-label, and y-label if you want. You can copy the code from the hint as an example.
"""
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")

plt.show()


