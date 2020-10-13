"""
LEARN STATISTICS WITH NUMPY
Betty's Bakery
Betty has always used her grandmother's recipe book to make cookies, cakes, pancakes, and bread for her friends and family. She's getting ready to open a business and will need to start buying all of her milk, eggs, sugar, flour, and butter in bulk.

Help Betty figure out how much she needs to buy using NumPy arrays describing her recipes.

If you get stuck during this project or would like to see an experienced developer work through it, click "Get Help" to see a project walkthrough video.
"""
"""
Reading Recipes
1.
Start by importing NumPy as np.
"""
import numpy as np

"""
All of Betty's recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:

Flour	Sugar	Eggs	Milk	Butter
2 cups	0.75 cups	2 eggs	1 cups	0.5 cups
Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for "2 cups"). Save this array as cupcakes.
"""
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

"""
Betty's assistant has compiled all of her recipes into a csv (comma-separated variable) file called recipes.csv. Load this file into a variable called recipes.
"""
recipes = np.genfromtxt("recipes.csv", delimiter = ",")

"""
Display recipes using print.

Each row represents a different recipe. Each column represents a different ingredient.
"""
print(recipes)

"""
The 3rd column represents the number of eggs that each recipe needs.

Select all elements from the 3rd column and save them to the variable eggs.
"""
eggs = recipes[:, 2]

"""
Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs.
"""
print([eggs == 1])
cupcakes = recipes[:, 0]
cookies = recipes[:, 2]
print("cupcakes: " + str(cupcakes))
print("cookies: " + str(cookies))

"""
Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch.
"""
double_batch = recipes[:, 0]*2
print("double_batch: " + str(double_batch))

"""
Create a new variable called grocery_list by adding cookies and double_batch.
"""
grocery_list = cookies + double_batch
print("grocery_list: " + str(grocery_list))




