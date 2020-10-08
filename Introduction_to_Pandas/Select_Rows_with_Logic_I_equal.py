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
           'clinic_west'])

#You’re going to staff the clinic for January of this year. You want to know how many visits took place in January of last year, to help you prepare.
#Create variable january using a logical statement that selects the row of df where the 'month' column is 'January'.
january = df[df.month == 'January']

#Inspect january using print.
print(january)