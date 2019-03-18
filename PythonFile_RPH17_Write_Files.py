
#  This will append to an existing file
Apollo_Crews = open("C:\\Users\\hancoro\\Documents\\PythonTutorialsAndInfo\\FileToBeAppendedByPython.txt", "a")
Apollo_Crews.write("\nAdding something to the bottom of the file")
Apollo_Crews.close()


#  This will overwrite an existing file
Apollo_Crews = open("C:\\Users\\hancoro\\Documents\\PythonTutorialsAndInfo\\FileToBeOverwittenByPython.txt", "w")
Apollo_Crews.write("\nOverwrite file")
Apollo_Crews.close()


#  This will create a new file if the file name does not exist already
Apollo_Crews = open("C:\\Users\\hancoro\\Documents\\PythonTutorialsAndInfo\\FileToBeCreatedByPython.txt", "w")
Apollo_Crews.write("This will be written to the new file")
Apollo_Crews.close()


#  This will create a new html file if the file name does not exist already
Apollo_Crews = open("C:\\Users\\hancoro\\Documents\\PythonTutorialsAndInfo\\FileToBeCreatedByPython.html", "w")
Apollo_Crews.write("<p>This is text for the html file</p>")
Apollo_Crews.close()
