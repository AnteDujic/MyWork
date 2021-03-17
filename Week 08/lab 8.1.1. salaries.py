# Program that makes a list with 10 random numbers (20000 - 10000)
# Author: Ante Dujic

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)

print (salaries)