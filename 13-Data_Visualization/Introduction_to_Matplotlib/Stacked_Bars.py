import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#You just made a chart with two sets of sales data plotted side by side. Let’s instead make a stacked bar chart by using the keyword bottom. Put the sales1 bars on the bottom and set the sales2 bars to start where the sales1 bars end.
plt.bar(range(len(sales1)), sales1)
plt.bar(range(len(sales2)), sales2, bottom = sales1)

#We should add a legend to make sure we know which set of bars corresponds to which location. Label the bottom set of bars as “Location 1” and the top set of bars as “Location 2” and add a legend to the chart.
plt.legend(["Location 1", "Location 2"])

plt.show()