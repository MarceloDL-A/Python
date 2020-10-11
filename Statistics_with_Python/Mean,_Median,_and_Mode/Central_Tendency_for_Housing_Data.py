"""
LEARN STATISTICS WITH PYTHON
Central Tendency for Housing Data
In this project, you will find the mean, median, and mode cost of one-bedroom apartments in three of the five New York City boroughs: Brooklyn, Manhattan, and Queens.

Using your findings, you will make conclusions about the cost of living in each of the boroughs. We will also discuss an important assumption that we make when we point out differences between the boroughs.

We worked with Streeteasy.com to collect this data. While we will only focus on the cost of one-bedroom apartments, the dataset includes a lot more information if you're interested in asking your own questions about the Brooklyn, Manhattan, and Queens housing market.
"""

# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

"""Observing your Data
We've imported data about one-bedroom apartments in three of New York City's boroughs: Brooklyn, Manhattan, and Queens. We saved the values to:

brooklyn_one_bed
manhattan_one_bed
queens_one_bed
In this project, we only care about the price of apartments, so we saved the price of apartments in each borough to:

brooklyn_price
manhattan_price
queens_price
If you want to see what these arrays look like, you can use print statements to see them in the output terminal."""

"""
Before starting the next few steps, delete any print() statements you've added.

Find the average value of one-bedroom apartments in Brooklyn and save the value to brooklyn_mean.
"""


# Add mean calculations below 
"""Before starting the next few steps, delete any print() statements you've added.
Find the average value of one-bedroom apartments in Brooklyn and save the value to brooklyn_mean.
Find the average value of one-bedroom apartments in Manhattan and save the value to manhattan_mean.
Find the average value of one-bedroom apartments in Queens and save the value to queens_mean.
"""
brooklyn_mean = np.average(brooklyn_price)
manhattan_mean =  np.average(manhattan_price)
queens_mean = np.average(queens_price)


# Add median calculations below
"""
Find the Median
Find the median value of one-bedroom apartments in Brooklyn and save the value to brooklyn_median.
Find the median value of one-bedroom apartments in Manhattan and save the value to manhattan_median.
Find the median value of one-bedroom apartments in Queens and save the value to queens_median.
"""
brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)


# Add mode calculations below
"""
Find the Mode
Find the mode value of one-bedroom apartments in Brooklyn and save the value to brooklyn_mode.
Find the mode value of one-bedroom apartments in Manhattan and save the value to manhattan_mode.
Find the mode value of one-bedroom apartments in Queens and save the value to queens_mode.
"""
brooklyn_mode = stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)

"""
What does our data tell us?
Now what?
We don't find the mean, median, and mode of a dataset for the sake of it.
The point is to make inferences from our data. What can you say about the housing prices in Brooklyn, Queens, and Manhattan? Besides, "It's really expensive to live in any of them."
"""




##############################################
##############################################
##############################################



# Don't look below here
# Mean
try:
    print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
except NameError:
    print("The mean price in Brooklyn is not yet defined.")
try:
    print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
except NameError:
    print("The mean in Manhattan is not yet defined.")
try:
    print("The mean price in Queens is " + str(round(queens_mean, 2)))
except NameError:
    print("The mean price in Queens is not yet defined.")
    
    
# Median
try:
    print("The median price in Brooklyn is " + str(brooklyn_median))
except NameError:
    print("The median price in Brooklyn is not yet defined.")
try:
    print("The median price in Manhattan is " + str(manhattan_median))
except NameError:
    print("The median price in Manhattan is not yet defined.")
try:
    print("The median price in Queens is " + str(queens_median))
except NameError:
    print("The median price in Queens is not yet defined.")
    
    
#Mode
try:
    print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
except NameError:
    print("The mode price in Brooklyn is not yet defined.")
try:
    print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
except NameError:
    print("The mode price in Manhattan is not yet defined.")
try:
    print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
except NameError:
    print("The mode price in Queens is not yet defined.")


