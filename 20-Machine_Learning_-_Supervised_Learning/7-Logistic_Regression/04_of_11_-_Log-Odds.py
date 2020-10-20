import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Create your log_odds() function here
def log_odds(features, coefficients,intercept):
  return np.dot(features, coefficients) + intercept 

# Calculate the log-odds for the Codecademy University data here
calculated_log_odds = log_odds(hours_studied, calculated_coefficients,intercept)
print(calculated_log_odds)
"""
[[-1.76125712]
 [-1.55447221]
 [-1.3476873 ]
 [-1.14090239]
 [-0.93411748]
 [-0.72733257]
 [-0.52054766]
 [-0.31376275]
 [-0.10697784]
 [ 0.09980707]
 [ 0.30659198]
 [ 0.51337689]
 [ 0.7201618 ]
 [ 0.92694671]
 [ 1.13373162]
 [ 1.34051653]
 [ 1.54730144]
 [ 1.75408635]
 [ 1.96087126]
 [ 2.16765617]]
 """