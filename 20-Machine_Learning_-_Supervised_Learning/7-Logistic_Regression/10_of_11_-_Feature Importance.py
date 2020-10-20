import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from exam import exam_features_scaled, passed_exam_2

# Train a sklearn logistic regression model on the normalized exam data
model_2 = LogisticRegression()
model_2.fit(exam_features_scaled,passed_exam_2)



"""
Let’s revisit the sklearn Logistic Regression model we fit to our exam data in the last exercise. Remember, the two features in the new model are the number of hours studied and the number of previous math courses taken.

Using the model, given to you as model_2 in the code editor, save the feature coefficients to the variable coefficients.
"""
# Assign and update coefficients
coefficients = model_2.coef_



"""
In order to visualize the coefficients, let’s pull them out of the numpy array in which they are currently stored. With numpys tolist() method we can convert the array into a list and grab the values we want to visualize.

Below your original assignment of coefficients, update coefficients to equal coefficients.tolist()[0].
"""
coefficients = coefficients.tolist()[0]



"""
Create a bar graph comparing the feature coefficients with matplotlib‘s plt.bar() method. Which feature appears to be more important in determining whether or not a student will pass the Introductory Machine Learning final exam?
"""

# Plot bar graph
plt.bar([1,2],coefficients)
plt.xticks([1,2],['hours studied','math courses taken'])
plt.xlabel('feature')
plt.ylabel('coefficient')
plt.show()



