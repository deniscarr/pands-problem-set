# Program Name: squareroot.py
# Programmer: Denis Carr
# Date: March 2019

#import math package for square root calculation
import math

# Request number from user, onvert to float type and store in variable number 
number = float(input("Please enter a positive number: "))

# print the number and the square root of the number 
print("The square root of {0:.1f} is approx. {1:.1f}.".format(number,math.sqrt(number)))