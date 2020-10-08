import codecademylib
from matplotlib import pyplot as plt
from script import sales_times

#For example, if we wanted to take our data from the last example and make a new histogram that just displayed the values from 66 to 69, divided into 40 bins (instead of 10), we could use this function call:
#plt.hist(dataset, range=(66,69), bins=40)

#We’ve provided data in the file sales_times.csv and loaded it into a list called sales_times. You can see how we did this in the script.py file. This set represents the 270 sales at MatplotSip’s first location from 8am to 10pm on a certain day.

#Make a histogram out of this data in histogram.py using the plt.hist function.
#create the histogram here form sales_times.csv that was imported #Use the bins keyword to create 20 bins instead of the default 10.
plt.hist(sales_times, bins = 20)

plt.show()