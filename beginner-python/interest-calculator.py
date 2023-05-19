# This is equivalent to the "Hello World" starting point in most other langauges.

print('Interest Calculator')
amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
years = int(input('Duration (no. of years) ?'))
total = (amount * pow(1 + (roi/100), years))
interest = total - amount
print('\nInterest = %0.2f' %interest)

#Step-1:
#In the first line, we are calling the print() function to display an informational message. This is the same as printing like the “Hello, World!”.

#Step-2:
#In the next three lines, we are using the following variables to store the input provided by the user.
#The variable ‘amount’ represents the principal amount borrowed.
#Another one is the ‘roi,’ which represents the rate of interest levied on the principal amount.
#The next identifier is ‘years,’ which is the no. of years representing the borrowing period.
#Also, you must note here that we are using Python’s input() function to prompt the user to enter the values.
#Furthermore, you can observe that we’ve used Python’s conversion operators (int() and float()) in this code.
#int(value) -> It converts any value to a plain integer.
#float(value) -> It converts a value to a float type number.

#Step-3:
#In the fifth line of code, we are using a variable called “total” to store the result of a complicated assignment.
#The total -> It represents the total amount to be paid after the borrowing period.
#But this line is a little different from the previous ones.
#It is because the first line was an output statement, and the next three were the simple assignment operations.
#Here, in the fifth line of code, we are computing the total amount, including the Interest part.

#Step-4:
#In the sixth line, we are using Python’s subtraction operator (-) to calculate the interest amount.

#Step-5:
#Finally, there is a print statement displaying the interest amount. Since it is a float value, so the print() function will show the full number by default.
#Hence, we are using the floating-point format specifier “%0.2f” in print() function so that we can limit the printing up to two decimal points.