# Program that prints out a random number between two given numbers
# Author: Ante Dujic

import random

x = int (input ("Set the start of the range: "))
y = int (input ("Set the end of the range: "))

number = random.randint (x, y)

print ("Here is a random number between {} and {}: {}" .format (x, y, number))