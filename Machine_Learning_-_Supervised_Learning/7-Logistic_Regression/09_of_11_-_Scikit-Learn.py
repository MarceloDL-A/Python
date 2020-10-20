import numpy as np
from sklearn.linear_model import LogisticRegression
from exam import hours_studied_scaled, passed_exam, exam_features_scaled_train, exam_features_scaled_test, passed_exam_2_train, passed_exam_2_test, guessed_hours_scaled


"""
1.
Let’s build, train and evaluate a Logistic Regression model in sklearn for our Codecademy University data! We’ve imported sklearn and the LogisiticRegression classifier for you. Create a Logistic Regression model named model.
"""
# Create and fit logistic regression model here
model = LogisticRegression()



"""
2.
Train the model using hours_studied_scaled as the training features and passed_exam as the training labels.
"""
model.fit(hours_studied_scaled, passed_exam)



"""
3.
Save the coefficients of the model to the variable calculated_coefficients, and the intercept of the model to intercept. Print calculated_coefficients and intercept.
"""
# Save the model coefficients and intercept here
calculated_coefficients = model.coef_
intercept = model.intercept_



"""
4.
The next semester a group of students in the Introductory Machine Learning course want to predict their final exam scores based on how much they intended to study for the exam. The number of hours each student thinks they will study, normalized, is given in guessed_hours_scaled. Use model to predict the probability that each student will pass the final exam, and save the probabilities to passed_predictions.
"""
# Predict the probabilities of passing for next semester's students here
passed_predictions = model.predict_proba(guessed_hours_scaled)




"""
5.
That same semester, the Data Science department decides to update the final exam passage model to consider two features instead of just one. During the final exam, students were asked to estimate how much time they spent studying, as well as how many previous math courses they have taken. The student responses, along with their exam results, were split into training and test sets. The training features, normalized, are given to you in exam_features_scaled_train, and the students’ results on the final are given in passed_exam_2_train.

Create a new Logistic Regression model named model_2 and train it on exam_features_scaled_train and passed_exam_2_train.
"""
# Create a new model on the training data with two features here
model_2 = LogisticRegression()
model_2.fit(exam_features_scaled_train, passed_exam_2_train)



"""
6.
Use the model you just trained to predict whether each student in the test set, exam_features_scaled_test, will pass the exam and save the predictions to passed_predictions_2. Print passed_predictions_2.

Compare the predictions to the actual student performance on the exam in the test set. How well did your model do?
"""
# Predict whether the students will pass here
passed_predictions_2 = model_2.predict(exam_features_scaled_test)
print("Predictions: \n" + str(passed_predictions_2))
print("Actual student performance: \n" + str(passed_exam_2_test))



