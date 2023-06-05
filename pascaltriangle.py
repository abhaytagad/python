def fac(n):
   
    if n==0 or n==1:
   
        return 1
    else:
   
        return n*fac(n-1)

        
n=int(input("n:"))    

for i in range(n):

    k=0

    for j in range(n+1):
        
        if j<n-i:

            print("  ",end="")

        else:

            c=fac(i)

            b=fac(abs(i-k))*fac(k)
            
            print(int(c/b),end="   ")

            k+=1
            
    print("\n")