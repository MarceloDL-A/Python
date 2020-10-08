import codecademylib
from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#Add a percentage to each slice using Matplotlib’s autopct parameter. Go to one decimal point of precision.
plt.pie(payment_method_freqs, autopct = '%0.1f%%')
plt.axis('equal')

#Add a legend to the chart by passing in a list of labels to plt.legend. For the labels, use the list payment_method_names.
plt.legend(payment_method_names)

plt.show()