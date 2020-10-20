"""
DATA CLEANING WITH PANDAS
More String Parsing
Sometimes we want to do analysis on numbers that are hidden within string values. We can use regex to extract this numerical data from the strings they are trapped in. Suppose we had this DataFrame df representing a workout regimen:

date	exerciseDescription
10/18/2018	“lunges - 30 reps”
10/18/2018	“squats - 20 reps”
10/18/2018	“deadlifts - 25 reps”
10/18/2018	“jumping jacks - 30 reps”
10/19/2018	“lunges - 40 reps”
10/19/2018	“chest flyes - 15 reps”
…	…

It would be helpful to separate out data like "30 lunges" into 2 columns with the number of reps, "30", and the type of exercise, "lunges". Then, we could compare the increase in the number of lunges done over time, for example.

To extract the numbers from the string we can use pandas’ .str.split() function:

split_df = df['exerciseDescription'].str.split('(\d+)', expand=True)
which would result in this DataFrame split_df:

* *	0	1	2
0	“lunges - “	“30”	“reps”
1	“squats - “	“20”	“reps”
2	“deadlifts - “	“25”	“reps”
3	“jumping jacks - “	“30”	“reps”
4	“lunges - “	“40”	“reps”
5	“chest flyes - “	“15”	“reps”
…	…	…	…

Then, we can assign columns from this DataFrame to the original df:

df.reps = pd.to_numeric(split_df[1])
df.exercise = split_df[2].replace('[\- ]', '', regex=True)
Now, our df looks like this:

date	exerciseDescription	reps	exercise
10/18/2018	“lunges - 30 reps”	30	“lunges”
10/18/2018	“squats - 20 reps”	20	“squats”
10/18/2018	“deadlifts - 25 reps”	25	“deadlifts”
10/18/2018	“jumping jacks - 30 reps”	30	“jumping jacks”
10/19/2018	“lunges - 40 reps”	40	“lunges”
10/19/2018	“chest flyes - 15 reps”	15	“chest flyes”
…	…	…	…

"""
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

"""
Print out the first five rows of the grade column.
"""
print("The first five rows of the grade column: \n" + str(students.grade.head()))


"""
Each value in grade looks like “9th grade”, “10th grade”, “11th grade”, or “12th grade”.

We want to pare that down to just having the numerical grade. Maybe we want to do linear regression on this data, which would require numerical inputs.

Use regex to extract the number from each string in grade and store those values back into the grade column.
"""
students["grade"] = students["grade"].str.split("(\d+)", expand = True)[1]
print(students)

"""
Print the dtypes of the students table.
"""
print("The dtypes of the students table: \n" + str(students.dtypes))

"""
Convert the grade column to be numerical values instead of objects.
"""
students["grade"] = pd.to_numeric(students["grade"])


"""
Calculate the mean of grade, store it in a variable called avg_grade, and then print it out!

We could not have done this with strings like “9th grade” or “10th grade”.
"""
avg_grade = students.grade.mean()
print("avg_grade: \n" + str(avg_grade))


