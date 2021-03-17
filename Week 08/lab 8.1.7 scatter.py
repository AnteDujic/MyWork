# Program that makes a list called ages that has
    # the same number random values as salaries (21 - 65)
# Program makes scatter plot of this data
# Author: Ante Dujic

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed (1)
salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)
ages = np.random.randint (low=21, high=65, size = numberOfEntries)

plt.scatter (ages, salaries)

xpoints = np.array (range (1, 101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints, color = "r")

plt.title ("random plot")
plt.xlabel ("salaries")
plt.ylabel ("age")
plt.legend ()

plt.show ()
#plt.savefig ("prettier-plot.png")