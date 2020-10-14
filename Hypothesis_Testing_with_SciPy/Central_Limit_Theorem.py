"""
STATISTICAL CONCEPTS
Central Limit Theorem
Perhaps, this time, you're a tailor of school uniforms at a middle school. You need to know the average height of people from 10-13 years old in order to know which sizes to make the uniforms. Knowing the best decisions are based on data, you set out to do some research at your local middle school.

Organizing with the school, you measure the heights of some students. Their average height is 145 centimeters. You know a little about sampling and decide that measuring 30 out of the 300 students gives enough data to assume 145 cm is roughly the average height of everyone at the middle school. You set to work with this dimension and make uniforms that fit people of this height, some smaller and some larger.

Unfortunately, when you go about making your uniforms many reports come back saying that they are too small. Something must have gone wrong with your decision-making process! You go back to collect the rest of the data: you measure the sixth graders one day (144, not so bad), the seventh graders after that (152 centimeters tall on average), and the eighth graders the next day (163 centimeters!). Your sample mean was so far off from your population mean. How did this happen?

Well, your sample selection was skewed to one direction of the total population. It looks like you must have measured more sixth graders than is representative of the whole middle school. How do you get an average sample height that looks more like the average population height?

In the previous exercise, we looked at different sets of samples taken from a population and how the mean of each set could be different from the population mean. This is a natural consequence of the fact that a set of samples has less data than the population to which it belongs. If our sample selection is poor then we will have a sample mean seriously skewed from our population mean.

In order to quantify our uncertainty about whether a particular sample mean is similar to the population mean, consider the following thought experiment: suppose we go back and take 100 more samples of 30 students each. For each, we record the mean height of the students in the sample. When we're done, we'll have 100 different sample means, each from a different randomly chosen group of 30 students! Now, we can look at those 100 sample means and see how much they differ from each other. If our sample means are all between 151 and 153 centimeters, we'll probably feel more confident that we can trust any individual sample mean to be representative of the population; however, if our sample means range from 142 to 168 centimeters, we'll be less confident about any individual estimate.

In real life, we probably won't be able to collect lots of repeated samples, but luckily we can use something called the Central Limit Theorem, which tells us that a sample mean is more likely to be similar to the population mean if the sample size is large.
"""
import numpy as np

# Create population and find population mean
population = np.random.normal(loc=65, scale=100, size=3000)
population_mean = np.mean(population)

# Select increasingly larger samples
extra_small_sample = population[:10]
small_sample = population[:50]
medium_sample = population[:100]
large_sample = population[:500]
extra_large_sample = population[:1000]

"""
In the workspace we've generated increasingly larger sets of samples from the same population. Calculate the mean of each set.
"""
# Calculate the mean of those samples
extra_small_sample_mean = np.mean(extra_small_sample)
small_sample_mean = np.mean(small_sample)
medium_sample_mean = np.mean(medium_sample)
large_sample_mean = np.mean(large_sample)
extra_large_sample_mean = np.mean(extra_large_sample)

# Print them all out!
print "Extra Small Sample Mean: {}".format(extra_small_sample_mean)
print "Small Sample Mean: {}".format(small_sample_mean)
print "Medium Sample Mean: {}".format(medium_sample_mean)
print "Large Sample Mean: {}".format(large_sample_mean)
print "Extra Large Sample Mean: {}".format(extra_large_sample_mean)

print "\nPopulation Mean: {}".format(population_mean)

"""
Take a look at the means you have calculated. How does the relationship these values have with the population mean change as the sample set gets larger?
Extra Small Sample Mean: 101.971560134
Small Sample Mean: 81.1191746492
Medium Sample Mean: 70.6791830199
Large Sample Mean: 63.2842747586
Extra Large Sample Mean: 66.694580904

Population Mean: 66.1395639066
"""
