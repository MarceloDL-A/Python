import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
breast_cancer_data = load_breast_cancer()
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
#let’s take a look at the data
#print(breast_cancer_data.data[0])
#print(breast_cancer_data.feature_names)

"""
[1.799e+01 1.038e+01 1.228e+02 1.001e+03 1.184e-01 2.776e-01 3.001e-01
 1.471e-01 2.419e-01 7.871e-02 1.095e+00 9.053e-01 8.589e+00 1.534e+02
 6.399e-03 4.904e-02 5.373e-02 1.587e-02 3.003e-02 6.193e-03 2.538e+01
 1.733e+01 1.846e+02 2.019e+03 1.622e-01 6.656e-01 7.119e-01 2.654e-01
 4.601e-01 1.189e-01]
['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
 """

"""
We now have a sense of what the data looks like, but what are we trying to classify? Let’s print both breast_cancer_data.target and breast_cancer_data.target_names.
"""
#print(breast_cancer_data.target)
#print(breast_cancer_data.target_names)
#print(breast_cancer_data.target[0])

"""
Splitting the data into Training and Validation Sets
Call the train_test_split function. It takes several parameters:

5. The data you want to split (for us breast_cancer_data.data)
The labels associated with that data (for us, breast_cancer_data.target).
The test_size. This is what percentage of your data you want to be in your testing set. Let’s use test_size = 0.2
random_state. This will ensure that every time you run your code, the data is split in the same way. This can be any number. We used random_state = 100.

6.
Right now we’re not storing the return value of train_test_split. train_test_split returns four values in the following order:

The training set
The validation set
The training labels
The validation labels
Store those values in variables named training_data, validation_data, training_labels, and validation_labels.
"""
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 80)
#print("train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100): \n" + str(train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)))


"""
7.
Let’s confirm that worked correctly. Print out the length of training_data and training_labels. They should be the same size - one label for every piece of data!
"""
print(len(training_data))
print(len(training_labels))


"""
Running the classifier
8.
Now that we’ve created training and validation sets, we can create a KNeighborsClassifier and test its accuracy. Begin by importing KNeighborsClassifier from sklearn.neighbors.
"""



"""
10.
Train your classifier using the fit function. This function takes two parameters: the training set and the training labels.

11.
Now that the classifier has been trained, let’s find how accurate it is on the validation set. Call the classifier’s score function. score takes two parameters: the validation set and the validation labels. Print the result!


Hint
print(classifier.score(____, validation_labels))
The first parameter of score should be the validation set.
"""
print("Classifiers scores: \n")
accuracies = []
for k in range(1, 101):
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)
  print(classifier.score(validation_data, validation_labels))
  accuracies.append(classifier.score(validation_data, validation_labels))


"""
Graphing the results
13.

We now have the validation accuracy for 100 different ks. Rather than just printing it out, let's make a graph using matplotlib. Begin by importing matplotlib.pyplot as plt.

14.
The x-axis should be the values of k that we tested. This should be a list of numbers between 1 and 100. You can use the range function to make this list. Store it in a variable named k_list.

15.
The y-axis of our graph should be the validation accuracy. Instead of printing the validation accuracies, we want to add them to a list. Outside of the for loop, create an empty list named accuracies. Inside the for loop, instead of printing each accuracy, append it to accuracies.
"""


k_list = range(1, 101)
print(accuracies)
plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()

"""
18.
Great work! If you want to play around with this more, try changing the random_state parameter when making the training set and validation set. This will change which points are in the training set and which are in the validation set.

Ideally, the graph will look the same no matter how you split up the training set and test set. This data set is fairly small, so there is slightly more variance than usual.
"""
