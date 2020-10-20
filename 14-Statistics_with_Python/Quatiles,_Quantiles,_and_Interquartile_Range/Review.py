"""
Review
Nice work! You can now calculate the Interquartile Range of a dataset by using the SciPy library. The main takeaway of the IQR is that it is a statistic, like the range, that helps describe the spread of the center of the data.

However, unlike the range, the IQR is robust. A statistic is robust when outliers have little impact on it. For example, the IQRs of the two datasets below are identical, even though one has a massive outlier.

dataset_one = [6, 9, 10, 45, 190, 200] #IQR is 144.5
dataset_two = [6, 9, 10, 45, 190, 20000000] #IQR is 144.5
By looking at the IQR instead of the range, you can get a better sense of the spread of the middle of the data.

The interquartile range is displayed in a commonly-used graph — the box plot.
"""
from scipy.stats import iqr

dataset = [-50, -24, -13, -2, 0, 12, 15, 18, 73, 90, 10000000]

dataset_range = max(dataset) - min(dataset)
dataset_iqr = iqr(dataset)

print("The range of the dataset is "+str(dataset_range))
print("The IQR of the dataset is "+str(dataset_iqr))


"""
We’ve set up a small dataset and are printing its range and IQR.

Try changing the maximum number in the dataset to different values.

What happens to the range when you make the maximum value 100000? What happens to the IQR?

Try changing the minimum value to be more of an outlier as well.
"""