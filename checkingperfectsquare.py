import math as m

a=int(input("enter the number:"))
k=m.sqrt(a)

d=k//1

if k-d==0:
    print(1)
else:
    print(0)