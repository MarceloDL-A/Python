import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby("year").totalprod.mean().reset_index()

print(prod_per_year)

#reshape to one column contening many rows. Take the years
X = prod_per_year["year"].values.reshape(-1, 1)
print(X)


y = prod_per_year["totalprod"]
print(y)

plt.scatter(X, y)




"""
Create and Fit a Linear Regression Model
"""
regr = linear_model.LinearRegression()
regr.fit(X, y)

print("regr.coef_[0]: \n" + str(regr.coef_[0]))
print("regr.intercept_: \n" + str(regr.intercept_))

y_predict = regr.predict(X)
plt.plot(X, y_predict)
plt.show()



"""
Predict the Honey Decline
"""
nums = np.array(range(2013, 2051))
X_future = nums.reshape(-1, 1)
print(X_future)

future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()

"""
How much honey will be produced in the year 2050, according to this?
Ans.: [array([2050]), 186545.34494683146]
"""
print([X_future[37], future_predict[37]])





