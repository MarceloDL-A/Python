import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here
#Create a figure of width 10 and height 8.
plt.figure(figsize = (10, 8))

#Plot the num_hardest_reported list as a pie chart.
plt.pie(num_hardest_reported, labels = unit_topics, autopct = "%1d%%")
#Label the slices with the unit_topics list and put a percentage label on each slice, rounded to the nearest int.

#Set the axes to be 'equal'.
plt.axis("equal")

#Add the title "Hardest Topics".
plt.title("Hardest Topics")

plt.show()

#Save your figure to a file called my_pie_chart.png
plt.savefig("my_pie_chart.png")