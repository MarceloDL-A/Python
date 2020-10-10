import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")

#Use sns.barplot() to create a chart with:
#data equal to df
#x equal to Age Range
#y equal to Response
#hue equal to Gender
#sns.barplot(data = df, x = "Age Range", y = "Response", hue = "Gender")

#How is this plot different from when hue is "Age Range" and x is "Gender"?
#Why might we use one and not the other?
sns.barplot(data = df, x = "Gender", y = "Response", hue = "Age Range")

#Use plt.show() to display the graph.
plt.show()