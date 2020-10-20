"""
Quartiles
The interquartile range is the difference between the third quartile (Q3) and the first quartile (Q1). 

For now, all you need to know is that the first quartile is the value that separates the first 25% of the data from the remaining 75%.

The third quartile is the opposite — it separates the first 75% of the data from the remaining 25%.

The interquartile range of the dataset is shown to be between Q3 and Q1.
The interquartile range is the difference between these two values.
"""
from song_data import songs
import numpy as np

"""
We’ve calculated the first quartile of songs and stored it in the variable q1.

Calculate the third quartile and store it in a variable named q3.

To calculate the third quartile, call the same function, but change the second parameter to 0.75.
"""

q1 = np.quantile(songs, 0.25)
#Create the variables q3 and interquartile_range here:
q3 = np.quantile(songs, 0.75)
"""
Now that we have both the first quartile and the third quartile, let’s calculate the IQR.

Create a variable named interquartile_range and set it equal to the difference between q3 and q1.
"""
interquartile_range = q3 - q1


# Ignore the code below here
try:
  print("The first quartile of the dataset is " + str(q1) + "\n")
except NameError:
  print("You haven't defined q1 yet\n")
  
try:
  print("The third quartile of the dataset is " + str(q3) + "\n")
except NameError:
  print("You haven't defined q3 yet\n")
  
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")