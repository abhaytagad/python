n=int(input("how many elements you want to enter?:"))
L=[]

a=0
while a<n:
    d=int(input("enter the element:"))
    L.append(d)
    a+=1
print(L)
k=int(input("how many times you want to rotate ?:"))
b=0
t=len(L)

while b<k:
    L.insert(t,L[0])
    L.remove(L[0])
    
    b+=1
print(L[:])