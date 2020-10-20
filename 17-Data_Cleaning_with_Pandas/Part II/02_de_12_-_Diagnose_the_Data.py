"""
DATA CLEANING WITH PANDAS
Diagnose the Data
We often describe data that is easy to analyze and visualize as “tidy data”. What does it mean to have tidy data?

For data to be tidy, it must have:

Each variable as a separate column
Each row as a separate observation
For example, we would want to reshape a table like:

Account	Checkings	Savings
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

The first step of diagnosing whether or not a dataset is tidy is using pandas functions to explore and probe the dataset.

You’ve seen most of the functions we often use to diagnose a dataset for cleaning. Some of the most useful ones are:

.head() — display the first 5 rows of the table
.info() — display a summary of the table
.describe() — display the summary statistics of the table
.columns — display the column names of the table
.value_counts() — display the distinct values for a column
"""
import codecademylib3_seaborn
import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

"""
We have provided two DataFrames, df1 and df2.

Inspect both of these DataFrames using the functions listed above.

Start by printing the .head() of both df1 and df2.
"""
print(df1.head())
print(df2.head())

"""
Explore the DataFrames using the other functions listed.

Which DataFrame is “clean”, and ready for analysis? Create a variable named clean and set it equal to 1 for df1 and 2 for df2.
"""
print("info: \n" + str(df1.info()))
print("describe: \n" + str(df1.describe()))
print("columns : \n" + str(df1.columns))
clean = 1
clean = 2

