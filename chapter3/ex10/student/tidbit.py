"""
Author: Ashley Francis
Date written: 01/27/2025
Assignment: Module 02 Practice Exercise 3-10
This program is designed to calculate loan payments based on the
given credit plan conditions. The user will input the purchase price. The
program will display a table with a payment schedule for the length of
the loan."
"""

def print_payment_schedule(purchase_price):
    # Constants
    down_payment_percent = 0.10
    annual_interest_rate = 0.12
    monthly_payment_percent = 0.05
    
    # Calculate the down payment
    down_payment = purchase_price * down_payment_percent
    loan_amount = purchase_price - down_payment  # This is the amount to be financed
    
    # Calculate monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12
    
    # Monthly payment is 5% of the listed price
    monthly_payment = purchase_price * monthly_payment_percent
    
    # Initialize variables for the loop
    balance = loan_amount
    month_number = 1
    
    # Print table headers
    print(f"{'Month':<6} {'Balance Owed':<15} {'Interest Owed':<15} {'Principal Owed':<15} {'Payment':<10} {'Remaining Balance':<15}")
    
    # Loop to generate the payment schedule
    while balance > 0:
        # Calculate the interest owed for the current month
        interest_owed = balance * monthly_interest_rate
        
        # Calculate the principal owed for the current month
        principal_owed = monthly_payment - interest_owed
        
        # If the balance is less than the monthly payment, adjust the principal payment
        if principal_owed > balance:
            principal_owed = balance
        
        # Calculate remaining balance after the payment
        balance -= principal_owed
        
        # Print the results for the current month
        print(f"{month_number:<6} {balance + principal_owed:<15.2f} {interest_owed:<15.2f} {principal_owed:<15.2f} {monthly_payment:<10.2f} {balance:<15.2f}")
        
        # Increment the month counter
        month_number += 1

# Main program
purchase_price = float(input("Enter the purchase price: $"))
print_payment_schedule(purchase_price)
