import math

x = int(input("Enter a positive number: "))

try:
    print('Square root of', x, 'is', math.sqrt(x))
except ValueError as ve:
    print("Please enter a valid positive number")



#OUTPUT
 #Enter a positive number: 2
 #Square root of 2 is 1.4142135623730951
 
 #Enter a positive number: -2
 #Please enter a valid positive number
