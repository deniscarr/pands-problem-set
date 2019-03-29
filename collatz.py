# Program Name: collatz.py
# Programmer: Denis Carr
# Date: March 2019

# request number from user to be used as final (collatz) number and convert to int
number=int(input("Please enter a positive integer: "))

# loop to continue infinitely till number is 1 | Python's print() function comes with a parameter called 'end'. By default, the value of this parameter is '\n', i.e. the new line character. You can end a print ...
while True:
    print(number, end=" ")

    # if number is 1, end (break) loop
    if number==1:
        break

    # if number iseven number = number/2
    # else number = (number * 3) + 1
    number = int(number / 2 if number % 2 == 0 else (number*3)+1)
print("") 