
'''
files can be opened using the open command

file can be opened in a few modes
r = read
w = write
a = append
r+ = read and write
'''


Apollo_Crews = open("C:\\Users\\hancoro\\Documents\\PythonTutorialsAndInfo\\FileToBeReadInByPython.txt", "r")

print(Apollo_Crews.readable())  # This will return true if the file is readable
# print(Apollo_Crews.read())  # reads the full file
# print(Apollo_Crews.readline())  # reads a single line
# print(Apollo_Crews.readlines())  # reads all lines into a list
# print(Apollo_Crews.readlines()[6])  # This will read out a line of the file based on index

# files can also be read in a for loop
for astronauts in Apollo_Crews.readlines():
    print(astronauts)

Apollo_Crews.close()  # closes the file
