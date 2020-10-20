import codecademylib
import pandas as pd

#You’re running a chain of pita shops called Pita Power. You want to create a DataFrame with information on your different store locations.
#Use a list of lists to create a DataFrame with the following data:
#We have filled in the information for the first two rows in df2.
#Add the code to create the 3rd and 4th rows, and the column names.
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
    #add column names here
  columns=['Store ID', 'Location', 'Number of Employees'

  ])

print(df2)