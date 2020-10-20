"""
INTRODUCTION TO STATISTICS WITH NUMPY
Calculating the Mean of 2D Arrays
If we have a two-dimensional array, np.mean can calculate the means of the larger array as well as the interior values.

Let's imagine a game of ring toss at a carnival. In this game, you have three different chances to get all three rings onto a stick. In our ring_toss array, each interior array (the arrays within the larger array) is one try, and each number is one ring toss. 1 represents a successful toss, 0 represents a fail.

First, we can use np.mean to find the mean across all the arrays:

>>> ring_toss = np.array([[1, 0, 0], 
                          [0, 0, 1], 
                          [1, 0, 1]])
>>> np.mean(ring_toss)
0.44444444444444442
To find the means of each interior array, we specify axis 1 (the "rows"):

>>> np.mean(ring_toss, axis=1)
array([ 0.33333333,  0.33333333,  0.66666667])
To find the means of each index position (i.e, mean of all 1st tosses, mean of all 2nd tosses, ...), we specify axis 0 (the "columns"):

>>> np.mean(ring_toss, axis=0)
array([ 0.66666667,  0.        ,  0.66666667])
"""

import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

"""
In script.py, we've provided data about a trial for a new allergy medication, AllerGeeThatSucks! Five participants were asked to rate how drowsy the medication made them once a day for three days on a scale of one (least drowsy) to ten (most drowsy).

Use np.mean to find the average level of drowsiness across all the trials and save the result to the variable total_mean.
"""
total_mean = np.mean(allergy_trials)
print("total_mean: " + str(total_mean))

"""
Use np.mean to find the average level of drowsiness across each day of the experiment and save to the variable trial_mean.
"""
trial_mean = np.mean(allergy_trials, axis = 1)
print("across each day of the experiment the trial_mean: " + str(trial_mean))

"""
Use np.mean to find the average level of drowsiness across for each individual patient to see if some were more sensitive to the drug than others and save it to the variable patient_mean.
"""
patient_mean = np.mean(allergy_trials, axis = 0)
print("patient_mean: " + str(patient_mean))

