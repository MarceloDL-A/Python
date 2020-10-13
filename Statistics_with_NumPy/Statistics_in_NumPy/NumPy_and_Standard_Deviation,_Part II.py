"""
INTRODUCTION TO STATISTICS WITH NUMPY
NumPy and Standard Deviation, Part II
As we saw in the last exercise, knowing the standard deviation of a dataset can help us understand how spread out our dataset is.

We can find the standard deviation of a dataset using the Numpy function np.std:

>>> nums = np.array([65, 36, 52, 91, 63, 79])
>>> np.std(nums)
17.716909687891082
"""
import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

"""
You've been asked to judge your town's annual squash festival. The festival organizer gives you a list that includes all the weights for the two competitions that you're judging: pumpkins and acorn squash.

Given the two data sets at the top of script.py, find the average weight for each competition and save them to the variables pumpkin_avg and acorn_squash_avg.
"""
pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)
print("pumpkin_avg: " + str(pumpkin_avg))
print("acorn_squash_avg: " + str(acorn_squash_avg))

"""
Now, the rest of the judges want you to give them an idea of how representative the mean values are in relation to the entirety of the submissions. Calculate the standard deviation for each of the datasets to find and save them to the variables pumpkin_std and acorn_squash_std. Print them to the console to see their values.
"""
pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)
print("pumpkin_std: " + str(pumpkin_std))
print("acorn_squash_std: " + str(acorn_squash_std))

"""
Determine the squash dataset that has the greater standard deviation and save it to the variable winner
"""
winner = pumpkin


