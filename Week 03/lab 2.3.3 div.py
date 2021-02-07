# Program that reads in two numbers and outputs integer answer and remainder
# Author: Ante Dujic

x = int (input ("Enter First number: "))
y = int (input ("Enter Number you want to devide by: "))

answer = x // y     # // gives the int division
remainder = x % y   # % gives the remainder

print ("{} devided by {} is {} with remainder {}" .format (x, y, answer, remainder))