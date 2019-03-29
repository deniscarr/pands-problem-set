# Program Name: divisors.py
# Programmer: Denis Carr
# Date: March 2019

# loop will continue from 1000 to 10000
for num in range(1000,10001):

    # if number is divisible by 6 but (AND) not by 12 - print on screen, otherwise ignore
    if num%6==0 and num%12!=0:
        print(num)