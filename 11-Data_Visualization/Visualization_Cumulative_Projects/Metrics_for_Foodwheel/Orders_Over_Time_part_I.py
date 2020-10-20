"""PROJECT: BOARD SLIDES FOR FOODWHEEL
Orders Over Time
FoodWheel is a relatively new startup. They launched in April, and have grown more popular since then. Management suspects that the average order size has increased over time. They'd like you to investigate if this claim is true and answer these questions:

How has the average order amount changed over time?
What does this say about the trajectory of the company?
"""
import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

#Start by loading the data from orders.csv into the DataFrame orders.
orders = pd.read_csv("orders.csv")

#Start by loading the data from orders.csv into the DataFrame orders.
print(orders.head())

#Create a new column in orders called month that contains the month that the order was placed.
orders["month"] = orders.date.apply(lambda x: x.split("-")[0])
print(orders)

#Group orders by month and get the average order price in each month. Save your answer to avg_order.
avg_order = orders.groupby("month").price.mean().reset_index()
print(str(avg_order) + " is de avg price per month")

#We're eventually going to make a bar chart with this information. It would be nice if our bar chart had error bars. Calculate the standard deviation for the average price of orders for each month using std. Save this to std_order.
std_order = orders.groupby("month").price.std().reset_index()
print(str(std_order) + " is the std for avg per mounth")
