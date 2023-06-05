def f(n):
    if n==1 :
        return 1
    elif n==0:
        return 0
    else:
        return f(n-1)+f(n-2)
n=int(input(" enter the number of term:"))  
print(" the fibonacci sequence term is:",f(n))     