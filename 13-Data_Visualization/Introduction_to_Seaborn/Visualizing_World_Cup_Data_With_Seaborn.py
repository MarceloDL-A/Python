#Import the modules that you’ll be using in this project:
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#Inspect the raw CSV files that you will be using in this project by selecting them in the file navigator.

#Inspect the raw CSV files that you will be using in this project by selecting them(folders) in the file navigator

#Load WorldCupMatches.csv into a DataFrame called df. This will allow you to eventually plot the DataFrame with Seaborn.
df = pd.read_csv("WorldCupMatches.csv")

#It is usually a good idea to check any new DataFrame to make sure the results are as expected.
#Inspect the DataFrame using .head(). Make sure to use print() to wrap any output you want to inspect.
print(df.head())

#The data in WorldCupMatches.csv has the goals scored in each match broken up by goals for the home team and goals for the away team. We want to visualize the total number of goals scored in each match.
#Create a new column in df named Total Goals, and set it equal to the sum of the columns Home Team Goals and Away Team Goals.
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]

#Print the results of df.head() to confirm your new column.
print(df.head())

#You are going to create a bar chart visualizing how many goals were scored each year the World Cup was held between 1930-2014.
#Set the style of your plot to be whitegrid . This will add gridlines to the plot which will make it easier to read the visualization.
sns.set_style("whitegrid")

#To make the text in your visualization bigger and easier to read, set the context to be "poster".
#If you would like to further adjust the font size of your plot, you can pass sns.set_context() a second optional argument using the keyword font_scale.
sns.set_context("poster", font_scale = 0.8)

#Create a figure and axes for your plot using the syntax:
f, ax = plt.subplots(figsize = (12, 7))
#Inside of plt.subplots(), set the size of the figure to be 12 inches wide and 7 inches tall.

#Using the data in df and the syntax:
ax = sns.barplot(x = df["Year"], y = df["Total Goals"])
#visualize the columns Year and Total Goals as a bar chart.
#Year should be on the x-axis, and Total Goals should be on the y-axis.

#Effective visualizations include a clear title.
#Give your bar chart a meaningful title using ax.set_title().
ax.set_title("Avg goals per year in World Cup")

#Render your bar chart so you can see it.
plt.show()

#***********************************
#***********************************
#Now you are going to create a box plot so you can visualize the distribution of the goals data instead of just the average with a bar chart.
#Load goals.csv into a DataFrame called df_goals, and take a quick look at the DataFrame using .head().
df_goals = pd.read_csv("goals.csv")
print(df_goals.head())

#Experimenting with different contexts and font scales can help you decide on the best context and font scale for the particular visualization.
#Try setting the context of the plot to be notebook and the font_scale to be 1.25.
sns.set_context("notebook", font_scale = 1.25)

#Create a figure for your second plot.
#Set the variables f, ax2 and instantiate a figure that is 12 inches wide and 7 inches tall.
f, ax2 = plt.subplots(figsize = (12, 7))

#Set ax2 equal to a box plot with the color palette Spectral that visualizes the data in the DataFrame df_goals with the column year on the x-axis and goals on the y-axis.
ax2 = sns.boxplot(x = "year", y = "goals", data = df_goals, palette = "Spectral")

#Give your box plot a meaningful and clear title.
ax2.set_title("Goals Visualization")

#Render your box plot so you can see it.
plt.show()

#Congrats you’re done! Feel free to continue iterating on your plots in this workspace.
#You can also explore more datasets at the Kaggle website.



