"""
HYPOTHESIS TESTING
One Sample T-Test II
In the last exercise, we got a p-value that was much higher than 0.05, so we cannot reject the null hypothesis. If we conduct another experiment and take a new sample of orders, will we get the same result? Not necessarily!

Just because we don't have enough data to detect a difference doesn't mean that there isn't one. Generally, the larger the sample(s) we have, the smaller a difference we'll be able to detect. You can learn more about the exact relationship between sample size and detectable differences in the Sample Size Determination course.

It's also possible that the true mean order price really is 1000 Rupees, but a single sample still leads us to incorrectly reject the null hypothesis. Remember that this is called Type 1 Error and the significance threshold we use for our test should be equal to the type 1 error rate under the null hypothesis. In other words, if we set a 0.05 significance threshold and the true mean purchase price is truly 1000 Rupees, we still expect to incorrectly reject the null (and say that the mean is not 1000 Rupees) in 5% of experiments.

To build intuition for the limitations of conclusions based on any individual sample, let's explore some more data from BuyPie.com and see whether we consistently observe the same results.
"""

from scipy.stats import ttest_1samp
import numpy as np

incorrect_results = 0 # Start the counter at 0

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")
"""
We have loaded a dataset daily_prices into the editor that represents the purchase prices of orders from BuyPie.com in the last 1000 days. Each entry daily_prices[i] is an array of entries representing the price per order on day i.

We predicted that the average price of an order would be 1000 Rupees, and we want to know if the actual data differs from that.

We have made a for loop that goes through the 1000 inner lists. Inside this loop, perform a 1 Sample T-Test with each day of data (daily_prices[i]). For now, just print out the p-value from each test.
"""
incorrect_results = 0
for i in range(1000): # 1000 experiments
   #your ttest here:
   tstat, pval = ttest_1samp(daily_prices[i], 1000)
   #print the pvalue here:
   print("pval "+str(i)+ ": " + str(pval))
   if pval > 0.5:
     incorrect_results += 1
"""
If we get a pval < 0.05, we can conclude that it is unlikely that our sample has a true mean of 1000. Suppose that the true mean purchase price really is 1000 Rupees. Thus, if we get a p-value less than 0.05, we will incorrectly reject the null hypothesis test and say that the experiment indicates the mean purchase price is not 1000 Rupees.

Below the t-test, add some code to check whether the outcome of the hypothesis test is incorrect (i.e., the p-value is less than .05). If so, add 1 to incorrect_results.

Now, incorrect_results is a count of the number of times the outcome of the test was incorrect. Code has been provided for you to print this number to the console. Since our significance threshold was 0.05, we expect about 5% or 50 of the 1000 experiments to return an incorrect result. Is the number you observe close to 50?
"""
print "We incorrectly thought that the distribution was different in " + str(incorrect_results) + " out of 1000 experiments with significance level alpha = 0.05."
