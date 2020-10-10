import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#Use Pandas to load in the data from results.csv and save it to the variable df.
# Load results.csv here:
df = pd.read_csv("results.csv")

#Display df using print
print(df)

#using the Seaborn sns.barplot
sns.barplot(data= df, x = "Gender" , y = "Mean Satisfaction")

#Type plt.show() to display the completed bar plot.
plt.show()