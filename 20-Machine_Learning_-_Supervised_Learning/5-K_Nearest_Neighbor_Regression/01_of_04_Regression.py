from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  total = 0
  for neighbor in neighbors:
    title = neighbor[1]
    total += movie_ratings[title]
  return total/len(neighbors)


"""
1.
We’ve imported most of the K-Nearest Neighbor algorithm. Before we dive into finishing the regressor, let’s refresh ourselves with the data.

At the bottom of your code, print movie_dataset["Life of Pi"]. You should see a list of three values. These values are the normalized values for the movie’s budget, runtime, and release year.
"""
print(movie_dataset["Life of Pi"])



"""
Print the rating for "Life of Pi". This can be found in movie_ratings.
"""
print(movie_ratings["Life of Pi"])


"""
3.
We’ve included the majority of the K-Nearest Neighbor algorithm in the predict() function. Right now, the variable neighbors stores a list of [distance, title] pairs.

Loop through every neighbor and find its rating in movie_ratings. Add those ratings together and return that sum divided by the total number of neighbors.
"""
"""
4.
Call predict with the following parameters:

[0.016, 0.300, 1.022]
movie_dataset
movie_ratings
5
Print the result.

Note that the list [0.016, 0.300, 1.022] is the normalized budget, runtime, and year of the movie Incredibles 2! The normalized year is larger than 1 because our training set only had movies that were released between 1927 and 2016 — Incredibles 2 was released in 2018.
"""
print(predict([0.016, 0.300, 1.022], movie_dataset, movie_ratings, 5))










