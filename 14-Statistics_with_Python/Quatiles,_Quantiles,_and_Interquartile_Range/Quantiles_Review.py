"""
Quantiles Review
Nice work! Here are some of the major takeaways about quantiles:

Quantiles are values that split a dataset into groups of equal size.
If you have n quantiles, the dataset will be split into n+1 groups of equal size.
The median is a quantile. It is the only 2-quantile. Half the data falls below the median and half falls above the median.
Quartiles and percentiles are other common quantiles. Quartiles split the data into 4 groups while percentiles split the data into 100 groups.
"""
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from data import school_one, school_two, school_three

deciles_one = np.quantile(school_one, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
deciles_two = np.quantile(school_two, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
deciles_three = np.quantile(school_three, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

plt.subplot(311)
plt.hist(school_one)
for decile in deciles_one:
  plt.axvline(x=decile, c = 'r')
plt.title("School One")
plt.xlabel("SAT Score")
  
plt.subplot(312)
plt.hist(school_two)
for decile in deciles_two:
  plt.axvline(x=decile, c = 'r')
plt.title("School Two")
plt.xlabel("SAT Score")
  
plt.subplot(313)
plt.hist(school_three)
for decile in deciles_three:
  plt.axvline(x=decile, c = 'r')
plt.title("School Three")
plt.xlabel("SAT Score")
plt.tight_layout()
plt.show()

"""
To the right, we’ve shown three different histograms along with the deciles. Each histogram shows the SAT scores of the students that a fake university has accepted.

If you had an SAT score of 1350, which tenth of the data would you be in for each school? Which schools should you apply to? Would any of the schools be unrealistic options?
"""