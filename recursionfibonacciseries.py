def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2))
n_terms=int(input("enter n no of value")) 
if n_terms<=0:
    print("invalid input !please input a positive value")
else:
    print("fibonacci series:")
    for i in range(n_terms):
         print(recursive_fibonacci(i))
