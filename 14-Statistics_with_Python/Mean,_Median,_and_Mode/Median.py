"""
MEDIAN
Median
The formal definition for the median of a dataset is:

The value that, assuming the dataset is ordered from smallest to largest, falls in the middle. If there are an even number of values in a dataset, you either report both of the middle two values or their average.

There are always two steps to finding the median of a dataset:

Order the values in the dataset from smallest to largest
Identify the number(s) that fall(s) in the middle
Example One: Even Number of Values
Say we have a dataset with the following ten numbers:

24, 16, 30, 10, 12, 28, 38, 2, 4, 36

The first step is to order these numbers from smallest to largest:

2, 4, 10, 12, [16, 24], 28, 30, 36, 38

Because this dataset has an even number of values, there are two medians: 16 and 24 — 16 has four datapoints to the left, and 24 has four datapoints to the right.

Although you can report both values as the median, people often average them. If you averaged 16 and 24, you could report the median as 20.

Example Two: Odd Number of Values
If we added another value (say, 24) to the dataset and sorted it, we would have:

2, 4, 10, 12, 16, [24], 24, 28, 30, 36, 38

The new median is equal to 24, because there are 5 values to the left of it, and 5 values to the right of it.
"""
import numpy as np

"""
In the next two steps, you will manually sort an array, and then determine which value in the array is the median.

In script.py, we have an array with the ages of the first five authors from Le Monde’s survey:

29, 49, 42, 43, 32
29,49,42,43,32
Under five_author_ages there is a variable called sorted_author_ages. Change the 0s in sorted_author_ages to the sorted values from five_author_ages.
"""
# Array of the first five author ages
five_author_ages = np.array([29, 49, 42, 43, 32])

# Fill in the empty array with the values sorted
sorted_author_ages = np.array([0, 0, 0, 0, 0])
five_author_ages.sort()
for i in range(len(five_author_ages)):
  sorted_author_ages[i] = five_author_ages[i]
if len(sorted_author_ages)%2 == 0:
  p = len(sorted_author_ages)//2
  median = (sorted_author_ages[p-1] + sorted_author_ages[p])/2
  #print("The avg between " + str(p) + "º and " + str(p + 1) + "º number represent median: " + str(median))
else:
  p = len(sorted_author_ages)//2
  median = sorted_author_ages[p]
  #print(str(p + 1) + "º number represent median: " + str(median))

#Set median_age equal to the median of the array.
# Save the median value to median_value
median_age = 0
median_age = median

# Print the sorted array and median value
print("The sorted array is: " + str(sorted_author_ages))
print("The median of the array is: " + str(median_age))