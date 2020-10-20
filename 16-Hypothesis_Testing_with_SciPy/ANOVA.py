"""
HYPOTHESIS TESTING
ANOVA
In the last exercise, we saw that the probability of making a Type I error got dangerously high as we performed more t-tests.

When comparing more than two numerical datasets, one way to preserve a Type I error probability of 0.05 is to use ANOVA. ANOVA (Analysis of Variance) tests the null hypothesis that all of the samples come from populations with the same mean. If we reject the null hypothesis with ANOVA, we're saying that at least one pair of populations (from which the samples were drawn) have different means; however, we cannot determine exactly which pair(s).

We can use the SciPy function f_oneway to perform ANOVA on multiple datasets. f_oneway takes in each dataset as a different input and returns the F-statistic and the p-value. For example, if we were comparing scores on a videogame between math majors, writing majors, and psychology majors, we could run an ANOVA test with this line:

fstat, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists)
The null hypothesis, in this case, is that all three populations have the same mean score on this videogame. If we reject this null hypothesis (if we get a p-value less than 0.05), we can say that we are reasonably confident that at least one pair of populations is significantly different. After using only ANOVA, we can't make any conclusions on which two populations have a significant difference.

Let's look at an example of ANOVA in action.
"""
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")
"""
Delete your three t-tests. We have a better way to do this now!

Perform an ANOVA test on a, b, and c and store the p-value in a variable called pval.
"""
fstat, pval = f_oneway(a, b, c)

"""
Print out your pval. Does this p-value lead you to reject the null hypothesis?
"""
print("pval of ANOVA: ", str(pval))

"""
Let's say the sales at location B have suddenly soared (maybe there's an ant convention happening nearby). Change the mean of the b distribution to be loaded from 'store_b_new.csv', instead of 'store_b.csv'.

Re-run the ANOVA test and see what the p-value is now. Does this new value make sense?
"""
b = np.genfromtxt("store_b_new.csv",  delimiter=",")
fstat, pval = f_oneway(a, b, c)
print("pval of ANOVA from store_b_new.csv: ", str(pval))

