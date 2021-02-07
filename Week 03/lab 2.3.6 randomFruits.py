# Program that prints out a random fruit
# Author: Ante Dujic

import random

fruits = ["Apple", "Orange", "Banana", "Pear"]

# We want a random number between 0 and length-1
index = random.randint (0, (len(fruits)-1))

fruit = fruits [index]
print ("A random fruit is: {}" .format (fruit))