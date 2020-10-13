"""
BOXPLOTS
Whiskers
The whiskers of a boxplot display information related to the spead of the dataset.

There are many different ways to plot the whiskers of a boxplot. You might see some boxplots where the whiskers extend to the minimum and maximum values. Some boxplots have whiskers that extend one standard deviation away from the mean of the data.

However, one of the most commonly used methods of drawing the whiskers is to extend them 1.5 times the interquartile range from the first and third quartile.

For example, let’s say you had a dataset where the first quartile was 4 and the third quartile was 9. The interquartile range for this dataset is 5.

The whiskers would extend 1.5 times the length of the IQR. In this case, that is 1.5 * 5, or 7.5.

We know the whiskers extend 7.5 units, but where do they start? They start at the edges of the box, or the first and third quartiles. In this case, the left whisker starts at the first quartile (4), and extend 7.5 units to the left. So the left whisker extends to -3.5. The right whisker starts at the third quartile (9) and extends to 16.5.


One more small detail to note — the whiskers usually don’t extend all the way to 1.5 times the IQR. Instead, they extend to the point closest to 1.5 times the IQR in the direction of the median. This means that instead of extending to -3.5 and 16.5, the whiskers would actually extend to the first point greater than -3.5 and the first point less than 16.5.
"""
import numpy as np
from data import dataset

quartile_one = np.quantile(dataset, 0.25) 
quartile_three = np.quantile(dataset, 0.75)
# Define your variables here:
iqr = quartile_three - quartile_one
distance = 1.5*iqr
left_whisker = quartile_one - distance
right_whisker = quartile_three + distance
#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
  
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
  
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
  
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")