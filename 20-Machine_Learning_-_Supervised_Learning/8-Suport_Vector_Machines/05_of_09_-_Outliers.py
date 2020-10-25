import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from graph import points, labels, draw_points, draw_margin

points.append([3, 3])
points.append([1, 1])
points.append([10, 8])
labels.append(0)
labels.append(1)
labels.append(0)

classifier = SVC(kernel='linear', C = 0.1)
classifier.fit(points, labels)

draw_points(points, labels)
draw_margin(classifier)

plt.show()
