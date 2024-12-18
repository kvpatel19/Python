def fib(n):
    """assumes n is an  int>0
returns fibbonacci of n"""
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter number of terms"))
print("fibonacci sequence")
for i in range(n):
    print(fib(i))

        
