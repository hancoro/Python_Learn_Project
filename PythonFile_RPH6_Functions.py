
# Functions are defined using 'def name_of_function():'


def my_first_python_funtion():
    print("This function has been called")


# Functions are called as follows
my_first_python_funtion()


# Functions with parameters


def python_function_with_parameters(param1, param2, param3):
    print(param1 + "\n" + param2 + "\n" + str(param3))


# calling a python function with parameters
python_function_with_parameters("Parameter passed to the function", "Second parameter passed to function", 42)


# Function with return
# this example returns a number raised to the power of another
def python_function_with_return(number, power):
    return pow(number, power)


# calling the function and using the return
print(python_function_with_return(3, 3))
