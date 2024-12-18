def series1(N):
    if N==1:
        return N
    else:
        return str(N)+" "+str(series1(N-1))
n=int(input("enter n no of value:"))
print(" ",series1(n))
