"""

Autumn Terry
lab1.py
Finding an individual's monthly interest rate charge by first finding the average daily balance and then
multiplying it by the monthly interest.
I certify that this assignment is entirely my own work.

"""
def monthly_interest():

    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    print("Annual interest rate", annual_interest_rate)

    number_days_billing_cycle = eval(input("Enter the number of days in billing cycle: "))
    print("Number of days in billing cycle", number_days_billing_cycle)

    previous_net_balance = eval(input("Enter previous net balance: "))
    print("Previous net balance", previous_net_balance)

    payment_amount = eval(input("Enter payment amount: "))
    print("Payment amount", payment_amount)

    day_payment = eval(input("Enter day in billing cycle payment was made: "))
    print("Day payment was made", day_payment)

    step_1 = previous_net_balance * number_days_billing_cycle
    step_2 = payment_amount * (number_days_billing_cycle - day_payment)
    step_3 = step_1 - step_2
    avg_daily = step_3 / number_days_billing_cycle

    monthly_interest = (avg_daily) * ((annual_interest_rate / 100) / 12)
    print("Monthly interest rate $", monthly_interest)

