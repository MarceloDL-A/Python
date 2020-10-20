"""
You just learned a commonly used method to calculate the quartiles of a dataset. However, there is another method that is equally accepted that results in different values!

Note that there is no universally agreed upon method of calculating quartiles, and as a result, two different tools might report different results.

The second method includes Q2 when trying to calculate Q1 and Q3. Let’s take a look at an example:

[-108, 4, 8, 15, 16, 23, 42][-108,4,8,15,16,23,42]
Using the first method, we found Q1 to be 4. When looking at all of the points below Q2, we excluded Q2. Using this second method, we include Q2 in each half.

For example, when calculating Q1 using this new method, we would now find the median of this dataset:

[-108, 4, 8, 15][-108,4,8,15]
Using this method, Q1 is 6.
"""
dataset_one = [50, 10, 4, -3, 4, -20, 2]
#Sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]

dataset_two = [24, 20, 1, 45, -15, 40]
dataset_two.sort()
print(dataset_two)
dataset_one_q2 = 4
dataset_two_q2 = 22
#Define the first and third quartile of both datasets here:
"""
Create a variable named dataset_one_q1 and set it equal to the first quartile of dataset one. This time, use the second method of finding quartiles.
"""
dataset_one_q1 = -0.5
dataset_one_q3 = 7

"""
Create two variables named dataset_two_q1 and dataset_two_q3 and set them equal to the first and third quartile of dataset three.

Use the second method of calculating quartiles. Since Q2 fell between two data points, this method is no different than the first method!
"""
dataset_two_q1 = 1
dataset_two_q3 = 40






#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(dataset_one_q1))
except NameError:
  print("You haven't defined dataset_one_q1")
try:
  print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
  print("You haven't defined dataset_one_q2")
try:
  print("The third quartile of dataset one is " + str(dataset_one_q3) + "\n")
except NameError:
  print("You haven't defined dataset_one_q3\n")
try:
  print("The first quartile of dataset two is " + str(dataset_two_q1))
except NameError:
  print("You haven't defined dataset_two_q1")
try:
  print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
  print("You haven't defined dataset_two_q2")
try:
  print("The third quartile of dataset two is " + str(dataset_two_q3))
except NameError:
  print("You haven't defined dataset_two_q3")
