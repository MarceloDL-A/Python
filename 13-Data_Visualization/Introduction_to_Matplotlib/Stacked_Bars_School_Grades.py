import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

#The Bs bars will go on top of the As bars, but at what heights will the Cs, Ds, and Fs bars start?
#The bottom of the bars representing the Cs will be at the height of the As plus the Bs. We can do this in NumPy (a scientific computing package for Python) with the np.add function. c_bottom, the starting heights for the Cs, will be:
#c_bottom = np.add(As, Bs)
#Underneath the definition of c_bottom, define d_bottom (where the Cs end), and f_bottom (where the Ds end).
c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

#create your plot here
#Create a figure of width 10 and height 8.
plt.figure(figsize = (10, 8))

#Plot the As, Bs, Cs, Ds, and Fs. Give each one the appropriate bottom list that will stack them on top of each other.
plt.subplot()
plt.bar(x, As)
plt.bar(x, Bs, bottom = As)
plt.bar(x, Cs, bottom = c_bottom)
plt.bar(x, Ds, bottom = d_bottom)
plt.bar(x, Fs, bottom = f_bottom)

#Create a set of axes and save them to ax.
ax = plt.subplot()

#Set the x-ticks to be range(len(unit_topics)).
ax.set_xticks(range(len(unit_topics)))

#Set the x-tick labels to be the unit_topics.
ax.set_xticklabels(unit_topics)

#Give the plot the title you see in the final graph, and the same x-axis label and y-axis label.
plt.title("Grade distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")

#Save your figure to a file called my_stacked_bar.png.
plt.savefig("my_stacked_bar.png")

plt.show()