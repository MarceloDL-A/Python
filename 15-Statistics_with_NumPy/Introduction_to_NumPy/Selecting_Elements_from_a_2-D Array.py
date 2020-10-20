"""
INTRODUCTION TO NUMPY
Selecting Elements from a 2-D Array
Selecting elements from a 2-d array is very similar to selecting them from a 1-d array, we just have two indices to select from. The syntax for selecting from a 2-d array is a[row,column] where a is the array.

It's important to note that when we work with arrays that have more than one dimension, the relationship between the interior arrays is defined in terms of axes. A two-dimensional array has two axes: axis 0 represents the values that share the same indexical position (are in the same column), and axis 1 represents the values that share an array (are in the same row). This is illustrated below.

Diagram showing the axes in an array

Consider the array

a = np.array([[32, 15, 6, 9, 14], 
              [12, 10, 5, 23, 1],
              [2, 16, 13, 40, 37]])
We can select specific elements using their indices:

>>> a[2,1]
16
Let's say we wanted to select an entire column, we can insert : as the row index:

# selects the first column
>>> a[:,0]
array([32, 12,  2])
The same works if we want to select an entire row:

# selects the second row
>>> a[1,:]
array([12, 10,  5, 23,  1])
We can further narrow it down and select a range from a specific row:

# selects the first three elements of the first row
>>> a[0,0:3]
array([32, 15,  6])
"""

import numpy as np

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
"""
Our students' test scores are now stored in the 2-d array student_scores. The first row stores the scores of the first test, the second row the second test, and the third row the third test, as shown in the following table:

Tanya	Manual	Adwoa	Jeremy	Cody
test_1	92	94	88	91	87
test_2	79	100	86	93	91
test_3	87	85	72	90	92

Tanya wants to know how well she did on third test. Select her score from the array and save it to tanya_test_3.
"""
tanya_test_3 = student_scores[2, 0]

"""
You have a parent teacher conference with Cody's parents coming up and would like to have all of his test scores handy.

Select all of Cody's test scores and save them to a new array cody_test_scores.
"""
cody_test_scores = student_scores[:, 4]

                      