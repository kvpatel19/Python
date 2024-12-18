LST=[]
for v in range(0,5):
    data=int(input("enter number:"))
    LST.insert(v,data)
print("create list is:",LST)
#LST.get()
LST.insert(3,100)
print("modified list:",LST)
LST.remove(100)
print("modified list:",LST)
#LST.removeAt(2)
#print("modified list:",LST)
