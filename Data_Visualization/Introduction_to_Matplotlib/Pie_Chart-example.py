import codecademylib
from matplotlib import pyplot as plt
import numpy as np

#If we want to display elements of a data set as proportions of a whole, we can use a pie chart.

#Pie charts are helpful for displaying data like:

##Different ethnicities that make up a school district
##Different macronutrients (carbohydrates, fat, protein) that make up a meal
##Different responses to an online poll
#In Matplotlib, you can make a pie chart with the command plt.pie, passing in the values you want to chart:
budget_data = [500, 1000, 750, 300, 100]
plt.pie(budget_data)
plt.show()

#This looks weird and tilted. When we make pie charts in Matplotlib, we almost always want to set the axes to be equal to fix this issue. To do this, we use plt.axis('equal'), which results in a chart like this:
plt.axis('equal')
plt.show()
