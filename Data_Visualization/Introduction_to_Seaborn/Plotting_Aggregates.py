import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)

#Use Seaborn to plot the average grade for each assignment. Take a look at gradebook.csv for the column names.
sns.barplot(data = gradebook, x = "assignment_name", y = "grade")

#Use plt.show() to display the graph
plt.show()