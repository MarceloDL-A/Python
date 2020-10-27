import numpy as np
from scipy.spatial.distance import cityblock, euclidean, cosine
import spacy

# load word embedding model
nlp = spacy.load('en')

# define word embedding vectors
happy_vec = nlp('happy').vector
sad_vec = nlp('sad').vector
angry_vec = nlp('angry').vector

# calculate Manhattan distance
man_happy_sad = cityblock(happy_vec, sad_vec)
man_sad_angry = cityblock(sad_vec, angry_vec)
print(f"man_happy_sad: {man_happy_sad}")
print(f"man_sad_angry: {man_sad_angry}")


# calculate Euclidean distance
euc_happy_sad = euclidean(happy_vec, sad_vec)
euc_sad_angry = euclidean(sad_vec, angry_vec)
print(f"euc_happy_sad: {euc_happy_sad}")
print(f"euc_sad_angry: {euc_sad_angry}")



# calculate cosine distance
cos_happy_sad = cosine(happy_vec, sad_vec)
cos_sad_angry = cosine(sad_vec, angry_vec)
print(f"cos_happy_sad: {cos_happy_sad}")
print(f"cos_sad_angry: {cos_sad_angry}")

