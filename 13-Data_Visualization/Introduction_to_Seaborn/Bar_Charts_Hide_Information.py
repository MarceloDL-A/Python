import codecademylib3_seaborn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#You work as a scientist and are measuring the amounts of plastic in different bodies of water. You’re interested in comparing data collected from different locations.

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

#Was imported four different datasets using NumPy and have combined them into one DataFrame, df.
# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

print(df)

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

#Use sns.barplot() to graph the datasets in one plot, with "label" as the x data and "value" as the y data.
# Add your code below:
sns.barplot(data = df, x = "label", y = "value")


plt.show()



