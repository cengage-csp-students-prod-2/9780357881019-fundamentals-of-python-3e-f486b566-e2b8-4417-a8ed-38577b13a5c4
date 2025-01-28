"""
Author: Ashley Francis
Date written: 01/27/2025
Assignment: Module 02 Practice Exercise 3-10
This program is designed to calculate loan payments based on the
given credit plan conditions. The user will input the purchase price. The
program will display a table with a payment schedule for the length of
the loan."
"""
def generate_payment_schedule(purchase_price):
    down_payment_percentage = 0.10
    annual_interest_rate = 0.12
    monthly_payment_percentage = 0.05
    down_payment = purchase_price * down_payment_percentage
    loan_amount = purchase_price - down_payment
    monthly_payment = purchase_price * monthly_payment_percentage
    balance = loan_amount
    print(f"{'Month':<6}{'Balance Owed':<15}{'Interest Owed':<15}{'Principal Owed':<20}{'Payment':<10}{'Remaining Balance':<20}")
    month = 1
    while balance > 0:
        interest_owed = balance * annual_interest_rate / 12
        principal_owed = monthly_payment - interest_owed
        if principal_owed > balance:
            principal_owed = balance
            monthly_payment = interest_owed + principal_owed
        balance -= principal_owed
        print(f"{month:<6}{balance + principal_owed:<15.2f}{interest_owed:<15.2f}{principal_owed:<20.2f}{monthly_payment:<10.2f}{max(0, balance):<20.2f}")
        month += 1
def main():
    purchase_price = float(input("Enter the purchase price: $"))
    generate_payment_schedule(purchase_price)
if __name__ == "__main__":
    main()