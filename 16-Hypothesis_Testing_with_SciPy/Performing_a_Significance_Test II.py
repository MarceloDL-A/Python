"""
ANALYZE FARMBURG'S A/B TEST
Performing a Significance Test II
Here is our table of purchases again:

group	is_purchase	user_id
A	No Purchase	1350
A	Purchase	316
B	No Purchase	1483
B	Purchase	183
C	No Purchase	1583
C	Purchase	83
We want to see if the percent of Group A that purchased an upgrade package is significantly greater than p_clicks_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our target of $1,000).

We are comparing a single set of samples to a target. Our data is still categorical.

Recall our table for determining which significance test to use:

Numerical	Categorical
Sample vs. Known Quantity	1 Sample T-Test	Binomial Test
2 Samples	2 Sample T-Test	Chi Square
More Than 2 Samples	ANOVA
and/or
Tukey	Chi Square
Which type of test should we use?
"""
import codecademylib
import pandas as pd
from scipy.stats import binom_test

df = pd.read_csv('clicks.csv')

num_visits = len(df)

p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits

"""
We should use a binomial test on each group to see if the observed purchase rate is significantly greater than what we need in order to generate at least $1,000 per week.

Import binom_test from scipy.stats.
"""
"""
For Group A ($0.99 price point), perform a binom_test to see if the observed purchase rate is significantly greater than p_clicks_099.

x will be the number of purchases for Group A
n will be the total number of visitors assigned Group A
p will be the target percent of purchases for that price point (calculated above as p_clicks_099)
Save the results to pvalueA.
"""
pvalueA = binom_test(316, 1666, p_clicks_099)

"""
For Group B ($1.99 price point), perform a binom_test to see if the observed purchase rate is significantly greater than p_clicks_199.

Save the results to pvalueB.
"""
pvalueB = binom_test(183, 1666, p_clicks_199)

"""
For Group C ($4.99 price point), perform a binom_test to see if the observed purchase rate is significantly greater than p_clicks_499.

Save the results to pvalueC.
"""
pvalueC = binom_test(83, 1666, p_clicks_499)
print("pvalueA: " + str(pvalueA))
print("pvalueB: " + str(pvalueB))
print("pvalueC: " + str(pvalueC))

"""
What price should Brian charge for the upgrade package? Save your answer to the variable final_answer.
Ans.:
pvalueA: 0.21112872994
pvalueB: 0.206602092466
pvalueC: 0.0456236724772
pvalueC incates that the number of clicks is significantly great than the need number clicks
"""
final_answer = 4.99





