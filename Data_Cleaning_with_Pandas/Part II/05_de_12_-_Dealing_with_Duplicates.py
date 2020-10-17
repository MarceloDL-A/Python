"""
DATA CLEANING WITH PANDAS
Dealing with Duplicates
Often we see duplicated rows of data in the DataFrames we are working with. This could happen due to errors in data collection or in saving and loading the data.

To check for duplicates, we can use the pandas function .duplicated(), which will return a Series telling us which rows are duplicate rows.

Let’s say we have a DataFrame fruits that represents this table:

item	price	calories
“banana”	“$1”	105
“apple”	“$0.75”	95
“apple”	“$0.75”	95
“peach”	“$3”	55
“peach”	“$4”	55
“clementine”	“$2.5”	35

If we call fruits.duplicated(), we would get the following table:

id	value
0	False
1	False
2	True
3	False
4	False
5	False

We can see that row 2, which represents an "apple" with price "$0.75" and 95 calories, is a duplicate row. Every value in this row is the same as in another row.

We can use the pandas .drop_duplicates() function to remove all rows that are duplicates of another row.

If we call fruits.drop_duplicates(), we would get the table:

item	price	calories
“banana”	“$1”	105
“apple”	“$0.75”	95
“peach”	“$3”	55
“peach”	“$4”	55
“clementine”	“$2.5”	35

The "apple" row was deleted because it was exactly the same as another row. But the two "peach" rows remain because there is a difference in the price column.

If we wanted to remove every row with a duplicate value in the item column, we could specify a subset:

fruits = fruits.drop_duplicates(subset=['item'])
By default, this keeps the first occurrence of the duplicate:

item	price	calories
“banana”	“$1”	105
“apple”	“$0.75”	95
“peach”	“$3”	55
“clementine”	“$2.5”	35

Make sure that the columns you drop duplicates from are specifically the ones where duplicates don’t belong. You wouldn’t want to drop duplicates with the price column as a subset, for example, because it’s okay if multiple items cost the same amount!
"""
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

"""
It seems like in the data collection process, some rows may have been recorded twice. Use the .duplicated() function on the students DataFrame to make a Series object called duplicates.
"""
duplicates = students.duplicated()

"""
Print out the .value_counts() of the duplicates Series to see how many rows are exact duplicates.
"""
print("duplicates: \n" + str(duplicates))

"""
Update the value of students to be the students table with the duplicates dropped.
"""
students = students.drop_duplicates()
print("students: \n" + str(students))


"""
.
Use the .duplicated() function again to make a Series object called duplicates after dropping the duplicates. Print out the value counts again. Are there any Trues left? 
Ans.: No
"""
#print("students.duplicated().value_counts(): \n" + str(students.duplicated().value_counts()))
duplicates = students.duplicated()
print("duplicates after: \n" + str(duplicates))





