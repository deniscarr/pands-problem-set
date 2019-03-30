# Program Name: secondstring.py
# Programmer: Denis Carr
# Date: March 2019

# request user to enter a text sentence and save it to string varibale input
string = input("Please enter a sentence: ")

# make an array from this string - by spliting the sentence into separate words
data = string.split()

# logic test variable - this will decide whether to print this word or not
printThis = True

# go through each word
for word in data:
    # Print every secord "word" in array data - if printThis is True
    if printThis:
        print(word, end=" ")
	# reset logic test variable printThis to False
    printThis = not printThis
        print("")