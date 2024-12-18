f=open("bcam-5.txt","w")
data=input("enter your data of string:")
f.write(data)
f.close()

f=open("bcam-5.txt","r")
print(f.read())
f.close()
print("data read successfully...")
