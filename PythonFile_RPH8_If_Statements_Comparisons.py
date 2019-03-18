# using comparison operators ==, !=, >=, <=, in

# Compare numbers function


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(7, 4, 5))


# it is also possible to check if character exists in a string
test_string = "this will check if the character X exists in the string"
if "x" in test_string.lower():
    print("X was defected")
