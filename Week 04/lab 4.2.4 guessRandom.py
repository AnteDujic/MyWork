# Program that generates a random number to guess
    # Prompts the user to guess until the user gets it
# Author: Ante Dujic

import random

numberToGuess = random.randint (0, 100)

guessNumber = int (input ("Guess the number between 0 and 100: "))

while guessNumber != numberToGuess:
    if guessNumber < numberToGuess:
        print ("{} is too low." .format (guessNumber))
    else:
        print ("{} is too high." .format (guessNumber))

    guessNumber = int (input ("Guess the number between 0 and 100 again: "))

print ("Well done. {} is the correct number" .format (guessNumber))

