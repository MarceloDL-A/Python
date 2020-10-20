import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#Inspect the DataFrames using print and head:
##visits lists all of the users who have visited the website
##cart lists all of the users who have added a t-shirt to their cart
##checkout lists all of the users who have started the checkout
##purchase lists all of the users who have purchased a t-shirt
"""print (visits.head())
print (cart.head())
print (checkout.head())
print (purchase.head())"""

#Combine visits and cart using a left merge.
visits_cart = pd.merge(visits, cart, how = 'left')
#print(visits_cart)

#How long is your merged DataFrame? Ans: [2000 rows x 3 columns]
#2000 rows
visit_cart_rows = len(visits_cart)
#print(visit_cart_rows)

#How many of the timestamps are null for the column cart_time? Ans:  of total 2000
#What do these null rows mean? Ans: No purchase
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
#print(null_cart_times)


#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
#Note: To calculate percentages, it will be helpful to turn either the numerator or the denominator into a float, by using float(), with the number to convert passed in as input. Otherwise, Python will use integer division, which truncates decimal points.
print(float(null_cart_times)/visit_cart_rows)


#Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = pd.merge(cart, checkout, how = 'left')
#print(cart_checkout)
cart_checkout_rows = len(cart_checkout)
null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])
#(cart_checkout_rows)
#print(null_checkout_times)
print(float(null_checkout_times)/cart_checkout_rows)

#Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.
#Examine the result using print and head.
all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')
#print(all_data.head())


#What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_purchase = pd.merge(checkout, purchase, how = 'left')
#rows number
checkout_purchase_rows = len(checkout_purchase)
null_purchase_times = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(float(null_purchase_times)/checkout_purchase_rows)

#*************************
#Average Time to Purchase
#Using the giant merged DataFrame all_data that you created, let's calculate the average time from initial visit to final purchase. Start by adding the following column to your DataFrame:
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#Examine the results using print(all_data.time_to_purchase)
print(all_data.head())

#Calculate the average time to purchase using the following code: print(all_data.time_to_purchase.mean())
print(all_data.time_to_purchase.mean())
