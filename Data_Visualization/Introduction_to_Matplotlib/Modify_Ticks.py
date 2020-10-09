import codecademylib
from matplotlib import pyplot as plt

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]


plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

#We will use ax to set the x- and y-ticks and labels to make this graph easier to read.
ax = plt.subplot()

#Using ax, set the x-ticks to be the months list.
ax.set_xticks(months)

#Set the x-tick labels to be the month_names list.
ax.set_xticklabels(month_names)

#Set the y-ticks to be [0.10, 0.25, 0.5, 0.75].
ax.set_yticks([0.10, 0.25, 0.5, 0.75])

#Label the y-ticks to be the percentages that correspond to the values [0.10, 0.25, 0.5, 0.75], instead of decimals.
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

plt.show()