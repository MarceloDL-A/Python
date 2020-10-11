"""
Introduction
Statistics is often pitched as a way to find certainty through data. As you’ll learn in this lesson, the power of statistics is more often used to communicate that certainty doesn’t really exist. Instead, it provides tools to communicate how uncertain we are about a problem.

There’s no better tool to visualize the uncertainty and chaos in data than a histogram. A histogram displays the distribution of your underlying data.

Histograms reveal, through numbers, interpretable trends in your data. They don’t provide a yes or no answer, but are often used as a starting point for discussion and informing an answer to your data.

Whether you’re brand new to statistics or know it well, this lesson will teach you how to use histograms to visualize your data and inform decision-making.

Instructions
Take a look at the histogram to the right. It shows the distribution of possible calories in a burrito bowl at a fast-casual Mexican restaurant. If you don’t understand the plot, that’s okay. We’ll discuss it throughout this lesson.

Below, I’ve listed a few questions that someone may ask after looking over this histogram:

How many calories should a restaurant say is in their burrito bowl?
What is so different about the burrito bowls with 600 calories, and those with 1000 calories?
What can the restaurant change to ensure they are consistently serving burrito bowls with the same number of calories?"""

# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
mu, sigma = 800, 100 # mean and standard deviation
burrito_calories = np.random.normal(mu, sigma, 320)

# Save transaction times to a separate numpy array
plt.hist(burrito_calories, range=(250, 1250), bins=100,  edgecolor='black')
plt.title("Calories in a Burrito Bowl", fontsize = 24)
plt.xlabel("Calories", fontsize=18)
plt.ylabel("Count", fontsize=18)

plt.show()