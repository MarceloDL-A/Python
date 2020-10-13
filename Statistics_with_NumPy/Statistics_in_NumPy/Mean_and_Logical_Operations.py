"""
INTRODUCTION TO STATISTICS WITH NUMPY
Mean and Logical Operations
We can also use np.mean to calculate the percent of array elements that have a certain property.

As we know, a logical operator will evaluate each item in an array to see if it matches the specified condition. If the item matches the given condition, the item will evaluate as True and equal 1. If it does not match, it will be False and equal 0.

When np.mean calculates a logical statement, the resulting mean value will be equivalent to the total number of True items divided by the total array length.

In our produce survey example, we can use this calculation to find out the percentage of people who bought more than 8 pounds of produce each week:

>>> np.mean(survey_array > 8)
0.2
The logical statement survey_array > 8 evaluates which survey answers were greater than 8, and assigns them a value of 1. np.mean adds all of the 1s up and divides them by the length of survey_array. The resulting output tells us that 20% of responders purchased more than 8 pounds of produce.
"""
import numpy as np

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])

"""
You're running an alumni reunion at your local college. You have a list of the names of each person in attendance and the year that they graduated.

We've saved this list as a NumPy array to the variable class_year. Calculate the percent of attending alumni who graduated on and after 2005 and save your result to the variable millennials.
"""
millennials = np.mean(class_year > 2005)

"""
Print the value of millennials to the terminal
"""
print("millennials: " + str(millennials))

