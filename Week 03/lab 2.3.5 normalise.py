# Program that reads in a string and strips any leading or trailing spaces
# It also converts all the letters to lower case and outputs the lenght of the original string and the normalised one
# Author: Ante Dujic

rawString = input ("Please enter a string: ")
normalisedString = rawString.strip() .lower()

lenghtOfRawString = len (rawString)
lenghtOfNormalisedString = len (normalisedString)

print ("That String normalised is: {}" .format (normalisedString))
print ("We reduced that string from {} to {} characters" .format (lenghtOfRawString, lenghtOfNormalisedString))
