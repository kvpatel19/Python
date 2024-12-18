s=0
for v in range(1,51):
    if v%2!=0:
        print(v,end=' ')
        s=s+v
average=s/25.0
print("sum is =",s)
print("average is =",average)
