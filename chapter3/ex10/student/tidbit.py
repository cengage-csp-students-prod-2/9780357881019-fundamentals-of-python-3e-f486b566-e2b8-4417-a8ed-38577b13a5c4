"""
Author: Ashley Francis
Date written: 02/03/2025
Assignment: Module 02 Practice Exercise 3-10
This program is designed to calculate loan payments based on the
given credit plan conditions. The user will input the purchase price. The
program will display a table with a payment schedule for the length of
the loan."
"""

# Input
fltPurchasePrice = float(input("Enter the purchase price: "))

# Constants
ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12
DOWNPAYMENT_RATE = 0.10
TABLEFORMATSTRING = "{:<5}{:<18.2f}{:<18.2f}{:<18.2f}{:<18.2f}{:<18.2f}"

# Initialize
monthlyPayment = 0.05 * fltPurchasePrice
month = 1
balance = fltPurchasePrice - (fltPurchasePrice * DOWNPAYMENT_RATE)

# Output header
print(f"{'Month':<5}{'Starting Balance':<18}{'Interest to Pay':<18}{'Principal to Pay':<18}{'Payment':<18}{'Ending Balance':<18}")

# While loop to display payment details
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * MONTHLY_RATE

    principal = monthlyPayment - interest
    remaining = balance - monthlyPayment

    # Display payment details
    print(TABLEFORMATSTRING.format(month, balance, interest, principal, monthlyPayment, remaining))

    # Update balance and increment month
    balance = remaining
    month += 1

# Write your program here
