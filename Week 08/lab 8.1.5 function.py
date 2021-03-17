# Program that plots the function y = x^2
# Author: Ante Dujic

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array (range(1, 101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints)
plt.show ()
