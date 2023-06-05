a=0
while a<3:

    print("Enter the value of n:")

    n=int(input())
    factoriale=1
    if n<0:
        print("Sorry the factorial of negative number does not exist")
    elif n ==0:
        print("the factorial of n is", 1)
    
    else:
    #factoriale=1
        for i in range(1,n+1):
        
            factoriale=factoriale*i
        print("the value of factorial of",n,"is",factoriale)
        