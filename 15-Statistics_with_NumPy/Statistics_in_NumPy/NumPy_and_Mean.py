"""
INTRODUCTION TO STATISTICS WITH NUMPY
NumPy and Mean
The first statistical concept we'll explore is mean, also commonly referred to as an average. The mean is a useful measurement to get the center of a dataset. NumPy has a built-in function to calculate the average or mean of arrays: np.mean

Let's say we want to find the average number of pounds of produce a person purchases per week. We administered a survey and received 1,000 responses:

survey_responses = [5, 10.2, 4, .3 ... 6.6]
We can then transform the dataset into a NumPy array and use the function np.mean to calculate the average:

>>> survey_array = np.array(survey_responses)
>>> np.mean(survey_array)
5.220
"""
import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

"""The beverage distributor, Wine Not? wants to calculate how many bottles of Bourdeaux it sells on average at three area wine sellers to determine whether or not it should increase its stock. The sales for the past week for each store are listed in script.py.

Find the average sales for each store, and save them to the variables store_one_avg, store_two_avg, and store_three_avg
"""
store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)
print("store_one_avg: " + str(store_one_avg))
print("store_two_avg: " + str(store_two_avg))
print("store_three_avg: " + str(store_three_avg))

"""
Notice the average sales per week for each store. The boss says that we should increase what we stock, but only if the store's average sales are greater than 7 bottles per week.

Save the store dataset variable name that fits this description to the variable best_seller.
"""
best_seller = store_two



