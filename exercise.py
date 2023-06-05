L=[4,5,2,1,7,6]
for i in range(len(L)):
    #for j in range(0,i):
        if i==0:
            print(-1)
        else:
            print(max(L[0:i]))