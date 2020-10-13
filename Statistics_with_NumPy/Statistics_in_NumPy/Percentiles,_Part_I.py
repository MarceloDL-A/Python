"""
INTRODUCTION TO STATISTICS WITH NUMPY
Percentiles, Part I
As we know, the median is the middle of a dataset: it is the number for which 50% of the samples are below, and 50% of the samples are above. But what if we wanted to find a point at which 40% of the samples are below, and 60% of the samples are above?

This type of point is called a percentile. The Nth percentile is defined as the point N% of samples lie below it. So the point where 40% of samples are below is called the 40th percentile. Percentiles are useful measurements because they can tell us where a particular value is situated within the greater dataset.

Let's look at the following array:

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
There are 11 numbers in the dataset. The 40th percentile will have 40% of the 10 remaining numbers below it (40% of 10 is 4) and 60% of the numbers above it (60% of 10 is 6). So in this example, the 40th percentile is 4.

percentile

In NumPy, we can calculate percentiles using the function np.percentile, which takes two arguments: the array and the percentile to calculate.

Here's how we would use NumPy to calculate the 40th percentile of array d:

>>> d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8])
>>> np.percentile(d, 40)
4.00
"""

import numpy as np
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

"""
The local public library wants to study how many hours a week their patrons use the computers. At the top of the script.py, we have included sample data from 11 users in a NumPy array.

Use NumPy to find the 30th percentile of the sorted array and save it to a variable named thirtieth_percentile.
"""
thirtieth_percentile = np.percentile(patrons, 30)
print("thirtieth_percentile: " + str(thirtieth_percentile))

"""
Next, use NumPy to find the 70th percentile and save it to the variable seventieth_percentile.
"""
seventieth_percentile = np.percentile(patrons, 70)
print("seventieth_percentile: " + str(seventieth_percentile))


