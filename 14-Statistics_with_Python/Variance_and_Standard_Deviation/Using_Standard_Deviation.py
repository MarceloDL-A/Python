"""
STANDARD DEVIATION
Using Standard Deviation
Now that we’re able to compute the standard deviation of a dataset, what can we do with it?

Now that our units match, our measure of spread is easier to interpret. By finding the number of standard deviations a data point is away from the mean, we can begin to investigate how unusual that datapoint truly is. In fact, you can usually expect around 68% of your data to fall within one standard deviation of the mean, 95% of your data to fall within two standard deviations of the mean, and 99.7% of your data to fall within three standard deviations of the mean.

A histogram showing where the standard deviations fallIf you have a data point that is over three standard deviations away from the mean, that's an incredibly unusual piece of data!
"""

import numpy as np
from data import nba_data, okcupid_data

nba_mean = np.mean(nba_data)
okcupid_mean = np.mean(okcupid_data)

nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)

"""Let’s find out how many standard deviations away from the mean NBA great Lebron James is. To begin, let’s find the difference between Lebron’s height (80 inches) and the mean of each dataset.

Set nba_difference equal to 80 minus nba_mean.

Find the difference between Lebron’s height and the OkCupid mean and store it in okcupid_difference. The OkCupid dataset’s mean is stored in okcupid_mean.
"""
#Step 1: Calcualte the difference between the player's height and the means
nba_difference = 65 - nba_mean
okcupid_difference = 65 - okcupid_mean

"""
We now want to find out how many times the standard deviation goes into those differences.

Set num_nba_deviations equal to nba_difference divided by nba_standard_deviation.

Do a similar calculation for num_okcupid_deviations.

What does that first number tell you about how unusual Lebron James is in the NBA? What does the second number tell you about how unusual Lebron James is in the dating pool?
*********************
Let’s check another NBA player. Earl Boykins is one of the smaller NBA players in history at 5’5” (65 inches). Replace Lebron James’ 80 inches with Earl Boykins’ 65.

What can you say about how unusual Earl Boykins is with respect to the two different datasets?

We were surprised that Boykins wasn’t more standard deviations away from the mean of the OkCupid dataset. Think about why he isn’t more of an outlier in this dataset.
"""
#Step 2: Use the difference between the point and the mean to find how many standard deviations the player is away from the mean.
num_nba_deviations = nba_difference/nba_standard_deviation
num_okcupid_deviations = okcupid_difference/okcupid_standard_deviation

#IGNORE CODE BELOW HERE
print("Your basketball player is " + str(num_nba_deviations) + " standard deviations away from the mean of NBA player heights\n")
print("Your basketball player is " + str(num_okcupid_deviations) + " standard deviations away from the mean of OkCupid profile heights")