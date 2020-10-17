"""
**********************************
WHY USE MACHINE LEARNING?
Supervised Learning
Machine learning can be branched out into the following categories:

Supervised Learning
Unsupervised Learning
Supervised Learning is where the data is labeled and the program learns to predict the output from the input data. For instance, a supervised learning algorithm for credit card fraud detection would take as input a set of recorded transactions. For each transaction, the program would predict if it is fraudulent or not.

Supervised learning problems can be further grouped into regression and classification problems.

Regression:

In regression problems, we are trying to predict a continuous-valued output. Examples are:

What is the housing price in Neo York?
What is the value of cryptocurrencies?
Classification:

In classification problems, we are trying to predict a discrete number of values. Examples are:

Is this a picture of a human or a picture of an AI?
Is this email spam?
For a quick preview, we will show you an example of supervised learning.

Instructions
1.
NYBD (Neo York Bot Department) wants to analyze how Neo Yorkers are talking to one another so that they can determine who is being negative.

They have built a Naive Bayes classifier that predicts whether an intercepted text is good or bad, based on the frequency that a word is used in a good training example or a bad one.

Run the code to see if the model classifies the sentence "This hot dog was awful!" as a negative sentiment.
**********************************
"""
from texts import text_counter, text_training
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

intercepted_text = "I hate bad people"

text_counts = text_counter.transform([intercepted_text])

text_classifier = MultinomialNB()

text_labels = [0] * 1000 + [1] * 1000

text_classifier.fit(text_training, text_labels)

final_pos = text_classifier.predict_proba(text_counts)[0][1]

final_neg = text_classifier.predict_proba(text_counts)[0][0]

if final_pos > final_neg:
  print("The text is positive.")
else:
  print("The text is negative.")



"""
**********************************
2.
The NYBD wants to know what its citizens are saying.

Put in the sentence "I love my government." in intercepted_text and see if the classifier predicts a positive sentiment!
**********************************
"""


"""
**********************************
3.
Put a sentence of your own in intercepted_text and see if the classifier predicts a positive sentiment!

Note: This Naive Bayes classifier won’t always get the sentiment correct!
**********************************
"""