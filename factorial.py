def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
n=int(input(" enter the number:"))
print(f" the factorial of {n}:",f(n))            