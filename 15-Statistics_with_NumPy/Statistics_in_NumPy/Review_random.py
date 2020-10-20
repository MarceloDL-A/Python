"""
STATISTICAL DISTRIBUTIONS WITH NUMPY
Review
Let's review! In this lesson, you learned how to use NumPy to analyze different distributions and generate random numbers to produce datasets. Here's what we covered:

What is a histogram and how to map one using Matplotlib
How to identify different dataset shapes, depending on peaks or distribution of data
The definition of a normal distribution and how to use NumPy to generate one using NumPy's random number functions
The relationships between normal distributions and standard deviations
The definition of a binomial distribution
Now you can use NumPy to analyze and graph your own datasets! You should practice building your intuition about not only what the data says, but what conclusions can be drawn from your observations.
"""
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

"""
Practice what you've just learned with a dataset on sunflower heights! Imagine that you work for a botanical garden and you want to see how the sunflowers you planted last year did to see if you want to plant more of them.

Calculate the mean and standard deviation of this dataset. Save the mean to sunflowers_mean and the standard deviation to sunflowers_std.
"""
# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)
print("sunflowers_mean: " + str(sunflowers_mean))
print("sunflowers_std: " + str(sunflowers_std))

"""
We can see from the histogram that our data isn't normally distributed. Let's create a normally distributed sample to compare against what we observed.

Generate 5,000 random samples with the same mean and standard deviation as sunflowers. Save these to sunflowers_normal.
np.random.normal(
    loc=desired_mean,
    scale=desired_std,
    size=num_samples)
"""
# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, 5000)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)


"""
Now that you generated sunflowers_normal, uncomment (remove all of the #) the second plt.hist statement. Press run to see your normal distribution and your observed distribution.
"""
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()

"""
Generally, 10% of sunflowers that are planted fail to bloom. We planted 200, and want to know the probability that fewer than 20 will fail to bloom.

First, generate 5,000 binomial random numbers that represent our situation. Save them to experiments.
    Recall that we can generate binomial samples using the following code:
    np.random.binomial(n, p, size=size)
    Where:
    n is the number of trials (i.e., how many sunflowers did we plant?)
    p is the probability of each event (i.e., what is the probability of any individual sunflower failing to bloom?)
    size is the number of random numbers we want to generate
"""
experiments = np.random.binomial(200, 0.1, 5000)
print("experiments: " + str(experiments))
"""
What percent of experiments had fewer than 20 sunflowers fail to bloom?

Save your answer to the variable prob. This is the approximate probability that fewer than 20 of our sunflowers will fail to bloom.
"""
# Calculate probabilities here:
prob = np.mean(experiments < 20)
print("prob: " + str(prob))



