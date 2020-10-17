"""
DATA CLEANING WITH PANDAS
Splitting by Character
Let’s say we have a column called “type” with data entries in the format "admin_US" or "user_Kenya". Just like we saw before, this column actually contains two types of data. One seems to be the user type (with values like “admin” or “user”) and one seems to be the country this user is in (with values like “US” or “Kenya”).

We can no longer just split along the first 4 characters because admin and user are of different lengths. Instead, we know that we want to split along the "_". Using that, we can split this column into two separate, cleaner columns:

# Create the 'str_split' column
df['str_split'] = df.type.str.split('_')

# Create the 'usertype' column
df['usertype'] = df.str_split.str.get(0)

# Create the 'country' column
df['country'] = df.str_split.str.get(1)
This would transform a table like:

id	type
1011	“user_Kenya”
1112	“admin_US”
1113	“moderator_UK”

into a table like:
"""
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

"""
The students’ names are stored in a column called full_name.

We want to separate this data out into two new columns, first_name and last_name.

First, let’s create a Series object called name_split that splits the full_name by the " " character.
"""
students["name_split"] = students.full_name.str.split(" ")
print("name_split: \n" + str(students))

"""
Now, let’s create a column called first_name that takes the first item in name_split.
"""
students["first_name"] = students.name_split.str.get(0)
print("name_split: \n" + str(students))

"""
Finally, let’s create a column called last_name that takes the second item in name_split.
"""
students["last_name"] = students.name_split.str.get(1)
print("name_split: \n" + str(students))

"""
Print out the .head() of students to see how the DataFrame has changed.
"""
print("students.head(): \n" + str(students.head()))




