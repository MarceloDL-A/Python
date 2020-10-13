"""
LEARN STATISTICS WITH PYTHON
Healthcare in Different States
In this project, we will use boxplots to investigate the way hospitals in different states across the United States charge their patients for medical procedures.

This dataset might look a bit familiar to you � we used it in our lesson about describing histograms. The data originally came from the United State Health and Human Services Department (https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/97k6-zzx3).

Let�s use boxplots to find more meaning in this data!
"""

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
print(healthcare.head())

"""
1.
We�ve imported the dataset into a variable named healthcare. Let�s take a look at what data we have to work with. Print healthcare.head(). This will print the first five rows of the dataset.

Scroll through the table to see what information we have. We know that we want to eventually look at the way heathcare works in different states. What column will be useful to do that?

Note that we�re going to ask you to print out multiple values over the course of the project. Feel free to comment out old print statements using # to avoid clutter:

# This is a comment

"""

"""
We�re going to focus on only the ways in which hospitals charge patients for chest pain. But you could do this for any of the diagnoses in our dataset. Print healthcare["DRG Definition"].unique() to see all of the different diagnoses in our dataset.

Can you find the official name of the diagnosis related to chest pain?
"""
print(healthcare["DRG Definition"].unique())

"""
Let�s grab only the rows in the dataset that are about chest pain. Use this line of code to do that.

chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
If you�re interested in investigating a different diagnosis, replace '313 - CHEST PAIN' with the name of the other diagnosis. You might want to change the new variable name to be something other than chest_pain if you do this!
"""
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
print(chest_pain)

"""
Separating By State

We now want to separate the dataset by state. Eventually, we�ll use a for loop to do this for every state, but for now, let�s prove to ourselves that we can make a boxplot for one state.

When we printed the head, we saw the first few rows had a 'Provider State' of "AL". Those were hospitals in Alabama.

To get every chest pain diagnosis in Alabama, use this line of code:

alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]
Make sure to use the variable that you created in the previous step. We called it chest_pain, but you might have named it something else if you used a different diagnosis.

Again, feel free to use a state of your choosing instead of Alabama. Different state abbreviations should work, like "CO" or "NY". Name your variable appropriately!
"""
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]

"""
We�re almost there! We now have all of the hospitals in Alabama that have a diagnosed chest pain. We now want to find the average cost of those diagnoses. These value is stored in the column ' Average Covered Charges ' (Note the spaces at the start and the end of the string!)

To get only these values, call this line of code:

costs = alabama_chest_pain[' Average Covered Charges '].values
Again, make sure that you�re using the correct variable names � yours might be different.
"""
costs = alabama_chest_pain[' Average Covered Charges '].values

"""
Let�s now make a boxplot of those values! Call plt.boxplot() using costs as the first parameter.

Then call plt.show() to see your boxplot!
"""
#plt.boxplot(costs)
#plt.show()

"""
Making a Boxplot for All States
ice work! We�ve made a boxplot for one state. But how does that state compare to the others? Let�s make a boxplot for every state! Comment out (or delete) the two lines of code you just wrote to make the boxplot.

To begin, we first need to create a list of all the states in our dataset. We can once again use the unique() function. We used this function when we looked at all of the diagnoses.

Find all of the unique states from the dataset chest_pain and store it in a variable named states.
"""
states = chest_pain["Provider State"].unique()

"""
We�ll now use a for loop to separate the dataset into a dataset for each state:

datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)
datasets now contains 50 datasets � one for each state.
"""
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

"""
We�re about to draw 50 boxplots. Before we draw them, let�s make sure there�s enough room. Call plt.figure(figsize=(20,6)). This will make your figure long to allow room for so many boxplots!
"""
plt.figure(figsize=(20,6))

"""
Draw the boxplot using datasets as the first parameter. Add the second parameter labels = states to label your boxplots.

Finally, make sure to call plt.show().
"""
plt.boxplot(datasets, labels = states)
plt.show()

"""
Interpret and Explore
Nice work! You should now see 50 boxplots. If the graph is too small to see, you can expand it by clicking on the arrows in the top right corner of the right panel. You can also take a look at this image to see what your final results should look like.

What information have you learned by looking at these boxplots side by side? What state has the largest spread? What state has the largest median? Which states have the most outliers?

Hint:
If looks like California, New Jersey, and Florida have the largest spreads. Vermont has almost no spread.

The state with the largest median cost for a chest pain diagnosis is New Jersey. The state with the smallest median cost is Maryland.

California, Georgia, and Tennessee all have a fair number of outliers.


Take some time to explore more from here. Here are some ways in which you can investigate the data more:

Look at diagnoses other than '313 - CHEST PAIN'.
Group states by regions. Maybe hospitals in the Northeast charge patients differently than hospitals in the South.
Plot something other than ' Average Covered Charges '. You have data about how much Meidcare pays in the 'Average Medicare Payments' column.
"""



