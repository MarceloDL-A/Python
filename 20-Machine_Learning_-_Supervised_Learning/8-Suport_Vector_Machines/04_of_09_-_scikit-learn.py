from sklearn.svm import SVC
from graph import points, labels
classifier = SVC(kernel = "linear")
classifier.fit(points, labels)
"""
1 as a red point and a 0 as a blue
[3, 4], [6, 7] = [0 1]
"""
print(classifier.predict([[3, 4], [6, 7]]))