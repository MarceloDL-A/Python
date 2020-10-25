from utils import calculate_variance
import numpy as np
# Import library here
from math import sqrt

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]

stddev_disney = np.std(returns_disney)
stddev_cbs = np.std(returns_cbs)

# Write code here
dataset = [10, 8, 9, 10, 12]

def calculate_stddev(dataset):
  variance = calculate_variance(dataset)
  stddev = sqrt(variance)
  return stddev
stddev_disney = calculate_stddev(returns_disney)
stddev_cbs = calculate_stddev(returns_cbs)
print('The standard deviation of Disney stock returns is', display_as_percentage(stddev_disney))
print('The standard deviation of CBS stock returns is', display_as_percentage(stddev_cbs))
