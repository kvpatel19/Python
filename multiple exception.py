try:
    first=int(input("enter first number:"))
    second=int(input("enter second number"))
    print("division is"(first/second))
except IOError:
    print("invalid proper data..")
except ZeroDivisionError:
    print("zero not divided by value..")
except Exception as e:
    print("error is:",e)
finally:
    print("thank you for executing code..")
    
