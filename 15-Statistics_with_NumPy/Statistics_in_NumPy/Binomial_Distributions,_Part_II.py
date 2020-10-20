"""
STATISTICAL DISTRIBUTIONS WITH NUMPY
Binomial Distributions, Part II
There are some complicated formulas for determining these types of probabilities. Luckily for us, we can use NumPy - specifically, its ability to generate random numbers. We can use these random numbers to model a distribution of numerical data that matches the real-life scenario we’re interested in understanding.

For instance, suppose we want to know the different probabilities of our basketball player making 1, 2, 3, etc. out of 10 shots.

NumPy has a function for generating binomial distributions: np.random.binomial, which we can use to determine the probability of different outcomes.

The function will return the number of successes for each “experiment”.

It takes the following arguments:

N: The number of samples or trials
P: The probability of success
size: The number of experiments
Let’s generate a bunch of “experiments” of our basketball player making 10 shots. We choose a big N to be sure that our probabilities converge on the correct answer.

# Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)

a = np.random.binomial(10, 0.30, size=10000)
Now we have a record of 10,000 experiments. We can use Matplotlib to plot the results of all of these experiments:

plt.hist(a, range=(0, 10), bins=10, normed=True)
plt.xlabel('Number of "Free Throws"')
plt.ylabel('Frequency')
plt.show()
"""
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

"""
A person sends 500 emails asking people to donate to their cause, with an estimated probability that 25 people (5%) will open the email and click to donate. There were 10,000 experiments.

Using the binomial distribution formula, calculate the distribution and save it to the variable emails.
"""
emails = np.random.binomial(500, 0.05, 10000)

"""
Plot the graph of the binomial distribution using the default histogram settings and display it using plt.show().
"""
plt.show()



