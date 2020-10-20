"""
WHY USE MACHINE LEARNING?
Unsupervised Learning
Unsupervised Learning is a type of machine learning where the program learns the inherent structure of the data based on unlabeled examples.

Clustering is a common unsupervised machine learning approach that finds patterns and structures in unlabeled data by grouping them into clusters.

Some examples:

Social networks clustering topics in their news feed
Consumer sites clustering users for recommendations
Search engines to group similar objects in one cluster
For a quick preview, we will show you an example of unsupervised learning.

Instructions
1.
NYBD wants to determine how humans and cyborgs differ from each other in terms of:

The speed of recovering from wounds
Emotional intelligence (EQ)
Words per minute (WPM) reading speed
They have taken measurements of these things for the Neo York population and have plotted them on 3 axes.

Press run to see the clusters!
"""

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np 

from os.path import join, dirname, abspath
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

fignum = 1

# Plot the ground truth

fig = plt.figure(fignum, figsize=(4, 3))

ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

for name, label in [('Robots', 0),
                    ('Cyborgs', 1),
                    ('Humans', 2)]:
    ax.text3D(x[y == label, 3].mean(),
              x[y == label, 0].mean(),
              x[y == label, 2].mean() + 2, name,
              horizontalalignment='center',
              bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))

# Reorder the labels to have colors matching the cluster results

y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(x[:, 3], x[:, 0], x[:, 2], c=y, edgecolor='k')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

ax.set_xlabel('Time to Heal')
ax.set_ylabel('Reading Speed')
ax.set_zlabel('EQ')

ax.set_title('')
ax.dist = 12

plt.show()