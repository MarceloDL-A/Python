"""
DATA CLEANING WITH PANDAS
Reshaping your Data
Since we want

Each variable as a separate column
Each row as a separate observation
We would want to reshape a table like:

Account	Checking	Savings
“12456543”	8500	8900
“12283942”	6410	8020
“12839485”	78000	92000

Into a table that looks more like:
Account	Account Type	Amount
“12456543”	“Checking”	8500
“12456543”	“Savings”	8900
“12283942”	“Checking”	6410
“12283942”	“Savings”	8020
“12839485”	“Checking”	78000
“12839485”	“Savings”	920000

We can use pd.melt() to do this transformation. .melt() takes in a DataFrame, and the columns to unpack:

pd.melt(frame=df, id_vars='name', value_vars=['Checking','Savings'], value_name="Amount", var_name="Account Type")
The parameters you provide are:

frame: the DataFrame you want to melt
id_vars: the column(s) of the old DataFrame to preserve
value_vars: the column(s) of the old DataFrame that you want to turn into variables
value_name: what to call the column of the new DataFrame that stores the values
var_name: what to call the column of the new DataFrame that stores the variables
The default names may work in certain situations, but it’s best to always have data that is self-explanatory. Thus, we often use .columns() to rename the columns after melting:

df.columns(["Account", "Account Type", "Amount"])
"""
import codecademylib3_seaborn
import pandas as pd
from students import students

"""
Print out the columns of students.
"""
print("students: \n" + str(students.columns))

"""
There is a column for the scores on the fractions exam, and a column for the scores on the probabilities exam.

We want to make each row an observation, so we want to transform this table to look like:

full_name	exam	score	gender_age	grade
“First Student”	“Fractions”	score%	…	…
“First Student”	“Probabilities”	score%	…	…
“Second Student”	“Fractions”	score%	…	…
“Second Student”	“Probabilities”	score%	…	…
…	…	…		
Use pd.melt() to create a new table (still called students) that follows this structure.
Hint:
The id_vars, the columns that should stay the same in the new DataFrame, are full_name, gender_age, and grade.

We want to turn fractions and probability into variables, so those are the value_vars.

We want to call that new column exam, so that’s our var_name.

The values previously held in fractions and probability, we want to store in a column called score, so that’s the value_name.
"""

students = pd.melt(frame = students, id_vars = ["full_name", "gender_age", "grade"], value_vars = ["fractions", "probability"], var_name = "exam", value_name = "score")

"""
Print the .head() and the .columns of students.

Also, print out the .value_counts() of the column exam.
"""

print("students.head(): \n" + str(students.head()))
print("students.columns: \n" + str(students.columns))
print("students.exam.value_counts(): \n" + str(students.exam.value_counts()))





