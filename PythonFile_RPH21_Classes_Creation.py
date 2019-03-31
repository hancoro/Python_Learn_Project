# Classes can be thought of as a newly created data type
# the __init__ function is used to assign values to object properties
# self parameter is a reference to the current instance of the class


class MyFirstPythonClass:

    def __init__(self, string1, string2, num1, num2, bool1):
        self.firstString = string1
        self.secondString = string2
        self.numberOne = num1
        self.numberTwo = num2
        self.trueOrFalse = bool1


# Example classes of Apollo Missions


class ApolloMissions:

    def __init__(self, mission, destination, crew1, crew2, crew3):
        self.mission = mission
        self.destination = destination
        self.crew1 = crew1
        self.crew2 = crew2
        self.crew3 = crew3


# Classes can include there own methods/functions
# This example class initialises three variables and includes a function to calculate an answer.


class ClassWithMethodExample:

    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def my_calculator(self):
        if self.operator == "+":
            print(self.num1 + self.num2)
        elif self.operator == "-":
            print(self.num1 - self.num2)
        elif self.operator == "/":
            print(self.num1 / self.num2)
        elif self.operator == "*":
            print(self.num1 * self.num2)
        else:
            print("Invalid operator")
