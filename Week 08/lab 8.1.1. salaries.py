# Program that makes a list with 10 random numbers (20000 - 10000)
# Author: Ante Dujic

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed (1)
salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000
salariesMult = salaries * 1.05
newSalaries = salariesMult.astype (int)

print (salaries)
print (salariesPlus)
print (salariesMult)
print (newSalaries)