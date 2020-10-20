"""
STANDARD DEVIATION
Standard Deviation
Variance is a tricky statistic to use because its units are different from both the mean and the data itself. For example, the mean of our NBA dataset is 77.98 inches. Because of this, we can say someone who is 80 inches tall is about two inches taller than the average NBA player.

However, because the formula for variance includes squaring the difference between the data and the mean, the variance is measured in units squared. This means that the variance for our NBA dataset is 13.32 inches squared.

This result is hard to interpret in context with the mean or the data because their units are different. This is where the statistic standard deviation is useful.

Standard deviation is computed by taking the square root of the variance. sigma is the symbol commonly used for standard deviation. Conveniently, sigma squared is the symbol commonly used for variance:

\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{N}{(X_i -\mu)^2}}{N}}?	 
?	 
In Python, you can take the square root of a number using ** 0.5:

num = 25
num_square_root = num ** 0.5
Instructions
1.
We’ve written some code that calculates the variance of the NBA dataset and the OkCupid dataset.

The variances are stored in variables named nba_variance and okcupid_variance.

Calculate the standard deviation by taking the square root of nba_variance and store it in the variable nba_standard_deviation (on line 8). Do the same for the variable okcupid_standard_deviation (on line 9).

"""
import numpy as np
from data import nba_data, okcupid_data

nba_variance = np.var(nba_data)
okcupid_variance = np.var(okcupid_data)

#Change these variables to be the standard deviation of each dataset.
nba_standard_deviation = nba_variance**0.5
okcupid_standard_deviation = okcupid_variance**0.5

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))