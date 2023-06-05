
u=int(input(" how many digit numbers you want to enter?: "))
b=int(input(" lower limt: "))
n=int(input(" upper limit: "))

for i in range(b, n):
    t=i
    #print(t)
    sum=0
    while t>0:
        d=t%10
        sum=sum+d**u
        t//=10
        
    if sum==i:
        print(i)
       
        
    

    