import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

#For someone who is learning about the different drink types at MatplotSip, a bar chart of milk amounts in each drink may be useful. We have provided the ounces_of_milk list, which contains the amount of milk in each 12oz drink in the drinks list. Plot this information as a bar chart.
# Plot the bar graph here #ncluded a list error #Add caps of size 5 to your error bars
plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr = error, capsize = 5)

plt.show()