
# set a boolean variable as true
boolean_for_if_statement = False
second_boolean_for_if_statement = False

# If statement with one condition
if boolean_for_if_statement:
    print("One condition if statement HAS been met")
else:
    print("One condition if statement was NOT met")

# If statement with multiple conditions
if boolean_for_if_statement and second_boolean_for_if_statement:
    print("Both conditions have been met")
else:
    print("Both conditions were not met")

# If statement with multiple conditions
if boolean_for_if_statement or second_boolean_for_if_statement:
    print("One conditions has been met")
else:
    print("Neither conditions were met")

# If statement where a condition is not equal and else if
if boolean_for_if_statement and second_boolean_for_if_statement:
    print("Both conditions has been met")
elif not boolean_for_if_statement and not second_boolean_for_if_statement:
    print("Neither condition has been met")
else:
    print("one of the conditions was met")
