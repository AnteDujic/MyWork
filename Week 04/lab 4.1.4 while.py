# Program that asks to input numbers until -1 is entered
# Author: Ante Dujic

number = int ( input ("Enter an integer: "))

while number != -1:
    number = int (input ("Enter an integer again: "))
    
print ("You entered -1")
