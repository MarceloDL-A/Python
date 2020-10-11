"""PROJECT: BOARD SLIDES FOR FOODWHEEL
Customer Types
There is a range of amounts that customers spend on FoodWheel. Let’s investigate and aim to answer our final question:

How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?

A great way to answer this question is to create a histogram of the amount spent by each customer over the past six months.
"""

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

#Start by grouping orders by customer_id and calculating the sum of price spent by each customer. Save your results to customer_amount.
customer_amount = orders.groupby("customer_id").price.sum().reset_index()

#Inspect customer_amount using print and .head().
print(customer_amount.head())

"""Create a histogram of this data.
The range should be from 0 to 200
The number of bins should be 40
Label the x-axis Total Spent
Label the y-axis Number of Customers
Add a title"""
plt.hist(customer_amount.price.values, range = (0, 200), bins = 40)
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Customer Expenditure Over 6 Months")

plt.show()

