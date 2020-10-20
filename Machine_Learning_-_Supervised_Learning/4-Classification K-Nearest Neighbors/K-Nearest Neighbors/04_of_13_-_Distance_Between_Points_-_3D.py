star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
  #length_difference = (movie1[0] - movie2[0]) ** 2
  #year_difference = (movie1[1] - movie2[1]) ** 2
  distance = 0
  for i in range(len(movie1)):
    distance += (movie1[i] - movie2[i])**2
  return distance**0.5

print("distance(star_wars, raiders): \n" + str(distance(star_wars, raiders)))
print("distance(star_wars, mean_girls): \n" + str(distance(star_wars, mean_girls)))