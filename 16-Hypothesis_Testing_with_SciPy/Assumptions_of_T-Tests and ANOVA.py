"""
HYPOTHESIS TESTING
Assumptions of TTests and ANOVA
Before we use one or two sample t-tests or ANOVA, we need to be sure that the following things are true:

1. The sample(s) should be normally distributed...ish
Data analysts in the real world often still perform t-tests or ANOVAs on data that are not normally distributed. This is usually not a problem if sample size is large, but it depends on how non-normal the data is. In general, the bigger the sample size, the safer you are!

2. The standard deviations of the samples should be equal
For ANOVA and 2-Sample T-Tests, using datasets with standard deviations that are significantly different from each other will often obscure the differences in group means. That said, there is also a way to run a 2-Sample T-Test without assuming equal standard deviations (for example, by setting the equal_var parameter in the scipy.stats.ttest_ind() function equal to False). Running the test in this way has some disadvantages (it essentially makes it harder to reject the null hypothesis even when there is a true difference between groups), so it's important to check for equal standard deviations before running a test.

To check this assumption, it is normally sufficient to divide the two standard deviations and see if the ratio is "close enough" to 1. "Close enough" may differ in different contexts but generally staying within 10% should suffice. This equates to a ratio between 0.9 and 1.1.

3. The samples must be independent
When comparing two or more datasets, the values in one distribution should not affect the values in another distribution. In other words, knowing more about one distribution should not give you any information about any other distribution.

Here are some examples where it would seem the samples are not independent:

the number of goals scored per soccer player before, during, and after undergoing a rigorous training regimen
a group of patients' blood pressure levels before, during, and after the administration of a drug
It is important to understand your datasets before you begin conducting hypothesis tests on them so that you know you are choosing the right test.
"""
import codecademylib
import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv",  delimiter=",")
dist_2 = np.genfromtxt("2.csv",  delimiter=",")

"""
Use Matplotlib's plt.hist() function to display dist_1 before the call to plt.show(). Does it look like this distribution is normal? (note: a normal distribution has a single mode or hump and is symmetric)
"""
#plot your histogram here
plt.hist(dist_1)
plt.show()

"""
Calculate the ratio of standard deviations between dist_1 and dist_2 and store it in a variable called ratio. Print it to the console. Is this "close enough" to perform a numerical hypothesis test between the two datasets?
"""
ratio = float(np.std(dist_1))/np.std(dist_2)
print("ratio: ", str(ratio))
print("stds not close enough. Shall prox between 0.9 and 1.1", )
