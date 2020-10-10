import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
gradebook = pd.read_csv("gradebook.csv")

#Next, take a minute to understand the data you’ll analyze. The DataFrame gradebook contains the complete gradebook for a hypothetical classroom. Use print to examine gradebook.
print(gradebook)

#Select all rows from the gradebook DataFrame where assignment_name is equal to Assignment 1. Save the result to the variable assignment1.
assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]

#Check out the DataFrame you just created. Print assignment1.
print(assignment1)

#Now use Numpy to calculate the median grade in assignment1.
#Use np.median() to calculate the median of the column grade from assignment1 and save it to asn1_median.
asn1_median = np.median(assignment1.grade)

#Display asn1_median using print. What is the median grade on Assignment 1?
print(asn1_median )