import numpy as np
from exam import passed_exam, probabilities, probabilities_2

# Function to calculate log-loss
def log_loss(probabilities,actual_class):
  return np.sum(-(1/actual_class.shape[0])*(actual_class*np.log(probabilities) + (1-actual_class)*np.log(1-probabilities)))

# Print passed_exam here
print(passed_exam)

# Calculate and print loss_1 here
loss_1 = log_loss(probabilities, passed_exam)
print(loss_1)
# Calculate and print loss_2 here
loss_2 = log_loss(probabilities_2, passed_exam) 
print(loss_2)

"""
The first set of coefficients produced a lower log-loss than the second set! This is because the first set of coefficients was determined by the Logistic Regression model as the optimized coefficient values. The second set of coefficients were initialized at 0, and served as a starting point.
"""