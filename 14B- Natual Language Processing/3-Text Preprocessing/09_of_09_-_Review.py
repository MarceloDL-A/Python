from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech
import re

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'
headline_no_tag = re.sub(r"<.?p>", "", oprah_wiki)

print(headline_no_tag)

headline_no_tag2 = re.sub(r"\.", "", headline_no_tag)
print()

print(headline_no_tag2)
print()

print(headline_no_tag2.lower())

print()
tokenized_string = word_tokenize(headline_no_tag2)
print(tokenized_string)

print()
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokenized_string]
print(lemmatized_words)




















