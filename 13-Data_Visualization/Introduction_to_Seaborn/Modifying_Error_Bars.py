import codecademylib3_seaborn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

#By default, Seaborn uses something called a bootstrapped confidence interval. Roughly speaking, this interval means that “based on this data, 95% of similar situations would have an outcome within this range”.
#If you’re calculating a mean and would prefer to use standard deviation for your error bars, you can pass in the keyword argument ci="sd" to sns.barplot() which will represent one standard deviation. It would look like this:


sns.barplot(data=gradebook, x="name", y="grade", ci="sd")

#sns.barplot(data=gradebook, x="name", y="grade")
plt.show()