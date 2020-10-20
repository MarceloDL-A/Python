"""
HOW TO CLEAN DATA WITH PYTHON
Cleaning US Census Data
You just got hired as a Data Analyst at the Census Bureau, which collects census data and creates interesting visualizations and insights from it.

The person who had your job before you left you all the data they had for the most recent census. It is in multiple csv files. They didn’t use pandas, they would just look through these csv files manually whenever they wanted to find something. Sometimes they would copy and paste certain numbers into Excel to make charts.

The thought of it makes you shiver. This is not scalable or repeatable.

Your boss wants you to make some scatterplots and histograms by the end of the day. Can you get this data into pandas and into reasonable shape so that you can make these histograms?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob


"""
The first visualization your boss wants you to make is a scatterplot that shows average income in a state vs proportion of women in that state.

Open some of the census csv files in the navigator. How are they named? What kind of information do they hold? Will they help us make this graph?
"""


"""
It will be easier to inspect this data once we have it in a DataFrame. You can’t even call .head() on these csvs! How are you supposed to read them?

Using glob, loop through the census files available and load them into DataFrames. Then, concatenate all of those DataFrames together into one DataFrame, called something like us_census.

hint:
With glob, we can take all of the files with the same naming structure and combine them:

import glob

files = glob.glob("file*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
Pandas can concatenate this list of DataFrames together:

df = pd.concat(df_list)
"""
files = glob.glob("states*.csv")
df_list = []
for i in files:
  df_temp = pd.read_csv(i)
  df_list.append(df_temp)
us_census = pd.concat(df_list)
print("us_census: \n" + str(us_census))

"""
Look at the .columns and the .dtypes of the us_census DataFrame. Are those datatypes going to hinder you as you try to make histograms?
"""
print("us_census.columns: \n" + str(us_census.columns))
print("us_census.dtypes: \n" + str(us_census.dtypes))
print("us_census.dtypes: \n" + str(us_census.dtypes))


"""
Look at the .head() of the DataFrame so that you can understand why some of these dtypes are objects instead of integers or floats.

Start to make a plan for how to convert these columns into the right types for manipulation.
"""
print("us_census.head(): \n" + str(us_census.head()))


"""
Regex to the Rescue
Use regex to turn the Income column into a format that is ready for conversion into a numerical type.
"""
us_census["Income"] = us_census["Income"].str.split("(\d+.\d+)", expand = True)[1]
print("us_census[\"Income\"] " + str(us_census["Income"] ))
us_census["Income"] = pd.to_numeric(us_census["Income"])
print("us_census[\"Income\"].to_numeric " + str(us_census["Income"] ))



"""
Look at the GenderPop column. We are going to want to separate this into two columns, the Men column, and the Women column.

Split the column into those two new columns using str.split and separating out those results.
"""
"""
Convert both of the columns into numerical datatypes.

There is still an M or an F character in each entry! We should remove those before we convert.
"""
split_us_census = us_census["GenderPop"].str.split(("_"), expand = True)
print("split_us_census: \n" + str(split_us_census))
us_census["Men"] = split_us_census.get(0).str.split(("M"), expand = True).get(0)
us_census["Men"] = pd.to_numeric(us_census["Men"],downcast='float')

us_census["Women"] = split_us_census.get(1).str.split(("F"), expand = True).get(0)
us_census["Women"] = pd.to_numeric(us_census["Women"])

print("us_census type: \n" + str(us_census.dtypes))
print("us_census: \n" + str(us_census))



"""
Now you should have the columns you need to make the graph and make sure your boss does not slam a ruler angrily on your desk because you’ve wasted your whole day cleaning your data with no results to show!

Use matplotlib to make a scatterplot!

plt.scatter(the_women_column, the_income_column) 
Remember to call plt.show() to see the graph!
"""
plt.scatter(us_census["Women"], us_census["Income"])
plt.show()




"""

Did you get an error? These monstrous csv files probably have nan values in them! Print out your column with the number of women per state to see.

We can fill in those nans by using pandas’ .fillna() function.

You have the TotalPop per state, and you have the Men per state. As an estimate for the nan values in the Women column, you could use the TotalPop of that state minus the Men for that state.

Print out the Women column after filling the nan values to see if it worked!
"""
print("us_census[\"Women\"]: \n" + str(us_census["Women"]))
us_census = us_census.fillna(value = {"Women": us_census["TotalPop"] - us_census["Men"]})
print("us_census[\"Women\"]: \n" + str(us_census["Women"]))





"""
We forgot to check for duplicates! Use .duplicated() on your census DataFrame to see if we have duplicate rows in there.
"""
print("us_census.duplicated(): \n" + str(us_census.duplicated()))




"""
Drop those duplicates using the .drop_duplicates() function.
"""
print("us_census.drop_duplicates(): \n" + str(us_census.drop_duplicates()))




"""
Make the scatterplot again. Now, it should be perfect! Your job is secure, for now.
"""
plt.clf()
plt.scatter(us_census["Women"], us_census["Income"])
plt.show()




"""
Histograms of Races
Now, your boss wants you to make a bunch of histograms out of the race data that you have. Look at the .columns again to see what the race categories are.
"""
print("us_census.columns: \n" + str(us_census.columns))

"""
Try to make a histogram for each one!

You will have to get the columns into numerical format, and those percentage signs will have to go.

Don’t forget to fill the nan values with something that makes sense! You probably dropped the duplicate rows when making your last graph, but it couldn’t hurt to check for duplicates again.
"""


"""

Phew. You’ve definitely impressed your boss on your first day of work.

But is there a way you really convey the power of pandas and Python over the drudgery of csv and Excel?

Try to make some more interesting graphs to show your boss, and the world! You may need to clean the data even more to do it, or the cleaning you have already done may give you the ease of manipulation you’ve been searching for.
"""

