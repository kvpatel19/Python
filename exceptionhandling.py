try:
    first=int(input("enter first number:"))
    second=int(input("enter second number"))
    print("division is"(first/second))
except Exception as e:
    print("OOPS...there is something wrong")
    print(e)
