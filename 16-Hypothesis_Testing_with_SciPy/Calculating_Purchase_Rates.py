"""
ANALYZE FARMBURG'S A/B TEST
Calculating Purchase Rates
We need to help Brian determine whether or not there is a significant difference in the percent of users who purchased the upgrade package among groups A, B, and C.
"""
import codecademylib
import pandas as pd

df = pd.read_csv("clicks.csv")
print(df.head())

"""
Define a new column called is_purchase which is "Purchase" if click_day is not None and "No Purchase" if click_day is None. This will tell us if each visitor clicked on the Purchase link.
"""
df["is_purchase"] = df.click_day.apply(lambda x: "Purchase" if pd.notnull(x) else "No Purchase")
print(df.head())

"""
We want to count the number of users who made a purchase from each group. Use groupby to count the number of "Purchase" and "No Purchase" from each group. Save your answer to the variable purchase_counts."""
purchase_counts = df.groupby(["group", "is_purchase"]).user_id.count().reset_index()

"""
Examine purchase_counts using print.
"""
print purchase_counts














