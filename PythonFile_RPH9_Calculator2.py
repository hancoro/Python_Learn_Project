
# setting the input string to a float will make it usable in math functions
num1 = float(input("Enter first number : "))
operator = input("Enter operator : ")
num2 = float(input("Enter second number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

