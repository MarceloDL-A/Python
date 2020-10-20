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

#You want to see how the number of clinic visits changed between March and April.
#Create the variable march_april, which contains the data from March and April. Do this using two logical statements combined using |, which means “or”.
march_april = df[(df.month == 'March') | (df.month == 'April')]

#Inspect march_april using print.
print (march_april)