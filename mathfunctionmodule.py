import Mymaths
a=int(input("enter first value"))
b=int(input("enter second value"))
print("addition is",Mymaths.addition(a,b))
print("substraction is",Mymaths.substraction(a,b))
print("multiplication is",Mymaths.multiplication(a,b))
print("division is",Mymaths.division(a,b))
print("modulus is",Mymaths.modulus(a,b))
print("power is",Mymaths.power(a,b))
print("absolute is",Mymaths.absolute(a))
print("square is",Mymaths.square(a,b))
print("cube is",Mymaths.cube(a,b))
a=3
for i in range(1, 11):
   print(a, 'x', i, '=', a*i)


