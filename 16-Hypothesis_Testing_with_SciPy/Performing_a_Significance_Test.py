"""
ANALYZE FARMBURG'S A/B TEST
Performing a Significance Test
Here is our table of purchases from the previous exercise:

group	is_purchase	user_id
A	No Purchase	1350
A	Purchase	316
B	No Purchase	1483
B	Purchase	183
C	No Purchase	1583
C	Purchase	83
The data from this A/B test is categorical data.

Why?

Because a user's response can be either "Purchase" or "No Purchase".

There are more than 2 conditions: users could be in either Group A, Group B, or Group C.

Recall our table for determining which significance test to use:

Numerical	Categorical
Sample vs. Known Quantity	1 Sample T-Test	Binomial Test
2 Samples	2 Sample T-Test	Chi Square
More Than 2 Samples	ANOVA
and/or
Tukey	Chi Square
Which type of test should we use?
"""
"""
You should perform a chi-squared test to determine if the differences between Groups A, B, and C are significant.

Import chi2_contingency from scipy.stats so that you can perform the chi-squared test.
"""
from scipy.stats import chi2_contingency 

"""
The function chi2_contingency accepts one argument: a contingency table.

Start by filling in the contingency table below with the correct values:

contingency = [[A_purchases, A_not_purchases],
               [B_purchases, B_not_purchases],
               [C_purchases, C_not_purchases]]
               group	is_purchase	user_id
A	No Purchase	1350
A	Purchase	316
B	No Purchase	1483
B	Purchase	183
C	No Purchase	1583
C	Purchase	83
The data from this A/B test is categorical data.
"""
contingency = [[316, 1350],
               [183, 1483],
               [83, 1583]]
print("contingency: \n" + str(contingency))               
"""
Use the function chi2_contingency with the data in contingency to calculate the p-value.

Save only the p-value to the variable pvalue.
"""
_, pvalue, _, _ = chi2_contingency(contingency)
print("pvalue from chi2_contingency: \n" + str(pvalue))   

"""
Is pvalue less than 0.05? If so, there is a significant difference between the three groups.

Create a variable called is_significant and make it:

True if pvalue is less than 0.05
False if pvalue is greater than 0.05
"""
if pvalue < 0.05:
  is_significant = True
else:
  is_significant = False

