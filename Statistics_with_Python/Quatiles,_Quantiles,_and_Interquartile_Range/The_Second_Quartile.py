"""
QUARTILES
The Second Quartile
We’ll come back to the music dataset in a bit, but let’s first practice on a small dataset.

Let’s begin by finding the second quartile (Q2). Q2 happens to be exactly the median. Half of the data falls below Q2 and half of the data falls above Q2.

The first step in finding the quartiles of a dataset is to sort the data from smallest to largest. For example, below is an unsorted dataset:

[8, 15, 4, -108, 16, 23, 42][8,15,4,-108,16,23,42]
After sorting the dataset, it looks like this:

[-108, 4, 8, 15, 16, 23, 42][-108,4,8,15,16,23,42]
Now that the list is sorted, we can find Q2. In the example dataset above, Q2 (and the median) is 15 — there are three points below 15 and three points above 15.

Even Number of Datapoints
You might be wondering what happens if there is an even number of points in the dataset. For example, if we remove the -108 from our dataset, it will now look like this:

[4, 8, 15, 16, 23, 42][4,8,15,16,23,42]
Q2 now falls somewhere between 15 and 16. There are a couple of different strategies that you can use to calculate Q2 in this situation. One of the more common ways is to take the average of those two numbers. In this case, that would be 15.5.

Recall that you can find the average of two numbers by adding them together and dividing by two.

"""

"""
We’ve included two small unsorted datasets named dataset_one and dataset_two.

We’ve also included, as a comment, the sorted version of the first dataset.

By looking at sorted version of dataset_one, find the second quartile of the dataset and store it in a variable named dataset_one_q2.
"""

dataset_one = [50, 10, 4, -3, 4, -20, 2]
#Sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]


"""
Find the second quartile of the dataset_two and store it in a variable named dataset_two_q2.

Remember to sort the dataset. It might help to write out the sorted dataset as a comment!

Since there are an even number of datapoints in this dataset, the second quartile will fall between two points. The second quartile will be the average of those two points.

"""
dataset_two = [24, 20, 1, 45, -15, 40]
dataset_two.sort()
print(dataset_two)

#Define the second quartile of both datasets here:
dataset_one_q2 = 4
dataset_two_q2 = 22

#Ignore the code below here:
try:
  print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
  print("You haven't defined dataset_one_q2")
try:
  print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
  print("You haven't defined dataset_two_q2")