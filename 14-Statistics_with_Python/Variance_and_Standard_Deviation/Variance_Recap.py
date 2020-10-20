"""
Variance Recap
When beginning to work with a dataset, one of the first pieces of information you might want to investigate is the spread — is the data close together or far apart? One of the tools in our statistics toolbelt to do this is the descriptive statistic variance:

\sigma^2 = \frac{\sum_{i=1}^{N}{(X_i -\mu)^2}}{N}s 

By finding the variance of a dataset, we can get a numeric representation of the spread of the data. If you want to take a deeper dive into how to calculate variance, check out our variance course.

But what does that number really mean? How can we use this number to interpret the spread?

It turns out, using variance isn’t necessarily the best statistic to use to describe spread. Luckily, there is another statistic — standard deviation — that can be used instead.

In this lesson, we’ll be working with two datasets. The first dataset contains the heights (in inches) of a random selection of players from the NBA. The second dataset contains the heights (in inches) of a random selection of users on the dating platform OkCupid — let’s hope these users were telling the truth about their height!

Instructions
1.
Run the code to see a histogram of the datasets. Look at the console to see the mean and variance of each dataset. Try to answer the following questions:

What does it mean for the OkCupid dataset to have a larger variance than the NBA dataset?
What are the units of the mean? Is someone who is 80 inches tall taller than the average of either group? Which group(s)?
In this example, the units of variance are inches squared. Can you interpret what it means for the variance of the NBA dataset to be 13.32 inches squared?

Hint
Because the OkCupid dataset has a larger variance than the NBA dataset, that means that NBA players are more similar in height to each other. The height of OkCupid users vary more.

Somebody who is 80 inches tall is above the average height of both datasets. We can directly compare 80 inches to the mean because they are in the same units (inches).

It’s a bit hard to wrap your head around how variance and mean are related since they are in different units.
"""
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from data import nba_data, okcupid_data

plt.hist(nba_data, alpha = 0.75, label = "NBA Data", bins = 20)
plt.hist(okcupid_data, alpha = 0.5, label = "OkCupid Data", bins = 20)
plt.xlabel("Height (inches)")
plt.legend()
plt.show()

print("The variance of the NBA dataset is " +str(np.var(nba_data)))
print("The variance of the OkCupid dataset is " +str(np.var(okcupid_data)) + "\n")
print("The mean of the NBA dataset is " +str(np.mean(nba_data)) + " inches")
print("The mean of the OkCupid dataset is " +str(np.mean(okcupid_data)) + " inches")