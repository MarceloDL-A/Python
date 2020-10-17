"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Review
Amazing! Now you know the basics of how to use BeautifulSoup to turn websites into data. If you take our Data Visualization or Data Manipulation courses, you can see how you might analyze this data and find patterns!

You now can see how far the rabbit hole goes by finding some interesting data you want to analyze on the web. But remember to be respectful to site owners if you test out your scraping chops on real sites.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")


"""
1.
Create a DataFrame out of the turtle_data dictionary you’ve created. Call it turtle_df.


Hint
You can use Pandas’ .from_dict() method to transform a dictionary into a Pandas DataFrame:

turtle_df = pd.DataFrame.from_dict(your_dictionary, orient='index')
"""
turtle_df = pd.DataFrame.from_dict(turtle_data, orient = "index")



"""
Wow! Now we have all of the turtles’ information in one DataFrame. But obviously, in just scraping this data and plopping it into Pandas, we’re left with a pretty messy DataFrame.

There are newlines in the data, the column names are hidden in strings in the rows, and none of the numerical data is stored as a numerical type.

It would be pretty hard to create any sort of analysis on this raw data. What if we wanted to make a histogram of the ages of turtles in the Shellter?

This is where Data Cleaning and Regex comes in! Try to practice what you know about data cleaning to get turtles_df into a usable state. It’s up to you to decide what “usable” means to you.
"""
print("turtle_df.head(): \n" + str(turtle_df.head()))
print("turtle_df.columns: \n" + str(turtle_df.columns))
print("turtle_df.columns.dtype: \n" + str(turtle_df.columns.dtype))
print("turtle_df[0]: \n" + str(turtle_df[0]))
print("turtle_df[1]: \n" + str(turtle_df[1]))
print("turtle_df[2]: \n" + str(turtle_df[2]))
print("turtle_df[3]: \n" + str(turtle_df[3]))
print("turtle_df[4]: \n" + str(turtle_df[4]))
print("turtle_df[5]: \n" + str(turtle_df[5]))








