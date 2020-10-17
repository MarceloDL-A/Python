"""
DATA CLEANING WITH PANDAS
Missing Values
We often have data with missing elements, as a result of a problem with the data collection process or errors in the way the data was stored. The missing elements normally show up as NaN (or Not a Number) values:

day	bill	tip	num_guests
“Mon”	10.1	1	1
“Mon”	20.75	5.5	2
“Tue”	19.95	5.5	NaN
“Wed”	44.10	15	3
“Wed”	NaN	1	1

The num_guests value for the 3rd row is missing, and the bill value for the 5th row is missing. Some calculations we do will just skip the NaN values, but some calculations or visualizations we try to perform will break when a NaN is encountered.

Most of the time, we use one of two methods to deal with missing values.

Method 1: drop all of the rows with a missing value
We can use .dropna() to do this:

bill_df = bill_df.dropna()
This command will result in the DataFrame without the incomplete rows:

day	bill	tip	num_guests
“Mon”	10.1	1	1
“Mon”	20.75	5.5	2
“Wed”	44.10	15	3

If we wanted to remove every row with a NaN value in the num_guests column only, we could specify a subset:

bill_df = bill_df.dropna(subset=['num_guests'])
Method 2: fill the missing values with the mean of the column, or with some other aggregate value.
We can use .fillna() to do this:

bill_df = bill_df.fillna(value={"bill":bill_df.bill.mean(), "num_guests":bill_df.num_guests.mean()})
This command will result in the DataFrame with the respective mean of the column in the place of the original NaNs:

day	bill	tip	num_guests
“Mon”	10.1	1	1
“Mon”	20.75	5.5	2
“Tue”	19.95	5.5	1.75
“Wed”	44.10	15	3
“Wed”	23.725	1	1

"""
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

"""
Get the mean of the score column. Store it in score_mean and print it out.
Ans.:
score_mean: 
77.69657422512235
"""
score_mean = students.score.mean()
print("score_mean: \n" + str(score_mean))

"""
We will assume that everyone who doesn’t have a score for an exam missed the test. We want to replace all nans with a score of 0. Let’s do this with the score column.

Fill all of the nans in students['score'] with 0.
"""
students = students.fillna(value = {"score": 0})
print(students)

"""
Get the mean of the score column again. Store it in score_mean_2 and print it out.
Ans.: 
score_mean_2: 
72.30971659919028
"""
score_mean_2  = students.score.mean()
print("score_mean_2: \n" + str(score_mean_2))

