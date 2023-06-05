
a=0
while a<4:




    N=int(input("please enter the N:"))
    M=int(input("enter the value of M:"))



    for i in range(N,-1000,-1):
        if i%M==0:
            print(i)
            break
           
        
            