"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Introduction
Before we get started, a quick note on prerequisites: This course requires knowledge of Python. Also some understanding of the Python library Pandas will be helpful later on in the lesson, but isn’t totally necessary. If you haven’t already, check out those courses before taking this one. Okay, let’s get scraping!

In Data Science, we can do a lot of exciting work with the right dataset. Once we have interesting data, we can use Pandas or Matplotlib to analyze or visualize trends. But how do we get that data in the first place?

If it’s provided to us in a well-organized csv or json file, we’re lucky! Most of the time, we need to go out and search for it ourselves.

Often times you’ll find the perfect website that has all the data you need, but there’s no way to download it. This is where BeautifulSoup comes in handy to scrape the HTML. If we find the data we want to analyze online, we can use BeautifulSoup to grab it and turn it into a structure we can understand. This Python library, which takes its name from a song in Alice in Wonderland, allows us to easily and quickly take information from a website and put it into a DataFrame.
"""
from preprocess import turtles



"""
We’ve used BeautifulSoup to take the turtle data from the Shellter website in the browser and put it into a DataFrame.

Explore the website a bit. Then, print the DataFrame turtles to see how this data is organized.
"""
print("The DataFrame turtles organized: \n" + str(turtles) )


"""
Result:
The DataFrame turtles organized: 
                            0  ...                             4
Aesop        AGE: 7 Years Old  ...    SOURCE: found in Lake Erie
Caesar       AGE: 2 Years Old  ...      SOURCE: hatched in house
Sulla         AGE: 1 Year Old  ...    SOURCE: found in Lake Erie
Spyro        AGE: 6 Years Old  ...      SOURCE: hatched in house
Zelda        AGE: 3 Years Old  ...  SOURCE: surrendered by owner
Bandicoot    AGE: 2 Years Old  ...      SOURCE: hatched in house
Hal           AGE: 1 Year Old  ...  SOURCE: surrendered by owner
Mock        AGE: 10 Years Old  ...  SOURCE: surrendered by owner
Sparrow    AGE: 1.5 Years Old  ...    SOURCE: found in Lake Erie

[9 rows x 5 columns]
"""