"""
INTRODUCTION TO STATISTICS WITH NUMPY
Sorting and Outliers
One way to quickly identify outliers is by sorting our data, Once our data is sorted, we can quickly glance at the beginning or end of an array to see if some values lie far beyond the expected range. We can use the NumPy function np.sort to sort our data.

Let's go back to our 3rd grade height example, and imagine an 8th grader walked into our experiement:

>>> heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])
If we use np.sort, we can immediately identify the taller student since their height (62") is noticeably outside the range of the dataset:

>>> np.sort(heights)
array([ 46.9,  47. ,  47.2,  48.3,  48.7,  49.7,  62])
"""
import numpy as np

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

"""
You've been tracking temperature data over the summer on your back porch, but realized that you placed your sensor right over a grill! Before you can use your data, you need to check to see if the heat from the grill caused any weird readings that could skew your data.

First, sort the temps data array and save the sorted data to a sorted_temps variable.
"""
sorted_temps = np.sort(temps)
print("sorted_temps: " + str(sorted_temps))


