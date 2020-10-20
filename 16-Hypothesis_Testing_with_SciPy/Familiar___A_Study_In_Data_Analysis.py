"""
HYPOTHESIS TESTING WITH SCIPY
Familiar: A Study In Data Analysis
Welcome to Familiar, a startup in the new market of blood transfusion! You've joined the team because you appreciate the flexible hours and extremely intelligent team, but the overeager doorman welcoming you into the office is a nice way to start your workday (well, work-evening).

Familiar has fallen into some tough times lately, so you're hoping to help them make some insights about their product and help move the needle (so to speak).
"""
"""
We're going to start by including a data interface that a previous software engineer wrote for you, it's aptly titled familiar, so just import that.
"""
import familiar as fm
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

"""

Perfect, now the first thing we want to show is that our most basic package, the Vein Pack, actually has a significant impact on the subscribers. It would be a marketing goldmine if we can show that subscribers to the Vein Pack live longer than other people.

Lifespans of Vein Pack users are returned by the function lifespans(package='vein'), which is part of the familiar module. Call that function and save the data into a variable called vein_pack_lifespans.
"""
vein_pack_lifespans = fm.lifespans(package="vein")
print("vein_pack_lifespans: \n" + str(vein_pack_lifespans))

"""
We'd like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 71 years.

Import the statistical test we would use to determine if a sample comes from a population that has a given mean from scipy.stats.
"""
ttest, vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print("vein_pack_test of ttest_1samp: \n" + str(vein_pack_test))

"""
Let's check if the results are significant! Check the pvalue of vein_pack_test. If it's less than 0.05, we've got significance!
"""
"""
We want to present this information to the CEO, Vlad, of this incredible finding. Let's print some information out! If the test's p-value is less than 0.05, print "The Vein Pack Is Proven To Make You Live Longer!". Otherwise print "The Vein Pack Is Probably Good For You Somehow!"
"""
if vein_pack_test < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

"""
Upselling Familiar: Pumping Life Into The Company

In order to differentiate Familiar's different product lines, we'd like to compare this lifespan data between our different packages. Our next step up from the Vein Pack is the Artery Pack. Let's get the lifespans of Artery Pack subscribers using the same method, called with package='artery' instead. Save the value into a variable called artery_pack_lifespans.
"""
artery_pack_lifespans = fm.lifespans(package="artery")
print("artery_pack_lifespans: \n" + str(artery_pack_lifespans))

"""
Now we want to show that the subscribers to the Artery Pack experience a significant improvement even beyond what a Vein Pack subscriber's benefits. Import the 2-Sample T-Test and we'll use that to see if there is a significant difference between the two subscriptions.
Don't forget to import ttest_ind from scipy.stats.
"""
"""
Okay let's run the 2-Sample test! Save the results into a variable named package_comparison_results.
"""
ttest, package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print("package_comparison_results: \n" + str(package_comparison_results))

"""
Let's see the results! If the p-value from our experiment is less than 0.05, the results are significant and we should print out "the Artery Package guarantees even stronger results!". Otherwise we should print out "the Artery Package is also a great product!"
"""
if package_comparison_results < 0.05:
  print("the Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")

"""
Well, shame that it's not significantly better, but maybe there's a way to demonstrate the benefits of the Artery Package yet.
"""
"""
Benefitting Everyone: A Familiar Problem

If your lifespan isn't significantly increased by signing up for the Artery Package, maybe we can make some other claim about the benefits of the package. To that end, we've sent out a survey collecting the iron counts for our subscribers, and filtered that data into "low", "normal", and "high".

We received 200 responses from our Vein Package subscribers. 70% of them had low iron counts, 20% had normal, and 10% of them have high iron counts.

We were only able to get 145 responses from our Artery Package subscribers, but only 20% of them had low iron counts. 60% had normal, and 20% have high iron counts.
"""
"""

The data from the survey has been collected and formatted into a contingency table. You can access that data from the function familiar.iron_counts_for_package(). Save the survey results into a variable called iron_contingency_table.
"""
iron_contingency_table = fm.iron_counts_for_package()
print("iron_contingency_table: \n" + str(iron_contingency_table))

"""
We want to be able to tell if what seems like a higher number of our Artery Package subscribers is a significant difference from what was reported by Vein Package subscribers. Import the Chi-Squared test so that we can find out.

Import the Chi-Squared test from scipy:
from scipy.stats import chi2_contingency
"""
"""
Run the Chi-Squared test on the iron_contingency_table and save the p-value in a variable called iron_pvalue. Remember that this test returns four things: the test statistic, the p-value, the number of degrees of freedom, and the expected frequencies.
"""
ttest, iron_pvalue, n, f = chi2_contingency(iron_contingency_table)
print("iron_pvalue: \n" + str(iron_pvalue))

"""
Here's the big moment: if the iron_pvalue is less than 0.05, print out "The Artery Package Is Proven To Make You Healthier!" otherwise we'll have to use our other marketing copy: "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"
"""
if iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")

"""
Fantastic! With proven benefits to both of our product lines, we can definitely ramp up our marketing and sales. Look out for a Familiar face in drug stores everywhere.
"""


