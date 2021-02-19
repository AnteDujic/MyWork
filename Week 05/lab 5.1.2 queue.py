# Program that puts 10 random numbers (0 - 100) into the queue and outputs them
    # It takes out numbers from the queue (from start) one at a time,
        # prints the current number and the rest of the queue

# Author: Ante Dujic

import random

queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range (0, numberOfNumbers):
    queue.append (random.randint (0, rangeTo))

while (len (queue) != 0):
    currentNumber = queue.pop (0)
    print ("Current number is {} and the remaining queue is {}" .format (currentNumber, queue))

print ("Queue is now empty!")