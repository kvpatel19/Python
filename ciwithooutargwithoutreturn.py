principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", ci)
compound_interest()
 
