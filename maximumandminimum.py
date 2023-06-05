L=[]
n=int(input("how many numbers you want to enter?:" ))
a=0
while a<n:
   b=float(input("enter the number : "))
    
   L.append(b)
   a=a+1
print(L)

print("the maximum number is :",max(L))
print("the minimum number is :",min(L))