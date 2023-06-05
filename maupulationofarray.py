L=[]
b=0
n=int(input("enter the size of array:"))
while b<n:
    e=int(input("enter the element of array:"))
    L.append(e)
    b+=1
print(L)
M=int(input("enter the value of M:"))

for i in range(len(L)):
    x=0
    for j in range(len(L)):
        if L[i]<=L[j]:
            x+=1
        
    if (x*L[i])==M:
        print("the value of k is:",L[i])

