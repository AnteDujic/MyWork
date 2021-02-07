# Program that rounds a number
    # !!! Do not use it accuracy is essential (4.5 rounds to 4, 5.5 rounds to 6) !!!
# Author: Ante Dujic

numberToRound = float (input ("Enter a float number: "))
roundedNumber = round (numberToRound)

print ("{} rounded is {}" .format (numberToRound, roundedNumber))