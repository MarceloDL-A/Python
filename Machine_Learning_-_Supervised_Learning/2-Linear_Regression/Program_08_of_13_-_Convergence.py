import codecademylib3_seaborn
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01

iterations = range(1400)

plt.plot(iterations, bs)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()


"""

How many iterations did it take for this program to converge?

Enter your answer in a variable called num_iterations.
"""
num_iterations = 800
convergence_b = 45