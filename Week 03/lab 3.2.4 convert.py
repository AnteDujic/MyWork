# Program that takes in a float amount of dollars and returns that absolute amount in cents
# Author: Ante Dujic


dollars = float (input ("Please enter amount in dollars: "))
absoluteDollar =  abs (dollars)

cent = round ((absoluteDollar * 100))

print ("That amount in cent is: {}" .format (cent))
