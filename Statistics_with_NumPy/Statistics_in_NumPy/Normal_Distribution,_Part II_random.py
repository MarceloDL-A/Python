"""
STATISTICAL DISTRIBUTIONS WITH NUMPY
Normal Distribution, Part II
We can generate our own normally distributed datasets using NumPy. Using these datasets can help us better understand the properties and behavior of different distributions. We can also use them to model results, which we can then use as a comparison to real data.

In order to create these datasets, we need to use a random number generator. The NumPy library has several functions for generating random numbers, including one specifically built to generate a set of numbers that fit a normal distribution: np.random.normal. This function takes the following keyword arguments:

loc: the mean for the normal distribution
scale: the standard deviation of the distribution
size: the number of random numbers to generate
a = np.random.normal(0, 1, size=100000)
"""

import codecademylib
import numpy as np
from matplotlib import pyplot as plt

"""
Our friend is a paleontologist. He’s studying two types of dinosaurs: brachiosaurus and fictionosaurus. He tells us that:

Brachiosaurus have femurs (thigh bone) with mean length of 6.7 ft and a standard deviation of 0.7 ft.
Fictionosaurus have femurs (thigh bone) with mean length of 7.7 ft and a standard deviation of 0.3 ft.
We’d like to know what these distributions look like.

Use np.random.normal to fill in b_data (brachiosaurus) and f_data (fictionosaurus) with randomly generated samples with the correct mean and standard deviation. Each dataset should have 1000 samples.

The code that we supplied below will graph the distributions for you.
"""
# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size = 1000)

# Fictionosaurus
f_data = np.random.normal(7.7, 0.3, size = 1000)

"""
Our friend discovered a femur from an unidentified dinosaur on his last dig. The femur is 6.6 feet long.

Your friend is pretty sure that the femur belongs to either a brachiosaurus or a fictionosaurus. Looking at the graphed data, determine which dinosaur this skeleton is most likely to belong, and save your answer to the variable mystery_dino.
"""
mystery_dino = "Brachiosaurus"

"""
Our friend discovered another femur. This femur is 7.5 ft long. Obviously, 7.5 ft is closer to the mean for a fictionosaurus (7.7 ft), than it is to the mean for a brachiosaurus (6.5 ft).

Can we be absolutely sure that the femur came from a fictionosaurus? Save you answer (either True or False) to answer.
"""
answer = False

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()
