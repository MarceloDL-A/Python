import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()

#Set the x-axis ticks to be the numbers from 0 to the length of drinks.
ax.set_xticks(range(6))

#Use the strings in the drinks list for the x-axis ticks of the plot you made with plt.bar.
ax.set_xticklabels(drinks)
plt.show()