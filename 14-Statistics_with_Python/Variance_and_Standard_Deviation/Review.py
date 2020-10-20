"""
STANDARD DEVIATION
Review
In the last exercise you saw that Lebron James was 0.55 standard deviations above the mean of NBA player heights. He’s taller than average, but compared to the other NBA players, he’s not absurdly tall.

However, compared to the OkCupid dating pool, he is extremely rare! He’s almost three full standard deviations above the mean. You’d expect only about 0.15% of people on OkCupid to be more than 3 standard deviations away from the mean.

This is the power of standard deviation. By taking the square root of the variance, the standard deviation gives you a statistic about spread that can be easily interpreted and compared to the mean.

Instructions
We’ve created a visualization that shows the mean, first, second, and third standard deviations of each dataset.

Enter your height (in inches) into the variable named your_height to see how you compare to the heights of NBA players and OkCupid daters!

You’re likely below the first standard deviation for the NBA. Are you below the second? How unusual is your height compared to the OkCupid members?
"""

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from data import nba_data, okcupid_data

nba_mean = np.mean(nba_data)
okcupid_mean = np.mean(okcupid_data)

#Change this variable to your height (in inches)!
your_height = 0

nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)

plt.subplot(211)
plt.title("NBA Player Heights")
plt.xlabel("Height (inches)")

plt.hist(nba_data)

plt.axvline(nba_mean, color='#FD4E40', linestyle='solid', linewidth=2, label = "Mean")

plt.axvline(nba_mean + nba_standard_deviation, color='#FFB908', linestyle='solid', linewidth=2, label = "Standard Deviations")
plt.axvline(nba_mean - nba_standard_deviation, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(nba_mean + nba_standard_deviation * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean - nba_standard_deviation * 2, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(nba_mean + nba_standard_deviation * 3, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean - nba_standard_deviation * 3, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(your_height, color='#62EDBF', linestyle='solid', linewidth=2, label = "You")

plt.xlim(55, 90)
plt.legend()


plt.subplot(212)
plt.title("OkCupid Profile Heights")
plt.xlabel("Height (inches)")

plt.hist(okcupid_data)

plt.axvline(okcupid_mean, color='#FD4E40', linestyle='solid', linewidth=2, label = "Mean")

plt.axvline(okcupid_mean + okcupid_standard_deviation, color='#FFB908', linestyle='solid', linewidth=2, label = "Standard Deviations")
plt.axvline(okcupid_mean - okcupid_standard_deviation, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(okcupid_mean + okcupid_standard_deviation * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(okcupid_mean - okcupid_standard_deviation * 2, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(okcupid_mean + okcupid_standard_deviation * 3, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(okcupid_mean - okcupid_standard_deviation * 3, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(your_height, color='#62EDBF', linestyle='solid', linewidth=2, label = "You")

plt.xlim(55, 90)
plt.legend()




plt.tight_layout()
plt.show()
