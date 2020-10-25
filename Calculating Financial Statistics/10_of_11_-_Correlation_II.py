from data import returns_general_motors, returns_ford, returns_exxon_mobil, returns_apple
from math import sqrt
import numpy as np

def calculate_correlation(set_x, set_y):
  # Sum of all values in each dataset
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  # Sum of all squared values in each dataset
  sum_x2 = sum([x ** 2 for x in set_x])

  sum_y2 = sum([x ** 2 for x in set_y])


  # Sum of the product of each respective element in each dataset 
  sum_xy = sum([i*k for i, k in zip(set_x, set_y)])
  

  # Length of dataset
  n = len(set_x)

  # Calculate correlation coefficient
  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator

# Function calls
print('The correlation coefficient between General Motors and Ford is', calculate_correlation(returns_general_motors, returns_ford))
print('The correlation coefficient between General Motors and ExxonMobil is', calculate_correlation(returns_general_motors, returns_exxon_mobil))
print('The correlation coefficient between General Motors and Apple is', calculate_correlation(returns_general_motors, returns_apple))
