"""
LEARN WEB SCRAPING WITH BEAUTIFUL SOUP
Chocolate Scraping with Beautiful Soup
After eating chocolate bars your whole life, you’ve decided to go on a quest to find the greatest chocolate bar in the world.

You’ve found a website that has over 1700 reviews of chocolate bars from all around the world. It’s displayed in the web browser on this page.

The data is displayed in a table, instead of in a csv or json. Thankfully, we have the power of BeautifulSoup that will help us transform this webpage into a DataFrame that we can manipulate and analyze.

The rating scale is from 1-5, as described in this review guide. A 1 is “unpleasant” chocolate, while a 5 is a bar that transcends “beyond the ordinary limits”.

Some questions we thought about when we found this dataset were: Where are the best cocoa beans grown? Which countries produce the highest-rated bars? What’s the relationship between cocoa solids percentage and rating?

Can we find a way to answer these questions, or uncover more questions, using BeautifulSoup and Pandas?
"""
import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame



"""
****************
Make Some Chocolate Soup
1.
Explore the webpage displayed in the browser. What elements could be useful to scrape here? Which elements do we not want to scrape?
****************
"""
"""
****************
2.
Let’s make a request to this site to get the raw HTML, which we can later turn into a BeautifulSoup object.

The URL is:

https://content.codecademy.com/courses/beautifulsoup/cacao/index.html
You can pass this into the .get() method of the requests module to get the HTML.

the HTML.

Hint
To make a request to a webpage, you can use the syntax:

webpage = requests.get("http://websitetoscrape.com")
****************
"""
webpage_reponse = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

webpage = webpage_reponse.content

"""
****************
3.
Create a BeautifulSoup object called soup to traverse this HTML.

Use "html.parser" as the parser, and the content of the response you got from your request as the document.

Hint
To make the object, you can use syntax like:

soup = BeautifulSoup(your_document, "your_parser")
your_document should be the .content of the webpage response you got from the last step.
****************
"""
soup = BeautifulSoup(webpage, "html.parser")



"""
****************
4.
If you want, print out the soup object to explore the HTML.

So many table rows! You’re probably very relieved that we don’t have to scrape this information by hand.
****************
"""
print(soup)



"""
****************
How are ratings distributed?
5.
How many terrible chocolate bars are out there? And how many earned a perfect 5? Let’s make a histogram of this data.

The first thing to do is to put all of the ratings into a list.

Use a command on the soup object to get all of the tags that contain the ratings.

Hint
It looks like all of the rating tds have a class "Rating".

Remember that we can use .find_all() to get all elements of a class "ClassName" with this syntax:

soup.find_all(attrs={"class": "ClassName"})
****************
"""
#print(soup.find_all(attrs = {"class": "Rating"}))
soup_rating = soup.find_all(attrs = {"class": "Rating"})
print(type(soup_rating))




"""
****************
6.
Create an empty list called ratings to store all the ratings in.
****************
"""
ratings = []




"""
****************
7.
Loop through the ratings tags and get the text contained in each one. Add it to the ratings list.

As you do this, convert the rating to a float, so that the ratings list will be numerical. This should help with calculations later.

Hint
The first element of your tags list probably contains the header string "Ratings", so we probably should leave this off the list. Start your loop at element 1 of the list instead.

You can cast a string x to a float with this syntax:

float(x)
You can get the text of a BeautifulSoup tag using .get_text()


Coments Thiago:
ratings_sec = []
print(ratings)
print(type(ratings))


ratings1 = ratings[1:]
ratings_float = [eval(ratings1[i]) for i in range(0, len(ratings1))]

print(type(ratings_float[0]))

a = float(ratings1[0])+1
print(a)
****************
"""
soup_rating_num = soup_rating[1:]
for i in soup_rating_num:
  soup_rating_num_txt = i.get_text()
  ratings.append(float(soup_rating_num_txt))

print(ratings)
print(type(ratings[0]))



"""
****************
8.
Using Matplotlib, create a histogram of the ratings values:

plt.hist(ratings)
Remember to show the plot using plt.show()!

Your plot will show up at localhost in the web browser. You will have to navigate away from the cacao ratings webpage to see it.
****************
"""
plt.hist(ratings)
plt.xlabel("Ratings")
plt.ylabel("Number of companies")
plt.show()



