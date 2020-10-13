"""
QUARTILES
Quartiles in NumPy
We were able to find quartiles manually by looking at the dataset and finding the correct division points. But that gets much harder when the dataset starts to get bigger. Luckily, there is a function in the NumPy library that will find the quartiles for you.

The NumPy function that we’ll be using is named quantile(). You can learn more about quantiles in our quantiles lesson, but for right now all you need to know is that a quartile is a specific kind of quantile.

The code below calculates the third quartile of the given dataset:

import numpy as np

dataset = [50, 10, 4, -3, 4, -20, 2]
third_quartile = np.quantile(dataset, 0.75)
The quantile() function takes two parameters. The first is the dataset you’re interested in. The second is a number between 0 and 1. Since we calculated the third quartile, we used 0.75 — we want the point that splits the first 75% of the data from the rest.

For the second quartile, we’d use 0.5. This will give you the point that 50% of the data is below and 50% is above.

Notice that the dataset doesn’t need to be sorted for NumPy’s function to work!
"""

from song_data import songs
import numpy as np

#Create the variables songs_q1, songs_q2, and songs_q3 here:
"""
We’ve brought back our music dataset. The lengths of 9,975 songs (in seconds) are stored in a variable named songs. Use Numpy’s quantile() function to find the first quartile. Store the result in a variable named songs_q1.

Find the second and third quartile of the dataset and store the values in two variables named songs_q2 and songs_q3

Look up the length of your favorite song in seconds. Store that value in a variable named favorite_song.
Does that song fall in the first, second, third, or fourth quarter of the data? Create a variable named quarter. Set quarter equal to 1 if your favorite song falls in the first quarter of the data. Set it equal to 2 if your song falls in the second fourth. Set it equal to 3 if your song falls in the third fourth. And set it to 4 if your song falls in the final fourth of the data.
"""
songs_q1 = np.quantile(songs, 0.25)
songs_q2 = np.quantile(songs, 0.50)
songs_q3 = np.quantile(songs, 0.75)
favorite_song = 200
quarter = 2


#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
  print("You haven't defined songs_q1")
try:
  print("The second quartile of dataset one is " + str(songs_q2)+ " seconds")
except NameError:
  print("You haven't defined songs_q2")
try:
  print("The third quartile of dataset one is " + str(songs_q3)+ " seconds")
except NameError:
  print("You haven't defined songs_q3\n")