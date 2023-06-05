n=int(input(" enter the number:"))
print("the square rooot of number:",n**0.5)
print(" the square of number:",n**2)
print(" the cube of the number:",n**3)
if n==1 or n==0:
    print(f" the {n} is not a prime:")
    
else:
    for i in range(2,n):
        if n%i==0:
            print(f"the {n} is not a prime number")
            break
    else:
         print(f" the {n} is a prime number")    
         
for j in range(2,n):
    if n%j==0:
         for i in range(2,j):
            if j%i==0:
                break
         else:
            print(" the prime factor:",j,end=" ,")