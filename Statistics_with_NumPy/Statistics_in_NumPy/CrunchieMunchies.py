"""
LEARN STATISTICS WITH NUMPY
CrunchieMunchies
You work in marketing for a food company YummyCorps, which is developing a new kind of tasty, wholesome cereal called CrunchieMunchies. You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you've dug up nutritional data on several different competitors.

Your task is to use NumPy statistical calculations to analyze this data and prove that your CrunchieMunchies cereal is the healthiest choice for consumers.
"""
import codecademylib

"""
First, import numpy.
"""
import numpy as np

"""
Look over the cereal.csv file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as calorie_stats.

To learn more about reading data from a CSV using NumPy, read this documentation page (https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.genfromtxt.html).
"""
calorie_stats = np.genfromtxt("cereal.csv", delimiter = ",")

"""
There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition?

Save the answer to the variable average_calories and print the variable to the terminal to see the answer.
"""
average_calories = np.mean(calorie_stats)
print("average_calories: " + str(average_calories))

"""
Does the average calorie count adequately reflect the distribution of the dataset? Let's sort the data and see.

Sort the data and save the result to the variable calorie_stats_sorted. Print the sorted data to the terminal.
"""
calorie_stats_sorted = np.sort(calorie_stats)
print("calorie_stats_sorted: " + str(calorie_stats_sorted))

"""
Do you see what I'm seeing? Looks like the majority of the cereals are higher than the mean. Let's see if the median is a better representative of the dataset.

Calculate the median of the dataset and save your answer to median_calories. Print the median so you can see how it compares to the mean.
"""
median_calories = np.median(calorie_stats)
print("median_calories: " + str(median_calories))

"""
While the median demonstrates that at least half of our values are over 100 calories, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.

Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable nth_percentile.
"""
nth_percentile = np.percentile(calorie_stats, 4)
print("nth_percentile: " + str(nth_percentile))

"""
While the percentile shows us that the majority of the competition has a much higher calorie count, it's an awkward concept to use in marketing materials.

Instead, let's calculate the percentage of cereals that have more than 60 calories per serving. Save your answer to the variable more_calories and print it to the terminal.
"""
more_calories = np.mean(calorie_stats > 60)
print("more_calories: " + str(round(100*more_calories, 2)) + "% of the competition")

"""
Wow! That's a really high percentage. That's going to be very useful when we promote CrunchieMunchies. But one question is, how much variation exists in the dataset? Can we make the generalization that most cereals have around 100 calories or is the spread even greater?

Calculate the amount of variation by finding the standard deviation. Save your answer to calorie_std and print to the terminal. How can we incorporate this value into our analysis?
Ans.: mean +- std
"""
calorie_std = np.std(calorie_stats)
print("calorie_std: " + str(calorie_std))








