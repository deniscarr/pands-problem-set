# Program Name: sumupto.py
# Programmer: Denis Carr
# Date: March 2019

# request number to be used as final (sumupto) number
number = int(input("Please enter a positive number: "))

# variable total will contain the final sum
total = 0

# go from 1 to number entered by user adding each number to total
for i in range(1,number+1):
    total +=i    

# print the total sum of numbers
print(total)