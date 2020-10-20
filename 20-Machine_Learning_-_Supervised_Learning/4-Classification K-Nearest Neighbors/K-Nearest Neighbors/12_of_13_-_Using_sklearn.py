from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

#Create a KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5)

#Train your classifier
classifier.fit(movie_dataset, labels)

#Let’s classify some movies
guesses = classifier.predict([[.45, .2, .5], [.25, .8, .9],[.1, .1, .9]])
print(guesses)

#Ans.: [1 1 0]
