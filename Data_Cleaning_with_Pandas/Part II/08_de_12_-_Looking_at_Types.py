"""
DATA CLEANING WITH PANDAS
Looking at Types
Each column of a DataFrame can hold items of the same data type or dtype. The dtypes that pandas uses are: float, int, bool, datetime, timedelta, category and object. Often, we want to convert between types so that we can do better analysis. If a numerical category like "num_users" is stored as a Series of objects instead of ints, for example, it makes it more difficult to do something like make a line graph of users over time.

To see the types of each column of a DataFrame, we can use:

print(df.dtypes)
For a DataFrame like this:

item	price	calories
“banana”	“$1”	105
“apple”	“$0.75”	95
“peach”	“$3”	55
“clementine”	“$2.5”	35

the .dtypes attribute would be:

item        object
price       object
calories     int64
dtype: object
We can see that the dtype of the dtypes attribute itself is an object! It is a Series object, which you have already worked with. Series objects compose all DataFrames.

We can see that the price column is made up of objects, which will probably make our analysis of price more difficult. We’ll look at how to convert columns into numeric values in the next few exercises.
"""
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.head())

"""
Let’s inspect the dtypes in the students table.

Print out the .dtypes attribute.
"""
print("students.dtypes: \n" + str(students.dtypes))

"""
If we wanted to make a scatterplot of age vs average exam score, would we be able to do it with this type of data?

Try to print out the mean of the score column of students.
Ans.: Return error
"""
#print(students.score.mean())