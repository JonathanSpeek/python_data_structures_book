# An employee's total weekly pay equals the hourly wage multiplied by the total number of regular hours plus an
# overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program
# that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee's total
# weekly pay.

hourly_wage = float(input('What is your hourly wage: '))
total_regular_hours = float(input('How many regular hours did you work: '))
total_overtime_hours = float(input('How many overtime hours did you work: '))


def calculate_pay(wage, hours):
    return wage * hours


def total_pay(regular, overtime):
    pay = regular + overtime
    print('Your total pay weekly pay will be ${pay}'.format(pay=pay))

total_pay(calculate_pay(hourly_wage, total_regular_hours), calculate_pay(hourly_wage, total_overtime_hours))
