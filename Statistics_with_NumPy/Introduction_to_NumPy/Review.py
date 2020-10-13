"""
INTRODUCTION TO NUMPY
Review
Let's take a second and review. In this lesson, you learned the basics of the NumPy package. Here are some key points:

Arrays are a special type of list that allows us to store values in an organized manner.
An array can be created by either defining it directly using np.array() or by importing a CSV using np.genfromtxt('file.csv', delimiter=',').
An operation (such as addition) can be performed on every element in an array by simply performing it on the array itself.
Elements can be selected from arrays using their index and array locations, both of which start at 0.
Logical operations can be used to create new, more focused arrays out of larger arrays.
The next lesson will explore how to analyze these arrays and use means, medians, and standard deviations to tell a story. But first, practice what you've learned by working through the following checkpoints.
"""
"""
You are working on a team of climate scientists and one of your roles is to take the weekly temperature data and input into NumPy arrays for later analysis. The sensor records the temperature 4 times a day, at 0:00, 6:00, 12:00, and 18:00. You are given last weeks data (Monday through Friday) and asked to create a NumPy array.

Get started by importing the numpy package.
"""
import numpy as np

"""
Create an array temperatures by importing the data in the CSV temperature_data.csv

(CSV based on data from the National Oceanic and Atmospheric Administration)
"""
temperatures = np.genfromtxt("temperature_data.csv", delimiter = ",")

"""
Inspect the data by printing it to the terminal.

The columns are the times, starting at 0:00, and the rows are days, starting on Monday, and the values are the recorded temperatures at that time on those days.
"""
print(temperatures)

"""
One of the researchers noticed that the sensor had been incorrectly zeroed and all of the recorded temperatures are 3.0 degrees too cold.

Adjust the array so that the temperature readings are accurate and save them to temperatures_fixed.
"""
temperatures_fixed = temperatures + 3

"""
Another researcher asked you for the temperature values from Monday. Save them to a new array, monday_temperatures.
"""
monday_temperatures = temperatures_fixed[0, :]
print("monday_temperatures: " + str(monday_temperatures))

"""
"Hmmm, interesting" the researcher mumbles, "can you also give me the 6:00 AM data for Thursday and Friday?"

Save this data to a new array thursday_friday_morning.
"""
thursday_friday_morning = temperatures_fixed[3:, 1]
print("thursday_friday_morning at 6:00: " + str(thursday_friday_morning))

"""Finally, the persistent researcher now wants all the high and low temperatures over the week.

Select all temperatures that are under 50 degrees or over 60 degrees and save them to a new array temperature_extremes.
"""
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
print("temperature_extremes: " + str(temperature_extremes))


