import spacy

# load word embedding model
nlp = spacy.load("en")

# define word embedding vectors
happy_vec = nlp("happy").vector
sad_vec = nlp("sad").vector
angry_vec = nlp("angry").vector

print(f"happy_vec: {happy_vec}")
print()
print(f"sad_vec: {sad_vec}")
print()
print(f"angry_vec: {angry_vec}")

# find vector length here
vector_length_happy = len(happy_vec)
vector_length_sad = len(sad_vec)
vector_length_angry = len(angry_vec)
print(f"vector_length_happy: {vector_length_happy}")
print(f"vector_length_sad: {vector_length_sad}")
print(f"vector_length_angry: {vector_length_angry}")

