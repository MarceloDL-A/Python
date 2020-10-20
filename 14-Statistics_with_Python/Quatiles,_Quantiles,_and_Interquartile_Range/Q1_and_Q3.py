"""
QUARTILES
Q1 and Q3
Now that we’ve found Q2, we can use that value to help us find Q1 and Q3. Recall our demo dataset:

[-108, 4, 8, 15, 16, 23, 42][-108,4,8,15,16,23,42]
In this example, Q2 is 15. To find Q1, we take all of the data points smaller than Q2 and find the median of those points. In this case, the points smaller than Q2 are:

[-108, 4, 8][-108,4,8]
The median of that smaller dataset is 4. That’s Q1!

To find Q3, do the same process using the points that are larger than Q2. We have the following points:

[16, 23, 42][16,23,42]
The median of those points is 23. That’s Q3! We now have three points that split the original dataset into groups of four equal sizes.
"""
dataset_one = [50, 10, 4, -3, 4, -20, 2]
#Sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]

dataset_two = [24, 20, 1, 45, -15, 40]
dataset_two.sort()
print(dataset_two)
dataset_one_q2 = 4
dataset_two_q2 = 22


"""
Find the first quartile of dataset_one and store it in a variable named dataset_one_q1.
Find the third quartile of dataset_one and store it in a variable named dataset_one_q3.
Find Q1 and Q3 of dataset_two. Store the values in variables named dataset_two_q1 and dataset_two_q3.
Hint:
Q1 will be the median of [-15, 1, 20] and Q3 will be the median of [24, 40, 45].
"""
#Define the first and third quartile of both datasets here:
dataset_one_q1 = -3
dataset_one_q3 = 10
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
