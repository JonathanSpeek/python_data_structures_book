# The TidBit Computer Store has a credit plan for computer purchases. There is a
# 10% down payment and an annual interest rate of 12%. Monthly payments are 5%
# of the listed purchase price minus the down payment. Write a program that takes
# the purchase price as input. The program should display a table, with appropriate
# headers, of a payment schedule for the lifetime of the loan. Each row of the table
# should contain the following items:
# - The month number (beginning with 1)
# - The current total balance owed
# - The interest owed for that month
# - The amount of principal owed for that month
# - The payment for that month
# - The balance remaining after payment
# The amount of interest for a month is equal to balance * rate / 12. The amount of
# principal for a month is equal to the monthly payment minus the interest owed.

purchase_price = int(input('How much does the computer cost: '))
down_payment = round(purchase_price * 0.10, 2)
monthly_payment = round((purchase_price - down_payment) * 0.05, 2)
current_balance = purchase_price
months = 0

print('Months | Current Bal. | Interest | Principal | Payment | Balance')
while current_balance > 0:
    initial_balance = round(current_balance, 2)
    months += 1
    monthly_interest = round(current_balance * (0.12 / 12), 2)
    monthly_principal = round(monthly_payment - monthly_interest, 2)
    current_balance -= monthly_principal
    print('{m} | {cb} | {i} | {p} | {pay} | {b}'.format(m=months,
                                                        cb=initial_balance,
                                                        i=monthly_interest,
                                                        p=monthly_principal,
                                                        pay=monthly_payment,
                                                        b=round(current_balance, 2)
                                                        )
          )
