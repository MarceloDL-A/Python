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

#Now, you want to compare visits to the Northern and Southern clinics.
#Create a variable called clinic_north_south that contains ONLY the data from the columns clinic_north and clinic_south.
clinic_north_south = df[['clinic_north', 'clinic_south']]

#When we select multiple columns, do we get a Series or a DataFrame? Ans: DataFrame
#After you’ve created the variable, enter the command:
#print(type(clinic_north_south))
#to see what data type you’ve created.
print(type(clinic_north_south))
