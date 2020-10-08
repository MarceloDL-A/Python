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

#The DataFrame df represents data collected by four health clinics run by the same organization. Each row represents a month from January through June and shows the number of appointments made at four different clinics.
#You want to analyze what's been happening at the North location. #Create a variable called clinic_north that contains ONLY the data from the column clinic_north.
clinic_north = df.clinic_north

#What exactly have you selected?
#After you create the variable, enter the command:
#print(type(clinic_north))
#to see what data type you've created.
#How is this different from what you get if you type the following?
#print(type(df))
print(type(clinic_north))
print(type(df))