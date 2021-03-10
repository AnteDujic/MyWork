# Program that counts how many times it was run
# Author: Ante Dujic

#a) Reading in a number from a file
filename = "count.txt"

def readNumber ():
    with open (filename) as f:
        number = int (f.read())
        return number
    

#b) Taking in a number and overwriting a file with that number
def writeNumber (number):
    with open (filename, "wt") as f:
        f.write (str(number))

#c) Counting how many times program has been run
num = readNumber()
num += 1

print ("We have run this program {} times" .format (num))
writeNumber (num)