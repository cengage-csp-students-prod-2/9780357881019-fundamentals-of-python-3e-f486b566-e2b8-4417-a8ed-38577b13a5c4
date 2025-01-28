"""
Author: Ashley Francis
Date written: 01/27/2025
Assignment: Module 02 Practice Exercise 3-10
This program is designed to calculate loan payments based on the
given credit plan conditions. The user will input the purchase price. The
program will display a table with a payment schedule for the length of
the loan."
"""
def payment_schedule(purchase_price):
    down_payment = purchase_price * 0.10
    annual_interest_rate = 0.12
    monthly_payment = (purchase_price * 0.05) - down_payment
    total_balance = purchase_price - down_payment

    print(f"{'Month':<10}{'Total Balance':<20}{'Interest Owed':<20}{'Principal Owed':<20}{'Payment':<20}{'Remaining Balance':<20}")
    
    month = 1
    while total_balance > 0:
        interest_owed = total_balance * (annual_interest_rate / 12)
        principal_owed = monthly_payment - interest_owed
        remaining_balance = total_balance - principal_owed
        
        if remaining_balance < 0:
            principal_owed += remaining_balance
            remaining_balance = 0
        
        print(f"{month:<10}{total_balance:<20.2f}{interest_owed:<20.2f}{principal_owed:<20.2f}{monthly_payment:<20.2f}{remaining_balance:<20.2f}")
        
        total_balance = remaining_balance
        month += 1

if __name__ == "__main__":
    purchase_price = float(input("Enter the purchase price: "))
    payment_schedule(purchase_price)