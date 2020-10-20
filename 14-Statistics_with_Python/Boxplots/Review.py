"""
BOXPLOTS
Review
Great work! Here are some of the major takeaways from boxplots:

The box of a boxplot visualizes the median, first quartile, and third quartile of a dataset.
The length of the box in a boxplot visualizes the interquartile range.
The whiskers extend from the box 1.5 times the size of the interquartile range.
Outliers are points that fall outside of the whiskers. They’re represented by dots.
Boxplots are especially useful for comparing the spread of multiple datasets.
"""
import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)


a = np.random.normal(1, 1, 1000)
b = np.random.normal(0, 3, 1000)
c = np.random.normal(2, 1.5, 1000)
d = np.random.normal(-4, 5, 1000)
e = np.random.normal(5, 2, 1000)
plt.boxplot([a,b,c,d,e])
plt.show()
plt.subplot(511)
plt.hist(a)
plt.xlim([-20,20])
plt.subplot(512)
plt.hist(b)
plt.xlim([-20,20])
plt.subplot(513)
plt.hist(c)
plt.xlim([-20,20])
plt.subplot(514)
plt.hist(d)
plt.xlim([-20,20])
plt.subplot(515)
plt.hist(e)
plt.xlim([-20,20])
plt.tight_layout()
plt.show()

"""
On this page, we’ve imported five different test datasets. We’ve drawn both the boxplot and the histogram for each dataset (you might need to scroll down to see all of the histograms). What are some of the advantages and disadvantages of each type of graph? Think about your ability to articulate your understanding of things like:

The spread of the data
The central tendency of the data
Your ability to compare different datasets
The number of data points in each dataset

"""
