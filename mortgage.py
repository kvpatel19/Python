import numpy as np
def calculate_mortgage(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**months) / ((1 + monthly_interest_rate)**months - 1)
    return monthly_payment
principal = 500000  
annual_interest_rate = 3.5  
years = 30 
monthly_payment = calculate_mortgage(principal, annual_interest_rate, years)
print(f"Monthly Mortgage Payment: Rs.{monthly_payment:.2f}")
