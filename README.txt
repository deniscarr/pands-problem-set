This Repository is made up of 10 solutions to problem: set pands-problem-set

Question 1: Write a program that asks the user to input any positive integer and outputs the
sum of all numbers between one and that number.
Simple question - read in number and loop until number is reached - adding the numbers to the total as you go


Question 2. Write a program that outputs whether or not today is a day that begins with the letter T.
Using datetime, read current day and check if first letter is "T"


Question 3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.
Loop from 1000 to 10000 - checking each number is divisible by 6 and not 12.


Question 4. Write a program that asks the user to input any positive integer and outputs the
successive values of the following calculation. At each step calculate the next value
by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
it by three and add one.

A more complicated program - it took quite a bit of trial and error before coming up with this algorithm:
Loop number until loop equals 1
if number is even number = number/2 - else number = (number * 3) + 1


Question 5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
Accept user input nuimber - loop through from 2 until number, if there is remainer 0 after division by the number - it is not prime.


Question 6. Write a program that takes a user input string and outputs every second word.
Request sentence from user - divide words into the array. Print every second word - by printing the word and resetting checker and repeat.


Question 7. Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.
Import the math package - which includes the math.sqrt method. Just pass the number into the format method and floating point number will be returned.


Question 8. Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
Import datetime package - get day part - find correct extension for day: st, nd, rd or th for the day. then print the rest of the date format


Question 9. Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.
Import sys package to work with the program arguments - then open file. Similar to Question 6. - print every second line beginning by printing line 1 and resetting checker and repeat.


Question 10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].
I didn't get to complete this question - but I indend on adding solution later.
