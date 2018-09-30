"""
Write a program that will take hours and rate per hour as input and will compute the total payment.
Here your program will give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Example:
Enter Hours: 45
Enter Rate: 10
Pay: 475.00

"""

# take hours and rate as input
hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate:'))

if hours > 40:
    pay = (40*rate)+((hours-40)*(rate*1.5))
else:
    pay = hours*rate

print('Pay: {:.2f}'.format(pay))
