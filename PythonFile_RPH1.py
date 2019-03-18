print("Hello World")
# This is a comment

'''
This is also a comment
on multiple lines
'''

# These are how to declare variables
my_first_string_variable = "Variable - No need to declare data type"
my_first_any_number_var = 3.14
my_first_boolean = True

# These are some basic print statements
print(my_first_string_variable)
print("This is a concatenation of text plus  - " + my_first_string_variable)
print("This is how to write on\na new line")
print("This is how to use an escape character \" and include it in the output")

# These are some string functions
print("this will all be set to upper case".upper())
print("This will return false if there are any uppercase characters".isupper())
print(len("This will return the length of a string"))
print("This is how to return and string character from index"[3])
print("This is how to return the index of a selected character".index("r"))
print("This is how to return the start index of selected characters".index("start"))
print("This is how to replace characters".replace("characters", "replacement text"))
print(str(1701) + " - The str(1701) coverts the number to a string")


# Working with numbers
print(-1976)
print(2 + 2)
print(2 * 3)
print(12 / 2)
print(10 - 5)
print(10 % 3)  # This is a modulus calculation that returns the remainder of a division
print(abs(-20))  # The abs returns absolute value of the number
print(pow(3, 2))  # This pow() function raises one number to the power of another
print(3**2)  # This does the same as pow
print(max(100, 42))  # Returns higher value
print(min(100, 42))  # Returns lower value
print(round(6.6666666))  # This rounds to an integer

# More math functions when importing library
from math import *

print(floor(3.7))
print(ceil(3.7))
print(sqrt(9))  # This is the square root


