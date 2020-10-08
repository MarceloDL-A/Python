import codecademylib
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#We have provided a set of data representing MatplotSip’s projected revenue per month for the next year in the variable revenue. Let’s plot these revenues against months as a line
#your work here
plt.plot(range(len(revenue)), revenue)

#Make an axis object, store it in the variable ax, and then use it to set the x-ticks to months and the x-axis tick labels to be the months of the year, given to you in the variable month_names.
#Make an axis object by using:
ax = plt.subplot()

#Set x-ticks using:
ax.set_xticks(months)

#Set x-ticklabels using:
ax.set_xticklabels(month_names)

#This data is a projection of future revenue. We don’t know that this will be the revenue, but it’s an estimate based on the patterns of past years. We can say that the real revenue will probably be plus or minus 10% of each value. Create a list containing the lower bound of the expected revenue for each month, and call it y_lower.
#Remember that 10% less than a number would be either: #You can use either of these in your list comprehension.
y_lower = [i - 0.1*i for i in revenue]

#Create a list containing the upper bound of the expected revenue for each month, and call it y_upper.
#Remember that 10% more than a number would be either: #You can use either of these in your list comprehension.
y_upper = [i + 0.1*i for i in revenue]

#Use fill_between to shade the error above and below the line we’ve plotted, with an alpha of 0.2 (alpha is a shade level).
plt.fill_between(months, y_lower, y_upper, alpha = 0.2)

plt.show()