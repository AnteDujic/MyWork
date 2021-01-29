#Program that reads a number and adds one to it
#Author: Ante Dujic

number = int (input ("Please enter a number:"))         #We must convert the string that input returns to an int
newNumber = number + 1
print ("{} plus 1 is {}".format(number, newNumber))