star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

def distance(movie1, movie2):
  distance = 0
  for i in range(len(movie1)):
    distance += (movie1[i] - movie2[i])**2
  return distance**0.5

print("distance(star_wars, raiders): \n" + str(distance(star_wars, raiders)))
print("distance(star_wars, mean_girls): \n" +str(distance(star_wars, mean_girls)))