labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(labels)):  
  if labels[i] == guesses[i]:
    if labels[i] == 1:
      true_positives += 1
    else:
      true_negatives += 1
  if labels[i] != guesses[i]:
    if guesses[i] == 1:
      false_positives += 1
    else:
      false_negatives += 1
  accuracy = (true_positives + true_negatives)/(true_positives + true_negatives + false_positives + false_negatives)
  

print(accuracy)
 
