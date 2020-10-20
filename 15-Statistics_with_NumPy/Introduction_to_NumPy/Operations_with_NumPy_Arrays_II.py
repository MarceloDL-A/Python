"""
INTRODUCTION TO NUMPY
Operations with NumPy Arrays II
Arrays can also be added to or subtracted from each other in NumPy, assuming the arrays have the same number of elements.

When adding or subtracting arrays in NumPy, each element will be added/subtracted to its matching element.

>>> a = np.array([1, 2, 3, 4, 5])
>>> b = np.array([6, 7, 8, 9, 10])
>>> a + b
array([ 7,  9, 11, 13, 15])
"""
import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

"""
Let's find the average of each student's test scores to calculate their final grade for the semester. Start by adding the three arrays together and save the answer to the variable total_grade. Remember to use the fixed scores for test three.
"""
total_grade = test_1 + test_2 + test_3_fixed


"""
Now, divide total_grade by the number of tests taken to find the average score for each student. Save the answer to the variable final_grade.
"""
final_grade = total_grade/3

"""
Print the results of final_grade to the terminal.
"""
print(final_grade)

