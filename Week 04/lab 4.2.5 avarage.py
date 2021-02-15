# Program that reads in numbers until the user enters 0
    # It prints out all the inputted numbers and gives avarage of them
# Author: Ante Dujic

numbers = []    # creates a list

number = int (input ("Enter a number (0 to quit): "))

while number != 0:
    numbers.append (number)     # adding to the list
    number = int (input ("Enter a next number (0 to quit): "))

for value in numbers:       # listing inputted numbers
    print (value)

avarage = float ( (sum (numbers)) / len (numbers))
print ("The avarage of inputted numbers is ", avarage)