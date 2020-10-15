"""
ANALYZE FARMBURG'S A/B TEST
Getting Familiar with FarmBurg
Brian is a Product Manager at FarmBurg, a company that makes a farming simulation social network game. In the FarmBurg game, you can plow, plant, and harvest different crops.

Today, you will be acting as Brian�s data analyst for an A/B Test that he has been conducting.

Brian tells you that he ran an A/B test with three different groups: A, B, and C. You�re kind of busy today, so you don�t ask too many questions about the differences between A, B, and C. Maybe they were shown three different versions of an ad. Who cares?

(HINT: you will care later)

Brian gives you a CSV of results called clicks.csv. It has the following columns:

user_id: a unique id for each visitor to the FarmBurg site
ab_test_group: either A, B, or C depending on which group the visitor was assigned to
click_day: only filled in if the user clicked on a link to purchase
"""
"""
Start by importing pandas as pd. You�ll be using this module for most of this project.
"""
import codecademylib
import pandas as pd

"""
Load clicks.csv into the variable df.
"""
df = pd.read_csv("clicks.csv", delimiter = ",")

print(df.head())