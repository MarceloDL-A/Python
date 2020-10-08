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

#One of your doctors thinks that there are more clinic visits in the late Spring.
#Write a command that will produce a DataFrame made up of the data for April, May, and June from df for all four sites (rows 3 through 6), and save it to april_may_june.
april_may_june = df.iloc[3:6]

#Inspect april_may_june using print.
print (april_may_june)