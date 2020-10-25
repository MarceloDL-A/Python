import numpy as np

returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]

variance_disney = np.var(returns_disney)
variance_cbs = np.var(returns_cbs)

# Write code here
dataset = [10, 8, 9, 10, 12]

def calculate_variance(dataset):
  mean = sum(dataset)/len(dataset)
  numerator = 0
  for i in dataset:
    numerator += (mean - i)**2
  variance = numerator/len(dataset)
  return variance
variance_disney = calculate_variance(returns_disney)
variance_cbs = calculate_variance(returns_cbs) 
print('The variance of Disney stock returns is', variance_disney)
print('The variance of CBS stock returns is', variance_cbs)
