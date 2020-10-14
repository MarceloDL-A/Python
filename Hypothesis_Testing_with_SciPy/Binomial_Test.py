"""
HYPOTHESIS TESTING
Binomial Test
Let's imagine that we are analyzing the percentage of customers who make a purchase after visiting a website. 1000 customers visited the site this month, and 58 of them made a purchase. The marketing department reports that historical data suggests about 72 of every 1000 visitors make a purchase. Thus, they estimate that the probability of any particular customer making a purchase is 7.2%. We would like to know if this month's number, 58 purchases, is significantly different from normal or a reasonable fluctuation due to random chance.

In previous exercises, we collected samples of numerical information (eg. order price) and then used the mean and standard deviation of those samples to make comparisons. In contrast, we now have a sample where each unit (a visitor) falls into one of two discrete categories:

"made a purchase"
"did not make a purchase"
Instead of comparing sample means, we want to compare the percent in the "made a purchase" category to some expectation. This can be done with a Binomial Test. The binomial distribution describes the number of expected "successes" in an experiment with some number of "trials". In this case, our experiment consists of 1000 people visiting the site. For each of those trials (visitors), we expect that there is a 7.2% chance of a purchase (success).

SciPy has a function called binom_test(), which performs a Binomial Test for you. In this example, the null hypothesis is that the true probability of a purchase is 7.2%. The default alternative hypothesis for the binom_test() function in this example is that the true probability is not 7.2%.

binom_test() requires three inputs, the number of observed successes, the number of total trials, and an expected probability of success. For example, with 1000 coin flips of a fair coin, we would expect a "success rate" (the rate of getting heads), to be 0.5, and the number of trials to be 1000. Let's imagine we get 525 heads. Is the coin weighted? This function call would look like:

pval = binom_test(525, n=1000, p=0.5)
It returns a p-value, telling us how likely we are to observe at least this much deviation from expectation (> 525 heads or < 475 heads) given that the true probability of heads on any flip was 0.5 (meaning our expectation was 500 heads). If we get a p-value less than 0.05, we can reject the null hypothesis and say it is unlikely that the true probability of heads was 0.5 on each flip, suggesting that the coin is weighted.
"""
from scipy.stats import binom_test

"""
Suppose the goal of VeryAnts's marketing team this quarter was to have 6% of customers click a link that was emailed to them. They sent out a link to 10,000 customers and 510 clicked the link, which comes out to 5.1% instead of 6%. Did they do significantly worse than the target? Let's use a binomial test to answer this question.

Use SciPy's binom_test function to calculate the p-value the experiment returns for this distribution, where we wanted the mean to be 6% of emails opened, or p=0.06, but only saw 5.1% of emails opened.

Store the p-value in a variable called pval and print it out.
"""
pval = binom_test(510, 10000, 0.06)
print("pval: " + str(pval))

"""
For the next quarter, marketing has tried out a new email tactic, including puns in every line of every email. As a result, 590 people out of 10000 opened the link in the newest email.

If we still wanted the mean to be 6% of emails opened, but now have 5.9% of emails opened, what is the new p-value. Save your results to the variable pval2

Does this new p-value make sense?
"""
pval2 = binom_test(590, 10000, 0.06)
print("pval2: " + str(pval2))
