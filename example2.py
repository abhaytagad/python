L=[8,4,2,1,5,4,2,1,2,3]
for i in range(len(L)):
    for j in range(len(L)) :
        if L[i]+L[j]==i+j and i!=j:
            print(L[i])
            print(L[j])