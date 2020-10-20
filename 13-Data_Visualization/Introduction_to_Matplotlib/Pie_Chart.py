import codecademylib
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#MatplotSip keeps track of how many people pay by credit card, cash, Apple pay, or other methods. This is given to you in the payment_method_names and payment_method_freqs lists.
#Display the payment_method_freqs list as a pie chart.
#make your pie chart here
plt.pie(payment_method_freqs)

#Now, set the axes to be equal.
plt.axis('equal')

plt.show()