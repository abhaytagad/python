L=[1,2,3,4,4,0,5,9,0,3]
r=len(L)-2
for i in range(0,r):
    if L[i]==0:
        L.remove(L[i])
        L.append(0)
        
print(L)