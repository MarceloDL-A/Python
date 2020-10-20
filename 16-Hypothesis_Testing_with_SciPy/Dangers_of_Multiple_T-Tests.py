"""
HYPOTHESIS TESTING
Dangers of Multiple T-Tests
Suppose that we own a chain of stores that sell ants, called VeryAnts. There are three different locations: A, B, and C. We want to know if the average ant sales over the past year are significantly different between the three locations.

At first, it seems that we could perform t-tests between each pair of stores.

We know that the p-value is the probability that we incorrectly reject the null hypothesis on each t-test. The more t-tests we perform, the more likely that we are to get a false positive, a Type I error.

For a significance threshold of 0.05, if the null hypothesis is true, then the probability of correctly failing to reject the null is 1 - 0.05 = 0.95. When we run another t-test where the null is true, the probability of correctly failing to reject the null on both of those tests is 0.95 * 0.95, or 0.9025. That means our probability of making an error is now 1 - 0.9025, or close to 10%! This error probability only gets bigger with the more t-tests we do.
"""
from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

"""
We have created samples a, b, and c, representing the sales at VeryAnts at locations A, B, and C, respectively. We want to see if there's a significant difference in sales between the three locations.

Explore datasets a, b, and c by finding and printing the means and standard deviations of each one. Store the means in variables called a_mean, b_mean, and c_mean. Store the standard deviations in variables called a_std, b_std, and c_std.
"""
a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)
a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)
print("a_mean: " + str(a_mean))
print("b_mean: " + str(b_mean))
print("c_mean: " + str(c_mean))
print("a_std: " + str(a_std))
print("b_std: " + str(b_std))
print("c_std: " + str(c_std))
"""
Perform a 2-Sample T-test between each pair of location data.

Store the p-values in variables called a_b_pval, a_c_pval, and b_c_pval. Print them to the console.
"""
ttest, a_b_pval = ttest_ind(a, b)
ttest, a_c_pval = ttest_ind(a, c)
ttest, b_c_pval = ttest_ind(b, c)
print("a_b_pval: " + str(a_b_pval))
print("a_c_pval: " + str(a_c_pval))
print("b_c_pval: " + str(b_c_pval))

"""
Store the probability of error in a variable called error_prob. Print it out to the console.
"""
error_prob = 1-0.95**3
print("error_prob: " + str(error_prob))



