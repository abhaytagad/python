def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
    
n=int(input(" enter the number:"))  
print(f" the sum of {n} number is:",sum(n))  