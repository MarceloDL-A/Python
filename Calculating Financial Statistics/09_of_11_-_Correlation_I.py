from utils import calculate_correlation
import numpy as np

returns_general_motors = [0.018, -0.005, -0.047, -0.009, -0.012, 0.003, -0.027, -0.014, 0.029, -0.062, 0.009]
returns_ford = [0.002, -0.004, -0.027, -0.022, -0.001, 0.002, -0.006, -0.017, 0.035, -0.029, 0.002]
returns_exxon_mobil = [0.008, 0.015, 0.009, 0.012, 0.003, -0.007, 0.006, 0.005, -0.048, 0.025, -0.012]
returns_apple = [-0.002, 0.007, -0.004, -0.004, 0.002, 0.013, -0.011, 0.017, -0.001, 0.012, 0.006]

corr_gm_ford = calculate_correlation(returns_general_motors, returns_ford)
print('The correlation coefficient between General Motors and Ford is', corr_gm_ford)

# Write code here
print("The correlation coefficient between General Motors and ExxonMobil is ", calculate_correlation(returns_general_motors, returns_apple))

print("The correlation coefficient between General Motors and Apple is ", calculate_correlation(returns_general_motors, returns_exxon_mobil))

corrcoef_matrix = np.corrcoef([returns_general_motors, returns_ford, returns_exxon_mobil, returns_apple])
print(corrcoef_matrix)

