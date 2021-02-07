# Program that gives an absolute of a number
# Author: Ante Dujic

# In the question, Number is ambigious but the output implies that we should be dealing with floats
# So, I'm casting the input to a float

number = float (input ("Enter a number: "))
absoluteValue = abs (number)

print ("The absolute value of {} is {}" .format (number, absoluteValue))