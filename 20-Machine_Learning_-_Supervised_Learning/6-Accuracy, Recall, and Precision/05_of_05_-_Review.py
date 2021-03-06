from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

"""
Different ways to analyze the predictive power of your algorithm. Some of the key insights for this course include:

Classifying a single point can result in a true positive (truth = 1, guess = 1), a true negative (truth = 0, guess = 0), a false positive (truth = 0, guess = 1), or a false negative (truth = 1, guess = 0).
Accuracy measures how many classifications your algorithm got correct out of every classification it made.
Recall measures the percentage of the relevant items your classifier was able to successfully find.
Precision measures the percentage of items your classifier found that were actually relevant.
Precision and recall are tied to each other. As one goes up, the other will go down.
F1 score is a combination of precision and recall.
F1 score will be low if either precision or recall is low.
"""

print(accuracy_score(labels, guesses))
print(recall_score(labels, guesses))
print(precision_score(labels, guesses))
print(f1_score(labels, guesses))

