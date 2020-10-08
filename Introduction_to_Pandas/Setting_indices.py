import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

#Examine the code in the workspace. Note that df2 is a subset of rows from df.
#Type the following and press “Run”:
#print(df2)
#Note that the indices on df2 are not consecutive.
df2 = df.loc[[1, 3, 5]]

#Create a new DataFrame called df3 by resetting the indices on df2 (don’t use inplace or drop). Did df2 change after you ran this command?
df3 = df2.reset_index()

print(df3)

#Reset the indices of df2 by using the keyword inplace=True and drop=True. Did the indices of df2 change? How is df2 different from df3?
df2.reset_index(inplace = True, drop = True)

print(df2)