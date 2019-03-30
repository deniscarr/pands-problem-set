# Program Name: primes.py
# Programmer: Denis Carr
# Date: March 2019

# request user for positive number - convert it to int and store in variable number
number = int(input("Please enter a positive integer: "))

# loop from 2 to number -1
for i in range(2,number):

    # if number is divisible, it is not prime
    if number % i==0:
        print("That is not a prime.")
        exit(0)
    # else it is a prime
	print("That is a prime.")