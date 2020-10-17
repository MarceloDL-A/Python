"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Select for CSS Selectors
Another way to capture your desired elements with the soup object is to use CSS selectors. The .select() method will take in all of the CSS selectors you normally use in a .css file!

<h1 class='results'>Search Results for: <span class='searchTerm'>Funfetti</span></h1>
<div class='recipeLink'><a href="spaghetti.html">Funfetti Spaghetti</a></div>
<div class='recipeLink' id="selected"><a href="lasagna.html">Lasagna de Funfetti</a></div>
<div class='recipeLink'><a href="cupcakes.html">Funfetti Cupcakes</a></div>
<div class='recipeLink'><a href="pie.html">Pecan Funfetti Pie</a></div>
If we wanted to select all of the elements that have the class 'recipeLink', we could use the command:

soup.select(".recipeLink")
If we wanted to select the element that has the id 'selected', we could use the command:

soup.select("#selected")
Let’s say we wanted to loop through all of the links to these funfetti recipes that we found from our search.

for link in soup.select(".recipeLink > a"):
  webpage = requests.get(link)
  new_soup = BeautifulSoup(webpage)
This loop will go through each link in each .recipeLink div and create a soup object out of the webpage it links to. So, it would first make soup out of <a href="spaghetti.html">Funfetti Spaghetti</a>, then <a href="lasagna.html">Lasagna de Funfetti</a>, and so on.
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
  turtle_name = turtle.select(".name")[0]
  #Add your code here:
  turtle_data[turtle_name] = []

print(turtle_data) 
  

  
"""
We have taken the links you found in the last exercise and turned them into links we can follow by prepending a prefix to them.

Now, we’re looping through each of the links on the home page and following them to learn more about each turtle!

We are going to want to store information about each turtle in a dictionary called turtle_data.

First, before the loop that goes through the turtle_links, create an empty dictionary called turtle_data.
""" 







"""
Now, let’s fill in some data from each turtle. Inside the loop that iterates through links, you’ll see that we’ve created a BeautifulSoup object out of each individual turtle’s page.

You can click on a turtle in the web browser to see how an individual turtle’s page looks. What kind of information from this page might we want to store?
"""

"""
If you used your Inspector tools to look at the turtle’s page, you might have seen that the turtle’s name is in a p tag with the class name.

Inside the loop, use .select() to select the tags with class name. Store the first entry of that list in a variable called turtle_name.

Add turtle_name to the dictionary as a key, and for now set the value of that key to an empty list.
"""

  