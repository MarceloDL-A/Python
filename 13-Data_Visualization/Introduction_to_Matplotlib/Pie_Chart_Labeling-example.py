import codecademylib
from matplotlib import pyplot as plt

#Pie Chart Labeling
#We also want to be able to understand what each slice of the pie represents. #To do this, we can either:
#use a legend to label each color, or
#put labels on the chart itself.
#Method 1
budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
#plt.pie(budget_data)
plt.legend(budget_categories)
#axes to be equal
plt.axis('equal')
#This puts the category names into a legend on the chart:

#Method 2
#option 2
plt.pie(budget_data, labels=budget_categories)
#This puts the category names into labels next to each corresponding slice

#One other useful labeling tool for pie charts is adding the percentage of the total that each slice occupies. Matplotlib can add this automatically with the keyword autopct. We pass in string formatting instructions to format the labels how we want. Some common formats are:
#'%0.2f' — 2 decimal places, like 4.08
#'%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. You need two consecutive percent signs because the first one acts as an escape character, so that the second one gets displayed on the chart.
#'%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.
#So, a full call to plt.pie might look like:
plt.pie(budget_data,
        labels=budget_categories,
        autopct='%0.1f%%')

plt.show()