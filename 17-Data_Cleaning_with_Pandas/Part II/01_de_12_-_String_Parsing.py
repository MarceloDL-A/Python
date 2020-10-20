"""
DATA CLEANING WITH PANDAS
String Parsing
Sometimes we need to modify strings in our DataFrames to help us transform them into more meaningful metrics. For example, in our fruits table from before:

item	price	calories
“banana”	“$1”	105
“apple”	“$0.75”	95
“peach”	“$3”	55
“peach”	“$4”	55
“clementine”	“$2.5”	35

We can see that the 'price' column is actually composed of strings representing dollar amounts. This column could be much better represented in floats, so that we could take the mean, calculate other aggregate statistics, or compare different fruits to one another in terms of price.

First, we can use what we know of regex to get rid of all of the dollar signs:

fruit.price = fruit['price'].replace('[\$,]', '', regex=True)
Then, we can use the pandas function .to_numeric() to convert strings containing numerical values to integers or floats:

fruit.price = pd.to_numeric(fruit.price)
Now, we have a DataFrame that looks like:

item	price	calories
“banana”	1	105
“apple”	0.75	95
“peach”	3	55
“peach”	4	55
“clementine”	2.5	35

"""
import codecademylib3_seaborn
import pandas as pd
from students import students

"""
We saw in the last exercise that finding the mean of the score column is hard to do when the data is stored as Objects and not numbers.

Use regex to take out the % signs in the score column.
"""
print(students)
students.score = students["score"].replace("[\%,]", "", regex = True)
print(students)

"""
Convert the score column to a numerical type using the pd.to_numeric() function.
"""
students.score = pd.to_numeric(students.score)
print(students)

