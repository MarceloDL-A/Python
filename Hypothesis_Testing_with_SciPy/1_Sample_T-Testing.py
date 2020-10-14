"""
HYPOTHESIS TESTING
1 Sample T-Testing
Let's imagine the fictional business BuyPie, which sends ingredients for pies to your household so that you can make them from scratch. Suppose that a product manager wants online BuyPie orders to cost around 1000 Rupees on average. In the past day, 50 people made an online purchase and the average payment per order was only 850 Rupees. Are people really spending less than 1000 Rupees on average? Or is this just the result of chance and a small sample size?

We can test this using a 1 Sample T Test, which compares a sample mean to a hypothetical population mean.

When we conduct a 1 Sample T Test, we want to first create a null hypothesis, which is a prediction that the observed sample comes from a population with a particular mean. For example: "the average cost of a BuyPie order is 1000 Rupees". Note that, even if the null hypothesis were true, it's very unlikely that any observed sample mean will be exactly 1000.00 Rupees.

We also have to determine an alternative hypothesis, which is a statement about the kind of difference we are interested in. For example, we might form the following alternative hypothesis: "The average cost of a BuyPie order is not 1000 Rupees".

If we form the null and alternative tests as indicated above, the test asks the following question: "Suppose that that the average cost of a BuyPie order is 1000 Rupees; what is the probability of observing a sample of 50 orders with cost as different or more different from 1000 as we did (i.e., < 850 or > 1150)?"

The result of the test is a p-value. If the p-value is less than our pre-chosen threshold (usually .05), we can reject the null hypothesis in favor of the alternative. When we reject the null, we are saying that it would be unlikely to observe our sample (or something more extreme) if the null hypothesis were true.

It is important to note that we cannot conclude anything about magnitude of differences based on this test; for example, we might conclude that it is unlikely that the average cost of all BuyPie orders is 1000 Rupees; however, we cannot then conclude that the average cost is closer to 850 Rupees.

SciPy has a function called ttest_1samp, which performs a 1 Sample T-Test for you.

ttest_1samp requires two inputs, a sample distribution (eg. the list of the 50 observed purchase prices) and a mean to test against (eg. 1000):

tstat, pval = ttest_1samp(example_distribution, expected_mean)
print pval
It also returns two outputs: the t-statistic (which we won't cover in this course), and the p-value - telling us how confident we can be that the sample of values came from a distribution with the specified mean.
"""
from scipy.stats import ttest_1samp
import numpy as np

"""
We have provided a small dataset called prices, representing the purchase prices of customers to BuyPie.com in the past hour.

First, print out prices to the console and examine the numbers.
"""
prices = np.genfromtxt("prices.csv")
print(prices)

"""
Even with a small dataset like this, it is hard to make judgments from just looking at the numbers.

To understand the data better, let's look at the mean. Calculate the mean of prices using np.mean. Store it in a variable called prices_mean and print it out.
"""
prices_mean = np.mean(prices)
print("prices_mean: " + str(prices_mean))

"""Use ttest_1samp with prices to see what p-value the experiment returns for this distribution, where we expect the mean to be 1000.
"""
tstat, pval = ttest_1samp(prices, 1000)
print("pval: " + str(pval))

