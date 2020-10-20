"""
HYPOTHESIS TESTING
Chi Square Test
In the last exercise, we looked at data where customers visited a website and either made a purchase or did not make a purchase. What if we also wanted to understand if the probability of making a purchase depends on some other categorical variable, like gender? If we want to understand whether the outcomes of two categorical variables are associated, we should use a Chi Square test. It is useful in situations like:

An A/B test where half of users were shown a green submit button and the other half were shown a purple submit button. Was one group more likely to click the submit button?
People under and over age 40 were given a survey asking "Which of the following three products is your favorite?" Did these age groups have significantly different preferences?
In SciPy, you can use the function chi2_contingency to perform a Chi Square test.

The input to chi2_contingency is a contingency table where:

The columns are each a different condition, such as Interface A vs. Interface B
The rows represent different outcomes, like "Clicked a Link" vs. "Didn't Click"
This table can have as many rows and columns as you need.

Let's return to the question of whether gender is associated with the probability of a website visitor making a purchase. The null hypothesis is that there's no association between the variables (eg. males, females, and non-binary people are all equally likely to make a purchase on the website, so gender and purchase-status are not associated). If the p-value is below our chosen threshold (often 0.05), we reject the null hypothesis and can conclude there is a statistically significant association between the two variables (eg. men, women, and non-binary people appear to have different probabilities of making a purchase, so gender is associated with purchase-status).
"""
from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12
"""
The management at the VeryAnts ant store wants to know if their two most popular species of ants, the Leaf Cutter and the Harvester, vary in popularity between 1st, 2nd, and 3rd graders.

We have created a table representing the different ants bought by the children in grades 1, 2, and 3 after the last big field trip to VeryAnts. Run the code to see what happens when we enter this table into SciPy's chi-square test.

Does the resulting p-value mean that we should reject or accept the null hypothesis?
Ans.: Reject on significance alpha 0.05, so p = 0.155082308077 > alpha
"""
X = [[30, 10],
     [35, 5],
     [28, 12]]
chi2, pval, dof, expected = chi2_contingency(X)
print ("pval: " + str(pval))
print("Reject at significance alpha 0.05, so p = 0.155082308077 > alpha.")

"""
A class of 40 4th graders comes into VeryAnts in the next week and buys 20 sets of Leaf Cutter ants and 20 sets of Harvester ants.

Add this data to the contingency table, rerun the chi-square test, and see if there is now a low enough value to reject the null hypothesis.

"""
X = [[30, 10],
     [35, 5],
     [28, 12], 
     [20, 20]]
chi2, pval2, dof, expected = chi2_contingency(X)
print ("pval2: " + str(pval2))
print("Reject at significance alpha 0.05, so p2 = 0.155082308077 < alpha.")



