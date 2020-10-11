"""PROJECT: BOARD SLIDES FOR FOODWHEEL
Orders Over Time
You’ve now created two new DataFrames from the orders DataFrame, avg_order, which gives the average amount spent on an order for each month and std_order, which gives the standard deviation for each month. Now it’s time to create a bar chart that uses both of these DataFrames.
"""
import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()


#Start by creating a set of axes using plt.subplot and saving them to the variable ax.
ax = plt.subplot()

#Create a variable with the average prices in it by selecting the column price from avg_order. Save this to bar_heights.
print(avg_order)
bar_heights = avg_order.price

#Create a variable with the standard deviation of prices in it by selecting the column price from std_order. Save this to bar_errors.
bar_errors = std_order.price

"""Create a bar chart to share this data.
Create an axes object called ax using plt.subplot.
The height of each bar should come from bar_heights
Use the standard deviations in bar_errors as the yerr
The error capsize should be 5
Make sure that you label each bar with the name of the month (i.e., 4 = April).
Also be sure to label the y-axis
Give your plot a descriptive title"""
ax = plt.subplot()
plt.bar(range(len(bar_heights)), bar_heights, yerr = bar_errors, capsize = 5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel("Average Order Amount")
plt.title("Order Amount over Time")


plt.show()


