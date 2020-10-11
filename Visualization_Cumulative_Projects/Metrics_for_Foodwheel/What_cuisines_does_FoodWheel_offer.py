"""
PROJECT: BOARD SLIDES FOR FOODWHEEL
What cuisines does FoodWheel offer?
You’ve generated the following table that counts the number of different restaurants for each cuisine that partner with FoodWheel.

cuisine	name
0	American	10
1	Chinese	11
2	Italian	8
3	Japanese	4
4	Korean	3
5	Pizza	4
6	Vegetarian	4
"""
import codecademylib3
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

"""Start by creating two variables:
cuisines contains the values of the column cuisine from cuisine_counts.
counts contains the number of restaurants of each cuisine from cuisine_counts."""
cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values

"""Let’s use this the values from counts to create a pie chart. Make sure that your pie chart includes:
Labels for each cuisine (i.e, “American”, “Chinese”, etc.) from cuisines
Percent labels using autopct
A title
Use plt.axis to make the pie chart a perfect circle
plt.show() to display your chart"""
plt.pie(counts, labels = cuisines, autopct = "%d%%")
plt.title("FoodWhell")
plt.axis("equal")
plt.show()


