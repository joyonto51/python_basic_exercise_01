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
    if hours > 40:
        pay = (40*rate)+((hours-40)*(rate*1.5))

    elif hours < 40:
        pay = (hours*rate)-((40-hours)*(rate*.5))

    else:
        pay = hours*rate

    return pay


try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate:'))
    pay = computepay(hours, rate)

    if pay:
        print('Pay: {:.2f}'.format(pay))

except:
    print("Error, please enter numeric input")