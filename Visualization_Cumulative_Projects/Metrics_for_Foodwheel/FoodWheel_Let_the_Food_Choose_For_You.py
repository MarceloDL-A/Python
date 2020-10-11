"""PROJECT: BOARD SLIDES FOR FOODWHEEL
FoodWheel: Let the Food Choose For You
FoodWheel is a startup delivery service that takes away the struggle of deciding where to eat! FoodWheel picks you an amazing local restaurant and lets you order through the app. Senior leadership is getting ready for a big board meeting, and as the resident Data Analyst, you have been enlisted to help decipher data and create a presentation to answer several key questions:

What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
How has the average order amount changed over time? What does this say about the trajectory of the company?
How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?

Over this project, you will analyze several DataFrames and create several visualizations to help answer these questions.

Time to get started.

What cuisines does FoodWheel offer?
The board wants to make sure that FoodWheel offers a wide, diverse, variety of restaurants. Having many different options makes customers more likely to come back. You've been provided with a CSV, restaurants.csv , which contains all of the restaurants that partner with FoodWheel.

Let's create pie chart showing the different types of cuisines available on FoodWheel."""

#We're going to use pandas and matplotlib for this project. Import both libraries, under their normal names (pd and plt).
import pandas as pd

#Start by loading restaurants.csv into a DataFrame called restaurants.
restaurants = pd.read_csv("restaurants.csv")

#Inspect restaurants using .head()
print(restaurants.head())

#How many different types of cuisine does FoodWheel offer?
#Save this number to the variable cuisine_options_count.
cuisine_options_count = restaurants.cuisine.nunique()
print(str(cuisine_options_count) + " cuisines")

#Let's count the number of restaurants of each cuisine. Use groupby and count. Save your results to cuisine_counts.
cuisine_counts = restaurants.groupby("cuisine").name.count().reset_index()
print(cuisine_counts)




