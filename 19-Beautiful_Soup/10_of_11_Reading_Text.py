"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Reading Text
When we use BeautifulSoup to select HTML elements, we often want to grab the text inside of the element, so that we can analyze it. We can use .get_text() to retrieve the text inside of whatever tag we want to call it on.

<h1 class="results">Search Results for: <span class='searchTerm'>Funfetti</span></h1>
If this is the HTML that has been used to create the soup object, we can make the call:

soup.get_text()
Which will return:

'Search Results for: Funfetti'
Notice that this combined the text inside of the outer h1 tag with the text contained in the span tag inside of it! Using get_text(), it looks like both of these strings are part of just one longer string. If we wanted to separate out the texts from different tags, we could specify a separator character. This command would use a . character to separate:

soup.get_text('|')
Now, the command returns:

'Search Results for: |Funfetti'
"""
import requests
from bs4 import BeautifulSoup

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  turtle_data[turtle_name] = [turtle.find("ul").get_text("|").split("|")]
print(turtle_data)


"""
After the loop, print out turtle_data. We have been storing the names as the whole p tag containing the name.

Instead, let’s call get_text() on the turtle_name element and store the result as the key of our dictionary instead.

hint:
turtle_name should now be equal to something like:

turtle.select(".name")[0].get_text()
"""


"""
Instead of associating each turtle with an empty list, let’s have each turtle associated with a list of the stats that are available on their page.

It looks like each piece of information is in a li element on the turtle’s page.

Get the ul element on the page, and get all of the text in it, separated by a '|' character so that we can easily split out each attribute later.

Store the resulting string in turtle_data[turtle_name] instead of storing an empty list there.

Hint:
At this point, the value of each turtle_data[turtle_name] should look something like:

turtle.find("ul").get_text("|")
"""


"""
When we store the list of info in each turtle_data[turtle_name], separate out each list element again by splitting on '|'.

Hint
At this point, the value of each turtle_data[turtle_name] should look something like:

turtle.find("ul").get_text("|").split("|")
"""

