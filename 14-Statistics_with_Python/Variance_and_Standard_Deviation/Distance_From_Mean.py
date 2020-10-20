"""
Now that you have learned the importance of describing the spread of a dataset, let’s figure out how to mathematically compute this number.

How would you attempt to capture the spread of the data in a single number?

Let’s start with our intuition — we want the variance of a dataset to be a large number if the data is spread out, and a small number if the data is close together.

Two histograms. One with a large spread and one with a smaller spread.
A lot of people may initially consider using the range of the data. But that only considers two points in your entire dataset. Instead, we can include every point in our calculation by finding the difference between every data point and the mean.

The difference between the mean and four different points.
If the data is close together, then each data point will tend to be close to the mean, and the difference will be small. If the data is spread out, the difference between every data point and the mean will be larger.

Mathematically, we can write this comparison as

\text{difference} = X - \mudifference=X-µ
Where X is a single data point and the Greek letter mu is the mean.

Instructions
1.
We’ve given you a very small dataset of five values named grades. These are five randomly chosen grades from the first teacher’s class. We’ve also calculated the mean of this small dataset and stored it in a variable named mean.

Let’s find the difference between each of these data points and the mean. We’ve created a variable for each difference. Start with difference_one. Change the value of difference_one — it should be equal to the first value in the data set minus mean.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Fill in the correct values for difference_two through difference_five. Some of these values will be negative! Make sure to follow the formula exactly.

\text{difference} = X - \mudifference=X-µ

"""

import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = grades[0] - mean
difference_two =  grades[1] - mean
difference_three =  grades[2] - mean
difference_four =  grades[3] - mean
difference_five =  grades[4] - mean


# IGNORE CODE BELOW HERE
print("The mean of the data set is " + str(mean) + "\n")
print("The first student is " +str(round(difference_one, 2)) + " percentage points away from the mean.")
print("The second student is " +str(round(difference_two, 2)) + " percentage points away from the mean.")
print("The third student is " +str(round(difference_three, 2)) + " percentage points away from the mean.")
print("The fourth student is " +str(round(difference_four, 2)) + " percentage points away from the mean.")
print("The fifth student is " +str(round(difference_five, 2)) + " percentage points away from the mean.")