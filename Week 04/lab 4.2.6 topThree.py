# Program that generates 10 numbers in a range 0 - 100
    # It prints them all out and then prints top 3
# Author: Ante Dujic (to be reviewed)

import random


howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100

numbers = []

for i in range(0,10):
 numbers.append(random.randint(rangeFrom,rangeto))

print ("{} random numbers\t {}".format(howMany,numbers))

topOnes = numbers.copy()
topOnes.sort(reverse = True)

print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))


