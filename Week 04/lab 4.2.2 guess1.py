# Program that prompts the user to guess the number until the user gets the right one
# Author: Ante Dujic

numberToGuess = 30

guessNumber = int (input ("Guess the number: "))

while guessNumber != numberToGuess:
    print ("Wrong!")
    guessNumber = int (input ("Guess the number again: "))
print ("Well done! The number was", numberToGuess)