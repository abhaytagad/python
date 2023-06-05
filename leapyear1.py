n=int(input("how many numbers you want to enter?:"))
L=[]
a=0
while a<n:
    d=int(input("enter the number:"))
    L.append(d)
    a+=1
    
    
print(L)

for i in L:
    if i%4==0 and (i%100)!=0 or i%400==0:
        print(f"the {i} is a leep year")
        
    else:
        print(f"the {i} is not a leep year")
        