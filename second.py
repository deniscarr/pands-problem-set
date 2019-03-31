# Program Name: second.py
# Programmer: Denis Carr
# Date: March 2019

# Add sys package to program
import sys
# store program arguments (sys.argv) in arguments
arguments = sys.argv[1:]

# get file name from command line arguments - array index 0
fileName = arguments[0]

# open the file specified as program argument
with open(fileName) as fp:  
    # read line from file
	line = fp.readline()

    # this will decide whether to print this line or not - printThis is set to True: so 1st line will be printed
    printThis = True
	# read the lines in the file until the end of the file
    while line:
    # we have to print this line
    if printThis:
	# print the line in the file to the screen
       print(line.strip())   
	   # As we have printed a line - reset printThis
       printThis = not printThis
       # read line from file
       line = fp.readline()
