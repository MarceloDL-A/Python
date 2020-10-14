"""
A p-value of 0.05 means that if the null hypothesis is true, there is a 5% chance that an observed sample statistic could have occurred due to random sampling error. For example, in comparing two sample means, a p-value of 0.05 indicates there is a 5% chance that the observed difference in sample means occurred by random chance, even though the population means are equal.

Before conducting a hypothesis test, we determine the necessary threshold we would need before concluding that the results are significant. A higher threshold is more likely to give a false positive so if we want to be very sure that the result is not due to just chance, we will select a very small threshold.

It is important that we choose the significance level before we perform our statistical hypothesis tests to yield a p-value. If we wait until after we see the results, we might pick our threshold such that we get the result we want to see. For instance, if we're trying to publish our results, we might set a significance level that makes our results seem statistically significant. Choosing our significance level in advance helps keep us honest.

Generally, we want a p-value of less than 0.05, meaning that there is less than a 5% chance that our results are due to random chance.
"""

"""
Fill in the body of the given function reject_null_hypothesis to return True if the p-value is small enough to reject the null hypothesis (i.e., it's less than 0.05), and return False otherwise.
"""
def reject_null_hypothesis(p_value):
  """
  Returns the truthiness of whether the null hypothesis can be rejected

  Takes a p-value as its input and assumes p <= 0.05 is significant
  """
  if p_value < 0.05:
    return True
  else:
    return False


hypothesis_tests = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

for p_value in hypothesis_tests:
    reject_null_hypothesis(p_value)
