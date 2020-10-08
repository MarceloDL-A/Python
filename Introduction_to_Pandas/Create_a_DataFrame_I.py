import codecademylib
import pandas as pd

#You run an online clothing store called Panda’s Wardrobe. You need a DataFrame containing information about your products.
#Create a DataFrame with the following data that your inventory manager sent you:
#We have already filled in the information for Product ID in df1.
#Add the code to create the columns Product Name and Color and their associated data.

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)