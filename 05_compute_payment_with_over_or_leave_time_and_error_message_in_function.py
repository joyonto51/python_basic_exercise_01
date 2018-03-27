"""
Write a function named computepay that will take hours and rate per hour as input and will compute the total payment.  your program will give the employee 1.5 times the hourly rate for hours worked above 40 hours and will deduct the .5 times the hourly rate for hours less than 40.

Here your program will show an error message for non-numeric value of hours/rate. After showing the error message, the program will exit

Example 01:
Enter Hours: 45
Enter Rate: 10
Pay: 475.00

Example 02:
Enter Hours: 40
Enter Rate: 10
Pay: 400.00

Example 03:
Enter Hours: 39
Enter Rate: 10
Pay: 385

Example 04:
Enter Hours: 45
Enter Rate: nine
Error, please enter numeric input

"""


def computepay(hours, rate):
    pay = 0
    # your code here

    return pay


# take hours and rate as input
hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate:'))
pay = computepay(hours, rate)

if pay:
    print('Pay: {:.2f}'.format())
