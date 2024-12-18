LST1=[1,2,3,4,5,6,7,8,9,0]
LST2=['a','b','c','d','e']
print("first list data:")
print("*"*40,end='\n')
for v in LST1:
    print(v,end=' ')
print("\n second list data")
print("*"*40,end='\n')
for v in LST2:
    print(v,end=' ')
LST1.append(30)
print("first list data using index")
print("*"*40,end='\n')
for v in range(0,len(LST1)):
    print(LST1[v],end=' ')
LST1.reverse()
print("\n reverse list :",LST1)
