# Program that tells if the input number is even or odd
# Author: Ante Dujic

number = int ( input ("Enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number" .format (number))
else:
    print ("{} is an odd number" .format (number))
