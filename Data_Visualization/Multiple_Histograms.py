import codecademylib
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

#Was provided another dataset in the file sales_times_s2.csv that represents the 371 sales at MatplotSip’s first location from 8am to 10pm on the same day. This data has the same structure as the sales times data from store 1, with an id, a card_no, and a time. Take a look at the data in the csv and familiarize yourself with it.

#Using script.py, was imported the times into a list called sales_times2. You can see how we did this in script.py, but you’ll only be interacting with the lists sales_times1 and sales_times2 in histogram.py, so don’t worry if you don’t understand the conversion from csv to list.
plt.hist(sales_times1, bins=20, alpha = 0.4, normed = True)

#Plot the histogram of times from the second location on top of the one from the last exercise.
#plot your other histogram here
plt.hist(sales_times2, bins=20, alpha = 0.4, normed = True)

#Notice that the histogram we plotted second completely obscures the first histogram we plotted. Modify the transparency value of both histograms to be 0.4 so that we can see the separate histograms better.

#Normalize both the histograms so that we can compare the patterns between them despite the differences in sample size.

plt.show()