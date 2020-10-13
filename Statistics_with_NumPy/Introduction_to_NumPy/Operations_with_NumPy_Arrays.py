"""
INTRODUCTION TO NUMPY
Operations with NumPy Arrays
Generally, NumPy arrays are more efficient than lists. One reason is that they allow you to do element-wise operations. An element-wise operation allows you to quickly perform an operation, such as addition, on each element in an array.

Let's compare how to add a number to each value in a python list versus a NumPy array:

# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)
# With an array
a = np.array(l)
a_plus_3 = a + 3
As we can see, if we were to add 3 to every number in a list, we would have to use a for loop or a list comprehension. With an array, we can just add 3. The same is true for subtraction, multiplication, and division.

We can also use NumPy Arrays to find the squares or square roots of each value.

Squaring each value:

>>> a ** 2
array([ 1,  4,  9, 16, 25, 36])
(Note: ** is the exponent notation in Python. For example, 3 squared can be calculated using 3 ** 2.)

Taking the square root of each value:

>>> np.sqrt(a)
array([ 1, 1.41421356, 1.73205081, 2, 2.23606798, 2.44948974])
"""
import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

"""
The student's grades on the third test are stored in the array test_3.

But it turns out that one of the questions on the third test had an error. Give each student two extra points and save the new array to test_3_fixed.
"""
test_3_fixed = test_3 + 2

