
e=int(input("enter the investment amount:"))
y=int(input("enter the number of years:"))
r=int(input("enter the rate of interest:"))
print("_"*57)

gap="|"
fmt=f"{gap} {' Year':5s} {gap} {'Starting balance':16s} {gap} {' Interest':9s} {gap} {'Ending balance':13s} {gap}"
print(fmt)
print("_"*57)
sum=0
for i in range(1,y+1):
    print(gap,end=" ")
    print(f"{i:^5d} ", end="")
    print(gap,end=" ")
   
    h=e*(1+(r/100))**(i-1)
    print(f"{h:^16.2f}", gap,end="")
   
    t=(r*h)/100
    print(f"{t:^10.2f}",gap,end="" )
    
    k=e*(1+(r/100))**(i)
    print(f"{k:^15.2f}",gap)
    
    sum=sum+t
print("_"*57)
print("Total interest earn:","$",round(sum,2))
j=e*(1+(r/100))**y
print("Ending balance:","$",round(j,2))



    
    