L=[4,5,4,5,6,6,6]
for i in range(len(L)):
    a=1
    for j in range(len(L)):
        if L[i]==L[j] and i!=j:
            a+=1
    print(a)       