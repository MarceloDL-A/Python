"""
STATISTICAL DISTRIBUTIONS WITH NUMPY
Binomial Distributions and Probability
Let's return to our original question:

Our basketball player has a 30% chance of making any individual basket. He took 10 shots and made 4 of them, even though we only expected him to make 3. What percent chance did he have of making those 4 shots?

We can calculate a different probability by counting the percent of experiments with the same outcome, using the np.mean function.

Remember that taking the mean of a logical statement will give us the percent of values that satisfy our logical statement.

Let's calculate the probability that he makes 4 baskets:

a = np.random.binomial(10, 0.30, size=10000)
np.mean(a == 4)
When we run this code, we might get:

>> 0.1973
Remember, because we're using a random number generator, we'll get a slightly different result each time. With the large *size we chose, the calculated probability should be accurate to about 2 decimal places.*

So, our basketball player has a roughly 20% chance of making 4 baskets.

This suggests that what we observed wasn't that unlikely. It's quite possible that he hasn't got any better; he just got lucky.
"""
import numpy as np
emails = np.random.binomial(500, 0.05, size=10000)

"""
Let's return to our email example. Remember that we sent 500 emails, with an estimated probability that 25 people would open the email. There were 10,000 trials.

What is the probability that no one opens the email? Save the results to the variable no_emails.
"""
no_emails = np.mean(emails == 0)
print("no_emails: " + str(no_emails))

"""
You recently hired a new marketing associate who wants to A/B test two emails to see if people respond better. What's the probability that 8% or more of people will open the email? Save the results to the variable b_test_emails.
"""
b_test_emails = np.mean(emails >= 40)
print("b_test_emails: " + str(b_test_emails))


