import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]



# Make your chart here
#Using create_x, make the lists school_a_x and school_b_x which will determine where to put the bars for Middle School A and Middle School B along the x-axis.
#For school_a_x, use the following inputs to create_x:
#t = 2 # There are two sets of data: A and B
#w = 0.8 # We generally want bars to be 0.8
#n = 1 # A is first set of data
#d = 5 # There are 5 topics we're plotting
def creat_x(t, w, n, d):
  return [t*x + w*n for x in range(d)]
school_a_x = creat_x(2, 0.8, 1, 5)
school_b_x = creat_x(2, 0.8, 2, 5)


#Create a figure of width 10 and height 8.
plt.figure(figsize = (10, 8))

#Create a set of axes and save them to ax.
ax = plt.subplot()

#Plot a set of bars representing middle_school_a and a set representing middle_school_b next to each other on the same graph.
ax.bar(school_a_x, middle_school_a)
ax.bar(school_b_x, middle_school_b)

#Create a new list of x-values called middle_x, which are the values in the middle of school_a_x and school_b_x. This is where we will place the x-ticks with the name of disciplines
middle_x = [(a + b)/2.0 for a, b in zip(school_a_x, school_b_x)]

#Set the x-ticks to be the middle_x list.
ax.set_xticks(middle_x)

#Set the x-tick labels to be the list unit_topics.
ax.set_xticklabels(unit_topics)

#Create a legend, as shown in the final graph, that labels the first set of bars Middle School A and the second set of bars Middle School B.
plt.legend(["Middle School A", "Middle School B"])

#Create a title (“Test Averages on Different Units”), x-axis label (“Unit”), and y-axis label (“Test Average”).
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")

#Save your figure to a file called my_side_by_side.png.
plt.savefig("my_side_by_side.png")



plt.show()