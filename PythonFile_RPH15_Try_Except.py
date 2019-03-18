'''
This is the equivalent to a try catch in c#
it is also possible to specify exceptions for different error types
'''

try:
    number = int(input("Please enter a number: "))
    print(number)
    number_error = 10/0  # This has been added to create an intentional error
except ValueError:
    print("Entry was not a number")
except ZeroDivisionError as err:
    print("There was a divide by zero error")  # this will print my error message
    print(err)  # this will capture the error type

