"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Find All
If we want to find all of the occurrences of a tag, instead of just the first one, we can use .find_all().

This function can take in just the name of a tag and returns a list of all occurrences of that tag.

print(soup.find_all("h1"))
['<h1>World's Best Chocolate Chip Cookies</h1>', '<h1>Ingredients</h1>']
.find_all() is far more flexible than just accessing elements directly through the soup object. With .find_all(), we can use regexes, attributes, or even functions to select HTML elements more intelligently.

Using Regex
What if we want every <ol> and every <ul> that the page contains? We can select both of these types of elements with a regex in our .find_all():

import re
soup.find_all(re.compile("[ou]l"))
What if we want all of the h1 - h9 tags that the page contains? Regex to the rescue again!

import re
soup.find_all(re.compile("h[1-9]"))
Using Lists
We can also just specify all of the elements we want to find by supplying the function with a list of the tag names we are looking for:

soup.find_all(['h1', 'a', 'p'])
Using Attributes
We can also try to match the elements with relevant attributes. We can pass a dictionary to the attrs parameter of find_all with the desired attributes of the elements we�re looking for. If we want to find all of the elements with the "banner" class, for example, we could use the command:

soup.find_all(attrs={'class':'banner'})
Or, we can specify multiple different attributes! What if we wanted a tag with a "banner" class and the id "jumbotron"?

soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})
Using A Function
If our selection starts to get really complicated, we can separate out all of the logic that we�re using to choose a tag into its own function. Then, we can pass that function into .find_all()!

def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"

soup.find_all(has_banner_class_and_hello_world)
This command would find an element that looks like this:

<div class="banner">Hello world</div>
but not an element that looks like this:

<div>Hello world</div>
Or this:

<div class="banner">What's up, world!</div>
"""
import requests
from bs4 import BeautifulSoup
import re
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")


"""
Find all of the a elements on the page and store them in a list called turtle_links.
"""
turtle_links = soup.find_all("a")



"""
Print turtle_links. Is this what you expected?
"""
print(turtle_links)
