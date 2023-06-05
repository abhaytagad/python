def f(n):
    if n==1:
        return 1
    elif n==0:
        return 0
       
    else:
        return f(n-2)+f(n-1)
      
n=int(input("n:"))

for i in range(n):
    print(f(i),end=" ")
    
    