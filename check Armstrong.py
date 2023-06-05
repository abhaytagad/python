n=int(input("enter the three digit number:"))
t=n
sum=0
while t>0:
    d=t%10
    sum+=d**3
    t//=10
if sum==n:
  print(f" {n} is a Armstrong number")
else:
  
  print(f" {n} is not a Armstrong number")
    
