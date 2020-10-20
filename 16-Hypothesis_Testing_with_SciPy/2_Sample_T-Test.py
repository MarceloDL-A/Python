"""
HYPOTHESIS TESTING
2 Sample T-Test
Suppose that a company has recently updated their website to make it more colorful and inviting. The company wants to know whether the new design is resulting in visitors staying on the site for a longer period of time. A sample of 100 visitors who saw the old design spent an average of 25 minutes on the site. A second sample of 100 visitors who saw the new version spent an average of 28 minutes on the site. Did the average time spent per visitor vary across groups? Or is this difference attributable to random chance?

One way of testing whether this difference is significant is by using a 2 Sample T-Test. A 2 Sample T-Test compares two sets of numerical data.

The null hypothesis of a 2 Sample T-Test is that the two observed samples come from populations with the same mean. In the example above, this means: if we could observe all site visitors in two alternate universes (one where they see each version of the site), the average visiting times in these universes would be equal.

The alternative hypothesis could be: The two observed samples come from populations with different means. In the example above, this would mean that the average visiting times in our two alternate universes are actually different, hence why we observed a difference in our samples.

We can use SciPy's ttest_ind function to perform a 2 Sample T-Test. It takes the two samples as inputs and returns the t-statistic and a p-value, which we can use to assess the probability of an observed difference happening by chance if the null hypothesis were true. For more information about p-values, refer to the earlier exercise on univariate t-tests.
"""
from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")
"""
We've created two distributions representing the time spent per visitor to BuyPie.com last week, week1, and the time spent per visitor to BuyPie.com this week, week2.

Find the means of these two distributions. Store them in week1_mean and week2_mean. Print them to the console.
"""
week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
print("week1_mean: " + str(week1_mean))
print("week2_mean: " + str(week2_mean))

"""
Find the standard deviations of these two distributions. Store them in week1_std and week2_std. Print them to the console.
"""
week1_std = np.std(week1)
week2_std = np.std(week2)
print("week1_std: " + str(week1_std))
print("week1_std: " + str(week1_std))

"""
Run a 2 Sample T-Test using the SciPy function ttest_ind.

Save the p-value in a variable called pval and print it out. Does this value make sense, knowing what you know about these datasets?
"""
ttest, pval = ttest_ind(week1, week2)
print("pval of ttest_ind between week1 and week2: " + str(pval))

