# The Payroll Department keeps a list of employee information for each pay period
# in a text file. The format of each line of the file is
# <last name> <hourly wage> <hours worked>
# Write a program that inputs a filename from the user and prints a report to the
# terminal of the wages paid to the employees for the given period. The report
# should be in tabular format with the appropriate header. Each line should contain
# an employee’s name, the hours worked, and the wages paid for that period.

payroll_file = open('project_6.txt', 'r')

print('Name\tWage\tHours\tPay')
for row in payroll_file:
    person = row.split('\t')
    last_name = person[0]
    wage = float(person[1])
    hours = int(person[2][:-2])
    pay = round(wage * hours, 2)
    print('{name}\t{wage}\t{hours}\t{pay}\n'.format(name=last_name, wage=wage, hours=hours, pay=pay))
