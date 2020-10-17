"""
WEB SCRAPING WITH BEAUTIFUL SOUP
Requests
In order to get the HTML of the website, we need to make a request to get the content of the webpage. To learn more about requests in a general sense, you can check out this article.

Python has a requests library that makes getting content really easy. All we have to do is import the library, and then feed in the URL we want to GET:

import requests

webpage = requests.get('https://www.codecademy.com/articles/http-requests')
print(webpage.text)
This code will print out the HTML of the page.

We don’t want to unleash a bunch of requests on any one website in this lesson, so for the rest of this lesson we will be scraping a local HTML file and pretending it’s an HTML file hosted online.
"""
"""
Import the requests library.
"""
import requests



"""
Make a GET request to the URL containing the turtle adoption website:

https://content.codecademy.com/courses/beautifulsoup/shellter.html

Store the result of your request in a variable called webpage_response.
"""
webpage_response = requests.get("https://content.codecademy.com/courses/beautifulsoup/shellter.html")



"""
Store the content of the response in a variable called webpage by using .content.

Print webpage out to see the content of this HTML.
"""
webpage = webpage_response.content
print("webpage: \n" + str(webpage))

