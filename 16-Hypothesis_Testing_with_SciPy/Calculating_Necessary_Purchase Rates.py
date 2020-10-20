"""
ANALYZE FARMBURG'S A/B TEST
Calculating Necessary Purchase Rates
Your day is a little less busy than you expected, so you decide to ask Brian about his test.

You: Hey Brian! What was that test you were running anyway?

Brian: It was awesome! We are trying to get users to purchase a small FarmBurg upgrade package. It's called a microtransaction. We're not sure how much to charge for it, so we tested three different price points: $0.99, $1.99, and $4.99. It looks like significantly more people bought the upgrade package for $0.99, so I guess that's what we'll charge.

You: Oh no! I should have asked you this before we did that chi-squared test. I don't think that this was the right test at all. It's true that more people wanted to purchase the upgrade at $0.99; you probably expected that. What we really want to know is if each price point allows us to make enough money that we can exceed some target goal. Brian, how much do you think it cost to build this feature?

Brian: Hmm. I guess that we need to generate a minimum of $1000 per week in order to justify this project.

You: We have some work to do!
"""
import codecademylib
import pandas as pd

df = pd.read_csv('clicks.csv')
print("df: " + str(df.head()))

"""
How many visitors came to the site this week? Save your answer to num_visits.
"""
num_visits = len(df)
print("num_visits by week: " + str(num_visits))

"""
Let's assume that num_visits is how many visitors we generally get each week. Given that, calculate the percent of visitors who would need to purchase the upgrade package at each price point ($0.99, $1.99, $4.99) in order to generate Brian's target of $1,000 per week.

Save the results to:

p_clicks_099
p_clicks_199
p_clicks_499
Note that for higher price points, you'll need to sell fewer upgrade packages in order to meet your target.
"""
p_clicks_099 = (1000/0.99)/num_visits
print("p_clicks_099 = " +str(round(100.0*p_clicks_099, 4)) + "% is the percent of visitors who would need to purchase the upgrade package in order to generate Brian's target of $1,000 per week." )
p_clicks_199 = (1000/1.99)/num_visits
p_clicks_499 = (1000/4.99)/num_visits
print("p_clicks_199 = " +str(round(100.0*p_clicks_199, 4)) + "% of visitors who would need to purchase")
print("p_clicks_499 = " +str(round(100.0*p_clicks_499, 4)) + "% of visitors who would need to purchase" )




