"""
****************
Which chocolatier makes the best chocolate?
9.
We want to now find the 10 most highly rated chocolatiers. One way to do this is to make a DataFrame that has the chocolate companies in one column, and the ratings in another. Then, we can do a groupby to find the ones with the highest average rating.

First, let’s find all the tags on the webpage that contain the company names.
****************
"""




"""
****************
It seems like all of the company tds have the class name "Company".

We can use .select() to grab BeautifulSoup elements by CSS selector:

soup.select(".ClassName")
Do this with the class name "Company" to get all of the right tags.
****************
"""
highly_rated = soup.select(".Company")





"""
****************
Just like we did with ratings, we now want to make an empty list to hold company names.
****************
"""
company_names = []




"""
****************
Loop through the tags containing company names, and add the text from each tag to the list you just created.

Hint
We might want to use syntax like

for td in company_tags[1:]:
  companies.append(td.get_text())
****************
"""
for i in highly_rated:
  company_names.append(i.get_text())

print(company_names)



"""
****************
Create a DataFrame with a column “Company” corresponding to your companies list, and a column “Ratings” corresponding to your ratings list.

Hint
You can make a DataFrame with defined columns using this syntax:

d = {"Column 1 Name": column_1_list, "Column 2 Name": column_2_list}
your_df = pd.DataFrame.from_dict(d)
****************
"""
company_names = company_names[1:]
dict_data = {"Company": company_names, "Rating": ratings}
df = pd.DataFrame.from_dict(dict_data)
print(df)


"""
****************
13.
Use .groupby to group your DataFrame by Company and take the average of the grouped ratings.

Then, use the .nlargest command to get the 10 highest rated chocolate companies. Print them out.

Look at the hint if you get stuck on this step!

Hint
Your Pandas commands should look something like:

mean_vals = cacao_df.groupby("Company").Rating.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)
****************
"""
mean_company_vals = df.groupby("Company").Rating.mean()
print("mean_company_vals: \n" + str(mean_company_vals))
top_company_10 = mean_company_vals.nlargest(10)
print("10_top_company: \n" + str(top_company_10))





"""
****************
Is more cacao better?
14.
We want to see if the chocolate experts tend to rate chocolate bars with higher levels of cacao to be better than those with lower levels of cacao.

It looks like the cocoa percentages are in the table under the Cocoa Percent column.

Using the same methods you used in the last couple of tasks, create a list that contains all of the cocoa percentages. Store each percent as an integer, after stripping off the % character.

You’ll have to access the tags with class "CocoaPercent" and loop through them to get the text.

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for td in cocoa_percent_tags[1:]:
  percent = int(td.get_text().strip('%'))
  cocoa_percents.append(percent)
****************
"""
print(soup)
cocoa_percents = []
cocoa_percents_tags = soup.select(".CocoaPercent")

for i in cocoa_percents_tags[1:]:
  percent = int(i.get_text().strip("%")[0:2])
  cocoa_percents.append(percent)

print("cocoa_percents: \n" + str(cocoa_percents))




"""
****************
15.
Add the cocoa percentages as a column called "CocoaPercentage" in the DataFrame that has companies and ratings in it.

Hint
You can add the pairing "CocoaPercentage":cocoa_percents to the dictionary you used to create the DataFrame.
****************
"""
df["CocoaPercentage"] = cocoa_percents
print("df: \n" + str(df))



"""
****************
16.
Make a scatterplot of ratings (your_df.Rating) vs percentage of cocoa (your_df.CocoaPercentage).

You can do this in Matplotlib with these commands:

plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()
Call plt.clf() to clear the figure between showing your histogram and this scatterplot.

Remember that your plots will show up at the address localhost in the web browser.
****************
"""
plt.clf()
plt.scatter(df.CocoaPercentage, df.Rating)
plt.xlabel("CocoaPercentage")
plt.ylabel("Rating")
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()



"""
****************
17.
Is there any correlation here? We can use some numpy commands to draw a line of best-fit over the scatterplot.

Copy this code and paste it after you create the scatterplot, but before you call .show():

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
****************
"""




"""
****************
18.
We have explored a couple of the questions about chocolate that inspired us when we looked at this chocolate table.

What other kinds of questions can you answer here? Try to use a combination of BeautifulSoup and Pandas to explore some more.

For inspiration: Where are the best cocoa beans grown? Which countries produce the highest-rated bars?
****************
"""

