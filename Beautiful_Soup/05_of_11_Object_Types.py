"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Object Types
BeautifulSoup breaks the HTML page into several types of objects.

Tags
A Tag corresponds to an HTML Tag in the original document. These lines of code:

soup = BeautifulSoup('<div id="example">An example div</div><p>An example p tag</p>')
print(soup.div)
Would produce output that looks like:

<div id="example">An example div</div>
Accessing a tag from the BeautifulSoup object in this way will get the first tag of that type on the page.

You can get the name of the tag using .name and a dictionary representing the attributes of the tag using .attrs:

print(soup.div.name)
print(soup.div.attrs)
div
{'id': 'example'}
NavigableStrings
NavigableStrings are the pieces of text that are in the HTML tags on the page. You can get the string inside of the tag by calling .string:

print(soup.div.string)
An example div
"""
import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")



"""
Print out the first p tag on the shellter.html page.
"""
print("The first \"p tag\" on the shellter.html page: \n" + str(soup.p))



"""
Print out the string associated with the first p tag on the shellter.html page.
"""
print("The string associated with the first p tag on the shellter.html page: \n" + str(soup.p.string))

