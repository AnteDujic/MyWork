# Program that makes a pie chart of the counties listed
# Author: Ante Dujic

import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ("Mayo", "Galway", "Limerick", "Cork", "Dublin")
counties = np.random.choice (
    possibleCounties,
    p = (0.1, 0.2, 0.3, 0.15, 0.25),
    size = (100)
)
unique, counts = np.unique (counties, return_counts = True)

# plt.pie (counts, labels = unique)
plt.bar (unique, counts)

plt.show()