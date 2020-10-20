import codecademylib
import pandas as pd

#You’re working for the County of Whoville and you just received a CSV of data about the different cities in your county. Read the CSV 'sample.csv' into a variable called df, so that you can learn more about the cities.
df = pd.read_csv("sample.csv")

#Let’s inspect the CSV.
#Type print(df) on the next line and then run your code. What sort of data were you sent?
print (df)