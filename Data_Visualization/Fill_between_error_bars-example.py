import codecademylib
from matplotlib import pyplot as plt

#Fill Between
#We’ve learned how to display errors on bar charts using error bars. Let’s take a look at how we might do this in an aesthetically pleasing way on line graphs. In Matplotlib, we can use plt.fill_between to shade error. This function takes three arguments:

#x-values — this works just like the x-values of plt.plot
#lower-bound for y-values — sets the bottom of the shared area
#upper-bound for y-values — sets the top of the shared area
#Generally, we use fill_between to create a shaded error region, and then plot the actual line over it. We can set the alpha keyword to a value between 0 and 1 in the fill_between call for

x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]

plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
plt.plot(x_values, y_values) #this is the line itself
plt.show()






#********************************************************
#********************************************************

#Having to calculate y_lower and y_upper by hand is time-consuming. If we try to just subtract 2 from y_values, we will get an error.

#TypeError: unsupported operand type(s) for -: 'list' and 'int'
#In order to correctly add or subtract from a list, we need to use list comprehension:

#y_lower = [i - 2 for i in y_values]
#This command looks at each element in y_values and calls the element its currently looking at i. For each new i, it subtracts 2. These opperations create a new list called y_lower.

#If we wanted to add 2 to each element in y_values, we use this code:

#y_upper = [i + 2 for i in y_values]



