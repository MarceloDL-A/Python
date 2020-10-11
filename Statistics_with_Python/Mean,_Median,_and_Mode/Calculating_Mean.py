"""
MEAN
Calculating Mean
The mean, often referred to as the average, is a way to measure the center of a dataset.

The average of a set is calculated using a two-step process:

Add all of the observations in your dataset.
Divide the total sum from step one by the number of points in your dataset.
\bar{x} = \frac{x_1 + x_2 … + x_{n}}{n} 
?	 
The equation above is used to calculate mean. x1, x2, … xn are observations from a dataset of n observations.

Example
Imagine that we wanted to calculate average of a dataset with the following four observations:

data = [4, 6, 2, 8]
Step One: Calculate the total
4 + 6 + 2 + 8 = 20

Step Two: Divide by the number of observations
The total is equal to 20, and the number of observations is equal to 4.

\frac{20}{4} = 5 
The average of this dataset is equal to 5.
"""
# Set total equal to the sum
total = 0
total = 29 + 49 + 42 + 43
# Set mean_value equal to the 

mean_value = 0
mean_value = total/4
# The following code prints the total and mean
print("The sum total is equal to: " + str(total))
print("The mean value is equal to: " + str(mean_value))

