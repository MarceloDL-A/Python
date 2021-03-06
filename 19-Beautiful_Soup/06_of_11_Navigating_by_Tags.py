"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Navigating by Tags
To navigate through a tree, we can call the tag names themselves. Imagine we have an HTML page that looks like this:

<h1>World's Best Chocolate Chip Cookies</h1>
<div class="banner">
  <h1>Ingredients</h1>
</div>
<ul>
  <li> 1 cup flour </li>
  <li> 1/2 cup sugar </li>
  <li> 2 tbsp oil </li>
  <li> 1/2 tsp baking soda </li>
  <li> � cup chocolate chips </li> 
  <li> 1/2 tsp vanilla <li>
  <li> 2 tbsp milk </li>
</ul>
If we made a soup object out of this HTML page, we have seen that we can get the first h1 element by calling:

print(soup.h1)
<h1>World's Best Chocolate Chip Cookies</h1>
We can get the children of a tag by accessing the .children attribute:

for child in soup.ul.children:
    print(child)
<li> 1 cup flour </li>
<li> 1/2 cup sugar </li>
<li> 2 tbsp oil </li>
<li> 1/2 tsp baking soda </li>
<li> � cup chocolate chips </li> 
<li> 1/2 tsp vanilla <li>
<li> 2 tbsp milk </li>
We can also navigate up the tree of a tag by accessing the .parents attribute:

for parent in soup.li.parents:
    print(parent)
This loop will first print:

<ul>
<li> 1 cup flour </li>
<li> 1/2 cup sugar </li>
<li> 2 tbsp oil </li>
<li> 1/2 tsp baking soda </li>
<li> � cup chocolate chips </li>
<li> 1/2 tsp vanilla </li>
<li> 2 tbsp milk </li>
</ul>
Then, it will print the tag that contains the ul (so, the body tag of the document). Then, it will print the tag that contains the body tag (so, the html tag of the document).
"""
import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")



"""
Loop through all of the children of the first div and print out each one.
"""
for i in soup.div.children:
  print(i)