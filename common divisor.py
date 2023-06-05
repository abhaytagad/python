n=int(input("enter the number:"))
b=int(input("enter the number:"))
if n>b:
    for i in range(1,b):
        if b%i==0 and n%i==0:
            print("smallest common divisor:",i,end=" ,")
            break
    for j in range(b,1,-1):
        if b%j==0 and n%j==0:
            print("greatest common divisor:",j)
            break          
            break
else:
    for i in range(1,n):
        if b%i==0 and n%i==0:
            print("smallest common divisor:",i,end=" ,")
            break
    for j in range(n,1,-1):
        if b%j==0 and n%j==0:
            print("greatest common divisor:",j)
            break          