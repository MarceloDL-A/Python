import codecademylib
import pandas as pd

#You re working for a Hollywood studio, trying to use data to #predict the next big hit. Load the CSV imdb.csv into a variable #called df, so that you can learn about popular movies from the past 90 years
#load the CSV below:
df = pd.read_csv("imdb.csv")

#Let' s learn about these movies.
#Paste the following code into script.py:
#print(df.head())
#What happens when you press "Run"?
print (df.head())

#What exactly is in this dataset?
#Paste the following code into script.py to learn more about this data:
#print(df.info())
#What happens when you press "Run"?
print (df.info())