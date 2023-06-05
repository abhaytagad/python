L=[]
x=0
n=int(input("enter the size of array:"))
while x<n:
    e=int(input("enter the element of array:"))
    L.append(e)
    x+=1
print(L)

for i in range(len(L)):
    for j in range(len(L)):
        if L[i]+L[j]==i+j and i!=j:
            print((L[i],L[j]))
             