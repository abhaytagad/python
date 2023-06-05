print("enter the number ")
a= int(input())
flag=False
for i in range(2, a):
    
    if (a%i)==0 : 
        flag=  True
        break
if flag:
    print(a,"  is not prime")   
else:
    print(a, " is  a prime")     