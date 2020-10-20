import codecademylib
from matplotlib import pyplot as plt

#Define three lists, x, y1, and y2 and fill them with integers. These numbers can be anything you want, but it would be neat to have them be actual metrics that you want to compare. This (http://www.tylervigen.com/spurious-correlations) is a fun site you can look at to find example datasets to plot!
x = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 11, 11, 25, 26]
y1 = [2, 4, 5, 6, 7, 8, 9, 9, 0, 4, 4, 3, 3, 3, 0, 2]
y2 = [4, 4, 5, 6, 6, 3, 5, 6, 1, 1, 3, 5, 7, 6, 4, 3]

#Plot y1 vs x com plt.plot(x, y1)
#Make the y1 line a pink line. Give line round markers.
plt.plot(x, y1, color="pink", marker='o')

#On the same graph, plot y2 vs x (after the line where you plot y1 vs x)
#plt.plot(x, y2)
#Make the y1 line a gray line. Give line round markers.
plt.plot(x, y2, color="gray", marker='o')

#Give your graph a title of “Two Lines on One Graph”, and label the x-axis ”Amazing X-axis” and y-axis ”Incredible Y-axis”.
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

#Give the graph a legend and put it in the lower right.
#To set a legend to be at the lower right of the graph, add loc=4 to the plt.legend call.
plt.legend(["Pink curve", "Gray curve"], loc = 4)

#display all plot to the scripts untill here.
plt.show()










