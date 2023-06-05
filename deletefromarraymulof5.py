L=[]
x=0
n=int(input("enter the size of array:"))
while x<n:
    e=int(input("enter the element of array:"))
    L.append(e)
    x+=1
print(L)
for i in L:
    if i%5==0:
        L.remove(i)
        
print(L)