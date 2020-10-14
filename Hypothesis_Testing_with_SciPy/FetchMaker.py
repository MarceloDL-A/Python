"""
HYPOTHESIS TESTING WITH SCIPY
FetchMaker
Congratulations! You've just started working at the hottest new tech startup, FetchMaker. FetchMaker's mission is to match up prospective dog owners with their perfect pet. Data on thousands of adoptable dogs are in FetchMaker's system, and it's your job to analyze some of that data.
"""
import numpy as np
import fetchmaker as ft
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

"""
Play around with the data

Let's start by including a data interface called fetchmaker that will give you access to FetchMaker's dog data.

Use import fetchmaker at the top of your script.py file to import the fetchmaker package.
"""
"""
The attributes that FetchMaker keeps track of are:

weight, an integer representing how heavy a dog is in pounds
tail_length, a float representing tail length in inches
age, in years
color, a String such as "brown" or "grey"
is_rescue, a boolean 0 or 1
The fetchmaker package lets you access this data for a specific breed of dog with the following format:

fetchmaker.get_weight("poodle")
This returns a Pandas DataFrame of the weights of the poodles recorded in the system. The other methods are get_tail_length, get_color, get_age, and get_is_rescue, which all take a breed as an input.

Get the tail lengths of all of the "rottweiler"s in the system, and store it in a variable called rottweiler_tl.
"""
rottweiler_tl = ft.get_tail_length("rottweiler")
print("rottweiler_tl:  \n" + str(rottweiler_tl))

"""
Print out the mean of rottweiler_tl and the standard deviation of rottweiler_tl, using np.mean and np.std
"""
print("mean of rottweiler_tl:  \n" + str(np.mean(rottweiler_tl)))
print("std of rottweiler_tl:  \n" + str(np.std(rottweiler_tl)))

"""
Data to the rescue
Over the years, we have seen that we expect 8% of dogs in the FetchMaker system to be rescues. We want to know if whippets are significantly more or less likely to be a rescue.

Store the is_rescue values for "whippet"s in a variable called whippet_rescue.
"""
whippet_rescue = ft.get_is_rescue("whippet")
print("whippet_rescue :  \n" + str(whippet_rescue))

"""
Use np.count_nonzero to get the number of entries in whippet_rescue that are 1. Store this number in a variable called num_whippet_rescues.
"""
num_whippet_rescue = np.count_nonzero(whippet_rescue)
print("num_whippet_rescue :  \n" + str(num_whippet_rescue))

"""
Get the number of samples in the whippet set by taking the np.size of whippet_rescue. Store this in a variable called num_whippets.
Ans:
num_whippets :  
100
"""
num_whippets = np.size(whippet_rescue)
print("num_whippets :  \n" + str(num_whippets))

"""
Use a binomial test to test the number of whippet rescues, num_whippet_rescues, against our expected percentage, 8%.

Remember to import the binomial test by using from scipy.stats import binom_test.
Ans: p-vaue is too large, so we can't reject de null hypothesis
pval of binom_test: 0.581178010624
"""
pval = binom_test(num_whippet_rescue, num_whippets, 0.08)
print("pval of binom_test: " + str(pval))

"""
Size does matter
Three of our most popular mid-sized dog breeds are whippets, terriers, and pitbulls. Is there a significant difference in the average weights of these three dog breeds? Perform a comparative numerical test to determine if there is a significant difference.
Hint:
Use ANOVA for this scenario. First, use the line from scipy.stats import f_oneway to import SciPy's ANOVA function.
You can use:
f_oneway(w, t, p).pvalue
Ans.:
pval of f_oneway(ANOVA): 3.27641558827e-17
"""
w = ft.get_weight("whippet")
t = ft.get_weight("terrier")
p = ft.get_weight("pitbull")
ftest, pval = f_oneway(w, t, p)
print("pval of f_oneway(ANOVA): " + str(pval))
print("So we reject de null hypothesis")

"""
Now, perform another test to determine which of the pairs of these dog breeds differ from each other.
Hint:
Use Tukey's Range Test for this scenario. First, use the line from statsmodels.stats.multicomp import pairwise_tukeyhsd to import the test.
Ans.:
Multiple Comparison of Means - Tukey HSD,FWER=0.05
==============================================
 group1  group2 meandiff  lower  upper  reject
----------------------------------------------
pitbull terrier  -13.24  -16.728 -9.752  True 
pitbull whippet  -3.34    -6.828 0.148  False 
terrier whippet   9.9     6.412  13.388  True 
----------------------------------------------
"""
values = np.concatenate([w, t, p])
labels = ["whippet"]*len(w) + ["terrier"]*len(t) +  ["pitbull"]*len(p)
print(pairwise_tukeyhsd(values, labels, 0.05))

"""
Categorical dog test
We want to see if "poodle"s and "shihtzu"s have significantly different color breakdowns.

Get the poodle colors and store it in a variable called poodle_colors.

Get the shih tzu colors and store it in a variable called shihtzu_colors.
"""
poodle_colors = ft.get_color("poodle")
shihtzu_colors = ft.get_color("shihtzu")
print("poodle_colors: " + str(poodle_colors))
print("shihtzu_colors: " + str(shihtzu_colors))

"""
You can get the number of occurrences of brown poodles by using np.count_nonzero(poodle_colors == "brown").

Use this function to build a Chi Square contingency table, called color_table, with the following structure:

Poodle	Shih Tzu
Black	x	x
Brown	x	x
Gold	x	x
Grey	x	x
White	x	x
Fill in the "x" entries with the number of each poodle or shih tzu with the specified color.

"""
color_table = [
  [np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")], 
  [np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")], 
  [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")], 
  [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")], 
  [np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]

]
print("color_table: \n" + str(color_table))
_, color_pval, _, _ = chi2_contingency(color_table)
print("color_pval of chi2_contingency: \n" + str(color_pval))

"""
Ans.: 
[[17, 10], [13, 36], [8, 6], [52, 41], [10, 7]]
color_pval of chi2_contingency: 
0.00530240829324
p < alpha => null hypothesis rejected
"""




