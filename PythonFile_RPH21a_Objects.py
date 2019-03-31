# First the classes must be imported from the file they exist in
from PythonFile_RPH21_Classes_Creation import ApolloMissions
from PythonFile_RPH21_Classes_Creation import ClassWithMethodExample

# This example creates objects (instances of the class ApolloMissions)

Apollo7 = ApolloMissions("Apollo_7", "Earth Orbit", "Wally Schirra", "Donn Eisele", "Walter Cunningham")
Apollo8 = ApolloMissions("Apollo_8", "Lunar Orbit", "Jim Lovell", "Bill Anders", "Frank Borman II")
Apollo9 = ApolloMissions("Apollo_9", "Earth Orbit", "James McDivitt", "David Scott", "Rusty Schweickart")
Apollo10 = ApolloMissions("Apollo_10", "Lunar Orbit", "Thomas Stafford", "John Young", "Eugene Cernan")
Apollo11 = ApolloMissions("Apollo_11", "Lunar Surface", "Neil Armstrong", "Buzz Aldrin", "Michael Collins")

print(Apollo7.destination)


# This example creates an object that includes it's own method

result_1 = ClassWithMethodExample(10, 32, "+")
result_1.my_calculator()

result_2 = ClassWithMethodExample(10, 3, "/")
result_2.my_calculator()
