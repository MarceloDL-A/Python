"""
DATA CLEANING WITH PANDAS
Splitting by Index
In trying to get clean data, we want to make sure each column represents one type of measurement. Often, multiple measurements are recorded in the same column, and we want to separate these out so that we can do individual analysis on each variable.

Let’s say we have a column “birthday” with data formatted in MMDDYYYY format. In other words, “11011993” represents a birthday of November 1, 1993. We want to split this data into day, month, and year so that we can use these columns as separate features.

In this case, we know the exact structure of these strings. The first two characters will always correspond to the month, the second two to the day, and the rest of the string will always correspond to year. We can easily break the data into three separate columns by splitting the strings using .str:

# Create the 'month' column
df['month'] = df.birthday.str[0:2]

# Create the 'day' column
df['day'] = df.birthday.str[2:4]

# Create the 'year' column
df['year'] = df.birthday.str[4:]
The first command takes the first two characters of each value in the birthday column and puts it into a month column. The second command takes the second two characters of each value in the birthday column and puts it into a day column. The third command takes the rest of each value in the birthday column and puts it into a year column.

This would transform a table like:

id	birthday
1011	“12241989”
1112	“10311966”
1113	“01052011”

into a table like:

id	birthday	month	day	year
1011	“12241989”	“12”	“24”	“1989”
1112	“10311966”	“10”	“31”	“1966”
1113	“01052011”	“01”	“05”	“2011”

We will practice changing string columns into numerical columns (like converting "10" to 10) in a future exercise.
"""
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

"""
Print out the columns of the students DataFrame.
"""
print("students.columns: \n" + str(students.columns))

"""
The column gender_age sounds like it contains both gender and age!

Print out the .head() of the column to see what kind of data it contains.
"""
print("students.gender_age.head(): \n" + str(students.gender_age.head()))

"""
It looks like the first character of the values in gender_age contains the gender, while the rest of the string contains the age. Let’s separate out the gender data into a new column called gender.
"""
students["gender"] = students.gender_age.str[0]
print("students.columns: \n" + str(students))

"""
Now, separate out the age data into a new column called age.
"""
students["age"] = students.gender_age.str[1:3]
print("students.columns: \n" + str(students))

"""
Good job! Let’s print the .head() of students to see how the DataFrame looks after our creation of new columns.
"""
print("students.columns: \n" + str(students.head()))

"""
Now, we don’t need that gender_age column anymore.

Let’s set the students DataFrame to be the students DataFrame with all columns except gender_age.
"""
print("students.columns: \n" + str(students.columns))
print("students.columns: \n" + str(students[['full_name',  'grade', 'exam', 'score', 'gender', 'age']]))




