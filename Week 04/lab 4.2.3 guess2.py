# Program that prompts the user to guess the number until the user gets the right one - UPDATED
# Author: Ante Dujic

numberToGuess = 30

guessNumber = int (input ("Guess the number: "))

while guessNumber != numberToGuess:
    print ("Wrong!")

    if guessNumber < numberToGuess:
        print ("{} is too low." .format (guessNumber))

    else:
        print ( "{} is too high." .format (guessNumber))

    guessNumber = int (input ("Guess the number again: "))
print ("Well done! The number was", numberToGuess)